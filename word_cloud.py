
## Espresso reviews

coff_rev = [i for i in test if any(w in i[u'reviewText'].lower() for w in wanted)]
coff_rev_ex = [i for i in coff_rev if not any(w in i[u'reviewText'].lower() for w in unwanted)]
coff_rev_espre = [i for i in coff_rev_ex if any(w in i[u'reviewText'].lower() for w in esprewanted)]


## review to text
def revew2revtext(rev_data):
    output_text = ''
    for i in range(len(rev_data)):
        rev = rev_data[i]['reviewText']
        rev = str(rev)
        output_text = output_text + rev
    return output_text

coff_rev_espre_text= revew2revtext(coff_rev_espre)


## word cloud plot
from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

text = coff_rev_espre_text

wordcloud = WordCloud(font_path='/Library/Fonts/AppleSDGothicNeo-ExtraBold.otf',width=800, height=800,stopwords=STOPWORDS.update(["buy","use", "reviewerID", "helpful"])).generate(text)


plt.imshow(wordcloud)
plt.axis("off")
plt.savefig('test2.png')
plt.show()