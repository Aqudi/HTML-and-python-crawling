import openpyxl
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

list = []
# 엑셀파일 열기
wb = openpyxl.load_workbook('C:/jungo2.xlsx')

ws = wb.active

sheet = wb.get_sheet_by_name('Sheet1')

for line in range(1, 230):
    print(sheet['A' + str(line)].value)
    list.append(sheet['A' + str(line)].value)

print(list)

#엑셀 파일 저장
wb.save("C:/excel_change_result.xlsx")
wb.close()
