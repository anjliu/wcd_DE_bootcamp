#!/usr/bin python3
"""
This is the main file for the lambda project. It will be used in EC2 IAM role situation
"""
import sqlalchemy as db
import pandas as pd
import subprocess
import toml
import os
from dotenv import load_dotenv
from collections.abc import Mapping

def mysql_connect(host, user, password, database, port,schema):
    """
    Connect to the database
    """
    engine = db.create_engine(f'mysql+mysqlconnector://{user}:{password}@{database}.{host}:{port}/{schema}')
    # engine = db.create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{schema}')
    return engine

if __name__=="__main__": 
    specs = toml.load('specs.toml')

    host=specs['db']['host']
    port=specs['db']['port']
    database=specs['db']['database']
    schema=specs['db']['schema']

    bucket=specs['s3']['bucket']
    folder=specs['s3']['folder']

    load_dotenv()
    user=os.getenv('wcd_user')
    password=os.getenv('wcd_password')


    sql="""
        select customerID, sum(sales) sum_sales
        from orders
        group by 1
        order by 2 desc
        limit 10;
    """
    engine = mysql_connect(host, user, password, database, port,schema)

    df = pd.read_sql(sql, con = engine)
    df[["customerID"]].head()
    df[["customerID"]].to_json('customer_id.json')

    subprocess.call(['aws','s3','cp','customer_id.json', f's3://{bucket}/{folder}/customer_id.json'])