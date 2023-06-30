#%% import stuff
import requests as rq 
import pandas as pd 
import json
import boto3
import toml
import os

if __name__=='__main__':
    specs = toml.load('specs.toml') 
    #%% get data
    print('Downloading data...')
    response = rq.get('https://www.themuse.com/api/public/jobs?page=50')
    dt = response.text
    dic = json.loads(dt)
    print('Data downloaded.')
    # %% convert to dataframe
    print('Processing data...')
    df = pd.json_normalize(dic['results'])
    # split locations to city and state/country
    df['city'] = df.locations.map(lambda x: x[-1]['name'].split(',')[0])
    df['country'] = df.locations.map(lambda x: x[-1]['name'].split(',')[1])
    df['date'] = pd.to_datetime(df.publication_date).dt.date
    df = df[[
        'company.name'
        ,'country'
        ,'city'
        ,'name'
        ,'type'
        ,'date'
    ]].rename({
        'name':'job_name'
        ,'type':'job_type'
        ,'company.name':'company_name'
    })
    # %% export to csv
    df.to_csv('jobs.csv')
    print('Data processed and saved locally.')
    #%% Upload to S3
    # access_key=os.getenv('access_key')
    # secret_access_key=os.getenv('secret_access_key')
    bucket = specs['aws']['bucket']
    folder = specs['aws']['folder']
    s3 = boto3.client('s3')
    s3.upload_file('jobs.csv', bucket, folder+'jobs.csv')

    print('File uploaded.')
