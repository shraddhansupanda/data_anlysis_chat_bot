from new_function import *
train1=['what is the country name','name all the country','country name','how many country are present']
k=country_name()
train2=['draw a box_plot of {}'.format(x) for x in k]+['draw the boxplot of {}'.format(x) for x in k]+['box_plot of {}'.format(x) for x in k]+['boxplot of {}'.format(x) for x in k]
train3=['draw the scatter_plot of {}'.format(x) for x in k]+['draw the scatterplot of {}'.format(x) for x in k]+['scatter_plot of {}'.format(x) for x in k]+['scatterplot of {}'.format(x) for x in k]
train4=['draw the histogram of {}'.format(x) for x in k]+['plot a histogram of {}'.format(x) for x in k]+['construct a histogram on {}'.format(x) for x in k]+['make a histgram on {}'.format(x) for x in k]
train5=['do a graphical exploritory data analysis on {}'.format(x) for x in k]+['']
