import csv,operator

def get_campaigns(filename):
	with open(filename) as csvfile:
		return list(csv.DictReader(csvfile))


def order_by_payout(filename):
	"""
	Returns a list of campaigns ID 's, order by payout from highest to lowest.
	"""
	listSorted =  sorted(get_campaigns(filename),key=operator.itemgetter('payout'),reverse=True)
	campaigns = [int(item['id']) for item in listSorted]
	return campaigns

def order_by_total_payout(filename):
	"""
	Returns a list of campaigns ID 's, order by total payout from highest to
	lowest.
	>>> total_payout = payout * installs
	"""
	#total_payout = payout*installs
	listResult = [{'id':item['id'],'total_payout':float(item['payout'].replace(',','.'))*float(item['installs'])} for item in get_campaigns(filename)]
	listSorted = sorted(listResult,key=operator.itemgetter('total_payout'),reverse=True)
	campaigns = [int(item['id']) for item in listSorted]

	return campaigns


def order_by_cr(filename):
	"""
	Returns a list of campaigns ID 's, order by conversion rate (CR) from highest
	to lowest.
	>>> cr = impressions / installs
	"""

	listResult = [{'id':item['id'],'cr':float(item['impressions'])/float(item['installs'])} for item in get_campaigns(filename)]
	listSorted = sorted(listResult,key=operator.itemgetter('cr'),reverse=True)
	campaigns = [int(item['id']) for item in listSorted]

	return campaigns


if __name__ == '__main__':
	filename = 'campaigns.csv'
	payout_order = [ 17 , 14 , 22 , 7 , 11 , 15 , 23 , 13 , 18 , 12 , 6 , 1 , 3 , 10 , 25 , 24, 21 , 16 , 20 , 5 , 4 , 8 , 9 , 19 , 2]
	total_payout_order = [ 15 , 11 , 18 , 7 , 14 , 21 , 3 , 6 , 25 , 13 , 16 , 5 , 24 , 20, 17 , 23 , 1 , 10 , 8 , 9 , 19 , 12 , 4 , 22 , 2]
	#List of cr is incorrect, because -> reverse=False -> lowest to highest
	#cr_order = [ 11 , 15 , 18 , 25 , 21 , 7 , 8 , 24 , 6 , 14 , 3 , 9 , 5 , 16 , 19 , 10 , 20, 2 , 13 , 4 , 17 , 1 , 23 , 12 , 22]
	cr_order = [22, 12, 23, 1, 17, 4, 13, 2, 20, 10, 19, 16, 5, 9, 3, 14, 6, 24, 8, 7, 21, 25, 18, 15, 11]

	assert order_by_payout(filename) == payout_order
	assert order_by_total_payout(filename) == total_payout_order
	assert order_by_cr(filename) == cr_order