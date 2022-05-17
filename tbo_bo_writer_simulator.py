# -*- coding: utf-8 -*-
"""
Created on Tue May 17 12:42:55 2022

@author: Giulia Paggi
"""
import time
from datetime import datetime
import random 


obdt_connectors = {
  'o':[234,36,50,48,44,46,41,204,220,217,219,233,214,237,15,169],
  'a':[222,45,49,52,43,209,53,51,215,235,238,28,30,31,20,17],
  'b':[14,16,108,13,221,89,90,57,88,198,42,38,37,39,186,0],
  'i':[6,47,207,54,208,205,206,212,225,18,101,12,110,111,126,125],
  'j':[112,188,187,154,170,179,180,182,183,199,195,193,189,191,203,190],
  'g':[4,211,210,228,230,224,236,25,21,106,103,127,131,172,85,151],
  'h':[218,150,158,160,56,86,75,87,173,174,178,200,202,201,5,26],
  'e':[33,27,10,231,232,109,213,239,226,223,7,227,2,8,114,113],
  'f':[229,139,141,143,161,59,63,65,58,60,175,171,177,181,185,184],
  'k':[104,35,98,11,1,3,24,9,121,102,123,107,138,128,129,130],
  'l':[216,55,91,93,66,72,79,76,81,78,74,64,70,176,162,69],
  'c':[119,115,96,29,32,19,34,22,142,105,137,120,124,152,149,165],
  'd':[40,62,73,153,148,155,156,157,159,166,61,82,77,68,146,147],
  'm':[122,117,23,99,100,116,118,134,132,136,135,144,145,163,164,167],
  'n':[140,92,94,95,97,67,71,80,83,168,196,192,194,84,133,197],
  }


pins = obdt_connectors['a']+obdt_connectors['b']+obdt_connectors['c']+obdt_connectors['d']

# ------- open data file ------- 

data_f_name = "FakeRun.txt"
data_f = open(data_f_name, "a")


# ------- set initial time -------
StartTime=datetime.now().strftime("%Y/%m/%d - %H:%M:%S")
t1 = time.time()

print("\n\n\n\nStarting simulated run, press CTRL-C to stop")

hitcount=0
old_hitcount=0
old_t=0

try: 
    while( True ):
        time.sleep(0.1)
        t2 = time.time()
        deltatime = t2-t1
        deltaprint = t2-old_t
        hit_bx = random.randint(1, 3564)
        hit_ch = pins[random.randint(0, 63)]
        hit_orbit = random.randint(0, 4095)
        hit_tdc = random.randint(0, 15)
        data_f.write(str(deltatime)+' '+str(hit_orbit)+' '+str(hit_ch)+' '+str(hit_bx)+' '+str(hit_tdc)+'\n') 
         
        data_f.flush()

except KeyboardInterrupt:
    print ('\nRun stopped.\n')
    #condition = False
        
    
# ------- closa data file -------
data_f.close()          
              

