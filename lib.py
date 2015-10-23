import requests
import sys

# config
key = "106833625:AAEWW14xxZqrHdhkIbgtT9aYVPvUHAeS18w"

# set url
headers = {"Content-type": "application/x-www-form-urlencoded"}
url = "https://api.telegram.org/bot"
sendMsgUrl = url + key + "/sendMessage"
getMsgUrl = url + key + "/getUpdates"
lastMessageId = 0;

def sendMessage(chatId, text):
    data = {"chat_id":chatId,"text":text}
    r = requests.post(sendMsgUrl,data=data)
    if r.status_code != 200:
        return True
    else:
        return False

def getMessage():
    global lastMessageId
    chat = []
    data = {
        "offset":lastMessageId,
    }
    bot = requests.post(getMsgUrl,data=data)
    if bot.status_code == 200:
        msg = bot.json()
        panjang = len(msg['result'])
        if (panjang > 0):
            for i in range(panjang):
                pesan = msg['result'][i]
                room  = pesan["message"]["chat"]["title"].encode('utf-8')
                from_ = pesan["message"]["from"]["username"].encode('utf-8')
                text  = pesan["message"]["text"].encode('utf-8')
                time  = pesan["message"]["date"]
                result = {
                    "room":room,
                    "from":from_,
                    "text":text,
                    "time":time
                }
                chat.append(result)
            lastMessageId = msg['result'][panjang-1]['update_id'] + 1
    return chat
