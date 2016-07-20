import pdb



lines_data = {}
with open('test.txt') as f:
    
    for line in f:
        lst = line.strip().split("\t")
        a = lst[1].split(':')        
        if lst[0] in lines_data and a[0] == "url":
            lines_data[lst[0]]["url"].append(a[1])
        elif lst[0] in lines_data and a[0] == "query":
            lines_data[lst[0]]["query"].append(a[1])
        else:
            s = [a[1]]
            if a[0] == 'query':
                lines_data[lst[0]] = {a[0]: s}
                lines_data[lst[0]]['url'] = []
            else:
                lines_data[lst[0]] = {a[0]: s}
                lines_data[lst[0]]['query'] = []

for user, data in lines_data.items():
    for url in data['url']:
        for query in data['query']:
            print user + "\t" + query + "\t" + url




'''for 
temp = ''
count = 1
for line in lst:
    out = line.strip().split(' ')
    if temp != out[0] and count > 2:
        print (out[0])
        temp = out[0]
        count += 1
    elif temp != out[0] and temp:
        print (temp[0])
        temp = out[0]        
    else:       
        temp = out[0]
        count += 1'''
    