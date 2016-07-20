# -*- coding: utf-8 -*-
"""
This script search for the most popular ip
in "access.log".
Example: python ip_search.py /dir1/dir2/access.log (path to file) 5 (number of ip)

"""
import sys
import pdb


def get_stat(filename):
    """
    filename - path to file
    """
    inf = dict()
    with open(filename) as f:
        #pdb.set_trace()
        for line in f:
            chunk = line.split(" ")
            if len(chunk) > 0:
                ip = chunk[0]
                inf[ip] = inf.get(ip,0) + 1
    
    return inf

def main():
    # Check the path to the file "access.log"
    if len(sys.argv) > 1:
        path = sys.argv[1] 
    else:
        path = "access.log"
    # Check the limit of number ip
    if len(sys.argv) > 2:
        try:
            limit = int(sys.argv[2])
        except Exception:
            limit = 5
    else:
        limit = 5

    stat = get_stat(path).items()
    stat = sorted(stat, key=lambda x:x[1], reverse = True)

    for res in stat[:limit]:
        print("%s  --> %s" % (res[0], res[1]))

if __name__ == "__main__":
    main()