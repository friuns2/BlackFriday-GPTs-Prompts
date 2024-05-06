

# One sentence to develop a whatsapp chat application | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22JTrPpMEzOBP79yuMCP9st%22%2C%22flow%22%3Atrue%7D%7D)
Describe your needs in one sentence, and give you a WeChat chatbot. For example: We publish an event in the group. After the event is released, group members can send #sign up to sign up for the event; record members who have signed up for the event, and when new members sign up Respond to the successful registration and the registered list; When #Cancel is sent in the group, it will be deleted from the registration list, and the cancellation will be successful; If the member has no registration activity, the reply will remind the current member that there is no registration activity

# Prompt

```
Below, we will use the latest version of Wchaty to develop a WhatsApp chat robot application using TS language. The following is the official provided example code： #!/usr/bin/env -S node --no-warnings --loader ts-node/esm import { Contact, Message, ScanStatus, types, WechatyBuilder, log, } from 'wechaty' import qrcodeTerminal from 'qrcode-terminal' import { FileBox } from 'file-box' function onScan(qrcode: string, status: ScanStatus) { if (status === ScanStatus.Waiting || status === ScanStatus.Timeout) { const qrcodeImageUrl = [ 'https://wechaty.js.org/qrcode/', encodeURIComponent(qrcode), ].join('') log.info('StarterBot', 'onScan: %s(%s) - %s', ScanStatus[status], status, qrcodeImageUrl) qrcodeTerminal.generate(qrcode, { small: true }) // show qrcode on console } else { log.info('StarterBot', 'onScan: %s(%s)', ScanStatus[status], status) } } function onLogin(user: Contact) { log.info('StarterBot', '%s login', user) } function onLogout(user: Contact) { log.info('StarterBot', '%s logout', user) } async function onMessage(msg: Message) { log.info('StarterBot', msg.toString()) if (msg.type() === types.Message.Video || msg.type() === types.Message.Attachment || msg.type() === types.Message.Audio) { log.info('isFile:',true) } if (msg.text() === 'ding') { await msg.say('dong') } } const bot = WechatyBuilder.build({ name: 'ding-dong-bot', puppet: 'wechaty-puppet-whatsapp', }) bot.on('scan', onScan) bot.on('login', onLogin) bot.on('logout', onLogout) bot.on('message', onMessage) bot.start() .then(() => log.info('StarterBot', 'Starter Bot Started.')) .catch(e => log.error('StarterBot', e)) Please refer to these codes to implement our requirements, and pay special attention to the method of obtaining the message type is types.Message instead of Message.Type. In the next question, I will describe the specific needs. For this question, you only need to reply "I am ready, please tell me your needs", and do not reply with any additional information. When I continue to state the requirements, I will give the sample code of ts implementation, and add the necessary Chinese comments in the code.
```

## Welcome Message
I am ready, please tell me your needs.

## Conversation

**ASSISTANT**: I am ready, please tell me your needs.
**USER**: Publish an event in a group

2When the event is released, group members can send #sign up to sign up for the event

3 The application records the members who have signed up for the event, and when a new member signs up, the registration is successful and the list of registered members is returned

4 When sending #cancellation in the group, delete it from the registration list, and reply that the cancellation is successful; if the member has no registration activity, the reply prompts that the current member has no registration activity
**ASSISTANT**: To implement the above requirements, you can use the following code as a reference:



```typescript

import { Contact, Message, ScanStatus, types, WechatyBuilder, log } from 'wechaty'

import qrcodeTerminal from 'qrcode-terminal'

import { FileBox } from 'file-box'



// Record of event participants

const participants = new Set<string>()



function onScan(qrcode: string, status: ScanStatus) {

  if (status === ScanStatus.Waiting || status === ScanStatus.Timeout) {

    const qrcodeImageUrl = [

      'https://wechaty.js.org/qrcode/',

      encodeURIComponent(qrcode)

    ].join('')

    log.info('StarterBot', 'onScan: %s(%s) - %s', ScanStatus[status], status, qrcodeImageUrl)

    qrcodeTerminal.generate(qrcode, { small: true }) // show qrcode on console

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



  // Check if message is in a group chat

  if (msg.room()) {

    // Check if message contains #signup hashtag

    if (msg.text().includes('#signup')) {

      const contact = await msg.from()

      participants.add(contact.id)

      await msg.say(`Registration successful! Current participants: ${Array.from(participants).join(', ')}`)

    }

    // Check if message contains #cancellation hashtag

    if (msg.text().includes('#cancellation')) {

      const contact = await msg.from()

      if (participants.has(contact.id)) {

        participants.delete(contact.id)

        await msg.say(`Cancellation successful. Current participants: ${Array.from(participants).join(', ')}`)

      } else {

        await msg.say('You have no registration activity.')

      }

    }

  }

}



const bot = WechatyBuilder.build({

  name: 'event-bot',

  puppet: 'wechaty-puppet-whatsapp',

})



bot.on('scan', onScan)

bot.on('login', onLogin)

bot.on('logout', onLogout)

bot.on('message', onMessage)



bot.start()

  .then(() => log.info('StarterBot', 'Event Bot Started.'))

  .catch(e => log.error('StarterBot', e))

```



Note that the above code assumes that the bot is added to a group chat where the event will take place, and that messages containing `#signup` or `#cancellation` are sent by group members. Also, we use a `Set` data structure to store the IDs of participants for easy adding and removing.

