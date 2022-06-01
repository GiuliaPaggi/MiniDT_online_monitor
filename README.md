# MiniDT_online_monitor
MiniDTs online monitor project. Show occupancy plots, rate, and timebox in real-time.

## Table of Contents
* [General Info](#general-information)
* [Usage](#usage)
* [Structure of the project](#structure-of-the-project)
* [Output](#output)
* [Technologies Used](#technologies-used)
* [Project Status](#project-status)

<!-- * [Features](#features)
* [Screenshots](#screenshots) 
--* [Setup](#setup)
  -->

<!-- * [Room for Improvement](#room-for-improvement) -->



## General Information
Using spare material from the original CMS DT chambers, eight smaller size SLs, called MiniDTs were built at INFN Legnaro National Laboratory in Padova. 
Using two of these MiniDTs we aim to install a cosmic rays telescope and test its efficiency and resolution. 
The MiniDTs are operated with the same high voltage and gas mixture condition used in CMS.
The signals on the front end are read using two boards: an On-detector Board for Drift Tube (OBDT) version 1 for the time to digital conversion, and a Xilinx Virtex-7 FPGA VC707 that provides the simulated LHC clock and can be used to implement the slow control.  
The telescope will be completed with three scintillator planes, instrumented with photomultipliers to read out the signals.
These will be located at the top, at the bottom, and in between the two MiniDTs to provide an independent signal, using the coincidence of two or more planes. This signal will be used to identify muons crossing the telescope in the offline analysis of the data from the miniDTs, which have a trigger-less data acquisition system. 
This project aims to develop an online monitor that can allow for a check of the data acquisition process, controlling the data quality and the detector status. 
The focus is on the occupancy of each channel and the time difference between the scintillator and the MiniDTs front-end signals. The first allows identifying during the data taking dead or particularly noisy channels.
The latter is related to the linearity of the MiniDT's space-time response, which depends on the electrons' drift velocity in the chamber.
It can help identify inhomogeneities in the gas distribution or problems in the cells' electric field configurations. 
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->

## Usage
This project is meant to be used on the text file written by the MiniDTs acquisition program. Each line in this file is one event recorded in the detector's channels or on the scintillator planes.
The format is a string of 5 numbers that, in this order, represent:
- "DAQ_time", the time elapsed since the beginning of the data taking in s;
- "orbit number", the LHC orbit number of the event simulated by the Xilinx Virtex-7 FPGA VC707 clock, it resets at 4095;
- "OBDT pin", the OBDT channel where the signal was recorded;
- "BX", the simulated bunch crossing associated with the measurement, in each orbit there are 3564 BX;
- "TDC fine measurement", the OBDT TDC measurement. 

A simulator of the MiniDTs readout program has been developed. The code generates random numbers for the pin, orbit, BX, and TDC measurement values. 
These are then formatted in the same shape as the actual readout program and written into a text file in the working directory.  
When the simulated pin corresponds to the scintillator pin, the program generates an event of four vertical hits in the chamber, starting from a random cell of the top layer. 
This feature is needed to build a timebox, i.d. the plot of the distribution of the time elapsing between the scintillator and the layers signals. 
Based on the analysis of actual data, the timebox has a width of tilde 400ns. For this reason, the events are randomly simulated in a 400ns interval before the scintillator signal. 

The path of the file is fixed but the run number can be passed as a parameter when executing the program. 
For example, when acquiring the run 32 file, the monitor can be called using  
> user@host $  python tbo_bo_reader.py 32


If no run number is passed as a parameter, the code opens the past runs' log file and computes the current run number. The simulated file run number is identified by -1 and has to be passed as a parameter.
<!-- the user is asked to specify it before the program begins, and the simulated file is identified by -1. 
> user@host $ python tbo_bo_reader.py 
> 'No run number specified. Enter the run number and press the enter key (to use the simulated data file, enter -1): -->






## Structure of the project
The project is divided in the following way:
- **tbo_bo_reader.py**:  the file that reads the run data file during the data taking and manages the online monitor. Every 30 seconds, it reads all lines that were written on the file in the elapsed time, and displays and saves the updated plots. When it is closed, it saves all the cumulative plots in a folder with the run name. The paths of the folders (the data file, and where the plots should be saved) is set via the configuration file ;
- **PLOTS.py**: file in which the plotting functions for the monitor are defined;
- **tbo_bo_writer_simulator.py**: the simulator of one MiniDT chamber readout, writes a line in a text file every 0.1s with randomly generated hits;
- **SORT.py**: file in which the sorting function of the simulator is defined;
- **test_writer.py**: test file for the simulator function.
- **config.txt**: text file containig the folders paths necessary for finding the data file and correctl save the plots.

## Output
#### Cumulative occupancy 
- per channel: the plot shows the cumulative hits in each channel of a MiniDT chamber, numbered from 0 to 63.

- 2D: the plot shows the cumulative hits on a 2D map, each rectangle represents one of the chamber cells. The occupancy plot helps in identifying channels with high noise rates or, on the other side, channels with a reduced rate.


#### Instantaneous rate
- per channel: the plot shows the rate in the last 30s of data taking. It can help identify transient external sources of noise.

-2D: the plot shows the rate on a 2D map, each rectangle represents one of the chamber cells. It can help identify channels with high transient noise.

#### Cumulative timebox
The plot shows the time difference between the scintillator signal and the chamber response. It depends on the drift time of the electrons in the cells and it can help to identify problems in the gas distribution inside the chamber.

#### Instantaneous timebox
The plot shows the time difference between the scintillator signal and the chamber response in the last 30s of events.


<!--## Screenshots
![Example screenshot](./img/screenshot.png)
<!-- If you have screenshots you'd like to share, include them here. -->

## Technologies Used
The project is developed in a python 3.9 environment, using the following modules: 
- Matplotlib - version 3.5
- time 
- sys 
- os
- datetime
- numpy 


## Project Status
The project is in progress. At the moment it's possible to visualize the channels occupancy, the 2D chamber occupancy, the rate of the last 30s both per channel and in the 2D configuration, the timebox of the whole run, and of the last 30s of data taking. 
The produced plots are also saved in .PNG format.
