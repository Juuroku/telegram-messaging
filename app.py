import re
import requests
import sys
import json

args = {}

for arg in sys.argv[1:]:
    variable = re.search('\-\-(.*)\=',arg)
    variable = variable.group(1)
    value = re.search('\=(.*)',arg,re.DOTALL)
    value = value.group(1)
    args[variable.lower()] = value

if 'token' not in args or 'chat_id' not in args or 'message' not in args:
    sys.exit("Missing Vars (Required: TOKEN, CHAT_ID, MESSAGE)")

if 'parse' in args:
    p = args['parse'].lower()
    if p == 'markdownv2' or p == 'md' or p == 'markdown' :
            parse = 'MarkdownV2'
    elif p == 'html' :
        parse = 'HTML'
    elif len(p) == 0 or p == 'default':
    else :
        sys.exit("Wrong Parse Mode: %s"%p)

url = "https://api.telegram.org/bot%s/sendMessage"%args['token']
obj = {}
obj['chat_id'] = args['chat_id']
obj['text'] = args['message']

if 'parse' in locals() or 'parse' in globals():
    obj['parse_mode'] = parse

x = requests.post(url, json = obj)

result = json.loads(x.text)
if not result['ok']:
    print("{} - {}".format(result['error_code'], result['description']))
    print(obj['text'])
    sys.exit()

print('Message Sent')
sys.exit()
