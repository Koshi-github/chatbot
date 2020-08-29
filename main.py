from syokuzai import Syokuzai
from kurashiru import Kurashiru
from tenki import Tenki
from modeController import ModeController
import commonEnum

def execute(message, userID):
    returnMessage = []

    modeController = ModeController(userID)
    mode = modeController.getMode()

    if("食材" in message):
        modeController.setMode(commonEnum.Mode.SYOKUZAI)
        returnMessage.append("何の材料が知りたいニャン？")
        return returnMessage
    
    elif("クラシル" in message):
        modeController.setMode(commonEnum.Mode.KURASHIRU)
        returnMessage.append("何の料理を検索するニャン？")
        return returnMessage

    try:

        if ("天気" in message):
            tenki = Tenki()
            returnMessage = tenki.createMessage(message)

        elif (mode == commonEnum.Mode.SYOKUZAI):
            syokuzai = Syokuzai()
            returnMessage = syokuzai.createMessage(message)

        elif (mode == commonEnum.Mode.KURASHIRU):
            kurashiru = Kurashiru()
            returnMessage = kurashiru.createMessage(message)

        else:
            returnMessage.append(message)
        
        return returnMessage
    
    except Exception as e:
        return str(e)
