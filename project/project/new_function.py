import sqlalchemy
import re
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import time
from sklearn.linear_model import LinearRegression
def connect():
    engine=sqlalchemy.create_engine('mysql+mysqlconnector://root:taj@0810@localhost:3306/taj')
    connection=engine.connect()
    return connection
def country_name():
    connection=connect()
    df=pd.read_sql('select * from life where year=0',connection)
    df=df.iloc[:,1:]
    df=list(df)
    return df
def box_plot(country,year=1800,year1=2016):
    if len(country)==1:
        country=country[0]
        connection=connect()
        df=pd.read_sql('select {} from life where year between {} AND {}'.format(country,year,year1),connection)
        plt.boxplot(df['{}'.format(country)])
        plt.grid()
        plt.xlabel(country)
        plt.ylabel('year')
        plt.title('boxplot of {}'.format(country))
        plt.show()
    if len(country)==2:
        country1=country[0]
        country2=country[1]
        connection=connect()
        df=pd.read_sql('select {} from life where year between {} AND {}'.format(country1,year,year1),connection)
        grid=plt.GridSpec(1,2)
        plt.subplot(grid[0,0])
        plt.boxplot(df['{}'.format(country1)])
        plt.grid()
        plt.xlabel(country1)
        plt.ylabel('year')
        plt.title('boxplot of {}'.format(country1))
        plt.subplot(grid[0,1])
        df=pd.read_sql('select {} from life where year between {} AND {}'.format(country2,year,year1),connection)
        plt.boxplot(df['{}'.format(country2)])
        plt.grid()
        plt.xlabel(country2)
        plt.ylabel('year')
        plt.title('boxplot of {}'.format(country2))
        plt.tight_layout()
        time.sleep(0.3)
        plt.show()
def scatter_plot(country,year=1800,year1=2016):
    if len(country)==1:
        country=country[0]
        connection=connect()
        df=pd.read_sql('select {} from life where year between {} AND {}'.format(country,year,year1),connection)
        df.index=[x for x in np.arange(year,year1+1)]
        #plt.style.use('ggplot')
        plt.plot(df.index,df['{}'.format(country)])
        plt.grid()
        plt.xlabel('year')
        plt.ylabel('life_expectancy')
        plt.title('Scatter plot of {}'.format(country))
        time.sleep(0.3)
        plt.show()
    if len(country)==2:
        connection=connect()
        country1=country[0]
        country2=country[1]
        df=pd.read_sql('select {} from life where year between {} AND {}'.format(country1,year,year1),connection)
        df.index=[x for x in np.arange(year,year1+1)]
        #plt.style.use('ggplot')
        grid=plt.GridSpec(2,1)
        plt.subplot(grid[0,0])
        plt.plot(df.index,df['{}'.format(country1)])
        plt.grid()
        plt.xlabel('year')
        plt.ylabel('life_expectancy')
        plt.title('Scatter plot of {}'.format(country1))
        df=pd.read_sql('select {} from life where year between {} AND {}'.format(country2,year,year1),connection)
        df.index=[x for x in np.arange(year,year1+1)]
        #plt.style.use('ggplot')
        plt.subplot(grid[1,0])
        plt.plot(df.index,df['{}'.format(country2)])
        plt.grid()
        plt.xlabel('year')
        plt.ylabel('life_expectancy')
        plt.title('Scatter plot of {}'.format(country2))
        plt.tight_layout()
        time.sleep(0.3)
        plt.show()
def histogram(country,year=1800,year1=2016,bins=20):
    connection=connect()
    df=pd.read_sql('select {} from life where year between {} AND {}'.format(country,year,year1),connection)
    plt.hist(df['{}'.format(country)],bins)
    plt.title('Histogram of {}'.format(country))
    plt.xlabel('Life expectancy')
    plt.grid()
    time.sleep(0.3)
    plt.show()
def graphical_EDA(country,year=1800,year1=2016):
    grid=plt.GridSpec(2,2)
    plt.subplot(grid[0,0])
    connection=connect()
    df=pd.read_sql('select {} from life where year between {} AND {}'.format(country,year,year1),connection)
    plt.boxplot(df['{}'.format(country)])
    plt.grid()
    plt.xlabel(country)
    plt.ylabel('year')
    plt.title('boxplot of {}'.format(country))
    plt.subplot(grid[0,1])
    connection=connect()
    df=pd.read_sql('select {} from life where year between {} AND {}'.format(country,year,year1),connection)
    plt.hist(df['{}'.format(country)],bins=20)
    plt.title('Histogram of {}'.format(country))
    plt.xlabel('Life expectancy')
    plt.grid()
    plt.subplot(grid[1,0:])
    connection=connect()
    df=pd.read_sql('select {} from life where year between {} AND {}'.format(country,year,year1),connection)
    df.index=[x for x in np.arange(year,year1+1)]
    #plt.style.use('ggplot')
    plt.plot(df.index,df['{}'.format(country)])
    plt.grid()
    plt.xlabel('year')
    plt.ylabel('life_expectancy')
    plt.title('Scatter plot of {}'.format(country))
    plt.tight_layout()
    time.sleep(0.3)
    plt.show()
def avg(country,year=1800,year1=2016):
    connection=connect()
    df=pd.read_sql('select AVG({}) from life where year between {} AND {}'.format(country,year,year1),connection)
    time.sleep(0.3)
    if year==1800 and year1==2016:
        print('{} is the Average of {}'.format(float(df.values),country))
    else:
        print('{} is the Average of {} from {} to {}'.format(float(df.values),country,year,year1))
def variance(country,year=1800,year1=2016):
    connection=connect()
    df=pd.read_sql('select VARIANCE({}) from life where year between {} AND {}'.format(country,year,year1),connection)
    time.sleep(0.3)
    if year==1800 and year1==2016:
        print('{} is the variance of {}'.format(float(df.values),country))
    else:
        print('{} is the variance of {} from {} to {}'.format(float(df.values),country,year,year1))
def standard_deviation(country,year=1800,year1=2016):
    connection=connect()
    df=pd.read_sql('select STDDEV({}) from life where year between {} AND {}'.format(country,year,year1),connection)
    time.sleep(0.3)
    if year==1800 and year1==2016:
        print('{} is the Standard deviation of {}'.format(float(df.values),country))
    else:
        print('{} is the Standard deviation of {} from {} to {}'.format(float(df.values),country,year,year1))
def statistical_EDA(country,year=1800,year1=2016):
    avg(country,year,year1)
    variance(country,year,year1)
    standard_deviation(country,year,year1)
def what_is(country,year):
    connection=connect()
    df=pd.read_sql('select {} from life where year = {}'.format(country,year),connection)
    time.sleep(0.3)
    print('{} is the life_expectancy of {} on {}'.format(float(df.values),country,year))
def highest_life_expectancy_of_country(country):
    connection=connect()
    df=pd.read_sql('select year,{} from life where {}=(select max({}) from life)'.format(country,country,country),connection)
    time.sleep(0.3)
    print('{} is the max life expectancy for {} on {}'.format(df['{}'.format(country)].values[0],country,df['year'].values[0]))
def lowest_life_expectancy_of_country(country):
    connection=connect()
    df=pd.read_sql('select year,{} from life where {}=(select min({}) from life)'.format(country,country,country),connection)
    time.sleep(0.3)
    print('{} is the min life expectancy for {} on {}'.format(df['{}'.format(country)].values[0],country,df['year'].values[0]))
def country_highest_life_expectancy(year):
    connection=connect()
    df=pd.read_sql('select * from life where year={}'.format(year),connection)
    df=df.iloc[0,1:][df.iloc[0,1:]==df.iloc[0,1:].max()]
    for i in range(len(df)):
        time.sleep(0.5)
        print('{} has highest Life_expectancey of {} on {}'.format(df.index[i],df[i],year))
def country_lowest_life_expectancy(year):
    connection=connect()
    df=pd.read_sql('select * from life where year={}'.format(year),connection)
    df=df.iloc[0,1:][df.iloc[0,1:]==df.iloc[0,1:].min()]
    for i in range(len(df)):
        time.sleep(0.5)
        print('{} has lowest Life_expectancey of {} on {}'.format(df.index[i],df[i],year))
def highest_life_expectancy():
    connection=connect()
    df=pd.read_sql('select * from life',con=connection)
    df1=df.iloc[:,1:]
    df2=df1.max()
    df3=df2[df2==df2.max()]
    for i in range(len(df3)):
        time.sleep(0.5)
        print('{} has highest life expectancy of {}'.format(df3.index[i],df3[i]))
def lowest_life_expectancy():
    connection=connect()
    df=pd.read_sql('select * from life',con=connection)
    df.index=df.iloc[:,0]
    df1=df.iloc[:,1:]
    df2=df1.min()
    df3=df2[df2==df2.min()]
    for i in range(len(df3)):
        year=int(df1[df1[df3.index[i]]==df3[i]].index.values)
        time.sleep(0.5)
        print('{} has lowest life expectancy of {} on {}'.format(df3.index[i],df3[i],year))
def predict(country,year):
    connection=connect()
    df=pd.read_sql('select year,{} from life where year between 1971 and 2016'.format(country),connection)
    x=df['year'].values.reshape(-1,1)
    y=df.iloc[:,1].values.reshape(-1,1)
    reg=LinearRegression()
    reg.fit(x,y)
    k=float(reg.predict(year))
    time.sleep(0.3)
    print('{} is the life expectancy for {} on {}'.format(k,country,str(year)))
