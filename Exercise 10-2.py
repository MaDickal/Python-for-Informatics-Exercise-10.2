fname = raw_input('Enter file name: ')
try:
	fhandle = open(fname)
except:
	print 'File cannot be opened:', fname
	exit()
emails = dict()
for line in fhandle:
	if line.startswith('From '):
		line = line.split()
		email = line[5]
		email = email.split(':')
		hour = email[0]
		emails[hour] = emails.get(hour,0) + 1
hourslist = []
for hour, count in emails.items():
	hourslist.append( (hour, count) )
hourslist.sort()
for hour, count in hourslist:
	print hour, count