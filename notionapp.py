# 8/17 커밋
# 8/17 커밋2

from notion_client import Client
from datetime import datetime, timezone

NOTION_TOKEN = 'secret_cjeUfDIlGbQEsQrXka3hdeb09xvocP01kVYc8C09DGf'
DATABASE_ID = 'c3527cec13264369919a055a7c6f2ce7'

notion = Client(auth=NOTION_TOKEN)

db = notion.databases.retrieve(DATABASE_ID)
pgid = "90eba0f1bf7049feb16964350135ba97"
pg = notion.pages.retrieve(pgid)

print(pg['id'])
beforedepart = pg['properties']["Department"]["select"]["name"]
print(f"before :{beforedepart}")

notion.pages.update(page_id=pgid, 
                    properties= {
                    "Department": {
                         "select": {
                             "name": "엔진개발"
					        }
                        }   
					},
                )


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


afterdepart = pg['properties']["Department"]["select"]["name"]
print(f"after :{afterdepart}")




#notion.pages.update

'''
response = notion.pages.create(
			parent = {"database_id": DATABASE_ID},			
			properties= {
                    "Name": {
                         "title":[{
                              "text": {"content": "New Task"}
						 }]
					},
                    "Department": {
                         "select": {
                             "name": "UI개발"
					    }
                    }
					
			},
            children= [{"paragraph": {
								"color": "default",
								'rich_text': [{'annotations': {'bold': False,
																'code': False,
																'color': 'default',
																'italic': False,
																'strikethrough': False,
																'underline': False},
												'href': None,
												'plain_text': "test body",
												'text': {'content': f"test body", 'link': None},
												'type': 'text'},],
						}                      
					}]
            )
'''
