## reviews to list of reviews

def revew2revlist(rev_data):
    output_list = []
    for i in range(len(rev_data)):
        rev = rev_data[i]['reviewText']
        rev = [str(rev)]
        output_list = output_list + rev
    return output_list



def revew2revtext(rev_data):
	output_text = ''
	for i in range(len(rev_data)):
	    rev = rev_data[i]['reviewText']
	    rev = str(rev)
	    output_text = output_text + rev
	return output_text