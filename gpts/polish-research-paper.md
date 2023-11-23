
[![Polish Research Paper](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/futuristic/futu_7.png)](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22tY_bAzr3y07d-FLZg2YvH%22%2C%22flow%22%3Atrue%7D%7D)
# Polish Research Paper | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22tY_bAzr3y07d-FLZg2YvH%22%2C%22flow%22%3Atrue%7D%7D)
The following paragraphs are part of an academic paper. Please fix the grammar mistakes and polish them as a native speaker.

# Prompt

```
The following paragraphs are part of an academic paper.
Please fix the grammar mistakes and polish them as a native speaker.

Global point cloud transformers~\cite{Guo2021,Yu2022,He2022} can only process point clouds containing several thousands points, 
thus we omit the comparisons with them and focus on the comparisons with efficient point cloud transformers proposed recently, including Stratified Transformer~\cite{Lai2022} and Point Transformer v2~\cite{Wu2022}.
Stratified Transformer extends window attentions~\cite{Liu2021a} to point clouds with cubic windows~\cite{Fan2022,Sun2022} and leverages stratified sampling to improve its performance.
Point Transformer v2 applies attentions to k nearest neighbours of each point in a sliding-window fashion.
Since the network configurations vary greatly,  we first record the running time of one \emph{single} transformer block on an Nvidia 3090 GPU to eliminate the influence of uncontrolled factors,
We choose the input tensor's spatial number  from $\{10k, 20k, 50k, 100k, 200k\}$ and set the channel as 96.
For the attention modules, we set the head number to 6, and set the point number and neighbourhood number to 32 for our OctFormer and Point Transformer v2.
Since the point number is variant in each window for Stratified Transformer, we set the window size to 7 so that the average point number is about 32.

The results are shown in Figure~\ref{fig:efficiency}.
It can be seen that although the computation complexities of three methods are all linear, our OctFormer runs significantly faster than  Point Transformer v2 and Stratified Transformer.
The speed of OctFormer is over 17 times faster than the other two methods when the spatial number of the input tensor is $200k$.
The key reason for the efficiency of our Octformer is that our novel octree attention 
% does not require expensive neighbourhood searching and turns sparse point clouds to dense tensors to
mainly leverages standard operators supported by deep learning frameworks, e,g. the multi-head attention of PyTorch, which is further based on general matrix multiplication routines on GPUs and has been optimized towards the computation limit of GPUs~\cite{cublas2022}.
However, the point number in each window of Stratified Transformer is highly unbalanced, which is hard for efficiency tuning even with hand-crafted GPU programming.
Although the neighbourhood number of Point Transformer v2 is  fixed, the sliding window execution pattern wastes considerable computation which could have been shared.

We also compare the efficiency of the whole network as shown in Figure~\ref{fig:teaser}.
We record the time of one forward pass of each network on an Nivida 3090 GPU taking a batch of $250k$ points.
The speed of our Octformer-Small is slightly faster than MinkowskiNet, and faster than Point Transformer V2 by 3 times and thanStratified Transformer by  20 times.
It is worth mentioning that our OctFormer takes point clouds quantized by a voxel size of 1cm as input, whereas the other networks takes point clouds quantized by a voxel size of 2cm.
We will ablate the effect of voxel sizes in the following experiments.
```

## Conversation

**ASSISTANT**: Global point cloud transformers can only handle point clouds with several thousand points. Therefore, we focus on comparing our efficient point cloud transformers, namely Stratified Transformer and Point Transformer v2, while omitting comparisons with Global point cloud transformers. Stratified Transformer applies window attentions to point clouds with cubic windows and utilizes stratified sampling to achieve better performance. On the other hand, Point Transformer v2 uses attentions on k nearest neighbours of each point via sliding-window method. For fair comparison, we recorded the running time of one single transformer block on an Nvidia 3090 GPU for each network configuration. We varied the input tensor's spatial number from $\{10k, 20k, 50k, 100k, 200k\}$ and set the channel as 96. The head number of attention modules was set to 6, and the point number and neighbourhood number were set to 32 for OctFormer and Point Transformer v2. As for Stratified Transformer, the window size was set to 7 to yield an average point number around 32.



Figure~\ref{fig:efficiency} shows the results of our experiments. Although the computation complexities of all three methods are linear, our OctFormer outperforms Point Transformer v2 and Stratified Transformer significantly in terms of speed. When the spatial number of the input tensor is 200k, OctFormer runs over 17 times faster than the other two methods. This efficiency is mainly due to the novel octree attention used in OctFormer, which leverages standard operators supported by deep learning frameworks and avoids costly neighbourhood searching while converting sparse point clouds into dense tensors. Conversely, the point number in each window of Stratified Transformer is highly unbalanced, making it challenging for efficiency tuning even with hand-crafted GPU programming. Furthermore, Point Transformer v2's sliding window execution pattern wastes considerable computation that could have been shared.



In addition, Figure~\ref{fig:teaser} depicts the efficiency of the entire network. We measured the time it takes for one forward pass on an Nvidia 3090 GPU, taking a batch of 250k points. Our Octformer-Small is slightly faster than MinkowskiNet and three times faster than Point Transformer v2 and 20 times faster than Stratified Transformer. It is worth noting that while our OctFormer takes point clouds quantized by a voxel size of 1cm as input, the other networks use point clouds quantized by a voxel size of 2cm. We will further investigate the effect of voxel sizes in subsequent experiments.


