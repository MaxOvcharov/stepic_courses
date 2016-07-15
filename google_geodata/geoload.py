import urllib
import sqlite3
import json
import time

# This url include the geocode information
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

# Create a database and create a table
conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('''
	CREATE TABLE IF NOT EXISTS Location (address TEXT, geodata TEXT)
	''')

# Open file with the names of plase
fh = open('where.data')
count = 0
for line in fh:
	if count > 200: break
	address = line.strip()
	print ''
	cur.execute('SELECT geodata FROM Location WHERE address= ?', (buffer(address), ))

	# If it's a duplicate in db skip this data
	try:
		data = cur.fetchone()[0]
		print 'Found in database', address
		continue
	except:
		pass

	print 'Resolving', address
	# Make url with the address and read data from this url
	url = serviceurl + urllib.urlencode({'sensor':'false', 'address':address})
	print "Retriving", url
	uh = urllib.urlopen(url)
	data = uh.read()
	print 'Retrieved', len(data), 'characters', data[:20].replace('\n', ' ')
	count += 1
	try:
	# Make json data if OK
		js = json.loads(str(data))
	except:
		continue

	if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS'):
		print '=== Failure To Retrive ==='
		print data
		break

	cur.execute('''INSERT INTO Location (address, geodata) 
					VALUES (?, ?)''', (buffer(address), buffer(data)))  
	conn.commit()
	time.sleep(1)

print "Run geodump.py to read the data from the database so you can visualize it on a map."