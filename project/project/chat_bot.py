from new_function import *
import re
print('                      welcome to Data Analysis Chat-Bot')
print('                             Ask your question')
#To make the country in lower case
con=[x.lower() for x in list(country_name())]
#To make the program excecute repeatedly
while True:
    #To get the input from the user
    x=input('Q:-')
    #To lower case the word and split it and store it in a list
    y=x.lower().split()
    try:
        #To find year in the string
        def year():
            pattern=re.compile(r'\b\d{4}\b')
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
        #to find the bins for histogram in the string
        def bin():
            pattern=re.compile(r'\b\d{1,3}\b')
            bins=re.findall(pattern,x)
            if len(bins) == 1:
                return int(bins[0])
            else:
                return 20
        #To find country name in the string
        def common_member():
            a_set = set(y)
            b_set = set(con)
            if len(a_set.intersection(b_set)) > 0:
                return(list(a_set.intersection(b_set)))
        if 'country' and 'name' in y:
            print(country_name())
        if 'box' in y and 'plot' in y:
            box_plot(common_member(),*year())
        if 'scatter' in y and 'plot' in y:
            scatter_plot(common_member(),*year())
        if 'histogram' in y:
            histogram(common_member(),*year(),int(bin()))
        if 'graphical' in y and 'eda' in y:
            graphical_EDA(common_member()[0],*year())
        if 'average' in y or 'avg' in y:
            avg(common_member(),*year())
        if 'variance' in y or 'var' in y:
            variance(common_member(),*year())
        if 'standard deviation' in y or 'std' in y:
            standard_deviation(common_member(),*year())
        if ('statistical' in y and 'eda' in y) or ('statistical' and 'exploritory' and 'data' and 'analysis' in y):
            statistical_EDA(common_member(),*year())
        if 'what' in y and (('life' in y and'expectancy' in y) or 'le' in y) and 'predict' not in y and 'will' not in y and 'maximum' not in y and 'highest' not in y and 'lowest' not in y and 'minimum' not in y:
            what_is(common_member(),year())
        if 'what' in y and ('highest' in y or 'maximum' in y or 'max' in y) and (('life' in y and 'expectancy' in y) or 'le' in y):
            highest_life_expectancy_of_country(common_member()[0])
        if 'what' in y and ('lowest' in y or 'minimum' in y or 'min' in y) and (('life' in y and 'expectancy' in y) or 'le' in y):
            lowest_life_expectancy_of_country(common_member()[0])
        if 'which' in y and 'country' in y and ('highest' in y or 'maximum' in y) and (('life' in y and 'expectancy' in y) or 'le' in y) and 'on' in y:
            country_highest_life_expectancy(year())
        if 'which' in y and 'country' in y and ('lowest' in y or 'minimum' in y) and (('life' in y and 'expectancy' in y) or 'le' in y) and 'on' in y:
            country_lowest_life_expectancy(year())
        if 'which' in y and 'country' in y and ('highest' in y or 'maximum' in y) and (('life' in y and 'expectancy' in y) or 'le' in y) and 'on' not in y:
            highest_life_expectancy()
        if 'which' in y and 'country' in y and ('lowest' in y or 'minimum' in y or 'min' in y) and (('life' in y and 'expectancy' in y) or 'le' in y) and 'on' not in y:
            lowest_life_expectancy()
        if 'predict' in y or 'will' in y:
            predict(common_member(),year())
    except:
        print('Please Enter correctly with proper meaning')
