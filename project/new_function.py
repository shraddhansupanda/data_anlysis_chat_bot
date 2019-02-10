import sqlalchemy
import re
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
def connect():
    engine=sqlalchemy.create_engine('mysql+mysqlconnector://root:taj@0810@localhost:3306/taj')
    connection=engine.connect()
    return connection
def box_plot(country_name):
    country=country_name
    connection=connect()
    df=pd.read_sql('select {} from life'.format(country),con=connection)
    plt.boxplot(df['{}'.format(country)])
    plt.grid()
    plt.ylabel('year')
    plt.title('boxplot')
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
