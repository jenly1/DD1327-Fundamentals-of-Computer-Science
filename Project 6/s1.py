# Jennifer Ly, grudat20 ovning 6

# coding: utf-8

import re

def dna():
    return '^[AGCT]+$'

def sorted():       
    return '^9*8*7*6*5*4*3*2*1*0*$'

def hidden1(x):     
    return '^.*'+x+'.*$'

def hidden2(x):    
    return '^.*'+'.*'.join(x)+'.*$'

def equation():     
    return '^[\+\-]?(\d+)([\+\-\*\/]\d+)*(=?[\+\-]?\d+)?([\+\-\*\/]\d+)*$'