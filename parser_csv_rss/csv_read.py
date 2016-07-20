
""" This script reads the file(email.csv)
	and sort email by their domain
    
"""
import itertools
import csv
import re
import sys


def csv_reader(filepath):
	'''
		Reads the file(email.csv)
		and sort email by their domain

	'''
	D = dict()
	with open(filepath, "rb") as csvfile:
		email_reader = csv.reader(csvfile)
		for email in email_reader:			
			res = re.match(r'^([a-z0-9"!:,._-]+)@([a-z0-9_-]+(\.[a-z0-9_-]+))$',email[0])
			email_dom = res.group(2)
			D[email_dom] = D.get(email_dom, []) + [(email[0], email[1])]

	result = [list(filter(None, i)) for i in itertools.izip_longest(*D.values())]
	
	return result

def main():
	# Check the path to the file "email.csv"
	if len(sys.argv) > 1:
		path = sys.argv[1]
	else:
		path = "email.csv"

	print csv_reader(path)

if __name__ == "__main__":
    main()