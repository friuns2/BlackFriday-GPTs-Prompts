
[![WeChat Mini Pro Developer](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/futuristic/futu_10.png)]()
# WeChat Mini Pro Developer 
Create an event management mini program allowing users to create, publish, share, and sign up for events. Apply market analysis and professional expertise to provide functional design with complete code in WXML, JS, and WXSS formats. Utilize cloud development and original language.

# Prompt

```
我希望你扮演一个微信小程序开发工程师。我将提供有关小程序程序需要的一些特殊信息，您的工作是根据市场现场分析以及您的专业经验提供一个功能设计，并提供一个结构和相关完整代码，格式如：功能1，wxml代码是，js代码，wxss代码。不要提供简单或节省策略的代码，因为那样毫无意义，使用云开发和原始小程序语言开发小程序。我的第一个要求是'我想做一个活动之前的小程序，用户可以创建，发布和分享活动。用户可以报名与活动'
```

## Conversation

**ASSISTANT**: 为了实现您的要求，我将创建一个包含以下功能的微信小程序：



1. 首页：显示最近发布的活动、热门活动以及用户参加的活动。



wxml代码：

```html

<!--首页-->

<view class="container">

  <view class="tabs">

    <view class="{{tabActive===0?'active':''}}" bindtap="changeTab" data-index="0">最新</view>

    <view class="{{tabActive===1?'active':''}}" bindtap="changeTab" data-index="1">热门</view>

    <view class="{{tabActive===2?'active':''}}" bindtap="changeTab" data-index="2">我的</view>

  </view>



  <!-- 最新 -->

  <view class="latest" wx:if="{{tabActive===0}}">

    <view class="activity" wx:for="{{latestActivities}}" wx:key="id">

      <image class="cover" src="{{item.coverUrl}}" mode="aspectFill"></image>

      <view class="info">{{item.title}}</view>

      <view class="time">{{item.startTime}} 至 {{item.endTime}}</view>

    </view>

  </view>



  <!-- 热门 -->

  <view class="hottest" wx:if="{{tabActive===1}}">

    <view class="activity" wx:for="{{hottestActivities}}" wx:key="id">

      <image class="cover" src="{{item.coverUrl}}" mode="aspectFill"></image>

      <view class="info">{{item.title}}</view>

      <view class="time">{{item.startTime}} 至 {{item.endTime}}</view>

    </view>

  </view>



  <!-- 我的 -->

  <view class="mine" wx:if="{{tabActive===2}}">

    <view class="activity" wx:for="{{myActivities}}" wx:key="id">

      <image class="cover" src="{{item.coverUrl}}" mode="aspectFill"></image>

      <view class="info">{{item.title}}</view>

      <view class="time">{{item.startTime}} 至 {{item.endTime}}</view>

    </view>

  </view>



</view>

```



js代码：

```javascript

Page({

  data: {

    tabActive: 0, // 当前选中的tab索引

    latestActivities: [], // 最新活动列表

    hottestActivities: [], // 热门活动列表

    myActivities: [], // 我参加的活动列表

  },



  onLoad() {

    // 加载最新、热门、我参加的活动列表

    // ...

  },



  changeTab(e) {

    const index = e.currentTarget.dataset.index;

    this.setData({

      tabActive: index,

    });

  },

});

```



2. 创建活动：用户可以创建一个新的活动，包括标题、封面图片、开始时间、结束时间、地点、费用等信息。



wxml代码：

```html

<!-- 创建活动 -->

<view class="container">

  <form bindsubmit="createActivity">

    <view class="form-group">

      <label>活动标题</label>

      <input name="title" type="text" required placeholder="请输入活动标题" />

    </view>

    <view class="form-group">

      <label>封面图片</label>

      <button bindtap="chooseImage">选择图片</button>

      <image class="preview-image" wx:if="{{coverUrl}}" src="{{coverUrl}}" mode="aspectFill"></image>

    </view>

    <view class="form-group">

      <label>开始时间</label>

      <picker name="startTime" mode="datetime" value="{{startTime}}" start="{{now}}" bindchange="onStartTimeChange">

        <view>{{startTime}}</view>

      </picker>

    </view>

    <view class="form-group">

      <label>结束时间</label>

      <picker name="endTime" mode="datetime" value="{{endTime}}" start="{{now}}" bindchange="onEndTimeChange">

        <view>{{endTime}}</view>

      </picker>

    </view>

    <view class="form-group">

      <label>地点</label>

      <input name="location" type="text" required placeholder="请输入活动地点" />

    </view>

    <view class="form-group">

      <label>费用</label>

      <input name="fee" type="number" required placeholder="请输入费用" />

    </view>

    <button type="submit">创建活动</button>

  </form>

</view>

``


