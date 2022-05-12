from __future__ import print_function
import time, os, sys



#Set the filename and open the file
n_run = 33
filename = "/home/gpaggi/dtupy/scripts/MiniDT_Runs/Run_" + str(n_run) + ".txt"             

# ----- Check if the file exists, close the program if it does not -----
if os.path.exists(filename):
    f = open(filename, 'r')

else:
    print("Error, output data file does not exists! Exiting...")
    sys.exit()



# ------ read file ------

# find the size of the file and set pointer to the end
st_results = os.stat(filename)
st_size = st_results[6]
f.seek(st_size)
  

try:
    
    while( True ):
        
        # try to read a line
        where = f.tell()
        line = f.readline()
        
        # if reading fails, sleep 0.1s and set pointer back before the failed reading
        if not line:
                    
            time.sleep(.1)
            f.seek(where)
        # if the reading is successfull process the string
        else :
            # if the line is completed, extract the pin information
            if line.endswith('\n'):
                data =line.split(' ')
                if len(data)==5: 
                    data_pins = data[2] 
                else: 
                    data_pins = -1
                
                print(data)
                print(data_pins)
                
                sys.stdout.flush()
            # if the line is not completed set pointer back to the beginning of the line (where it was before reading)
            else :
                f.seek(where)
        			 
		
        
except KeyboardInterrupt:
    print ('\nReading stopped.\n')
        





        
