# 주석 테스트
# 주석 테스트 ㅇㅇㅇ
# 23.8.17 일 테스트
# 23.8.17 일 테스트2

import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from notion_client import Client
from datetime import datetime, timezone
import csv
from github import Github

# Slack Info 
SLACK_BOT_TOKEN='xoxb-5225787109154-5471874969926-RYr0fofJT7o8M2IRVRy8EoDA'
SLACK_APP_TOKEN='xapp-1-A05E4UA2RD2-5475600482549-04a3afbe63026af085dfd741cd66f3bf78111a7f6a95bc938ddeb0de70253033'

# Notion Page info
NOTION_TOKEN = 'secret_cjeUfDIlGbQEsQrXka3hdeb09xvocP01kVYc8C09DGf'
DATABASE_ID = 'c3527cec13264369919a055a7c6f2ce7'

# GIT HUB info
GIT_TOKEN='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'
OWNER='vmssupport'
REPO='TechDoc'

# Initializes your app with your bot token and socket mode handler
app = App(token=SLACK_BOT_TOKEN)
notion = Client(auth=NOTION_TOKEN)

git = Github(GIT_TOKEN)
repo = git.get_repo(f"{OWNER}/{REPO}")


f = open('langdic.csv','r')
reader = csv.reader(f) 
techDic = {}
for line in reader:
    
    techDic[line[0].upper()] = line[1]
f.close()

#현재 Glossary 코드 제외중
@app.message()
def message_hello(message, say, client):
    if message['text'].find('?') >=0 : 
        find_answer(message, say)
    elif message['text'].find('$') >=0 : 
        reg_dictionary(message, say)
    else:
        notion_to_git(message,say)
        
# create git issue & branch from notion task message
def notion_to_git(message,say):
    # 0. retrieve notion page info 
    link = message['blocks'][1]['fields'][0]['text']        
    pgid = get_pgid(link)

    pg = notion.pages.retrieve(pgid)
    url = pg['url']
    nid = pg['properties']["ID"]["unique_id"]["number"]
    pgtitle = pg['properties']['Name']['title'][0]['plain_text']
    pgtitle = pgtitle.replace(' ','-')

    # 1. create git issue 
    issue = create_git_issue(pgid, nid, pgtitle, url)

    # 2. notion page update (embed git issue link)        
    update_notion_page(pgid, issue)

    # 3. create git branch
    # create_git_branch(issue)


def get_pgid(str):
    slst = str.split('?')
    id = slst[0].replace('*<https://www.notion.so/','')
    lst = id.split('-')
    return lst[-1]

def create_git_issue(page_id, task_id, page_title, url):
    issue_title = f"{task_id}_{page_title}"
    body = f"notion link={url}\r\npage id={page_id}\r\ntask id={task_id}"
    issue = repo.create_issue(
        title=issue_title, 
        body=body    
    )    
    return issue

def create_git_branch(issue):
    sb = repo.get_branch('master')    
    branchid = f"{issue.number}-{issue.title}"
    repo.create_git_ref(ref=f"refs/heads/{branchid}", sha=sb.commit.sha)    

def update_notion_page(pgid, issue):
    issue_url = issue.html_url    
    notion.pages.update(page_id=pgid, 
                    properties= {
                        "gitissue_url": {
                             "url": issue_url					     
                        }   
					},
                )

    '''
    git_issue_url_block = {
                            "paragraph": {
                                "rich_text": [{
                                    "type": "text",
                                    "text": {
                                        "content": f"git issue url = {issue_url}"                                        
                                    }
                                }],
                                "color": "default"
                            }
                        }
    children_blocks =[]
    children_blocks.append(git_issue_url_block)
    notion.blocks.children.append(block_id=pgid, children=children_blocks)
    '''
   
def find_answer(message, say):
    key = message['text'].replace("?", "")
    key = key.strip().upper()

    if key in techDic:
        say(f"{techDic[key]}")
    else:
        say(f"등록된 용어가 없습니다.")              

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

