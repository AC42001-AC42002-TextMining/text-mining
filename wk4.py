import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

# 3644 / 911 / 2733
'''
trainData = pd.read_csv('./HansardData.csv',
                        delimiter=',',
                        encoding='latin1',
                        header=0,
                        )
pds = trainData.to_dict()
# print(pds['IsEthotic'])

print(pds)
'''

# Get training data
trainData = pd.read_csv('./train.csv',
                        delimiter=',',
                        encoding='latin1',
                        header=0,
                        )
trainDict = trainData.to_dict()

# Get test data
testData = pd.read_csv('./test.csv',
                        delimiter=',',
                        encoding='latin1',
                        header=0,
                        )
testDict = testData.to_dict()

pipeline = Pipeline([('BagOfWords', CountVectorizer()), ('classifier', MultinomialNB())])
model = pipeline.fit(trainData['Text'], trainData['IsEthotic'])
predictions = model.predict(testData['Text']) # TODO SPLIT DATA

target_names = ['0', '1']

print(confusion_matrix(testData['SentimentPolarity'], predictions))
print(accuracy_score(testData['SentimentPolarity'], predictions))
