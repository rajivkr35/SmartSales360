import pandas as pd
from sqlalchemy import create_engine

# Load cleaned CSV
df = pd.read_csv("indian_ecommerce_cleaned.csv")

# MySQL connection string
user = 'root'
password = 'Rajiv95085'
host = 'localhost'
port = '3306'
database = 'ecommerce_db'

# Create SQLAlchemy engine
engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}")

# Load into MySQL (replace 'ecommerce_sales' with your table name)
df.to_sql(name='ecommerce_sales', con=engine, if_exists='replace', index=False)

print("✅ Data successfully uploaded to MySQL!")
