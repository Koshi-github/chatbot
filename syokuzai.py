from spreadSheetControler import SpreadSheet

WORK_SHEET_NAME = "sheet1"

class Syokuzai:
    def createMessage(self, message):
        returnList =[]

        sp = SpreadSheet(WORK_SHEET_NAME)
        targetRow = sp.GetDataRow(message)
        if targetRow > 0:
            ryoriName = sp.Read(targetRow,1)
            returnList.append("これが" + ryoriName + "の材料ニャン！")
            returnList.append(self.GetDataColumn(sp,targetRow))

        else:
            returnList.append("その料理は材料が登録されてないニャン（泣）")

        return returnList

    def GetDataColumn(self,sp,row):
        column = 2
        syokuzaiList = []
        while(True):
            val = sp.Read(row, column)
            if(val == ""): 
                return '\n'.join(syokuzaiList)
            else:
                syokuzaiList.append(val)
            column = column + 1
