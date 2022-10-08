import os
import time

import camelot
from camelot.core import TableList
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

print("Parsing")

currentPage = 47
tables: [TableList] = []
while currentPage <= 14531:
    start = time.time()
    print("Scanning pages", currentPage, 'to', currentPage + 4)
    tables.append(camelot.read_pdf('celsius.pdf',
                                   pages=f'{currentPage}-{currentPage + 4}',
                                   flavor='stream',
                                   table_areas=['0,750,612,0'],
                                   edge_tol=500))
    currentPage = currentPage + 5
    end = time.time()
    print("Took: ", end - start)

print("Exporting")
dfsArray = []
for table in tables:
    for tableList in table:
        dfsArray.append(tableList.df)

dfs = pd.concat(dfsArray)
dfs = dfs.rename(columns={
    '0': 'Name',
    '1': 'Address',
    '2': 'Date',
    '3': 'Account',
    '4': 'Type',
    '5': 'Description',
    '6': 'Coin',
    '7': 'Coin Quantity',
    '8': 'USD Value',
})

# Write to csv for later import
dfs.to_csv('out.csv', index=False, header=False)

# Write directly to database
# engine = create_engine(os.environ.get('DATABASE_URL'), echo=False)
# dfs.to_sql('users', con=engine, if_exists='replace')
#
# users = engine.execute("SELECT * FROM users").fetchall()
# print(users)
