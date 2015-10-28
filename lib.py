import requests
import sys

lastMessageId = 0;
url = "https://api.telegram.org/bot"

def sendMessage(chatId, text, key):
    sendMsgUrl = url + key + "/sendMessage"
    data = {
        "chat_id" : chatId,
        "text" : text,
        "parse_mode" : "markdown",
        "disable_web_page_preview" : 1
    }
    r = requests.post(sendMsgUrl,data=data)
    if r.status_code != 200:
        return True
    else:
        return False

def getMessage(key):
    getMsgUrl = url + key + "/getUpdates"
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
                try:
                    pesan = msg['result'][i]["message"]
                    room  = pesan["chat"]["title"].encode('utf-8')
                    from_ = pesan["from"]["username"].encode('utf-8')
                    text  = pesan["text"].encode('utf-8')
                    time  = pesan["date"]
                    result = {
                        "room":room,
                        "from":from_,
                        "text":text,
                        "time":time
                    }
                    chat.append(result)
                except:
                    pass
            lastMessageId = msg['result'][panjang-1]['update_id'] + 1
    return chat
