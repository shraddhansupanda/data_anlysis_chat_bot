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
def box_plot(country):
    connection=connect()
    df=pd.read_sql('select {} from life'.format(country),connection)
    plt.boxplot(df['{}'.format(country)])
    plt.grid()
    plt.ylabel('year')
    plt.title('boxplot of {}'.format(country))
    plt.show()
def scatter_plot(country):
    connection=connect()
    df=pd.read_sql('select {} from life'.format(country),connection)
    df.index=[x for x in np.arange(1800,2017)]
    #plt.style.use('ggplot')
    plt.plot(df.index,df['{}'.format(country)])
    plt.grid()
    plt.xlabel('year')
    plt.ylabel('life_expectancy')
    plt.title('Scatter plot of {}'.format(country))
    plt.show()
def histogram(country):
    connection=connect()
    df=pd.read_sql('select {} from life'.format(country),connection)
    plt.hist(df['{}'.format(country)],bins=20)
    plt.title('Histogram of {}'.format(country))
    plt.grid()
    plt.show()
def graphical_EDA(country):
    box_plot(country)
    scatter_plot(country)
    histogram(country)
def avg(country):
    connection=connect()
    df=pd.read_sql('select AVG({}) from life'.format(country),connection)
    print('{} is the Average of {}'.format(float(df.values),country))
def variance(country):
    connection=connect()
    df=pd.read_sql('select VARIANCE({}) from life'.format(country),connection)
    print('{} is the variance of {}'.format(float(df.values),country))
def standard_deviation(country):
    connection=connect()
    df=pd.read_sql('select STDDEV({}) from life'.format(country),connection)
    print('{} is the Standard deviation of {}'.format(float(df.values),country))
def statistical_EDA(country):
    avg(country)
    variance(country)
    standard_deviation(country)
def what_is(year,country):
    connection=connect()
    df=pd.read_sql('select {} from life where year = {}'.format(country,year),connection)
    print('{} is the life_expectancy'.format(float(df.values)))
    #def predict(country_name):
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
    print('{} is the life_expectancy for {} on {}'.format(k,country_name,str(year)))
