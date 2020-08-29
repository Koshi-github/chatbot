import gspread
import json
#ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
from oauth2client.service_account import ServiceAccountCredentials

SCOPE = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
KEY_FILE = 'gspread-test-285207-d7f0e41d76af.json'
SPREAD_SHEET_KEY = '105mTAD0oza2j12_4ZySeXMoBrPOLw3scdG5unXVmgm8'

class SpreadSheet:
    def __init__(self,workSheetName):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE, SCOPE)
        gc = gspread.authorize(credentials)
        self.WorkBook = gc.open_by_key(SPREAD_SHEET_KEY)

        self.SheetUpdate(workSheetName)

    def SheetUpdate(self,workSheetName):
        self.WorkSheet = self.WorkBook.worksheet(str(workSheetName))

    def Read(self,row,colm):
        val = self.WorkSheet.cell(row,colm).value
        return val

    def Write(self,row,colm,val):
        self.WorkSheet.update_cell(row,colm,val)
        # self.SheetUpdate()
    
    def GetDataRow(self,ryoriName):
        row = 1
        while(True):
            val = self.Read(row,1)
            if(val == ryoriName): 
                return row
            if(val == ""): 
                return 0
            row = row + 1

    def GetDataBottomRow(self):
        row = 1
        while(True):
            val = self.Read(row,1)
            if(val == ""): 
                return row
            row = row + 1