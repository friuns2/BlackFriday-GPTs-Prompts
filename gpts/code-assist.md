
[![Code Assist](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/futuristic/futu_6.png)](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%225QCjePEaaUM23z0-lKVqD%22%2C%22flow%22%3Atrue%7D%7D)
# Code Assist | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%225QCjePEaaUM23z0-lKVqD%22%2C%22flow%22%3Atrue%7D%7D)
Are there any logical issues in the following Solidity code?



// SPDX-License-Identifier: MIT

pragma solidity 0.6.12;

pragma experimental ABIEncoderV2;



import "@openzeppelin/contracts-old/access/Ownable.sol";

import "@openzeppelin/contracts-old/token/ERC20/IERC20.sol";

import "@openzeppelin/contracts-old/token/ERC20/SafeERC20.sol";

import "@openzeppelin/contracts-old/math/SafeMath.sol";

import "@openzeppelin/contracts-old/math/Math.sol";

import "@openzeppelin/contracts-old/utils/Pausable.sol";

import "./interfaces/IUniswapV2Router.sol";



interface INFT {

    function compoundForTokenId(uint256, uint256) external;

    function individualShares(uint256) external view returns (uint256);

    function totalShares() external view returns (uint256);

    function ownerOf(uint256) external view returns (address);

    function tokenURI(uint256) external view returns (string memory);

    function tokenByWallet(address) external view returns (uint256);

}



interface IFarmV2 {

    function withdraw(uint256, uint256) external;

    function deposit(uint256, uint256) external;

    function poolInfo(uint256) external view returns (PoolInfo memory);

    struct PoolInfo {

       IERC20 token; // Address of LP token contract.

       uint256 allocPoint; // How many allocation points assigned to this pool. tSHAREs to distribute per block.

       uint256 lastRewardTime; // Last time that tSHAREs distribution occurs.

       uint256 accESharePerShare; // Accumulated tSHAREs per share, times 1e18. See below.

       bool isStarted; // if lastRewardTime has passed

    }

}



contract FusionRewardDistributor is Ownable, Pausable {

    using SafeERC20 for IERC20;

    using SafeMath for uint256;



    INFT public nft;

    IERC20 public eshare;

    IFarmV2 public farm;

    uint256 public poolId;

    

    mapping(uint256 => uint256) public last_distPoints;

    mapping(uint256 => Receiver[]) public receivers;

    mapping(uint256 => uint256) public receiversTotalAllocPoints;



    struct Receiver {

        address to;

        uint256 allocPoints;

    }



    uint256 public esharePending;

    uint256 public eshareCompounded;

    uint256 public eshareClaimed;

    uint256 public totalDistributePoints;

    uint256 public constant MULTIPLIER = 10e18;

    event Compound(uint256 indexed id, uint256 amount);

    event Claim(uint256 indexed id, uint256 amount);



    constructor(address _nft, address _eshare, address _farm, uint256 _poolId) public {

        nft = INFT(_nft);

        eshare =IERC20( _eshare);

        farm = IFarmV2(_farm);

        poolId = _poolId;

    }



    // receive() external payable {}



    function setNft(address _nft) external onlyOwner {

        nft = INFT(_nft);

    }



    function numReceivers(uint256 _id) external view returns (uint256) {

        return receivers[_id].length;

    }



    function listReceivers(uint256 _id) external view returns (Receiver[] memory) {

        return receivers[_id];

    }



    function addReceiver(uint256 _id, Receiver memory _receiver) public onlyOwner {

        receivers[_id].push(_receiver);

        receiversTotalAllocPoints[_id] = receiversTotalAllocPoints[_id].add(_receiver.allocPoints);

    }



    function setReceiver(uint256 _id, uint256 _index, Receiver memory _receiver) public onlyOwner {

        Receiver[] storage receiverArray = receivers[_id];

        require(_index < receiverArray.length, "Index out of bounds");

        receiversTotalAllocPoints[_id] = receiversTotalAllocPoints[_id].sub(receiverArray[_index].allocPoints).add(_receiver.allocPoints);

        receiverArray[_index].to = _receiver.to;

        receiverArray[_index].allocPoints = _receiver.allocPoints;

    }



    function setReceiverMany(uint256[] calldata _ids, Receiver[][] memory _receivers) external onlyOwner {

        require(_ids.length == _receivers.length, "Length mismatch");

        for (uint256 i = 0; i < _ids.length; i++) {

            if (i < receivers[_ids[i]].length) {

                for (uint256 j = 0; j < _receivers[i].length; j++) {

                    setReceiver(_ids[i], j, _receivers[i][j]);

                }

            } else {

                for (uint256 j = 0; j < _receivers[i].length; j++) {

                    addReceiver(_ids[i], j, _receivers[i][j]);

                }

            }

        }

    }



    function removeReceiver(uint256 _id, uint256 _index) external onlyOwner {

        Receiver[] storage receiverArray = receivers[_id];

        require(_index < receiverArray.length, "Index out of bounds");



        receiversTotalAllocPoints[_id] = receiversTotalAllocPoints[_id].sub(receiverArray[_index].allocPoints);

        receiverArray[_index] = receiverArray[receiverArray.length - 1];

        receiverArray.pop();

    }



    function approveToken(address token, address spender) external onlyOwner {

		if (IERC20(token).allowance(address(this), address(spender)) == 0) {

			IERC20(token).safeApprove(spender, uint256(-1));

		}

	}



    function setPaused(bool pause) external onlyOwner {

		pause ? _pause() : _unpause();

	}



    function withdraw_z115(address token, address to, uint256 amnt) external onlyOwner {

        if (token == address(0)) {

            payable(to).transfer(amnt);

        } else {

            if (token == address(eshare)) {

                eshareCompounded = eshareCompounded.sub(amnt);

            }

            IERC20(token).safeTransfer(to, amnt);

        }

    }

    

    function migrateDistPoints(uint256 _id, uint256 _last_distPoints) external onlyOwner {

        last_distPoints[_id] =  _last_distPoints;

    }

    

    function migrateReceivers(uint256 _id, Receiver[] memory _receivers) external onlyOwner {

        if (_receivers[_id].length == 0) {

        

        receivers[_id] = _receiver;

        }

    }



    function migrateGlobals(

        uint256 _esharePending, 

        uint256 _eshareCompounded, 

        uint256 _eshareClaimed, 

        uint256 _totalDistributePoints

    ) external onlyOwner {

        esharePending = _esharePending;

        eshareCompounded = _eshareCompounded;

        eshareClaimed = _eshareClaimed;

        totalDistributePoints = _totalDistributePoints;

    }



    function totalShares() public view returns (uint256) {

        return nft.totalShares();

    }

    

    function userShares(address account) public view returns (uint256) {

        return nft.individualShares(nft.tokenByWallet(account));

    }



    function getShare(address _account) external view returns (uint256) {

        return userShares(_account).mul(MULTIPLIER).div(totalShares());

    }



    function getDistributionRewards(uint256 _id) external view returns (uint256) {

        return _getDistributionRewards(_id);

    }



    function _getDistributionRewards(uint256 _id) internal view returns (uint256) {

        uint256 _points = last_distPoints[_id];

        return _points > 0 

            ? nft.individualShares(_id).mul(totalDistributePoints.sub(_points)).div(MULTIPLIER)

            : 0;

    }



    function getTotalRewardsFor(address _sender) external view returns (uint256) {

        return getTotalRewards(nft.tokenByWallet(_sender));

    }

    

    function getTotalRewards(uint256 _id) public view returns (uint256) {

        uint256 _individualShares = nft.individualShares(_id);

        uint256 _totalShares = nft.totalShares();

        uint256 _points = last_distPoints[_id];

        return _totalShares > 0 && _individualShares > 0 && _points > 0

            ? _getDistributionRewards(_id).add(

                    getPoolBalance()

                        .mul(_individualShares)

                        .div(_totalShares)

            ) : 0;

    }



    function compound() external {

        compoundFor(nft.tokenByWallet(_msgSender()), true);

    }



    function compoundFor(uint256 _id, bool _claimBefore) public whenNotPaused {

        if (last_distPoints[_id] == 0) {

            last_distPoints[_id] = totalDistributePoints;

        }

        if (_claimBefore) {

            _tryClaimFarm();

        }



        uint256 distributed = _getDistributionRewards(_id);



        if (distributed > 0) {

        

            last_distPoints[_id] = totalDistributePoints;

            esharePending = esharePending.sub(distributed);

            eshareCompounded = eshareCompounded.add(distributed);

            

            nft.compoundForTokenId(distributed, _id);



            _tryClaimFarm();



            if (last_distPoints[_id] != totalDistributePoints)

                last_distPoints[_id] = totalDistributePoints;



            emit Compound(_id, distributed);

        }

    }



    function compoundForMany(uint256[] calldata _ids) external {

        _tryClaimFarm();



        for (uint256 i = 0; i < _ids.length; i++) {

            compoundFor(_ids[i], false);

        }

    }



    function claim() external {

        claimFor(nft.tokenByWallet(_msgSender()), true);

    }



    function claimFor(uint256 _id, bool _claimBefore) public whenNotPaused {

        Receiver[] memory receiverArray = receivers[_id];

        if (receiverArray.length > 0) {



            if (last_distPoints[_id] == 0) {

                last_distPoints[_id] = totalDistributePoints;

            }

            if (_claimBefore) {

                _tryClaimFarm();

            }



            uint256 distributed = _getDistributionRewards(_id);



            if (distributed > 0) {

            

                esharePending = esharePending.sub(distributed);

                eshareClaimed = eshareClaimed.add(distributed);

                last_distPoints[_id] = totalDistributePoints;



                for (uint256 i = 0; i < receiverArray.length; i++) {

                    Receiver memory receiver = receiverArray[i];

                    eshare.safeTransfer(receiver.to, distributed.mul(receiver.allocPoints).div(receiversTotalAllocPoints[_id]));

                }



                emit Claim(_id, distributed);

            }

        }

    }



    function claimForMany(uint256[] calldata _ids) external {

        _tryClaimFarm();



        for (uint256 i = 0; i < _ids.length; i++) {

            claimFor(_ids[i], false);

        }

    }



    function _distributeRewards() internal {

        uint256 _poolBalance = getPoolBalance();

        uint256 _totalShares = nft.totalShares();



        if (_poolBalance > 0 && _totalShares > 0) {

            totalDistributePoints = totalDistributePoints.add(_poolBalance.mul(MULTIPLIER).div(_totalShares));

            esharePending = esharePending.add(_poolBalance);

        }

    }





    function distributeRewards() external {

        _distributeRewards();

    }



    function getTokenURI(address account) external view returns (string memory) {

        return nft.tokenURI(nft.tokenByWallet(account));

    }



    function getBalance() public view returns (uint256) {

        return eshare.balanceOf(address(this));

    }



    function getPoolBalance() public view returns (uint256) {

        return getBalance().sub(esharePending).sub(eshareCompounded);

    }



    function lastClaimTime() public view returns (uint256) {

        return farm.poolInfo(poolId).lastRewardTime;

    }



    function updateRewardsAndPoints(uint256 _id) external {

        require(_msgSender() == address(nft), "Caller is not MicroGridNFT");



        if (receivers[_id].length == 0 || receiversTotalAllocPoints[_id] == 0) {

            compoundFor(_id, true);

        } else {

            claimFor(_id, true);

        }



        // _tryClaimFarm();

        // if (last_distPoints[_id] == 0) {

        //     last_distPoints[_id] = totalDistributePoints;

        // }

    }



    function _tryClaimFarm() internal {

        address farmAddr = address(farm);

        bytes4 functionSelector = farm.withdraw.selector;

        uint256 _poolId = poolId;

        uint256 _amount = 0;



        assembly {

            let ptr := mload(0x40)          // Load free memory pointer

            mstore(ptr, functionSelector)  // Store function selector

            mstore(add(ptr, 0x04), _poolId) // Store poolId argument after the function selector

            mstore(add(ptr, 0x24), _amount) // Store amount argument after the poolId



            // Call the external function and ignore the success value using 'pop()'

            pop(call(

                gas(),                   // Forward all available gas

                farmAddr,                // Address of the farm contract

                0,                       // No value transfer

                ptr,                     // Input (function selector, poolId, and amount)

                0x44,                    // Input size (4 bytes for function selector + 32 bytes for poolId + 32 bytes for amount)

                0,                       // Output pointer (0 bytes, since we don't expect any output)

                0                        // Output size (0 bytes, since we don't expect any output)

            ))

        }



        _distributeRewards();

    }



    function adminClaimFarm() external onlyOwner {

        farm.withdraw(poolId, 0);

        _distributeRewards();

    }



    function adminDepositFarm(uint256 _amount) external onlyOwner {

        farm.poolInfo(poolId).token.approve(address(farm), _amount);

        farm.deposit(poolId, _amount);

        farm.poolInfo(poolId).token.approve(address(farm), 0);



        // _tryClaimFarm();

    }



    function adminWithdrawFarm(uint256 _amount, address _to) public onlyOwner {

        farm.withdraw(poolId, _amount);

        farm.poolInfo(poolId).token.transfer(_to, _amount);

        _tryClaimFarm();

    }



    function adminWithdrawFarm(uint256 _amount) external onlyOwner {

        adminWithdrawFarm(_amount, address(this));

    }



    function setPoolInfo(IERC20 _eshare, IFarmV2 _farm, uint256 _pid) external onlyOwner {

        eshare = _eshare;

        farm = _farm;

        poolId = _pid;

    }



    /**

     * @notice Performs a generic transaction.

     * @param _target The address for the transaction.

     * @param _value The value for the transaction.

     * @param _data The data of the transaction.

     */

    function invoke_z115(

        address _target,

        uint256 _value,

        bytes memory _data

    ) external onlyOwner returns (bytes memory _result) {

        bool success;

        (success, _result) = _target.call{value: _value}(_data);

        if (!success) {

            // solhint-disable-next-line no-inline-assembly

            assembly {

                returndatacopy(0, 0, returndatasize())

                revert(0, returndatasize())

            }

        }

    }

}

# Prompt

```
Solidity code help
```

## Conversation

**ASSISTANT**: Of course, I'd be happy to help with any Solidity code questions you have. What do you need help with specifically?


