import pandas as pd

# Load your large DataFrame
df = pd.read_csv('input.csv')

# Determine how many smaller DataFrames you need
num_parts = len(df) // 1048576 + 1

# Create a new Excel writer object
with pd.ExcelWriter('output.xlsx') as writer:
    for i in range(num_parts):
        # Extract the part of the DataFrame that fits into a Excel sheet
        df_part = df[i * 1048576:(i + 1) * 1048576 - 1]

        # Write it to a new sheet in the workbook
        df_part.to_excel(writer, sheet_name=f'sheet_{i + 1}', index=False)
        
        # Print progress
        print(f"Progress: {(i + 1) / num_parts * 100:.2f}%")
