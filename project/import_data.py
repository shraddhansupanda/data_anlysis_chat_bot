#for web scraping
import requests
#for data analysis
import pandas as pd
#for numarical calculation
import numpy as np
#for quering mysql
import sqlalchemy
try:
    #for getting the data form csv_file present in the present folder
    df=pd.read_csv('data.csv',index_col='Unnamed: 0')
#if the csv file in not present
except:
    try:
        #webscraping for getting the data
        r=requests.get('https://assets.datacamp.com/production/repositories/497/datasets/162a52b5c1991182d67391cf650bfffb33a47f54/life_expectancy_at_birth.csv')
        #create a file object f
        with open("data.csv","w+") as f:
            #putting the data in f by using request object r with file object f
            f.write(r.text)
        #putting the data in dataframe
        df=pd.read_csv('data.csv',index_col='Unnamed: 0')
    except:
        #handling the exceptation
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
        else:
            print("Data has enter to mysql database-you are now ready to rock")
