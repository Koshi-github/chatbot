from syokuzai import Syokuzai
from kurashiru import Kurashiru
from tenki import Tenki

def execute(message, userID):
    mode = 2
    returnMessage = []

    try:

        if ("天気" in message):
            t = Tenki()
            returnMessage = t.createMessage(message)

        elif (mode == 1):
            s = Syokuzai()
            returnMessage = s.createMessage(message)

        elif (mode == 2):
            k = Kurashiru()
            returnMessage = k.createMessage(message)

        else:
            returnMessage.append(message)
        
        return returnMessage
    
    except Exception as e:
        return str(e)
