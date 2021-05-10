import openpyxl as p
import telegram as t
wb = p.load_workbook('database.xlsx')
articles = wb['articels']
command = input('cmd: ')

if command == 'start':
    art = input('Ведите артикул: ')
    for i in range(1, 100):
        if articles.cell(row=i, column=1).value == 'None':
            articles.cell(row=i, column=1).value = art
            print(articles.cell(row=i, column=1).value)
            break
        else:
            print('ЛОл')
            break