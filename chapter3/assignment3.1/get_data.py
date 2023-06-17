import requests as rq 
import pandas as pd 
import json

response = rq.get('https://www.themuse.com/api/public/jobs?page=50')
dt = response.text
dic = json.loads(dt)