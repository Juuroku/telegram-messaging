# Telegram Messaging

This is a simple action to send message to Telegram chat with Telegram bot.  
About Telegram bot, see [official intrudoction](https://core.telegram.org/bots).  

[![telegram messaging test](https://github.com/Juuroku/telegram-messaging/actions/workflows/main.yml/badge.svg?branch=master&event=push)](https://github.com/Juuroku/telegram-messaging/actions/workflows/main.yml)

## Usage

Example: ([see the whole file](.github/workflows/main.yml))

```yml
name: action name
on: [push]

jobs:
    job_name:
        runs-on: ubuntu-latest
        name: send message by telegram bot
        steps:
            - name: Send Message
              uses: Juuroku/telegram-messaging@master
              with: 
                telegram-token:  ${{ secrets.TELEGRAM_TOKEN }}
                telegram-chat: ${{ secrets.TELEGRAM_ID }}
                message: |
                    *Push Event Triggered*
                    REF: ${{ github.ref_name }}
                    COMMIT: ${{ github.event.head_commit.message }}
                    
                parse: 'markdown'
``` 

## Inputs

### `telegram-token`

**Required**  
Token of your Telegram bot, which you can get from [BotFather](https://core.telegram.org/bots#6-botfather).  
You can put the token in secrets.

### `telegram-chat`

**Required**  
ID of the chat you want to send to. You need to send a message to the chat and get it from [getUpdates API](https://core.telegram.org/bots/api#getupdates).  
You can put the chat id in secrets.

### `message`

**Required**  
Content you want to send, can be witten in markdown-style or HTML-style.  
If using markdown-style or HTML-style, please check [official documention](https://core.telegram.org/bots/api#formatting-options) to avoid invalid syntax.  
For example, while using markdown-style, `.`(dot) must be escaped if not in `pre`, `code` or inline links, so you have to process URL first or always treat them as inline links.  
See [Contexts](https://docs.github.com/en/actions/learn-github-actions/contexts) for more variables to use.

### `parse`

Define how to parse your message, markdown-style or HTML-style.  
If you don't need this, not use this input is ok.

## Output

The action will set an output named `status` after execution.
If the response from the api server said `OK`, `status` will be `Message Sent`.
Otherwise, it will be `{HTTP Status Code} - {Description Got from Server}`.
If you did not set any step after the action, the output will show on action page.
Or you can use the output to decide what to do next.