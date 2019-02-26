from new_function import *
import spacy
import pandas as pd
from sklearn.svm import SVC
import numpy as np
import spacy
nlp=spacy.load('en')
k=country_name()
train3=['draw the scatter_plot of {}'.format(x) for x in k]+['draw the scatterplot of {}'.format(x) for x in k]+['scatter_plot of {}'.format(x) for x in k]+['scatterplot of {}'.format(x) for x in k]
train5=['do a graphical EDA on {}'.format(x) for x in k]+['grahical exploritory data analysis of {}'.format(x) for x in k]+['do a graphical exploritory data analysis on {}'.format(x) for x in k]+['graphical_EDA on {}'.format(x) for x in k]
train=train3+train5
label3=['scatter_plot' for x in range(len(train3))]
label5=['grapical_EDA' for x in range(len(train5))]
label=label3+label5
n_sentences=len(train)
embedding_dim=384
X=np.zeros((n_sentences,embedding_dim))
for idx,sentence in enumerate(train):
    doc=nlp(sentence)
    X[idx, :]=doc.vector
