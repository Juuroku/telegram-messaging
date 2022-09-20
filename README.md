# Telegram Messaging

This is a simple action to send message to Telegram chat with Telegram bot.
About Telegram bot, see [official intrudoction](https://core.telegram.org/bots).

[![telegram messaging test](https://github.com/Juuroku/telegram-messaging/actions/workflows/main.yml/badge.svg?branch=master&event=push)](https://github.com/Juuroku/telegram-messaging/actions/workflows/main.yml)

## Inputs

### `telegram-token`

**Required** Token of your Telegram bot, which you can get from [BotFather](https://core.telegram.org/bots#6-botfather).

### `telegram-chat`

**Required** ID of the chat you want to send to. You need to send a message to the chat and get it from [getUpdates API](https://core.telegram.org/bots/api#getupdates).

### `message`

**Requirred** Content you want to send, can be witten in markdown-style or HTML-style.
If using markdown-style or HTML-style, please check [official documention](https://core.telegram.org/bots/api#formatting-options) to avoid invalid syntax.
For example, while using markdown-style, `.`(dot) must be escaped if not in `pre`, `code` or inline links, so you have to process URL first or always treat them as inline links.

### `parse`

Define how to parse your message, markdown-style or HTML-style.