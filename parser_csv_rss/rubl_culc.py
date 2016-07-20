# -*- coding: utf-8 -*-
import sys
import pdb


def get_total(filename):
  
  summ = 0
  with open(filename) as f:
    #pdb.set_trace()
    for line in f:
      rubl = line.strip().split(".")
      if len(rubl) == 0:
        continue
      elif len(rubl) == 1:
        line = line.strip() + ".00"
      summ += float(line)
  return summ

def main():
  if len(sys.argv) > 1:
    path = sys.argv[1] 
  else:
    path = "charges.txt"

  total = str(get_total(path)).split(".")
  
  print("rublуs: %s kop: %s" % (total[0], total[1]))

if __name__ == "__main__":
  main()