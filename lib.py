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
    chat = []
    data = {
        "offset":lastMessageId,
    }
    try:
        bot = requests.post(getMsgUrl,data=data)
        if bot.status_code == 200:
            msg = bot.json()
            panjang = len(msg['result'])
            for pesan in msg['result']:
                result = {
                    "room":pesan["message"]["chat"]["title"],
                    "from":pesan["message"]["username"],
                    "chat":pesan["message"]["text"],
                    "time":pesan["message"]["date"]
                }
                chat.append(result)
            lastMessageId = msg['result'][panjang-1]['update_id'] + 1
    except:
        print ("Unexpected error:", sys.exc_info()[0])
    return chat
