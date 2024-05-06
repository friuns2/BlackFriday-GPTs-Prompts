

# 开发一个Wechaty应用 | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%228-nkARDYvawUNRAfibIQW%22%2C%22flow%22%3Atrue%7D%7D)
一句话描述你的需求，给你一个微信聊天机器人

例如：

我们在群内发布一个活动，当活动发布后，群成员可以发送 #报名 来报名活动；

记录已报名活动的成员，当新成员报名时回复报名成功以及已报名名单；

当在群内发送 #取消 时，将其从报名名单中删除，且回复取消成功；

如果成员没有报名活动则回复提示当前成员没有报名活动

# Prompt

```
下面我们将使用基于最新版本的Wchaty使用ts语言开发一个聊天机器人应用，以下是官方提供的示例代码：
#!/usr/bin/env -S node --no-warnings --loader ts-node/esm
import {
  Contact,
  Message,
  ScanStatus,
  types,
  WechatyBuilder,
  log,
} from 'wechaty'
import qrcodeTerminal from 'qrcode-terminal'
import { FileBox } from 'file-box'
function onScan(qrcode: string, status: ScanStatus) {
  if (status === ScanStatus.Waiting || status === ScanStatus.Timeout) {
    const qrcodeImageUrl = [
      'https://wechaty.js.org/qrcode/',
      encodeURIComponent(qrcode),
    ].join('')
    log.info('StarterBot', 'onScan: %s(%s) - %s', ScanStatus[status], status, qrcodeImageUrl)

    qrcodeTerminal.generate(qrcode, { small: true })  // show qrcode on console

  } else {
    log.info('StarterBot', 'onScan: %s(%s)', ScanStatus[status], status)
  }
}
function onLogin(user: Contact) {
  log.info('StarterBot', '%s login', user)
}
function onLogout(user: Contact) {
  log.info('StarterBot', '%s logout', user)
}
async function onMessage(msg: Message) {
  log.info('StarterBot', msg.toString())

  if (msg.type() === types.Message.Video
    || msg.type() === types.Message.Attachment
    || msg.type() === types.Message.Audio) {
log.info('isFile:',true)
  }

  if (msg.text() === 'ding') {
    await msg.say('dong')
  }
}
const bot = WechatyBuilder.build({
  name: 'ding-dong-bot',
  puppet: 'wechaty-puppet-wechat4u',
})
bot.on('scan', onScan)
bot.on('login', onLogin)
bot.on('logout', onLogout)
bot.on('message', onMessage)
bot.start()
  .then(() => log.info('StarterBot', 'Starter Bot Started.'))
  .catch(e => log.error('StarterBot', e))
请参考这些代码实现我们的需求,特别注意获取消息类型的方法是types.Message而不是Message.Type。
在下一个问题中我将描述具体的需求，本次提问你只需要回复”我已经准备好了，请说出你的需求“，不要回复任何额外信息。当我继续说出需求时，给出ts实现的示例代码，并在代码中添加必要的中文注释。
```

## Welcome Message
我已经准备好了，请说出你的需求。

## Conversation

**ASSISTANT**: 我已经准备好了，请说出你的需求。
**USER**: 我们在群内发布一个活动，当活动发布后，群成员可以发送 #报名 来报名活动；

记录已报名活动的成员，当新成员报名时回复报名成功以及已报名名单；

当在群内发送 #取消 时，将其从报名名单中删除，且回复取消成功；

如果成员没有报名活动则回复提示当前成员没有报名活动
**ASSISTANT**: 以下是基于Wchaty和TypeScript的实现代码，包含必要的中文注释。



```typescript

#!/usr/bin/env -S node --no-warnings --loader ts-node/esm

import {

  Contact,

  Message,

  ScanStatus,

  types,

  WechatyBuilder,

  log,

} from 'wechaty'

import qrcodeTerminal from 'qrcode-terminal'

import { FileBox } from 'file-box'



// 存储已报名成员的Set对象

const participants = new Set<string>()



function onScan(qrcode: string, status: ScanStatus) {

  if (status === ScanStatus.Waiting || status === ScanStatus.Timeout) {

    const qrcodeImageUrl = [

      'https://wechaty.js.org/qrcode/',

      encodeURIComponent(qrcode),

    ].join('')

    log.info('StarterBot', 'onScan: %s(%s) - %s', ScanStatus[status], status, qrcodeImageUrl)



    qrcodeTerminal.generate(qrcode, { small: true })  // 在控制台展示二维码



  } else {

    log.info('StarterBot', 'onScan: %s(%s)', ScanStatus[status], status)

  }

}



function onLogin(user: Contact) {

  log.info('StarterBot', '%s 登录了', user.name())

}



function onLogout(user: Contact) {

  log.info('StarterBot', '%s 退出了', user.name())

}



async function onMessage(msg: Message) {

  log.info('StarterBot', msg.toString())



  const room = msg.room() // 获取消息所在的群聊对象

  if (!room) return // 如果不在群聊内则忽略消息



  const text = msg.text().trim() // 获取消息内容并去除两端空格



  if (/^#报名$/.test(text)) { // 如果是报名消息

    const from = msg.from() // 获取发送消息的成员对象

    if (!from) return // 如果没有发送者则忽略消息



    participants.add(from.name()) // 将发送者添加到已报名成员列表中



    const names = Array.from(participants).join(', ') // 将已报名成员列表转换为逗号分隔的字符串



    await room.say(`${from.name()} 报名成功！\n已报名成员：${names}`) // 回复报名成功以及已报名成员列表

  } else if (/^#取消$/.test(text)) { // 如果是取消消息

    const from = msg.from() // 获取发送消息的成员对象

    if (!from) return // 如果没有发送者则忽略消息



    participants.delete(from.name()) // 将发送者从已报名成员列表中删除



    const names = Array.from(participants).join(', ') // 将已报名成员列表转换为逗号分隔的字符串



    await room.say(`${from.name()} 取消成功！\n已报名成员：${names}`) // 回复取消成功以及已报名成员列表

  } else if (text === '活动发布') { // 如果是活动发布消息

    await room.say('请在本群内发送 #报名 进行报名，发送 #取消 可以取消报名。') // 提示如何进行报名和取消报名

    if (participants.size > 0) { // 如果已有成员报名

      const names = Array.from(participants).join(', ') // 将已报名成员列表转换为逗号分隔的字符串

      await room.say(`已报名成员：${names}`) // 发送已报名成员列表

    } else {

      await room.say('当前没有成员报名。') // 发送提示信息

    }

  }

}



const bot = WechatyBuilder.build({

  name: '活动报名机器人',

  puppet: 'wechaty-puppet-wechat4u',

})



bot.on('scan', onScan)

bot.on('login', onLogin)

bot.on('logout', onLogout)

bot.on('message', onMessage)



bot.start()

  .then(() => log.info('StarterBot', '机器人已启动'))

  .catch(e => log.error('StarterBot', e))

```



需要注意的是，以上代码仅实现了最基本的功能，还有很多情况和

