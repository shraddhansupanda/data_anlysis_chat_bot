import sqlalchemy
import re
import matplotlib.pyplot as plt
import pandas as pd

class country:
    def __init__(self):
        self.engine=sqlalchemy.create_engine('mysql+mysqlconnector://root:taj@0810@localhost:3306/taj')
        self.connection=self.engine.connect()
    def country_name(self):
        self.df=pd.read_sql('select * from life',con=self.connection)
        self.ls=list(self.df.columns)
        self.ls.remove('year')
        return self.ls
    '''def is_country_name(self,name):
        name=str(name)
        self.df=pd.read_sql('select * from life where year=0',con=self.connection)
        self.ls=list(self.df.columns)
        self.ls.remove('year')
        self.find=''
        pattern=re.compile(self.name,re.I)
        for x in self.ls:
            if pattern.search(x) != None:
                self.find=self.name
        if self.find!=None:
            return str(self.find)+' is there'
        else:
            return 'No such country found'''




#class graphical_EDA:
    #def
