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
    df=pd.read_sql('select * from life where year=0',con=connection)
    del(df['year'])
    return df
def box_plot(country_name):
    country=country_name
    connection=connect()
    df=pd.read_sql('select {} from life'.format(country),con=connection)
    plt.boxplot(df['{}'.format(country)])
    plt.grid()
    plt.ylabel('year')
    plt.title('boxplot of {}'.format(country))
    plt.show()
def scatter_plot(country_name):
    country=country_name
    connection=connect()
    df=pd.read_sql('select {} from life'.format(country),con=connection)
    df.index=[x for x in np.arange(1800,2017)]
    plt.plot(df.index,df['{}'.format(country)])
    plt.grid()
    plt.xlabel('year')
    plt.ylabel('life_expectancy')
    plt.title('Scatter plot of {}'.format(country))
    plt.show()
def histogram(country_name):
    country=country_name
    connection=connect()
    df=pd.read_sql('select {} from life'.format(country),con=connection)
    plt.hist(df['{}'.format(country_name)],bins=20)
    plt.title('Histogram of {}'.format(country))
    plt.grid()
    plt.show()
def graphical_EDA(country_name):
    country=country_name
    box_plot(country)
    scatter_plot(country)
    histogram(country)
def avg(country_name):
    country=country_name
    connection=connect()
    df=pd.read_sql('select AVG({}) from life'.format(country),con=connection)
    print('{} is the Average of {}'.format(float(df.values).country))
def variance(country_name):
    country=country_name
    connection=connect()
    df=pd.read_sql('select VARIANCE({}) from life'.format(country),con=connection)
    print('{} is the variance of {}'.format(float(df.values),country))
def standard_deviation(country_name):
    country=country_name
    connection=connect()
    df=pd.read_sql('select STDDEV({}) from life'.format(country),con=connection)
    print('{} is the Standard deviation of {}'.format(float(df.values),country))
def statistical_EDA(country_name):
    country=country_name
    avg(country)
    variance(country)
    standard_deviation(country)
def what_is(year,country):
    connection=connect()
    df=pd.read_sql('select {} from life where year = {}'.format(country,year),con=connection)
    print('{} is the life_expectancy'.format(float(df.values)))
def country_highest_life_expectancy(year):
    connectin=connect()
    #df=pd.read_sql(select)
def highest_file_expectancy():
    pass
def predict(country_name)
    country=country_name
