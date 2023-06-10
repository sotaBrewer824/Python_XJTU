import pandas as pd

def xlsx_to_csv(filename):
    data_xls = pd.read_excel(filename, index_col=0)
    data_xls.to_csv('target_csv.csv', encoding='utf-8')

def csv_to_xlsx(filename):
    data_csv = pd.read_csv(filename,  encoding='utf-8')
    data_csv.to_excel('target_excel.xlsx', sheet_name='data')