import pandas as pd

years = range(2000, 2015)
cofftypes = coffee_types[:]
coff_rev_senti = []
coff_rev_senti_ave = []
coff_rev_senti_ratio = []
for year in years:
    yearly = []
    sent_ave = []
    sent_ratio = []
    wantyear = {str(year)}
    coff_rev_year = [i for i in coff_rev_ex if any(w in i[u'reviewTime'].lower() for w in wantyear)]
    print("Year" + str(year) + " coffee review sentiment")
    for n in cofftypes:
        coff_rev_type_year = [i for i in coff_rev_year if any(w in i[u'reviewText'].lower() for w in n)]
        coff_rev_type_year_list = revew2revlist(coff_rev_type_year) 
        coff_senti = rev2sentiment(coff_rev_type_year_list)
        coff_senti_ave = coff_senti.sum()/len(coff_senti)
        senti_count = coff_senti[coff_senti > 0].count()
        senti_count_ratio = senti_count/len(coff_senti)
        yearly += [coff_senti]
        try:
            sent_ave += [coff_senti_ave[0]]
            sent_ratio += [senti_count_ratio[0]]
        except:
            sent_ave += [0]
            sent_ratio += [0]
  
    coff_rev_senti += [yearly]
    coff_rev_senti_ave += [sent_ave]
    coff_rev_senti_ratio += [sent_ratio]


coff_senti_colname = ['coldbrew','espresso','latte','cappuccino','frenchpress','pourover'
                ,'percolator','americano','aeropress','siphon','macchiato']


### plotting

cofsen = pd.DataFrame(coff_rev_senti_ave, columns=coff_senti_colname)
rati = pd.DataFrame(coff_rev_senti_ratio, columns=coff_senti_colname)

pd.DataFrame.plot(rati, x=None, y=None, kind='line')
plt.show()
