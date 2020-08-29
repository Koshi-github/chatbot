from spreadSheetController import SpreadSheet
import commonEnum

WORK_SHEET_NAME = "UserID"

class ModeController:
    def __init__(self,userID):
        self.sp = SpreadSheet(WORK_SHEET_NAME)
        self.userID = userID

    def getMode(self):
        targetRow = self.sp.GetDataRow(self.userID)
        if targetRow > 0:
            mode = self.sp.Read(targetRow,2)
            return commonEnum.Mode(mode)
        else:
            newRow = self.sp.GetDataBottomRow()
            self.sp.Write(newRow,1,self.userID)
            self.sp.Write(newRow,2,0)
            return commonEnum.Mode(0)

    def setMode(self,mode):
        targetRow = self.sp.GetDataRow(self.userID)
        if targetRow > 0:
            self.sp.Write(targetRow,2,commonEnum.Mode[mode])




