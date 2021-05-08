Book_1= open('Beyond the Wall of Sleep.txt', encoding="utf8")
Beyond= Book_1.read()

Book_2= open('Pride and Prejudice.txt', encoding="utf8")
Pride= Book_2.read()

Beyond=Beyond.lower().split()
Pride=Pride.lower().split()

inner=set(Beyond).intersection(set(Pride))

Book_1.close()
Book_2.close()

inner=str(inner)
import re
inner=re.split(r'\W+',inner)

#from nltk.corpus import stopwords
Stop_words=['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours','us', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll','p', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn', '','would','more','much','many','none','first','second','third','year','month','week',]

inner=set(inner)
for z in Stop_words:
    inner.discard(z)

def use(x):
    for idx, word in enumerate(x):
        print((idx + 1,word))
        
print('The number of words = ',len(inner))
print('The words are : ')
use(inner)