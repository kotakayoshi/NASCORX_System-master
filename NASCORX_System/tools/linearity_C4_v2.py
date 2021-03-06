#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
=== About this script ===

* Purpose and Abstract
To carry out Linearity measurement.
Spectrum is measured for each attenuation level.(0-11 [dBm])
Thanks to PATT, changing attenuation level and measurement are all automatically carried out.
Note that this script is written for C4_System with Sirius(192,168.100.101). ## C4 means 4F Laboratory in Building C

* Devices
- Programable Attenuator (Model - Driver: 11713C(Agilent), Step Att: 8494H(KEYSIGHT))
- Spectrum Analyzer (Model - MS2830A(Anritsu))
- ondotori (Model - TR-72W)
- Calculator (Sirius 192.168.100.101 @ C4_System)

* How to use
** Input
- title : This string becomes filename
- purpose : The aim of each experiment
- sleep time : How long do you wait for trace after switching attenuation level
- Frequency Band : Used to calculate average

** Output
- data (csv file)
- images x 12 (Raw data and linearity check. References are 0-10 [dBm] )
- logfile (A text file recording conditions, settings of devices and results. Contents are showed in the bottom of script)
- result (Show Average value on terminal)
This script automatically makes two directories like below whose name are "date of experiment" and "title".
Data and images are saved in the "title" directory.
Only logfile is saved in the "date" directory.
+++++++ Directory Structure +++++++++++
/home/amigos/experiment/
linearity/
         - date/
            - logfile(text file)
            - title/
                - data(csv file)
                - images(png file)
+++++++++++++++++++++++++++++++++++++++


* History
** Written by T.Inaba

** Update
2016/05/12 T.Inaba : Add "About this script", and "autolog"
2016/05/13 T.Inaba : Add "Band", "temp, hum". Improve around "title"
2016/05/18 T.Inaba : Add "Sleep" to figure

'''

import time, sys, os
sys.path.append('/home/amigos/pymeasure2-master/')
import pymeasure
sys.path.append('/home/amigos/NASCORX_System/device/')
import CPZ7204
import numpy as np
import matplotlib.pyplot as plt

# Conditions
purpose = raw_input("About this experiment ?  :")
date = time.strftime("%m%d")
datetime = time.strftime("%m%d%H%M")
datetime2 = time.strftime("%m/%d - %H:%M:%S")


# Outputs
savedir = "/home/amigos/data/SIS/HotCold/SA/"
filename = savedir+"HC"+datetime



# Devices =====================================
"""
#Ondoroti
ond = TR72W.tr72w()
# Attenuator
att = A11713B.a11713b()
"""
# Spectrum Analyze
IP_SA = "192.168.100.107"
port_SA = 49153
com_SA = pymeasure.ethernet(IP_SA, port_SA)
sp = pymeasure.Agilent.N9343C(com_SA)

load = CPZ7204.cpz7204()
load.set_home()
print "============"
print "HOT LOAD"
print "Current position is defined as the COLD position"
print "　　　"

# settings of spectrum analyzer
band_start = 2 #[GHz]
band_end = 14 #[GHz]

## Query Setting of Spectrum Analyzer
sp.com.send("BAND?")
rbw_raw = sp.com.readline()
rbw_arr = rbw_raw.split("\n")
rbw = float(rbw_arr[0])/1000
sp.com.send("BAND:VID?")
vbw_raw = sp.com.readline()
vbw_arr = vbw_raw.split("\n")
vbw = float(vbw_arr[0])/1000
sp.com.send("SWE:TIME?")
swtime_raw = sp.com.readline()
swtime_arr = swtime_raw.split("\n")
swtime = float(swtime_arr[0])
sp.com.send("AVER:COUN?")
average_raw = sp.com.readline()
average_arr = average_raw.split("\n")
average = average_arr[0]
sp.com.send('FREQ:STAR?')
start_freq = float(sp.com.readline())/1e9 #[GHz]
sp.com.send('FREQ:STOP?')
stop_freq = float(sp.com.readline())/1e9 #[GHz]
sp.com.send('SWE:POIN?')
trace_point = float(sp.com.readline())

#Calculate Band range
ch_width = (stop_freq - start_freq)/trace_point
ch_start = int((band_start - start_freq)/ch_width)
ch_end = int((band_end - start_freq)/ch_width)
freq = np.linspace(start_freq, stop_freq, trace_point)
sa = np.array([freq])   #sa means "spec array"


# Start Measurement ===========================
sp.com.send('TRAC? TRAC1')
spec_raw = sp.com.readline()
spec = np.array([spec_raw.split(',')], float)
sa = np.r_[sa, spec]
load.rot_angle(speed=3000, angle=-90)
time.sleep(2)
sp.com.send('TRAC? TRAC1')
spec_raw = sp.com.readline()
spec = np.array([spec_raw.split(',')], float)
sa = np.r_[sa, spec]
load.go_home(speed=3000)
np.savetxt(filename+".csv", sa, delimiter=",")


##plot raw data
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.plot(sa[0], sa[1], label="COLD")
ax1.plot(sa[0], sa[2], label="HOT")
ax1.set_xlabel("frequency[GHz]")
ax1.set_ylabel("Amplitude [dBm]")
ax1.set_title("raw data")
ax1.set_xlim([start_freq, stop_freq])
ax1.grid()
ax1.legend(loc='upper left', prop={'size': 13})
'''
plt.subplots_adjust(left=0.1, right=0.8)
ax1.annotate("RBW: "+str(rbw)+"[kHz]", xy=(1.01, 0.25), xycoords='axes fraction', fontsize=10,
             horizontalalignment='left', verticalalignment='bottom')
ax1.annotate("VBW: "+str(vbw)+"[kHz]", xy=(1.01, 0.20), xycoords='axes fraction', fontsize=10,
             horizontalalignment='left', verticalalignment='bottom')
ax1.annotate("Sweep: "+str(swtime)+"[s]", xy=(1.01, 0.15), xycoords='axes fraction', fontsize=10,
             horizontalalignment='left', verticalalignment='bottom')
ax1.annotate("Average: "+str(average), xy=(1.01, 0.95), xycoords='axes fraction', fontsize=10,
             horizontalalignment='left', verticalalignment='bottom')
'''
plt.savefig(filename+"_rawdata.png")
plt.show()


#plot linearity measurement
results = []
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.plot(sa[0], sa[1] - sa[2], label="difference")
ax1.set_xlabel("frequency[GHz]")
ax1.set_ylabel("Amplitude [dBm]")
ax1.set_title("difference of HOT and COLD")
ax1.set_xlim([start_freq, stop_freq])
ax1.grid()
ax1.legend(loc='upper left', prop={'size': 13})
'''
plt.subplots_adjust(left=0.1, right=0.8)
ax1.annotate("RBW: "+str(rbw)+"[kHz]", xy=(1.01, 0.25), xycoords='axes fraction', fontsize=10,
            horizontalalignment='left', verticalalignment='bottom')
ax1.annotate("VBW: "+str(vbw)+"[kHz]", xy=(1.01, 0.20), xycoords='axes fraction', fontsize=10,
            horizontalalignment='left', verticalalignment='bottom')
ax1.annotate("Sweep: "+str(swtime)+"[s]", xy=(1.01, 0.15), xycoords='axes fraction', fontsize=10,
            horizontalalignment='left', verticalalignment='bottom')
ax1.annotate("Average: "+str(average), xy=(1.01, 0.10), xycoords='axes fraction', fontsize=10,
                horizontalalignment='left', verticalalignment='bottom')
'''
plt.savefig(filename+"_dif.png")
plt.show()


#Writing Log file
logfile = savedir+"autolog_%s.txt"%(date)
f = open(logfile, 'a')
log = """

======== Experiment ==================
Date time : %s
Temperature : ** [deg]
Humidity : ** [percent]

** About this experiment **
%s

** Setting of Spectrum Analyzer **
RBW : %s [kHz]
VBW : %s [kHz]
Sweep time : %s [s]
Average : %s
Start freq : %s [GHz]
End freq : %s [GHz]
Trace point : %s
Band : %s - %s [GHz]

"""%(datetime2, purpose, rbw, vbw, swtime, average, start_freq, stop_freq, trace_point, band_start, band_end)
f.write(log)
f.close()