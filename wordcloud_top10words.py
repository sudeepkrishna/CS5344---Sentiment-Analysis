import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.tokenize import word_tokenize
from scipy.sparse import hstack
from textblob import TextBlob
import collections

df = pd.read_csv('minedtweets.csv')
print(df.shape)
df=df.drop(columns=df.columns[0])

df['tweet'].replace('', np.nan,inplace=True)
df=df.drop_duplicates(subset='tweet')

df = df[df['tweet'].notnull()]
print(df.shape)


sns.set(style="darkgrid")
ax = sns.countplot(x="sentiment", data=df)
ax.set_ylabel("Number of Samples in training Set")
ax.set_xlabel("Sentiment")
print(df['sentiment'].value_counts())


pos_words=df['tweet'][df['sentiment'] == 1]
neg_words=df['tweet'][df['sentiment'] == -1]
pos = ' '.join([text for text in pos_words])
neg = ' '.join([text for text in neg_words])


wordcloud = WordCloud(background_color='white',width=800, height=500, random_state=21, max_font_size=80).generate(pos)

plt.figure(figsize=(10, 7))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis('off')
plt.savefig('positive_cloud.jpg')
plt.show()

wordcloud = WordCloud(background_color='white',width=800, height=500, random_state=21, max_font_size=80).generate(neg)
plt.figure(figsize=(10, 7))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis('off')
plt.savefig('negative_cloud.jpg')
plt.show()


#Top 10 frequent words

pos_words=[]
neg_words=[]
pos_words=df['tweet'][df['sentiment'] == 1]
neg_words=df['tweet'][df['sentiment'] == -1]

worddict=collections.defaultdict(int)
stoplists=set(['``','...','\'s','covid-19','coronavirus','SARSCoV2','coronavirusoutbreak','covid','covid19','19','sarscov2','corona','covid_19','virus'])

#positive
for line in pos_words:
    for word in line.split():
        if word not in stoplists and len(word)>3:
            worddict[word]+=1
mc = sorted(worddict.items(), key=lambda k_v: k_v[1], reverse=True)[:10]
for word, count in mc:
    print(word, ":", count)
   
mc = dict(mc)
names = list(mc.keys())
values = list(mc.values())
plt.bar(range(len(mc)),values,tick_label=names)
plt.xticks(rotation=90)
plt.savefig('bar.png')
plt.show()

#negative
worddict=collections.defaultdict(int)
for line in neg_words:
    for word in line.split():
        if word not in stoplists and len(word)>3:
            worddict[word]+=1
mc = sorted(worddict.items(), key=lambda k_v: k_v[1], reverse=True)[:10]
for word, count in mc:
    print(word, ":", count)
   
mc = dict(mc)
names = list(mc.keys())
values = list(mc.values())
plt.bar(range(len(mc)),values,tick_label=names)
plt.xticks(rotation=90)
plt.savefig('bar2.png')
plt.show()