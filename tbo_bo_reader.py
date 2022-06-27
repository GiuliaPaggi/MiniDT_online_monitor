import time, os, sys
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import configparser
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import streamlit as st
import PLOTS


#plt.switch_backend('TkAgg')

# ------ set up webpage ------
st.set_page_config(
    page_title="Monitor",
    layout="wide",
)
monitor = st.empty()

# ----- import path from configuration file -----
config = configparser.ConfigParser()
config_file = 'config.txt'                  #/home/gpaggi/dtupy/scripts/
if os.path.exists(config_file): 
    config.read(config_file)     
else : 
    print( 'Select the configuration file', flush=True)
    Tk().withdraw()
    config_file = askopenfilename()
    config.read(config_file)


data_path = config.get('path', 'DataFolderPath')
plot_path = config.get('path', 'PlotFolderPath')
logfile_path = config.get('file', 'LogFile')
show_plt = config.getboolean('option', 'ShowPlots')
# ----- run number can be passed as an argument from the terminal command line -----

if len(sys.argv)>1:
    n_run = int(sys.argv[1])
    run_name = "Run_" + str(n_run)
# if run number is not given, read runs log files to find the current one 
else :
    if os.path.exists(logfile_path):
        log_file = open(logfile_path, 'r')
        n_run = int(log_file.readlines()[-1].split(' ')[0]) + 1
        run_name = "Run_" + str(n_run)
    else :
        n_run = -1
        run_name = "FakeRun"
    
# ----- to use the file generated with the simulator use r_number = -1 -----
if n_run == -1: 
    filename = "FakeRun.txt"
    data_path = ''
    plot_path = ''
    dir_path = run_name+'/'
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

else : 
    filename =  run_name + ".txt"  
    dir_path = plot_path+run_name+'/' 
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)          


# ----- check if the file exists, close the program if it does not -----
if os.path.exists(data_path+filename):
    f = open(data_path+filename, 'r')
    print(datetime.now().strftime("%Y/%m/%d - %H:%M:%S")+ ' Reading ' + filename )

else:
    print("Error, output data file "+filename+" does not exists! Press CTRL-C to exit")
    st.write("Error, output data file does not exists! Exiting...")
    st.stop()
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

if show_plt:
    # ----- set interactive mode so that pyplot.show() displays the figures and immediately returns ----
    plt.ion() 
    fig, ax = plt.subplots(2, 2, figsize = (15, 10))
    fig_timebox, ax_timebox = plt.subplots(2, 3, figsize = (15, 10))

# ----- set up 1d channel occupancy -----
entries = [0] *64 

# ----- set up 2d chamber occupancy -----
entries_2d = np.array([[0]*16]*4)

# ------ set up rate ------
rate_entries = [0] *64 

# ----- set up 2d rate -----
rate_2d = np.array([[0]*16]*4, dtype = float)

# ----- set up timebox cumulative and instantaneous -----
timebox_xaxis = range(200)
timebox_entries = [0] *200
inst_timebox = []
inst_timebox_entries = [0] *200
timebox_ticks = [0, 25, 50, 75, 100, 125, 150, 175, 200]

# ----- set up occupancy of scintillators events -----
scint_entries = [0]*64
scint_entries_2d = np.array([[0]*16]*4)
scint_rate = [0]*64
scint_rate_2d = np.array([[0]*16]*4, dtype = float)


# ------ read file ------

# find the size of the file and set pointer to the end
st_results = os.stat(data_path+filename)
st_size = st_results[6]
f.seek(st_size)


try:
    
    while( True ):
        
        # try to read a line
        where = f.tell()
        time.sleep(30)
        line = f.readlines()

        # if reading fails, sleep 0.1s and set pointer back before the failed reading
        if not line:
            print('No new lines to be read.')
            # print(time.time() - os.path.getmtime(filename))
            if time.time() - os.path.getmtime(filename) > 120 :
                print ('\nReading stopped.\n') 
                f.close()
                os._exit(0)
                st.stop()
                #sys.exit()
            f.seek(where)
            
        # if the reading is successfull process the string
        else:    
            #reset rate histo
            rate_entries = [0] *64 
            rate_2d [rate_2d>0] = 0
            inst_timebox_entries = [0] *200
            scint_rate = [0] *64
            scint_rate_2d[scint_rate_2d>0] = 0
            
            scint = False
            #check line integrity
            if not line[0].startswith('_'):
                line.pop(0)
        
            if not line[len(line)-1].endswith('\n'):
                line.pop(len(line)-1)
            
            delta_t = float( line[len(line)-1].split(' ')[1] )- float(line[0].split(' ')[1] )
            rate =round (len(line)/delta_t, 2)
            
            for i in range(0, len(line)):
                try: 
                    data_pin = int( line[i].split(' ')[3])
                    data_channel = pins.index( data_pin )
                    # ---- fill 1d occupancy ----
                    entries[data_channel] +=1
                    rate_entries[data_channel] += 1/delta_t
                    
                    
                    data_wires = wire[data_channel]
                    data_layers = layer[data_channel]
                    # ---- fill 2d occupancy ----
                    entries_2d[data_layers -1][data_wires -1] +=1
                    rate_2d[data_layers -1][data_wires -1] += 1/delta_t
                    
                    
                    
                except ValueError:
                    data_pin=230
                    scint = True
                    #recover trigger hit info
                    tr_systime = float(line[ i ].split(' ')[1])
                    tr_bx =  int( line[ i ].split(' ')[4] )
                    tr_tdc = int( line[ i ].split(' ')[5].strip('\n') )
                    tr_time = tr_bx*25.0 + tr_tdc*25/30
                    j=1
                    while( line[ i ].split(' ')[2] == line[ i-j ].split(' ')[2]) :
                        #fill scintillator channel occupancy
                        hit_pin = int(line[ i-j ].split(' ')[3]  )
                        if hit_pin != 230:
                            hit_channel = pins.index(hit_pin)
                            scint_entries[hit_channel] += 1
                            scint_rate[hit_channel] += 1/delta_t
                            
                            #fill scintillator 2d occupancy
                            hit_wire = wire[hit_channel]
                            hit_layer = layer[hit_channel]
                            scint_entries_2d[hit_layer-1][hit_wire -1] +=1
                            scint_rate_2d[hit_layer-1][hit_wire -1] += 1/delta_t
                            
                            #compute hits time
                            hit_bx =  int( line[ i-j ].split(' ')[4] )
                            hit_tdc = int( line[ i-j ].split(' ')[5].strip('\n') )
                            hit_time = hit_bx*25.0 + hit_tdc*25/30
                            #compute time diff and fill a histo with bin width = tdc resolution for cumulative timebox
                            time_diff= hit_time - tr_time + 1000
                            index=round(time_diff * 30/25 *.125) 
                            try: 
                                timebox_entries[index] +=1
                                inst_timebox_entries[index] +=1
                            except IndexError: 
                                print(time_diff, line[i], line[i-j] )
                                #sys.exit()
                        
                        j +=1
            # display plots with matplotlib
            if show_plt:
                PLOTS.plot_1D(fig, ax[0][0], channel, entries, "Entries", n_run, "Channel", "Entries")
                PLOTS.plot_2D(fig, ax[1][0], entries_2d, "Entries_2D", n_run, "Wire", "Layer")
                PLOTS.plot_1D(fig, ax[0][1], channel, rate_entries, "Rate", n_run, "Channel", "Rate (Hz)")
                PLOTS.plot_2D(fig, ax[1][1], rate_2d, "Rate_2D", n_run, "Wire", "Layer")   
                if scint:
                    PLOTS.plot_1D(fig_timebox, ax_timebox[0][0], timebox_xaxis , timebox_entries, "Cumulative_Timebox", n_run, "TDC units", "Entries" , xticks= timebox_ticks)
                    PLOTS.plot_1D(fig_timebox, ax_timebox[1][0], timebox_xaxis , inst_timebox_entries, "Inst_Timebox", n_run, "TDC units", "Entries",  xticks= timebox_ticks )
                    PLOTS.plot_1D(fig_timebox, ax_timebox[0][1], channel, scint_entries, "Scintillator_event_entries", run_name, "Channel", "Entries")
                    PLOTS.plot_2D(fig_timebox, ax_timebox[0][2], scint_entries_2d, "Scintillator_event_entries_2D", run_name, "Wire", "Layer")
                    PLOTS.plot_1D(fig_timebox, ax_timebox[1][1], channel, scint_rate, "Scintillator_event_rate", run_name, "Channel", "Rate")
                    PLOTS.plot_2D(fig_timebox, ax_timebox[1][2], scint_rate_2d, "Scintillator_event_rate_2D", run_name, "Wire", "Layer")
 
            # save plots in folder and update monitor web page 
            PLOTS.save_1D(dir_path, channel, entries, "Entries", run_name, "Channel", "Entries")
            PLOTS.save_2D(dir_path, entries_2d, "Entries_2D", run_name, "Wire", "Layer")
            PLOTS.save_1D(dir_path, channel, rate_entries, "Rate", run_name, "Channel", "Rate (Hz)")
            PLOTS.save_2D(dir_path, rate_2d, "Rate_2D", run_name, "Wire", "Layer")
            images_list = ['Entries.PNG', 'Entries_2D.PNG', 'Rate.PNG', 'Rate_2D.PNG']
            PLOTS.make_monitor(dir_path, images_list, 'occupancy')
            
        
            if scint:
                PLOTS.save_1D(dir_path, timebox_xaxis, timebox_entries, "Cumulative_Timebox", run_name, "TDC units", "Entries", xticks= timebox_ticks)
                PLOTS.save_1D(dir_path, timebox_xaxis, inst_timebox_entries, "Inst_Timebox",run_name, "TDC units", "Entries", xticks= timebox_ticks)
                PLOTS.save_1D(dir_path, channel, scint_entries, "Scintillator_event_entries", run_name, "Channel", "Entries")
                PLOTS.save_2D(dir_path, scint_entries_2d, "Scintillator_event_entries_2D", run_name, "Wire", "Layer")
                PLOTS.save_1D(dir_path, channel, scint_rate, "Scintillator_event_rate", run_name, "Channel", "Rate")
                PLOTS.save_2D(dir_path, scint_rate_2d, "Scintillator_event_rate_2D", run_name, "Wire", "Layer")
                scint_list = ['Cumulative_Timebox.PNG', "Scintillator_event_entries.PNG", "Scintillator_event_rate.PNG",
                                'Inst_Timebox.PNG', "Scintillator_event_rate.PNG", "Scintillator_event_rate_2D.PNG"]
                PLOTS.make_monitor(dir_path, scint_list, 'scintillator')
                PLOTS.update_monitor(dir_path, monitor, [ 'occupancy_monitor.PNG', 'scintillator_monitor.PNG'], str(rate))
            else:
                PLOTS.update_monitor(dir_path, monitor, [ 'occupancy_monitor.PNG'], str(rate))
                     
                
except KeyboardInterrupt:
    print ('\nReading stopped.\n') 
    sys.exit()
    f.close()
    