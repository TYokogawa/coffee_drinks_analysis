## count number of review

years = range(2000, 2015)
cofftypes = coffee_types[:]
coff_num = []
for year in years:
    yearly = []
    wantyear = {str(year)}
    coff_rev_year = [i for i in coff_rev_ex if any(w in i[u'reviewTime'].lower() for w in wantyear)]
    yearly = yearly + [len(coff_rev_year)]
    print "Year " + str(year) + " coffee review is:"
    print len(coff_rev_year)
    for n in cofftypes:
        coff_rev_type_year = [i for i in coff_rev_year if any(w in i[u'reviewText'].lower() for w in n)]
        yearly = yearly + [len(coff_rev_type_year)]

    coff_num = coff_num + [yearly]
    #print yearly
    print coff_num


coff_colname = ['allcoffee','coldbrew','espresso','latte','cappuccino','frenchpress','pourover'
                ,'percolator','americano','aeropress','siphon','macchiato']


import pandas as pd
dfcof = pd.DataFrame(coff_num, columns=coff_colname)