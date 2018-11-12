import xlwt
import xlrd
from xlrd import open_workbook 
from xlutils.copy import copy
def createExcelFromTemplate(excelName,dayStr,sheetDataList):
	cf = Utils.getConf("excel")
	sheetLength = int(cf.get(excelName,"sheetLength"))
	templatePath = os.path.join(os.path.abspath(os.path.dirname(__file__)), "./template/%s.xls" % excelName)
	targetPath = Utils.excelPath+"/%s-%s.xls" %(excelName,dayStr)
	rb = open_workbook(templatePath)
    #通过sheet_by_index()获取的sheet没有write()方法
	wb = copy(rb) #通过get_sheet()获取的sheet有write()方法
	for idx in range(0,sheetLength):
		sheetColumn = cf.get(excelName,"sheet%s_column" % idx)
		columnIdxList = [int(x) for x in sheetColumn.split(",")]
		sheetStartIdx = int(cf.get(excelName,"sheet%s_startIdx" % idx))
		ws = wb.get_sheet(idx)
		insertList = sheetDataList[idx]
		for data in insertList:
			try:
				newData =[]
				for newIdx in columnIdxList:
					newData.append(data[newIdx])
					writeRow(ws,sheetStartIdx,newData,{})
				sheetStartIdx +=1
			except:
				pass
	wb.save(targetPath)            
 


