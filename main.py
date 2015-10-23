from lib import sendMessage, getMessage
from threading import Thread
import sys

muter = True;
PY_VERSION = sys.version[0]

def loop():
    while(muter):
        data = getMessage()
        for r in data:
            chat = "[{}] {} => {}".format(r["room"], r["from"], r["text"])
            print(chat)
    print ("good bye")

t = Thread(target=loop)
t.start()

try:
    while True:
        pesan = None
        if (PY_VERSION == '2'):
            pesan = str(raw_input(""))
        else:
            pesan = input("Pesan : ").encode('ascii')
        send = sendMessage(-34961324,pesan)
        if send :
            print ("Tomonori => {}".format(pesan))
except KeyboardInterrupt:
    print ("cape coy")

muter = False
t.join()
