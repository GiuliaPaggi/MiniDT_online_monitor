# MiniDT_online_monitor
MiniDTs online monitor project. Read data and show occupancy plot in real time.

## Table of Contents
* [General Info](#general-information)
* [Usage](#usage)
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
The MiniDTs are operated with the same high volatge and gas mixture condition used in CMS.
The signals on the front end are read using two boards: an On-detector Board for Drift Tube (OBDT) version 1 for the time to digital conversion, and a Xilinx Virtex-7 FPGA VC707 that provides the simulated LHC clock and can be used to implement the slow control.  
The telescope will be completed with three scintillator planes, instrumented with photomultipliers to read out the signals.
These are going to be located at the top, at the bottom, and in between the two MiniDTs to provide an independent signal, using the coincidence of two or more planes. This signal will be used to identify muons crossing the telescope in the offline analysis of the data from the miniDTs, which have a trigger-less data acquisition system. 
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
The path of the file is fixed but the run number can be passed as a parameter when executing the program. 
For example, when acquiring the run 32 file, the monitor can be called using  
> user@host $  python tbo_bo_reader.py 32


If no run number is passed as a parameter, the user is asked to specify it before the program begins.


> user@host $ python tbo_bo_reader.py 
> Error, no run number specified. Enter the run number and press the enter key: 




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


## Project Status
The project is in progress. At the moment only the occupancy for one chamber is displayed. 
