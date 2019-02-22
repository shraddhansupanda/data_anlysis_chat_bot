from new_function import *
import spacy
nlp=spacy.load('en')
k=country_name()
train1=['what is the country name']
train2=['draw a box_plot of {}'.format(x) for x in k]
train3=['draw the scatter_plot of {}'.format(x) for x in k]
train4=['draw the histogram of {}'.format(x) for x in k]
train5=['do a graphical EDA on {}'.format(x) for x in k]
train6=['what is the avg of {}'.format(x) for x in k]
train7=['what is the variance of {}'.format(x) for x in k]
train8=['what is the standard_deviation of {}'.format(x) for x in k]
train9=['statistical_EDA on {}'.format(x) for x in k]
train10=['what is the life expectancy of india on year']
train11=['which country has highest life expectancy on {}'.format(x) for x in range(1800,2017)]
train12=['which country has highest life expectancy']
#train13=['predict what will be the life expectacy of {} on {}'.format(x,y) for x in k for y in range(1800,2017)]
train=train1+train2+train3+train4+train5+train6+train7+train8+train9+train10+train11+train12
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
#label13=['prdict' for x in range(len(train13))]
label=label1+label2+label3+label4+label5+label6+label7+label8+label9+label10+label11+label12
n_sentences=len(train)
embedding_dim=384
X=np.zeros((n_sentences,embedding_dim))
for idx,sentence in enumerate(train):
    doc=nlp(sentence)
    X[idx, :]=doc.vector
