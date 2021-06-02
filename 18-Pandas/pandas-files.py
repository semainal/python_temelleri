import sqlite3
import pandas as pd

# df = pd.read_csv("sample.csv")
# df = pd.read_json("sample.json", encoding = "UTF-8")
# df = pd.read_excel("sample.xlsx")

connection = sqlite3.connect("sample.db")
df = pd.read_sql_query("SELECT * FROM students", connection)


print(df)
