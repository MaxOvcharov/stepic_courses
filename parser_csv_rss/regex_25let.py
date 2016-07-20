# -*- coding: utf-8 -*-

import sys
import re

def check_lst(values):
  out = []
  for value in values:    
    res = re.match(ur'^(25)\s*([лЛlL][еЕeE][тТtT])*\s*$', value.decode('utf-8'))
    # Check value using a regular expression
    if res:
      out.append(value)
  return out     

values = ["25 лет ", "25 let\n", "25ЛЕТ", "25 \n", "25 месяцев", "125 лет", "25 лет Победы","55 леТ", "25 чего?", "2 5", "25 зим"]

print values
print check_lst(values)