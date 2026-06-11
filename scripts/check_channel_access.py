import json, urllib.request

cfg = json.load(open('scripts/slack_config.json'))
channel = 'C0AMVTNFHC6'

for bot_name, bot_data in cfg['bots'].items():
    token = bot_data['token']
    req = urllib.request.Request(
        'https://slack.com/api/conversations.info?channel=' + channel,
        headers={'Authorization': 'Bearer ' + token}
    )
    try:
        resp = json.loads(urllib.request.urlopen(req, timeout=5).read())
        if resp.get('ok'):
            ch_name = resp['channel']['name']
            print(f'Bot {bot_name}: OK - #{ch_name}')
        else:
            print(f'Bot {bot_name}: {resp.get("error")}')
    except Exception as e:
        print(f'Bot {bot_name}: ERROR {e}')
