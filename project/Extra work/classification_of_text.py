import pandas as pd
from sklearn.svm import SVC
from very_simple_training_data import *
import numpy as np
import spacy
nlp=spacy.load('en')
Y=X.reshape(-1,384)
y=input()
y=str(y)
doc=nlp(y)
doc1=doc.vector
doc2=np.array(doc1)
doc3=doc1.reshape(-1,384)
svm=SVC()
svm.fit(Y,label)
pred=svm.predict(doc3)
print(pred)
