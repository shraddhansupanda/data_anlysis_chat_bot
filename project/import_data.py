import requests
import pandas as pd
import numpy as np
import sqlalchemy
'''Geting the file into DataFrame if the file is not there
then it will download form internet
if internet is not there other then terminatin it will
return a message "please connect to internet and try again".'''
try:
    df=pd.read_csv('data.csv',index_col='Unnamed: 0')
except:
    try:
        r=requests.get('https://assets.datacamp.com/production/repositories/497/datasets/162a52b5c1991182d67391cf650bfffb33a47f54/life_expectancy_at_birth.csv')
        with open("data.csv","w+") as f:
            f.write(r.text)
        df=pd.read_csv('data.csv',index_col='Unnamed: 0')
    except:
        print("please connect to internet and try again later")
else:
    '''this is not in a format of analysis
    i.e the columns are not variable and rows are not observation
    so it will make analysis friendly dataframe'''
    df=pd.melt(df,id_vars='Life expectancy',var_name='year',value_name='expectancy')
    df=pd.pivot_table(df,index='year',columns='Life expectancy',values='expectancy',aggfunc=np.mean)
    '''due to insufficient data present in the country we have to delete
    those country from the actual data for better analysis and
    drawing graph'''
    df=df.dropna(axis=1)
    df.index.name=None
    df.columns.name=None
    df.index=[x for x in range(1800,2017)]
    df.index.name='year'
    engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:taj@0810@localhost:3306/taj')
    try:
        df.to_sql('life',engine,if_exists='replace')
    except:
        print("please make the server on with host='localhost',user_name='taj',port_number='3306' and password='taj@0810'")
