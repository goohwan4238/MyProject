techDic = {}
techDic["hello"] = "this is answer for ''hello''"
techDic["MRP"] = "MRP is acronyms of 'Material Requirement Planning'."

message = {}
message['text'] = '? MRP'

key = message['text'].replace("?", "")
key = key.strip()

print(key)
print(techDic)

if key in techDic:
    print(f"{techDic[key]}")
else:
    print(f"등록된 용어가 없습니다.")           

print(techDic)

message = "test,this is summary of test"
msglist = message.split(',')
if msglist[0] not in techDic:
    techDic[msglist[0].strip()] = msglist[1]

print(techDic)