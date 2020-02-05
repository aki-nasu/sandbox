import openpyxl as xl

FILE_NAME = 'd:/dev/sandbox/record_costs/costs.xlsx'
SHEET_NAME = 'Sheet1'

# add
def add_row(sheet,data):
    r = str(sheet.max_row + 1)
    sheet['A'+r] = data[0]
    sheet['B'+r] = data[1]
    sheet['C'+r] = data[2]
    sheet['D'+r] = data[3]
    return

# mod(TBD)
# del(TBD)

def w_xl(data):
    wb = xl.load_workbook(FILE_NAME)
    sheet = wb.get_sheet_by_name(SHEET_NAME)
    add_row(sheet,data)
    # save
    wb.save(FILE_NAME)
    return