import pandas as pd

# Load the Excel file
file_path = 'Downloads/CSMD202.xlsx'
excel_data = pd.ExcelFile(file_path)

# Display sheet names to understand the structure
sheet_names = excel_data.sheet_names
sheet_names
