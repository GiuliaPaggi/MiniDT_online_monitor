# MiniDT_online_monitor
MiniDTs online monitor project. Show occupancy plots, rate, and timebox in real-time.

## Project Status
The project is in progress. At the moment, for one chamber it's possible to visualize:
- the channels' and 2D chamber cumulative occupancy, 
- the rate of the last 30s both per channel and in the 2D configuration,
- the timebox of the whole run, and the last 30s of data taking,
- the channels' and 2D chamber cumulative and the last 30s occupancy relative to the events linked with a scintillator signal.

The produced plots are saved in .PNG format in a specific folder that can be specified using the configuration file, and refreshed every 30s. 
The plots are shown live on a local web page while the monitor is active.
If the readout file is not modified for 2 minutes, the monitor stops. 


## Table of Contents
* [General Info](#general-information)
* [Usage](#usage)
* [Structure of the project](#structure-of-the-project)
* [Output](#output)
* [Dependencies](#dependencies)



## General Information
Using spare material from the original CMS DT chambers, eight smaller-size SLs, called MiniDTs, were built at INFN Legnaro National Laboratory in Padova. 
Using two of these MiniDTs we aim to install a cosmic rays telescope and test its efficiency and resolution. 
The MiniDTs are operated with the same high voltage and gas mixture condition used in CMS.
The signals on the front end are read using two boards: an On-detector Board for Drift Tube (OBDT) version 1 for the time to digital conversion, and a Xilinx Virtex-7 FPGA VC707 that provides the simulated LHC clock and can be used to implement the slow control.  
The telescope will be completed with three scintillator planes, instrumented with photomultipliers to read out the signals.
These will be located at the top, at the bottom, and in between the two MiniDTs to provide an independent signal, using the coincidence of two or more planes. This signal will be used to identify muons crossing the telescope in the offline analysis of the data from the miniDTs, which have a trigger-less data acquisition system. 

This project aims to develop an online monitor that can allow for a check of the data acquisition process, controlling the data quality and the detector status. 
The focus is on the occupancy of each channel and the time difference between the scintillator and the MiniDTs front-end signals. The first allows identifying during the data taking dead or particularly noisy channels.
The latter is related to the linearity of the MiniDT's space-time response, which depends on the electrons' drift velocity in the chamber.
It can help identify inhomogeneities in the gas distribution or problems in the cells' electric field configurations. 

## Usage
This project is meant to be used on the text file written by the MiniDTs acquisition program. Each line in this file is one event recorded in the detector's channels or on the scintillator planes.
As can be seen in the data example file, the format is a string of 5 numbers that, in this order, represent:
- "DAQ_time", the time elapsed since the beginning of the data taking in s;
- "orbit number", the LHC orbit number of the event simulated by the Xilinx Virtex-7 FPGA VC707 clock, it resets at 4095;
- "OBDT pin", the OBDT channel where the signal was recorded;
- "BX", the simulated bunch crossing associated with the measurement, in each orbit there are 3564 BX;
- "TDC fine measurement", the OBDT TDC measurement. 

A simulator of the MiniDTs readout program has been developed. The code generates random numbers for the pin, orbit, BX, and TDC measurement values. 
These are then formatted in the same shape as the actual readout program and written into a text file in the working directory.  
When the simulated pin corresponds to the scintillator pin, the program generates an event of four vertical hits in the chamber, starting from a random cell of the top layer. 
This feature is needed to simulate a timebox, i.d. the plot of the distribution of the time elapsing between the scintillator and the layers signals. 
Based on the analysis of actual data, the timebox has a width of around 400ns. For this reason, the events are randomly simulated in a 400ns interval before the scintillator signal. 


Before running the monitor program, the user needs to specify in the configuration file the paths to the data and runs' log files, where the plots should be saved and refreshed every 30s. 
Through the configuration file, the user can also decide if the plots are to be shown as a matplotlib figure during the program execution or only saved in the chosen folders.
If the program does not find the configuration file in the working folder, the user is asked to specify the file through a graphical interface.  

The run number can be passed as a parameter when executing the program. 
Since for the monitor display streamlit is used, when acquiring the run 32 file, the monitor can be called using  
> user@host $  streamlit run tbo_bo_reader.py 32

If the user only wants to save the plots or prefers to display them using matplotlib, it can run the monitor as
> user@host $  python tbo_bo_reader.py 32

The simulated file run number is identified by -1, in this case, when running with streamlit the monitor should be run using the following command

> user@host $  streamlit run tbo_bo_reader.py -- -1

in order to stop streamlit to parse further than --. 

If no run number is passed as a parameter, the code opens the previous runs' log file and computes the current run number. If there is no such file, the program assumes the simulated file is being used. 

When the monitor starts, it moves to the end of the text file produced by the MiniDTs acquisition program and reads the newly written lines every 30 seconds.
With these data, it builds the rate and instantaneous timebox plots that are refreshed at each reading, and it stores them in the cumulative occupancy and timebox plots.
These plots are saved in a folder with the run name, in the folder specified by the user through the configuration file.
Moreover, the produced plots are shown on a local web page, refreshing each time new data is plotted.
<img src="https://github.com/GiuliaPaggi/MiniDT_online_monitor/blob/main/plot_examples/monitorpage.png" width="1000">

If the readout stop and the file read by the monitor program is not modified anymore, the monitor stops after 2 minutes from the last modification.


## Structure of the project
The project is divided in the following way:
- **tbo_bo_reader.py**:  the file that reads the run data file during the data taking and manages the online monitor. Every 30 seconds, it reads all lines that were written on the file in the elapsed time, and displays and saves the updated plots. The paths of the folders (the data file, past runs log file, and where the plots should be saved) are set via the configuration file ;
- **PLOTS.py**: file in which the plotting functions for the monitor are defined;
- **tbo_bo_writer_simulator.py**: the simulator of one MiniDT chamber readout, writes a line in a text file every 0.1s with randomly generated hits;
- **SORT.py**: file in which the sorting function of the simulator is defined;
- **test_writer.py**: test file for the simulator function.
- **config.txt**: the text file containing the folder paths necessary for finding the data file and correctly saving the plots. The user can choose whether to display the plots using matplotlib, or just save them through the configuration file and visualize them on the online web page.

## Output
#### Cumulative occupancy 
- per channel: the plot shows the cumulative hits in each channel of a MiniDT chamber, numbered from 0 to 63.
<img src="https://github.com/GiuliaPaggi/MiniDT_online_monitor/blob/main/plot_examples/Entries.PNG" width="500">


- 2D: the plot shows the cumulative hits on a 2D map, each rectangle represents one of the chamber cells. The occupancy plot helps in identifying channels with high noise rates or, on the other side, channels with a reduced rate.
<img src="https://github.com/GiuliaPaggi/MiniDT_online_monitor/blob/main/plot_examples/Entries_2D.PNG" width="500">

- relative to scintillator events, both per channel and 2D: to identify and monitor which channels are covered by the scintillator area
<p float="left">
  <img src="https://github.com/GiuliaPaggi/MiniDT_online_monitor/blob/main/plot_examples/Scintillator_event_entries.PNG" width="500" />
  <img src="https://github.com/GiuliaPaggi/MiniDT_online_monitor/blob/main/plot_examples/Scintillator_event_entries_2D.PNG" width="500" /> 
</p>


#### Instantaneous rate
- per channel: the plot shows the rate in the last 30s of data taking. It can help identify transient external sources of noise.
<img src="https://github.com/GiuliaPaggi/MiniDT_online_monitor/blob/main/plot_examples/Rate.PNG" width="500">

-2D: the plot shows the rate on a 2D map, each rectangle represents one of the chamber cells. It can help identify channels with high transient noise.

<img src="https://github.com/GiuliaPaggi/MiniDT_online_monitor/blob/main/plot_examples/Rate_2D.PNG" width="500">

- relative to scintillator events, both per channel and 2D: to identify and monitor which channels are covered by the scintillator area
<p float="left">
  <img src="https://github.com/GiuliaPaggi/MiniDT_online_monitor/blob/main/plot_examples/Scintillator_event_rate.PNG" width="500" />
  <img src="https://github.com/GiuliaPaggi/MiniDT_online_monitor/blob/main/plot_examples/Scintillator_event_rate_2D.PNG" width="500" /> 
</p>

#### Cumulative timebox
The plot shows the time difference between the scintillator signal and the chamber response. It depends on the drift time of the electrons in the cells and it can help to identify problems in the gas distribution inside the chamber.
<img src="https://github.com/GiuliaPaggi/MiniDT_online_monitor/blob/main/plot_examples/Cumulative_Timebox.PNG" width="500">

#### Instantaneous timebox
The plot shows the time difference between the scintillator signal and the chamber response in the last 30s of events.
<img src="https://github.com/GiuliaPaggi/MiniDT_online_monitor/blob/main/plot_examples/Inst_Timebox.PNG" width="500">

<!--## Screenshots
![Example screenshot](./img/screenshot.png)
<!-- If you have screenshots you'd like to share, include them here. -->

## Dependencies
All the modules can be also found in the dependencies.txt file.

In particular, the monitor project is developed in a python 3.9 environment, using the following modules: 
- configparser
- datetime
- matplotlib 
- numpy 
- os
- streamlit
- sys
- time
- tkinter

Additionally, for the readout simulator, the following modules are used:
- datetime
- random 
- sys
- streamlit
- time



