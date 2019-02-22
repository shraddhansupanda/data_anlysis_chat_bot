from perfect_training_data import *
from new_function import *
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
pred=str(pred[0])
#if pred=='scatter_plot':
#scatter_plot(str(doc.ents[0])
#if pred=='graphical_EDA':
#graphical_EDA(str(doc.ents[0])
