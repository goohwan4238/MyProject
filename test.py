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

#주석을 추가함
#주석을 추가함 2
#주석을 추가함 3
#주석을 추가함 4
#주석을 추가함 5
#주석을 추가함 6
#주석을 추가함 11
#주석을 추가함 12
#주석을 추가함 13
#주석을 추가함 14


#주석을 추가함 20
#주석을 추가함 21
#주석을 추가함 22
#주석을 추가함 22
#주석을 추가함 23
#주석을 추가함 23
