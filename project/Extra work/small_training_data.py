from new_function import *
import spacy
nlp=spacy.load('en')
k=country_name()
train1=['what is the country name','name all the country','country name','how many country are present']
train2=['draw a box_plot of country name']+['draw the boxplot of country name']+['box_plot of country_name']+['boxplot of country_name']
train3=['draw the scatter_plot of country name']+['draw the scatterplot of country name']+['scatter_plot of country_name']+['scatterplot of country_name']
train4=['draw the histogram of country_name']+['plot a histogram of country_name']+['construct a histogram on country_name']+['make a histgram on country_name']
train5=['do a graphical EDA on country name']+['grahical exploritory data analysis of country_name']+['do a graphical exploritory data analysis on country name']+['graphical_EDA on country_name']
train6=['what is the avg of country name']+['avg of country name']
train7=['what is the variance of country name']+['variance of country name']
train8=['what is the standard_deviation of country name']+['standard_deviation of country name']+['std of country name']+['what is the std of country name']
train9=['statistical_EDA on country name']+['statistical_exploritory data analysis on country_name']
train10=['what is the life expectancy of india on year']
train11=['which country has highest life expectancy on year']
train12=['which country has highest life expectancy']
train13=['predict what will be the life expectacy of country name on year']+['predict life expectacy of country name on year']+['life expectacy of country name on year']
train=train1+train2+train3+train4+train5+train6+train7+train8+train9+train10+train11+train12+train13
label1=['country_name' for x in range(len(train1))]
label2=['box_plot' for x in range(len(train2))]
label3=['scatter_plot' for x in range(len(train3))]
label4=['histogram' for x in range(len(train4))]
label5=['grapical_EDA' for x in range(len(train5))]
label6=['avg' for x in range(len(train6))]
label7=['variance' for x in range(len(train7))]
label8=['standard_deviation' for x in range(len(train8))]
label9=['statistical_EDA' for x in range(len(train9))]
label10=['what_is' for x in range(len(train10))]
label11=['country_highest_life_expectancy' for x in range(len(train11))]
label12=['highest_life_expectancy' for x in range(len(train12))]
label13=['prdict' for x in range(len(train13))]
label=label1+label2+label3+label4+label5+label6+label7+label8+label9+label10+label11+label12+label13
n_sentences=len(train)
embedding_dim=384
X=np.zeros((n_sentences,embedding_dim))
for idx,sentence in enumerate(train):
    doc=nlp(sentence)
    X[idx, :]=doc.vector
