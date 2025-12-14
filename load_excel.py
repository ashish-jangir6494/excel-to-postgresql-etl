import pandas as pd
from sqlalchemy import create_engine

# 1️⃣ PostgreSQL connection
engine = create_engine(
    'postgresql://postgres:admin@localhost:5432/project_1_db'
)

# 2️⃣ Excel file load karo
excel_file = pd.ExcelFile("Profit_Leakage_Dataset_Last.xlsx")

# 3️⃣ Saari sheet ke naam dekho
print(excel_file.sheet_names)

# 4️⃣ Har sheet ko PostgreSQL table me daalo
for sheet in excel_file.sheet_names:
    df = pd.read_excel(excel_file, sheet_name=sheet)

    # table name clean (space → underscore)
    table_name = sheet.lower().replace(" ", "_")

    df.to_sql(
        table_name,
        engine,
        if_exists='replace',   # table already ho to overwrite
        index=False
    )

    print(f"Loaded sheet: {sheet} → table: {table_name}")
