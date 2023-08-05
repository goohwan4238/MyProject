# 충돌
# 초기 Glossary bot 코드
# payload 버전


SLACK_BOT_TOKEN='xoxb-5225787109154-5471874969926-RYr0fofJT7o8M2IRVRy8EoDA'
SLACK_APP_TOKEN='xapp-1-A05E4UA2RD2-5475600482549-04a3afbe63026af085dfd741cd66f3bf78111a7f6a95bc938ddeb0de70253033'

import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

import csv

# Initializes your app with your bot token and socket mode handler
app = App(token=SLACK_BOT_TOKEN)

f = open('langdic.csv','r')
reader = csv.reader(f) 
techDic = {}
for line in reader:
    
    techDic[line[0].upper()] = line[1]
f.close()

@app.message()
def message_hello(message, say):
    if message['text'].find('?') ==0 : 
        find_answer(message, say)
    elif message['text'].find('$') ==0 : 
        reg_dictionary(message, say)
   
def find_answer(message, say):
    key = message['text'].replace("?", "")
    key = key.strip().upper()

    if key in techDic:
        blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f">*용어*: {key}\n>{techDic[key]}"
                }
            }
        ]        
        say(text = "test", blocks = blocks)
    else:
        blocks = [
            {
			"type": "input",
            "block_id": "contents-text",
			"dispatch_action": True,
			"element": {
				"type": "plain_text_input",
				"action_id": "plain_text_input-action",
				"dispatch_action_config": {
					"trigger_actions_on": [
						"on_character_entered"
					]
				},
			},
			"label": {
				"type": "plain_text",
				"text": "용어 정의",
				"emoji": True
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "actions",
            "block_id": "text_input_poll",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "등록",
						"emoji": True
					},
					"style": "primary",
					"value": "click_me_123",
					"action_id": "actionId-0"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "취소",
						"emoji": True
					},
					"style": "danger",
					"value": "click_me_123",
					"action_id": "actionId-1"
				}
			]
		}

        ]
        #say(f"등록된 용어가 없습니다.")        
        say(text = "test", blocks = blocks)       

@app.action("actionId-0")
def action_holiyday_ok_button(ack, payload, body, action, respond, command, say, context):
    definition = body['state']['values']['contents-text']['plain_text_input-action']['value']
    say(f"등록버튼이 눌렸습니다. 등록된 내용 \n: {definition}")

def reg_dictionary(message, say):    
    item = message['text'].replace("$", "")
    lst = item.split(':')        

    if lst[0] not in techDic:
        techDic[lst[0].strip().upper()] = lst[1].strip()
        #write_file([lst[0],lst[1]])
        write_file(lst)
        say(f"용어 {lst[0]} 을 신규로 등록하였습니다.")        

def write_file(lst):
    f = open('langdic.csv','a', newline="")
    wr = csv.writer(f)
    wr.writerow(lst)
    f.close()

# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()

