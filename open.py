import openpyxl
from openpyxl import Workbook, load_workbook

wb =load_workbook("record.xlsx")

wb.save("record.xlsx")
print(wb)
