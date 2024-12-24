import pandas as pd
import pymysql

from integrate_lists_2 import output_file

# Use f-string to insert variables
file_path = f"/users/lilianlee/{output_file}"

# Read CSV file
df = pd.read_csv(file_path)

df = df.fillna(0)  # Replace NaN values ​​with 0

# Establish MySQL connection
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="coffee",
)

cursor = connection.cursor()

#Insert data
for index, row in df.iterrows():
    sql = """
    INSERT INTO coffee.coffee_roasting_database (timestamp, time, temp1, temp2, bean_type, process_type) 
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, tuple(row))

# Submit and close
connection.commit()
cursor.close()
connection.close()

print("Data successfully inserted!")

