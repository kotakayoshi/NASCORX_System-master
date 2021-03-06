# ! /usr/bin/env python
# _*_ coding: UTF-8 _*_


# import modules
import time, sys, datetime, os, csv, signal
import matplotlib.pyplot as plt
import numpy as np
sys.path.append('/home/amigos/NASCORX_System/base/')
import Cryo, Lo
sys.path.append('/home/amigos/NASCORX_System/device/')
import ML2437A, CPZ7204

def IVtrace(ch, Vrange=[0, 12], average=5, pngpath='/home/amigos/data/SIS/IV/', LOrange=[90, 120], LOres=5.0, Loatt_list=[20, 20, 20, 20, 20, 20], gragh=1):
    '''
    DESCRIPTION
    ================

    ARGUMENT
    ================
        1. : 
            Type: 

    RETURN
    ================
    Nothing.
    '''
    Vres = 0.1
    Vrres = 0.5
    if ch==0:
        DAch = 0
        VADch = 0
        IADch = 1
    else:
        DAch = 1
        VADch = 2
        IADch = 3
    box = Cryo.mixer()
    Lo.sg = Lo.firstlo(multiplier=6)
    load = CPZ7204.cpz7204()
    pm = ML2437A.ml2437a(IP='192.168.100.113', GPIB=13)
    t = datetime.datetime.now()
    ut = t.strftime('%Y%m%d_%H%M%S')
    V_mon1 = np.array([])
    Verr_mon1 = np.array([])
    I_mon1 = np.array([])
    Ierr_mon1 = np.array([])
    V_list1 = np.arange(Vrange[0], Vrange[1], 0.05)
    V_list2 = np.arange(Vrange[0], Vrange[1], 0.05)
    load.set_home() # define HOT position
    print('INPUT Room Temperature [℃]')
    tr = raw_input()
    Tamb = float(tr) + 273.2
    print(V_list1)
    print('======== START ========')
    for v in V_list1:
        print('V = '+str(round(v, 2))+' mV')
        box.set_sisv(Vmix=v, ch=DAch)
        Vmon = box.monitor_sis()
        Vmon = Vmon[VADch]*1e+1
        dV1 = np.array([])
        dI1 = np.array([])
        time.sleep(0.1)
        for j in range(average):
            ret = box.monitor_sis()
            dV1 = np.append(dV1, ret[VADch]*1e+1)
            dI1 = np.append(dI1, ret[IADch]*1e+3)
        dV_mean1 = np.mean(dV1, axis=0)
        dV_std1 = np.std(dV1, axis=0)
        V_mon1 = np.append(V_mon1, dV_mean1)
        Verr_mon1 = np.append(Verr_mon1, dV_std1)
        dI_mean1 = np.mean(dI1, axis=0)
        dI_std1 = np.std(dI1, axis=0)
        I_mon1 = np.append(I_mon1, dI_mean1)
        Ierr_mon1 = np.append(Ierr_mon1, dI_std1)
    V_rlist1 = np.arange(Vrange[0], Vrange[1], Vrres)
    V_rlist1 = np.sort(V_rlist1)[::-1]
    for v in V_rlist1:
        print('V = '+str(round(v, 2))+' mV')
        box.set_sisv(Vmix=v, ch=DAch)
        time.sleep(0.1)
    print('======== END ========')
    print(dV1)
    print(dI1)
    time.sleep(1.0)
    print('set SG')
    Lo.sg.start_osci(LOrange[0], 19.0)
    Lo_list = np.arange(LOrange[0], LOrange[1], LOres)
    for i in range(len(Lo_list)):
        Lo.sg.change_freq(freq=Lo_list[i])
        box.set_loatt(att=Loatt_list[i], ch=ch)
        lf = Lo.sg.query_status
        V_mon2 = np.array([])
        V_mon3 = np.array([])
        Verr_mon2 = np.array([])
        Verr_mon3 = np.array([])
        I_mon2 = np.array([])
        I_mon3 = np.array([])
        Ierr_mon2 = np.array([])
        Ierr_mon3 = np.array([])
        hot = np.array([])
        cold = np.array([])
        yfac = np.array([])
        trx = np.array([])
        print(V_list2)
        print('======== START ========')
        for v in V_list2:
            print('V = '+str(round(v, 2))+' mV')
            box.set_sisv(Vmix=v, ch=DAch)
            dV2 = np.array([])
            dI2 = np.array([])
            dV3 = np.array([])
            dI3 = np.array([])
            time.sleep(0.1)
            
            if 4.0 < v < 10:
                #measure IFV
                Vmon = box.monitor_sis()
                Vmon = Vmon[VADch]*1e+1
                Phot = pm.measure(ch=1, resolution=3)
                load.rot_angle(speed=2000, angle=-90) # COLD
                time.sleep(0.4)
                Pcold = pm.measure(ch=1, resolution=3)
                load.go_home(speed=2000) # HOT
                for j in range(average):
                    ret = box.monitor_sis()
                    dV3 = np.append(dV3, ret[VADch]*1e+1)
                    dI3 = np.append(dI3, ret[IADch]*1e+3)
                dV_mean3 = np.mean(dV3, axis=0)
                dV_std3 = np.std(dV3, axis=0)
                V_mon3 = np.append(V_mon3, dV_mean3)
                Verr_mon3 = np.append(Verr_mon3, dV_std3)
                dI_mean3 = np.mean(dI3, axis=0)
                dI_std3 = np.std(dI3, axis=0)
                I_mon3 = np.append(I_mon3, dI_mean3)
                Ierr_mon3 = np.append(Ierr_mon3, dI_std3)
                yfac_col = Phot - Pcold
                hot = np.append(hot, Phot)
                cold = np.append(cold, Pcold)
                try:
                    trx_col = (Tamb - 77.79*10**(yfac_col/10))/(10**(yfac_col/10) - 1)
                    if trx_col < 0:
                        trx_col = 1000
                    else:
                        pass
                except ZeroDivisionError:
                    trx_col = 1000
                yfac = np.append(yfac, yfac_col)
                trx = np.append(trx, trx_col)
            else:
               pass
                
            #measure IV
            for j in range(average):
                ret = box.monitor_sis()
                dV2 = np.append(dV2, ret[VADch]*1e+1)
                dI2 = np.append(dI2, ret[IADch]*1e+3)
            dV_mean2 = np.mean(dV2, axis=0)
            dV_std2 = np.std(dV2, axis=0)
            V_mon2 = np.append(V_mon2, dV_mean2)
            Verr_mon2 = np.append(Verr_mon2, dV_std2)
            dI_mean2 = np.mean(dI2, axis=0)
            dI_std2 = np.std(dI2, axis=0)
            I_mon2 = np.append(I_mon2, dI_mean2)
            Ierr_mon2 = np.append(Ierr_mon2, dI_std2)
            
        V_rlist2 = np.arange(Vrange[0], Vrange[1], Vrres)
        V_rlist2 = np.sort(V_rlist2)[::-1]
        for v in V_rlist2:
            print('V = '+str(round(v, 2))+' mV')
            box.set_sisv(Vmix=v, ch=DAch)
            time.sleep(0.1)
        
        
        print('======== END ========')
        print(dV2)
        print(dI2)
    
        #plot part
        filename1 = 'SISIV'+ut+str(Lo_list[i])+'.png'
        filename2 = 'SISIFV'+ut+str(Lo_list[i])+'.png'
        filename3 = 'SISTrx and Y-factor'+ut+str(Lo_list[i])+'.png'
        plt.figure()
        #plt.errorbar(V_mon1, I_mon1, xerr=Verr_mon1, yerr=Ierr_mon1, fmt='.', ecolor='red', color='red', label='ch='+str(DAch))
        plt.plot(V_mon1, I_mon1, linestyle='-', color='black', linewidth=1.0, label='LO nashi')
        #plt.errorbar(V_mon2, I_mon2, xerr=Verr_mon2, yerr=Ierr_mon1, fmt='.', ecolor='blue', color='blue', label='ch='+str(DAch))
        plt.plot(V_mon2, I_mon2, linestyle='-', color='red', linewidth=1.0, label='LO ari')
        plt.title('SIS Mixer I-V '+t.strftime('%Y/%m/%d/ %H:%M:%S' + ' LO ='+str(Lo_list[i])+'GHz'+' LOatt='+str(Loatt_list[i])))
        plt.xlim(0, V_mon1.max())
        plt.ylim(I_mon1.min(), I_mon1.max())
        plt.xlabel('Mixer Voltage [mV]')
        plt.ylabel('Mixer Current [uA]')
        plt.grid()
        plt.legend(loc='upper left')
        plt.savefig(pngpath+'IV/'+filename1)
        if gragh == 1:
            plt.show()
        else:
        	pass
        
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        ax2 = ax1.twinx()
        ax1.plot(V_mon3, I_mon3, linestyle='-', color='black', linewidth=1.0, label='I-V')
        ax2.plot(V_mon3, hot, linestyle='-', color='red', linewidth=1.0, label='hot')
        ax2.plot(V_mon3, cold, linestyle='-', color='blue', linewidth=1.0, label='cold')
        plt.title('SIS Mixer I-V '+t.strftime('%Y/%m/%d/ %H:%M:%S' + ' LO ='+str(Lo_list[i])+'GHz'+' LOatt='+str(Loatt_list[i])))
        ax1.set_xlim(4.0, 10)
        ax1.set_ylim(I_mon2.min(), I_mon2.max())
        ax2.set_ylim(-40, -20)
        ax1.set_xlabel('Mixer Voltage [mV]')
        ax1.set_ylabel('Mixer Current [uA]')
        ax2.set_ylabel('IF power [dbm]')
        ax1.grid(True)
        plt.legend(loc='upper left')
        plt.savefig(pngpath+'IFV/'+filename2)
        if gragh == 1:
            plt.show()
        else:
        	pass
        
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        ax2 = ax1.twinx()
        #ax3 = ax1.twinx()
        ax1.plot(V_mon3, I_mon3, linestyle='-', color='black', linewidth=1.0, label='I-V')
        ax2.plot(V_mon3, yfac, linestyle='-', color='green', linewidth=1.0, label='Y-factor')
        #ax3.plot(V_mon3, trx, linestyle='-', color='red', linewidth=1.0, label='Trx')
        plt.title('SIS Mixer I-V '+t.strftime('%Y/%m/%d/ %H:%M:%S' + ' LO ='+str(Lo_list[i])+'GHz'+' LOatt='+str(Loatt_list[i])))
        fig.subplots_adjust(right=0.75)
        #ax3.spines['right'].set_position(('axes', 1.2))
        #ax3.set_frame_on(True)
        ax1.set_xlim(4.0, 10)
        ax1.set_ylim(I_mon2.min(), I_mon2.max())
        ax2.set_ylim(0, 6)
        #ax3.set_ylim(0, 300)
        ax1.set_xlabel('Mixer Voltage [mV]')
        ax1.set_ylabel('Mixer Current [uA]')
        ax2.set_ylabel('Y-factor [dBm]')
        #ax3.set_ylabel('Trx [K]')
        ax1.grid(True)
        plt.legend(loc='upper left')
        plt.savefig(pngpath+'IFV/'+filename3)
        if gragh == 1:
            plt.show()
        else:
        	pass
    
    print('END MEASUREMENT')
    Lo.sg.end_osci()
    
IVtrace(ch=0, LOrange=[90, 120], LOres=5.0, Loatt_list=[25, 28, 21, 21, 17, 15], gragh=0)
# written by K.Urushihara

