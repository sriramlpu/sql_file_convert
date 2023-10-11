import pandas as pd
# Load the XLSX file
xlsx_file_path = r"c:\Users\mujay\Downloads\guntur3 adb list.xlsx"
data = pd.read_excel(xlsx_file_path)

# Specify the output SQL file
output_sql_file = 'excel16.sql'

# Open the output SQL file in write mode with UTF-8 encoding
with open(output_sql_file, 'w', encoding='utf-8') as sql_file:
    for index, row in data.iterrows():
        name = row['name'] if not pd.isna(row['name']) else ''
        address = row['address'] if not pd.isna(row['address']) else ''
        qualif = row['qualif'] if not pd.isna(row['qualif']) else ''
        wdays = row['wdays'] if not pd.isna(row['wdays']) else ''
        email = row['email'] if not pd.isna(row['email']) else ''
        eid = int(row['eid'] ) if not pd.isna(row['eid']) else ''
        timings = row['timings'] if not pd.isna(row['timings']) else ''
        spid = int(row['spid']) if not pd.isna(row['spid']) else 0
        cid = int(row['cid']) if not pd.isna(row['cid']) else 0
        did = int(row['did']) if not pd.isna(row['did']) else 0
        ntm = int(row['ntm']) if not pd.isna(row['ntm']) else 0
        phone = row['phone'] if not pd.isna(row['phone']) else ''
        hosp = row['hosp'] if not pd.isna(row['hosp']) else ''
        dob=row['dob'] if not pd.isna(row['dob']) else ''
        gender=row['gender'] if not pd.isna(row['gender']) else ''
        
        sql_statement = f"INSERT INTO doctors ( name,address,phone,did,cid,spid,eid,ntm,wdays,email,hosp,qualif,dob,timings,gender) VALUES ('{name}','{address}','{phone}',{did},{cid},{spid},{eid},{ntm},'{wdays}','{email}','{hosp}','{qualif}','{dob}','{timings}','{gender}');\n"
        sql_file.write(sql_statement)

print(f"SQL data saved to {output_sql_file}")													
