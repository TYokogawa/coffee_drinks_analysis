## wanted and unwanted keywords

wanted = {u'coffee',u'espresso',u'ristretto',u'doppio',u'lungo',u'macchiato',u'cortado',u'cortadito'
          ,u'cafe au lait',u'cappuccino',u'cold coffee',u'cold brew coffee',u'french press',u'mocha'
          ,u'latte',u'cappucino', u'pour over', u'pourover', u'paper drip', u'pour-over', u'chemex', u'cloth filter'
          ,u'nel drip',u'stovetop extracts', u'percolator', u'aeropress' , u'americano' , u'cafe latte'
          ,u'caramel Macchiato', u'K-Cup', u'siphon', u'syphon'}

unwanted = {u'book',u'table', u'books', u'mug', u'coffee cup'}



## filter meta data with title including coffee related word

def cafewanted(dat):
	coff_meta = []
	for i in dat[:]:
	    try:
	        tex = [w in i[u'title'].lower() for w in wanted]
	        if any(tex)== True:
	            coff_meta = coff_meta + [i]
	    except:
	        pass
	return coff_meta
	#len(coff_meta)

coff_meta = cafewanted(meta)




##  filter meta data with title including coffee related word

coff_rev = [i for i in data if any(w in i[u'reviewText'].lower() for w in wanted)]
coff_rev_ex = [i for i in coff_rev if not any(w in i[u'reviewText'] for w in unwanted)]