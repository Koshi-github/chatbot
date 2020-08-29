from syokuzai import Syokuzai
from kurashiru import Kurashiru
from tenki import Tenki

def execute(message, userID):
    mode = 2
    returnMessage = []

    if (mode == 1):
        s = Syokuzai()
        returnMessage = s.createMessage(message)

    elif (mode == 2):
        k = Kurashiru()
        returnMessage = k.createMessage(message)

    elif ("天気" in message):
        t = Tenki()
        returnMessage = t.createMessage(message)

    else:
        returnMessage.append(message)

    return returnMessage