# requests 와 json 을 활용하여 slack bot 조작하기
import requests
import json
import crawling

Token = '' # 자신의 Token 입력
Channel = '#hotdeal-notice' # 메시지를 전송할 채널이름

def get_attachs(last_item):
    attachs = []
    titles, links, identifiers, infos = crawling.get_hotdeal_items()
    for title, link, identifier, info in zip(titles, links, identifiers, infos):
        if last_item >= identifier: 
            break
        attach_dict = {
            'color' : '#ff0000',
            'author_name' : 'Slack Bot',
            'title' : title,
            'title_link' : link,
            'text' : info
        }
        attachs.append([attach_dict])
    if len(identifiers) != 0:
        last_item = identifiers[0]
    return attachs, last_item

def notice_message(token, channel, text, attachments):
    attachments = json.dumps(attachments) # 리스트를 Json 으로 덤핑
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+ token},
        data={"channel": channel, "text": text ,"attachments": attachments})

def notice_messages(last_item):
    attachs, last_item = get_attachs(last_item)
    for attachment in attachs:
        notice_message(Token, Channel, "물건 메시지", attachment)
    return attachs, last_item