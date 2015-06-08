## review to data

def review2data(rev_data):
    output_list = []
    asin_list =[]
    helpful_list =[]
    overall_list =[]
    for i in range(len(rev_data)):
        rev = rev_data[i]['reviewText']
        rev = [str(rev)]
        asi = rev_data[i]['asin']
        asi = [str(asi)]
        hel = rev_data[i]['helpful'][0]
        hel = [str(hel)]
        ove = rev_data[i]['overall']
        ove = [str(ove)]
        output_list = output_list + rev
        asin_list = asin_list + asi
        helpful_list = helpful_list + hel
        overall_list = overall_list + ove
    return output_list, asin_list, helpful_list, overall_list

revtext, asid, helpscore, rating = review2data(coff_rev_espre[:])


    
## asin ID to title name
mtest = metadata[:]
titles = []
for ad in asid[:]:
    asinid = ad
    #print asinid
    try:
        for i in mtest[:]:
            try:
                titl = i[u'title']
            except:
                pass
            ids = str(i['asin'])
            if asinid==ids:
                #print 'yes'
                titles = titles + [titl]
                break       
            elif i == mtest[-1]:
                    titles = titles + ["unknown"]
            else:
                pass
    except:
        pass
len(titles)