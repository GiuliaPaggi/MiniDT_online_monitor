from __future__ import print_function
import time, os, sys
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np



def ch_occupancy_plot(ax, channels, entries):
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
a = [222,  45,  49,  52,  43, 209,  53,  51, 215, 235, 238,  28,  30,  31,  20,  17]
b = [ 14,  16, 108,  13, 221,  89,  90,  57,  88, 198,  42,  38,  37,  39, 186,   0]
c = [119, 115,  96,  29,  32,  19,  34,  22, 142, 105, 137, 120, 124, 152, 149, 165]
d = [ 40,  62,  73, 153, 148, 155, 156, 157, 159, 166,  61,  82,  77,  68, 146, 147]


layer=[4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1]
wire=[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13,14,14,14,14,15,15,15,15,16,16,16,16]


channel = range(64)
pins = a+b+c+d

# ----- set interactive mode so that pyplot.show() displays the figures and immediately returns -----
plt.ion() 
fig, ax = plt.subplots(2, 1, figsize = (25, 10))

# ----- set up 1d channel occupancy -----
ax[0].set_xticks([0, 8, 16, 24, 32, 40, 48, 56, 64])
ax[0].set_xlabel('Channels')
ax[0].set_ylabel('Entries')

entries = [0] *64 




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

                    
                else: 
                    data_pins = -1
                
            # if the line is not completed set pointer back to the beginning of the line (where it was before reading)
            else :
                f.seek(where)
            
            #refresh plot if more than 1s is passed since previous one
            t2 = time.time()
            if t2-t1 > 1 :
                ch_occupancy_plot(ax[0], channel, entries)

                # reset timer
                t1 = t2 
        			 
		
        
except KeyboardInterrupt:
    print ('\nReading stopped.\n')
    f.close()






        
