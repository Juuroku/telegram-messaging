import re
import argparse
import requests
import sys
import json

parser = argparse.ArgumentParser(add_help=True)

parser.add_argument('-t', '--token',
        required=True,
        dest='token',
        help='Token of Telegram bot. Required',
        type=str)
parser.add_argument('-c', '--chat',
        required=True,
        dest='chat_id',
        help='Chat id of Telegram chat. Required',
        type=str)
parser.add_argument('-m', '--message',
        required=True,
        dest='message',
        help='Message you want to send. Required',
        type=str)
parser.add_argument('-p', '--parse',
        dest='parse',
        help='Parse style of message. Markdown or HTML. Optional',
        type=str)

args = parser.parse_args()

if args.parse is not None:
    p = args.parse.lower()
    if p == 'markdownv2' or p == 'md' or p == 'markdown' :
            parse = 'MarkdownV2'
    elif p == 'html' :
        parse = 'HTML'
    elif len(p) != 0 and p != 'default':
        sys.exit("Wrong Parse Mode: %s"%p)

url = "https://api.telegram.org/bot%s/sendMessage"%args.token
obj = {}
obj = {}
obj['chat_id'] = args.chat_id
obj['text'] = args.message

if 'parse' in locals() or 'parse' in globals():
    obj['parse_mode'] = parse

x = requests.post(url, json = obj)

result = json.loads(x.text)
if not result['ok']:
    print("{} - {}".format(result['error_code'], result['description']))
    sys.exit(obj['text'])

print('Message Sent')
sys.exit()
