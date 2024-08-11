import pandas as pd
import re

excel_file = pd.ExcelFile('D:/HE/cabinettest.xlsx', engine= 'openpyxl')
writer = pd.ExcelWriter('D:/HE/cabinettest.xlsx', engine='openpyxl')


pattern = re.compile(r'abc-c(\d{2})-')
def replace_with_prefixed_zero(text):
    return re.sub(pattern, lambda match: f'abc-c0{match.group(1)}-', text)

try:
    # Load the workbook
    excel_file = pd.ExcelFile('D:/HE/cabinettest.xlsx', engine='openpyxl')
except Exception as e:
    print(f"Error loading Excel file: {e}")
    exit()

for sheet_name in excel_file.sheet_names:
    try:
        df = pd.read_excel(excel_file, sheet_name=sheet_name)
        print(f"Processing sheet: {sheet_name}")
        for row_index, row in df.iterrows():
            for col_index, cell in row.iteritems():
                cell_str = str(cell)
                if 'abc-c' in cell_str:
                    replaced_str = replace_with_prefixed_zero(cell_str)
                    df.at[row_index, col_index] = replaced_str
        df.to_excel(writer, sheet_name=sheet_name, index=False)
    except Exception as e:
        print(f"Error processing sheet '{sheet_name}': {e}")

writer.save()

'''
    filtered_df = df[df.apply(lambda row: row.astype(str).str.contains('abc-c').any(), axis=1)]
    if not filtered_df.empty:
        for row in filtered_df.itertuples(index=False):
            for cell in row:
                cell_str = str(cell)
                if 'abc-c' in cell_str:
                    replaced_str = replace_with_prefixed_zero(cell_str)
                    print(replaced_str)
                    print(row)
    
    else:
        print("No rows contain 'abc-c' in this sheet.")
'''