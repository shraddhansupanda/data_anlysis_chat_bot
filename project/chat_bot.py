from new_function import *
import re
#To get the input from the user
x=input()
#To lower case the word and split it and store it in a list
y=x.lower().split()
#To make the country in lower case
con=[x.lower() for x in list(country_name())]
#To find year in the string
def year():
    pattern=re.compile('\d{4}')
    years=re.findall(pattern,x)
    if len(years) == 1:
        year=int(years[0])
        return year
    if len(years)==2:
        year=int(years[0])
        year1=int(years[1])
        return year,year1
    if len(years)==0:
        return 1800,2016
#To find country name in the string
def common_member():
    a_set = set(y)
    b_set = set(con)
    if len(a_set.intersection(b_set)) > 0:
        return(list(a_set.intersection(b_set))[0])
if 'country' and 'name' in y:
    print(country_name())
if 'box' in y and 'plot' in y:
    box_plot(common_member(),*year())
if 'scatter' in y and 'plot' in y:
    scatter_plot(common_member(),*year())
if 'histogram' in y:
    histogram(common_member(),*year())
if 'graphical' in y and 'eda' in y:
    graphical_EDA(common_member(),*year())
if 'average' in y or 'avg' in y:
    avg(common_member(),*year())
if 'variance' in y or 'var' in y:
    variance(common_member(),*year())
if 'standard deviation' in y or 'std' in y:
    standard_deviation(common_member(),*year())
if ('statistical' in y and 'eda' in y) or ('statistical' and 'exploritory' and 'data' and 'analysis' in y):
    statistical_EDA(common_member(),*year())
if 'what' in y and (('life' in y and'expectancy' in y) or 'le' in y) and 'predict' not in y and 'will' not in y:
    what_is(common_member(),year())
if 'which' in y and 'country' in y and 'highest' in y and (('life' in y and 'expectancy' in y) or 'le' in y) and 'on' in y:
    country_highest_life_expectancy(year())
if 'which' in y and 'country' in y and 'highest' in y and (('life' in y and 'expectancy' in y) or 'le' in y):
    highest_life_expectancy()
if 'predict' in y or 'will' in y:
    predict(common_member(),year())
