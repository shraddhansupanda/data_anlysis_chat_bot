import sqlalchemy
import re
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
def connect():
    engine=sqlalchemy.create_engine('mysql+mysqlconnector://root:taj@0810@localhost:3306/taj')
    connection=engine.connect()
    return connection
def country_name():
    connection=connect()
    df=pd.read_sql('select * from life where year=0',connection)
    df=df.iloc[:,1:]
    return df
def box_plot(country,year=1800,year1=2016):
    connection=connect()
    df=pd.read_sql('select {} from life where year between {} AND {}'.format(country,year,year1),connection)
    plt.boxplot(df['{}'.format(country)])
    plt.grid()
    plt.ylabel('year')
    plt.title('boxplot of {}'.format(country))
    plt.show()
def scatter_plot(country,year=1800,year1=2016):
    connection=connect()
    df=pd.read_sql('select {} from life where year between {} AND {}'.format(country,year,year1),connection)
    df.index=[x for x in np.arange(year,year1+1)]
    #plt.style.use('ggplot')
    plt.plot(df.index,df['{}'.format(country)])
    plt.grid()
    plt.xlabel('year')
    plt.ylabel('life_expectancy')
    plt.title('Scatter plot of {}'.format(country))
    plt.show()
def histogram(country,year=1800,year1=2016,bins=20):
    connection=connect()
    df=pd.read_sql('select {} from life where year between {} AND {}'.format(country,year,year1),connection)
    plt.hist(df['{}'.format(country)],bins)
    plt.title('Histogram of {}'.format(country))
    plt.grid()
    plt.show()
def graphical_EDA(country,year=1800,year1=2016):
    box_plot(country,year,year1)
    scatter_plot(country,year,year1)
    histogram(country,year,year1)
def avg(country,year=1800,year1=2016):
    connection=connect()
    df=pd.read_sql('select AVG({}) from life where year between {} AND {}'.format(country,year,year1),connection)
    print('{} is the Average of {}'.format(float(df.values),country))
def variance(country,year=1800,year1=2016):
    connection=connect()
    df=pd.read_sql('select VARIANCE({}) from life where year between {} AND {}'.format(country,year,year1),connection)
    print('{} is the variance of {}'.format(float(df.values),country))
def standard_deviation(country,year=1800,year1=2016):
    connection=connect()
    df=pd.read_sql('select STDDEV({}) from life where year between {} AND {}'.format(country,year,year1),connection)
    print('{} is the Standard deviation of {}'.format(float(df.values),country))
def statistical_EDA(country,year=1800,year1=2016):
    avg(country,year,year1)
    variance(country,year,year1)
    standard_deviation(country,year,year1)
def what_is(country,year):
    connection=connect()
    df=pd.read_sql('select {} from life where year = {}'.format(country,year),connection)
    print('{} is the life_expectancy'.format(float(df.values)))
def country_highest_life_expectancy(year):
    connection=connect()
    df=pd.read_sql('select * from life where year={}'.format(year),connection)
    df=df.iloc[0,1:][df.iloc[0,1:]==df.iloc[0,1:].max()]
    print('{} has highest Life_expectancey of {}'.format(df.index[0],df[0]))
def highest_life_expectancy():
    connection=connect()
    df=pd.read_sql('select * from life',con=connection)
    df1=df.iloc[:,1:]
    df2=df1.max()
    df3=df2[df2==df2.max()]
    print('{} has higest life expectancy of {}'.format(df3.index[0],df3[0]))
def predict(country_name,year):
    connection=connect()
    df=pd.read_sql('select year,{} from life where year between 1971 and 2016'.format(country_name),connection)
    x=df['year'].values.reshape(-1,1)
    y=df.iloc[:,1].values.reshape(-1,1)
    reg=LinearRegression()
    reg.fit(x,y)
    k=float(reg.predict(year))
    print('{} is the life expectancy for {} on {}'.format(k,country_name,str(year)))
