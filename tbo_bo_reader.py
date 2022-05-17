from __future__ import print_function
import time, os, sys
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np



def occupancy_1D(ax, channels, entries):
    # ----- The function plots the histogram of the occupancy of 64 channels (1 MiniDT chamber) -----
    #       
    # Parameters
    # ----------
    # ax : AxesSubplot
    #       axes of the subplot to modify
    # channels : array
    #     It represent the x coordinates
    #
    # entries : list
    #     The information about the height of the columns
       
    ax.cla()
    ax.bar(channel,entries, width =1, color = '#1f77b4')
    ax.set_title(filename+datetime.now().strftime("%Y/%m/%d - %H:%M:%S"))
    plt.pause(.0001)
    plt.show()
    
def occupancy_2D(ax, entries):
    # ----- The function plots the 2D histogram of the occupancy of the chamber (1 MiniDT chamber) -----
    #       
    # Parameters
    # ----------
    # ax : AxesSubplot
    #       axes of the subplot to modify
    #
    # entries : 2d array
    #     The information about the entries of each chamber cell 

    ax.cla()
    ax.pcolormesh(entries)       
    ax.set_title(filename+datetime.now().strftime("%Y/%m/%d - %H:%M:%S"))
    plt.pause(.0001)
    plt.show()



# ----- run number can be passed as an argument from the terminal command line

if len(sys.argv)>1:
    n_run = sys.argv[1] 
else :
    n_run = int( input('Error, no run number specified. Enter the run number and press the enter key (to use the simulated data file, enter -1) :') )

# ----- to use the file generated with the simulator use r_number = -1 -----
    if n_run == -1: 
        filename = "FakeRun.txt"
    else : 
        filename = "/home/gpaggi/dtupy/scripts/MiniDT_Runs/Run_" + str(n_run) + ".txt"             

# ----- check if the file exists, close the program if it does not -----
if os.path.exists(filename):
    f = open(filename, 'r')
    print('Reading ' + filename )

else:
    print("Error, output data file does not exists! Exiting...")
    sys.exit()

# ------ assign channel to pin -------
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

layer=[4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1]
wire=[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13,14,14,14,14,15,15,15,15,16,16,16,16]


channel = range(64)
pins = obdt_connectors['a'] + obdt_connectors['b'] + obdt_connectors['c'] + obdt_connectors['d']

# ----- set interactive mode so that pyplot.show() displays the figures and immediately returns -----
plt.ion() 
fig, ax = plt.subplots(2, 1, figsize = (25, 10))

# ----- set up 1d channel occupancy -----
ax[0].set_xticks([0, 8, 16, 24, 32, 40, 48, 56, 64])
ax[0].set_xlabel('Channels')
ax[0].set_ylabel('Entries')

entries = [0] *64 

# ----- set up 2d chamber occupancy -----
ax[1].set_xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]) 
ax[1].set_yticks([1, 2, 3, 4])
ax[1].set_xlabel('Wire')
ax[1].set_ylabel('Layer') 

entries_2d = np.array([[0]*16]*4)


# ------ read file ------

# find the size of the file and set pointer to the end
st_results = os.stat(filename)
st_size = st_results[6]
f.seek(st_size)

# ----- start timer to refresh plot -----  
t1 = time.time() 

try:
    
    while( True ):
        
        # try to read a line
        where = f.tell()
        line = f.readline()
        
        # if reading fails, sleep 0.1s and set pointer back before the failed reading
        if not line:

            time.sleep(.5)
            f.seek(where)
        # if the reading is successfull process the string
        else :
            # if the line is completed, extract the pin information
            if line.endswith('\n'):
                data =line.split(' ')
                if len(data)==5: 
                    data_pin = int(data[2] )
                    # pin 230 is the scintillator coincidence, it is not a OBDT channel
                    if data_pin != 230:
                        # assign the channel to the pin and count the entries for each channel value
                        data_channel = pins.index(data_pin)
                        entries[data_channel] +=1
                        data_wire = wire[data_channel]
                        data_layer = layer[data_channel]
                        entries_2d[data_layer -1][data_wire -1] +=1
                    
                else: 
                    data_pins = -1
                
            # if the line is not completed set pointer back to the beginning of the line (where it was before reading)
            else :
                f.seek(where)
            
            #refresh plot if more than 1s is passed since previous one
            t2 = time.time()
            if t2-t1 > 1 :
                occupancy_1D(ax[0], channel, entries)
                occupancy_2D(ax[1], entries_2d)
                # reset timer
                t1 = t2 
            
except KeyboardInterrupt:
    print ('\nReading stopped.\n')
    f.close()






        


