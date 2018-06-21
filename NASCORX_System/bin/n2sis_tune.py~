#! /usr/bin/env python

# import modules
# --------------
import time

import numpy
import matplotlib.pyplot

import equipment_nanten
from base import config_handler
from ..base import Cryo


class IV_curve(object):
    method = 'IV Curve Measurement'
    ver = '2017.11.09'
    savedir = '/home/amigos/NASCORX_Measurement/SIStune/'

    def __init__(self):
        pass

    def run(self, initV=0.0, finV=6.0, interval=0.1, driver=None, onoff=range(2), reconfigure=True,
            filefmt='csv'):

        # Print Welcome massage
        # ---------------------
        print('\n\n'
              ' =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'
              '   N2 RX : SIS IV curve Measurement \n'
              ' =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'
              ' ver - {}\n'
              '\n\n'.format(self.ver))

        # Input value check
        # -----------------
        repeat = self.input_value_check(initV=initV, finV=finV, interval=interval)

        # Set Driver
        # ----------
        if driver is None: self.driver = Cryo.box()
        else: self.driver = driver
        print('PCI board drivers are set.')

        # == Main ========

        # Measurement part
        # ----------------
        AD_data = self.IVcurve_measure(repeat=repeat, initV=initV, interval=interval, onoff=onoff)

        # Data saving part
        # ----------------
        datetime = time.strftime('%Y%m%d-%H%M')
        filename = self.savedir + 'SISIV_{}.{}'.format(datetime, filefmt)
        header = 'D/A-SISV,1L-V,1L-I,1R-V,1R-I'
        numpy.savetxt(filename, AD_data, fmt='%.5f', header=header, delimiter=',')

        # Reconfigure SIS bias setting
        # ----------------------------
        #TODO --> test
        if driver is None: self.driver.close_box()
        if reconfigure is True: self.IVcurve_recofigure()

        # Data loading
        # ------------
        AD_data = numpy.loadtxt(filename, skiprows=1, delimiter=',')

        # Plot part
        # ---------
        self.IVcurve_ttlplot(AD_data=AD_data, initV=initV, finV=finV, datetime=datetime)

        # Output information on terminal
        # ------------------------------
        print('\n'
              ' ======== SIS IV Curve MEASUREMENT ========\n'
              ' Time Stamp    : {}\n'
              ' Start SISV    : {} [mV]\n'
              ' Finish SISV   : {} [mV]\n'
              ' Lo Attenuation: !!coming soon!! [mA]\n'.format(datetime, initV, finV))
        return

    def input_value_check(self, initV, finV, interval):
        Vmix_limit = 30  # [mv]
        if -Vmix_limit <= initV <= finV <= Vmix_limit:
            pass
        else:
            msg = '{0}\n{1}\n{2}'.format('-- Input Invalid Value Error --',
                                         '!!! Invalid Voltage !!!',
                                         'Available Voltage: -30 -- 30 [mV]')
            raise ValueError(msg)
        repeat = int(abs(initV - finV) / interval)
        return repeat

    def IVcurve_divplot(self, AD_data, ch, initV, finV, datetime):
        fig = matplotlib.pyplot.figure()
        ax = fig.add_subplot(1, 1, 1)
        label = '230GHz-SIS'
        ax.plot(AD_data[:, 1+2*(ch-1)], AD_data[:, 2+2*(ch-1)], label=label)
        ax.set_xlabel('SIS V [mV]')
        ax.set_ylabel('SIS I [uA]')
        ax.set_xlim([initV, finV])
        ax.legend(loc='upper left', prop={'size': 7})
        ax.grid(color='gray', linestyle='--')

        fig.tight_layout()
        # fig.subplots_adjust(top=0.9)
        figname = self.savedir + 'n2sisIV_ch{}_{}.png'.format(ch, datetime)
        fig.savefig(figname)
        fig.show()
        return

    def IVcurve_ttlplot(self, AD_data, initV, finV, datetime):
        fig = matplotlib.pyplot.figure(figsize=(9, 7))
        ax = [fig.add_subplot(1, 2, i+1) for i in range(2)]
        labels = ['230GHz-CH1', '230GHz-CH2']
        [_ax.plot(AD_data[:, 1+2*i], AD_data[:, 2+2*i], label=labels[i]) for i, _ax in enumerate(ax)]
        [_ax.set_xlim([initV, finV]) for _ax in ax]
        [_ax.set_ylim([-10, 500]) for _ax in ax]
        [_ax.set_yticklabels('') for i, _ax in enumerate(ax) if i==1]
        [_ax.set_xlabel('SIS V [mV]') for i, _ax in enumerate(ax)]
        [_ax.set_ylabel('SIS I [uA]') for i, _ax in enumerate(ax) if i==0]
        [_ax.legend(loc='upper left', prop={'size': 7}, numpoints=1) for _ax in ax]
        [_ax.grid(color='gray', linestyle='--') for _ax in ax]

        fig.tight_layout()
        fig.subplots_adjust(top=0.9)
        fig.suptitle('SIS IV Curve Measurement: {}'.format(datetime), fontsize=15)
        figname = self.savedir + 'n2sisIV_{}.png'.format(datetime)
        fig.savefig(figname)
        fig.show()
        return

    def IVcurve_measure(self, repeat, initV=0.0, interval=0.1, onoff=[0]*2):
        AD_data = []

        # Measurement part
        # ----------------
        for i in range(repeat+1):
            temp = []
            setV = initV + i * interval
            setV_list = [0] * 2
            for j in range(2):
                if onoff[j] == 1: setV_list[j] = setV
                else: pass
            self.driver.set_sisv(Vmix=setV_list)
            time.sleep(0.2)
            ret = self.driver.monitor_sis()
            temp.append(setV)
            # scaling
            # -------
            # TODO : 計算処理を後でまとめた方が効率がいい??
            for j in range(4):
                if j % 2 == 0:
                    temp.append(ret[j]*1e+1)  # AD[V] --> bias [mV]
                elif j % 2 == 1:
                    temp.append(ret[j]*1e+3)  # AD[V] --> current [uA]
            AD_data.append(temp)
        return AD_data

    def IVcurve_recofigure(self):
        # get params --
        params = config_handler.Config_handler.load_sis_params(ret='array')
        # set bias --
        self.driver.set_sisv(Vmix=params[:, 0])
        # self.box.set_Vd(voltage=params[:, 1])
        # self.box.set_Vg1(voltage=params[:, 2])
        # self.box.set_Vg2(voltage=params[:, 3])
        self.driver.set_loatt(att=params[:, 4])
        return


class Trx_curve(object):
    method = 'Trx Curve Measurement'
    ver = '2017.11.09'
    savedir = '/home/amigos/NASCORX_Measurement/SIStune/'

    def __init__(self):
        self.dfs = equipment_nanten.dfs()
        self.m4 = equipment_nanten.m4()
        self.hot = equipment_nanten.hot_load()
        pass

    def run(self, initV=0.0, finV=6.0, interval=0.1, ch=1, integ=0.1, driver=None, reconfigure=True, fmt='csv'):

        # Print Welcome massage
        # ---------------------
        print('\n\n'
              ' =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'
              '   N2 RX : SIS Tsys curve Measurement \n'
              ' =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'
              ' ver - {}\n'
              '\n\n'.format(self.ver))

        # Input value check
        # -----------------
        repeat = self.input_value_check(initV=initV, finV=finV, interval=interval)

        # Set Driver
        # ----------
        if driver is None: self.driver = Cryo.box()
        else: self.driver = driver
        print('PCI board drivers are set.')

        # == Main ========

        # Measurement part
        # ----------------
        result = self.Trx_measure(repeat=repeat, initV=initV, interval=interval, ch=ch, integ=integ)
        lo_att = self.driver.query_loatt()

        # Calculate Y-Factor and Tsys
        # ---------------------------
        result = self.Trx_calculate(result=result)

        # Data saving part
        # ----------------
        datetime = time.strftime('%Y%m%d-%H%M')
        filename = self.savedir + 'tsys_curve_Lo{}mA_{}.{}'.format(lo_att, datetime, fmt)
        header = 'DA-V,Vhot,Ihot,Phot1,Phot2,Vcold,Icold,Pcold1,Pcold2,Yfac1,Yfac2,Tsys1,Tsys2'
        numpy.savetxt(filename, result, fmt='%.5f', header=header, delimiter=',')

        # Reconfigure SIS bias setting
        # ----------------------------
        #TODO --> test
        if driver is None: self.driver.close_box()
        if reconfigure is True: self.Trx_recofigure()

        # Data loading
        # ------------
        data = numpy.loadtxt(filename, skiprows=1, delimiter=',')

        # Plot part
        # ---------
        self.Trx_ttlplot(data=data, initV=initV, finV=finV, datetime=datetime, lo_att=lo_att)
        return

    def input_value_check(self, initV, finV, interval):
        Vmix_limit = 30  # [mv]
        if -Vmix_limit <= initV <= finV <= Vmix_limit:
            pass
        else:
            msg = '{0}\n{1}\n{2}'.format('-- Input Invalid Value Error --',
                                         '!!! Invalid Voltage !!!',
                                         'Available Voltage: -30 -- 30 [mV]')
            raise ValueError(msg)
        repeat = int(abs(initV - finV) / interval)
        return repeat

    def Trx_measure(self, repeat, initV=0.0, interval=0.1, ch=1, integ=0.1):
        result = []

        # HOT measurement
        # ---------------
        # TODO : HOT IN
        data_hot = self.Trx_sweep_sisv(repeat, initV=initV, interval=interval, ch=ch, integ=integ)

        # COLD measurement
        # ----------------
        # TODO : HOT OUT, OBS SKY
        data_sky = self.Trx_sweep_sisv(repeat, initV=initV, interval=interval, ch=ch, integ=integ)

        # data arrangement
        # ----------------
        result.append(data_hot)
        result.append(data_sky)
        ret = numpy.array(result)
        return ret

    def Trx_sweep_sisv(self, repeat, initV=0.0, interval=0.1, ch=1, integ=0.1):
        result = []
        setV_list = [0] * 2

        for i in range(repeat+1):
            temp = []
            setV = initV + i * interval

            # bias set
            # --------
            setV_list[ch-1] = setV
            self.driver.set_sisv(Vmix=setV_list)

            time.sleep(0.2)

            # data receive
            # ------------
            # spec = self.client.oneshot(integtime=integ, repeat=1, start=None)
            spec = self.dfs.oneshot(1, integ, 0)
            ad = self.driver.monitor_sis()

            # data arrangement
            # ----------------
            temp.append(setV)
            temp.append(ad[(ch-1)*2]*1e+1)      # AD[V] --> bias [mV]
            temp.append(ad[(ch-1)*2+1]*1e+3)    # AD[V] --> current [uA]
            power = numpy.sum(spec, axis=0)
            temp.append(power)
            result.append(temp)
        return result

    def Trx_calculate(self, result, Tamb=300):
        # dB Y-factor --
        Yfac1 = 10*numpy.log10(result[3]/result[7])
        Yfac2 = 10*numpy.log10(result[4]/result[8])

        # Tsys calculation --
        Tsys1 = (Tamb*result[7]) / (result[3]-result[7])
        Tsys2 = (Tamb*result[8]) / (result[8]-result[8])

        # data arrangement --
        result = numpy.concatenate((result, [Yfac1]), axis=0)
        result = numpy.concatenate((result, [Yfac2]), axis=0)
        result = numpy.concatenate((result, [Tsys1]), axis=0)
        result = numpy.concatenate((result, [Tsys2]), axis=0)
        return result

    def Trx_ttlplot(self, data, initV, finV, lo_att, datetime):
        fig = matplotlib.pyplot.figure()
        fig.subplots_adjust(right=0.75)

        # data list --
        x = data[:, 1]
        sisi = data[:, 2]
        hot1 = data[:, 3]
        cold1 = data[:, 7]
        hot2 = data[:, 4]
        cold2 = data[:, 8]
        Tsys1 = data[:, 11]
        Tsys2 = data[:, 12]

        # define axes --
        ax1 = fig.add_subplot(1, 1, 1)
        t_ax = ax1.twinx()
        p_ax = ax1.twinx()
        p_ax.spines['right'].set_position(('axes', 1.16))

        # plot lines --
        p1, = ax1.plot(x, sisi, color='black', marker=None, ls='solid', label='SIS-IV')
        p2, = t_ax.plot(x, Tsys1, color='green', marker=None, ls='solid', label='Tsys')
        p3, = p_ax.plot(x, cold1, color='blue', marker=None, ls='solid', label='Sky')
        p4, = p_ax.plot(x, hot1, color='red', marker=None, ls='solid', label='HOT')
        lines = [p1, p2, p3, p4]

        # set labels --
        ax1.set_xlabel('bias [mV]')
        ax1.set_ylabel('current [uA]')
        t_ax.set_ylabel('Tsys [K]')
        p_ax.set_ylabel('count')

        # set limits --
        if min(sisi) <= -500: Imin = -500
        else: Imin = min(sisi)

        if 500 <= max(sisi): Imax = 500
        else: Imax = max(sisi)

        ax1.set_xlim(initV, finV)
        ax1.set_ylim(Imin, Imax)
        t_ax.set_ylim(50, 300)      # TODO
        p_ax.set_ylim(3000, 20000)  # TODO

        # set label colors --
        ax1.yaxis.label.set_color('black')
        ax1.tick_params(axis='y', colors='black')
        t_ax.yaxis.label.set_color('green')
        t_ax.tick_params(axis='y', colors='green')
        p_ax.yaxis.label.set_color('red')
        p_ax.tick_params(axis='y', colors='red')

        # set legend --
        ax1.legend(lines, [l.get_label() for l in lines], loc='upper left', ncol=2)

        # others --
        ax1.set_title('SIS tuning : Tsys curve - {}')
        ax1.grid(which='both', color='gray', ls='--')
        ax1.patch.set_facecolor('lightgray')
        ax1.patch.set_alpha(0.1)

        fig.savefig(self.savedir+'tsys_curve_Lo{}mA_{}.png'.format(lo_att, datetime))
        fig.show()
        return

    def Trx_recofigure(self):
        # get params --
        params = config_handler.Config_handler.load_sis_params(ret='array')
        # set bias --
        self.driver.set_sisv(Vmix=params[:, 0])
        # self.box.set_Vd(voltage=params[:, 1])
        # self.box.set_Vg1(voltage=params[:, 2])
        # self.box.set_Vg2(voltage=params[:, 3])
        self.driver.set_loatt(att=params[:, 4])
        return

class Lo_sweep(object):
    method = 'Lo Sweep Measurement'
    ver = '2017.11.09'
    savedir = '/home/amigos/NASCORX_Measurement/SIStune/'

    def __init__(self):
        self.dfs = equipment_nanten.dfs()
        self.m4 = equipment_nanten.m4()
        self.hot = equipment_nanten.hot_load()
        pass

    def run(self, initI=1, finI=2, interval=0.05, ch=1, driver=None, integ=0.1, reconfigure=True, fmt='csv'):

        # Print Welcome massage
        # ---------------------
        print('\n\n'
              ' =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
              '   N2 RX : SIS Lo Sweep Measurement  \n'
              ' =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
              ' ver - {}\n'
              '\n\n'.format(self.ver))

        # Input value check
        # -----------------
        repeat = self.input_value_check(initI=initI, finI=finI, interval=interval)

        # Set driver
        # ----------
        if driver is None: self.driver = Cryo.box()
        else: self.driver = driver
        print('PCI board drivers are set.')

        # == Main ========

        # Measurement part
        # ----------------
        data = self.Lo_measure(repeat=repeat, initI=initI, interval=interval, ch=ch, integ=integ)
        sisv = self.driver.query_sisv()[ch-1]

        # Calculate Y-factor and Tsys
        # ---------------------------
        result = self.Lo_calculate(data=data, Tamb=300)

        # Data saving part
        # ----------------
        datetime = time.strftime('%Y%m%d-%H%M')
        filename = self.savedir + 'Lo_sweep_sisv-{}mV_{}.{}'.format(sisv, datetime, fmt)
        header = 'Lo-att,Vhot,Ihot,Phot1,Phot2,Vcold,Icold,Pcold1,Pcold2,Yfac1,Yfac2,Tsys1,Tsys2'
        numpy.savetxt(filename, result, fmt='%.5f', header=header, delimiter=',')

        # Reconfigure SIS setting
        # -----------------------
        #TODO --> test
        if driver is None: self.driver.close_box()
        if reconfigure is True: self.Lo_recofigure()

        # Data loading
        # ------------
        data = numpy.loadtxt(filename, skiprows=1, delimiter=',')

        # Plot part
        # ---------
        self.Lo_ttlplot(data=data, initV=initI, finV=finI, datetime=datetime, sisv=sisv)
        return

    def input_value_check(self, initI, finI, interval):
        lo_limit = 100    # [mA]
        if 0 <= initI < finI <= lo_limit:
            pass
        else:
            msg = '{0}\n{1}\n{2}'.format('-- Input Invalid Value Error --',
                                         '    !!! Invalid Current !!!',
                                         'Available Voltage: 0 -- 100 [mA]')
            raise ValueError(msg)
        repeat = int(abs(initI - finI) / interval)
        return repeat

    def Lo_measure(self, repeat, initI=1.0, interval=0.05, ch=1, integ=0.1):
        data = []

        # HOT measurement
        # ---------------
        # TODO : HOT IN
        data_hot = self.Lo_sweep_lo(repeat, initI=initI, interval=interval, ch=ch, integ=integ)

        # COLD measurement
        # ----------------
        # TODO : HOT OUT, SKYを見る
        data_cold = self.Lo_sweep_lo(repeat, initI=initI, interval=interval, ch=ch, integ=integ)

        # data arrangement
        # ----------------
        data.append(data_hot)
        data.append(data_cold)
        ret = numpy.array(data)
        return ret

    def Lo_sweep_lo(self, repeat, initI=1.0, interval=0.05, ch=1, integ=0.1):
        data = []

        for i in range(repeat+1):
            temp = []
            setI = initI + i * interval

            # Set Lo att
            # -----------
            self.driver.set_loatt(setI)

            time.sleep(0.2)

            # data receive
            # ------------
            temp.append(setI)
            # spec = self.client.oneshot(integtime=0.1, repeat=1, start=None)
            spec = self.dfs.oneshot(1, integ, 0)
            ad = self.driver.monitor_sis()

            # data arrangement
            # ----------------
            power = numpy.sum(spec, axis=0)
            temp.append(ad[(ch-1)*2]*1e+1)      # AD[V] --> bias [mV]
            temp.append(ad[(ch-1)*2+1]*1e+3)    # AD[V] --> current [uA]
            temp.append(power)
            data.append(temp)
        return data

    def Lo_calculate(self, data, Tamb=300):
        # dB Y-factor --
        Yfac1 = 10*numpy.log10(data[3]/data[7])
        Yfac2 = 10*numpy.log10(data[4]/data[8])

        # Tsys calculation --
        Tsys1 = (Tamb*data[7]) / (data[3]-data[7])
        Tsys2 = (Tamb*data[8]) / (data[8]-data[8])

        # data arrangement --
        data.concatenate((data, [Yfac1]), axis=0)
        data.concatenate((data, [Yfac2]), axis=0)
        data.concatenate((data, [Tsys1]), axis=0)
        data.concatenate((data, [Tsys2]), axis=0)
        return data

    def Lo_ttlplot(self, data, initI, finI, bias, datetime):
        fig = matplotlib.pyplot.figure()
        fig.subplots_adjust(right=0.75)

        # data list --
        x = data[:, 0]
        sisv = data[:, 1]
        hot1 = data[:, 3]
        cold1 = data[:, 7]
        hot2 = data[:, 4]
        cold2 = data[:, 8]
        Tsys1 = data[:, 11]
        Tsys2 = data[:, 12]

        # define axes --
        ax1 = fig.add_subplot(1, 1, 1)
        t_ax = ax1.twinx()
        p_ax = ax1.twinx()
        p_ax.spines['right'].set_position(('axes', 1.16))

        # plot lines --
        p1, = ax1.plot(x, sisv, color='black', marker=None, ls='solid', label='SIS-IV')
        p2, = t_ax.plot(x, Tsys1, color='green', marker=None, ls='solid', label='Tsys')
        p3, = p_ax.plot(x, cold1, color='blue', marker=None, ls='solid', label='Sky')
        p4, = p_ax.plot(x, hot1, color='red', marker=None, ls='solid', label='HOT')
        lines = [p1, p2, p3, p4]

        # set labels --
        ax1.set_xlabel('Lo_att [mA]')
        ax1.set_ylabel('SIS bias [mV]')
        t_ax.set_ylabel('Tsys [K]')
        p_ax.set_ylabel('count')

        # set limits --
        ax1.set_xlim(initI, finI)
        ax1.set_ylim(bias-2, bias+2)     # TODO
        t_ax.set_ylim(50, 300)           # TODO
        p_ax.set_ylim(3000, 20000)       # TODO

        # set label colors --
        ax1.yaxis.label.set_color('black')
        ax1.tick_params(axis='y', colors='black')
        t_ax.yaxis.label.set_color('green')
        t_ax.tick_params(axis='y', colors='green')
        p_ax.yaxis.label.set_color('red')
        p_ax.tick_params(axis='y', colors='red')

        # set legend --
        ax1.legend(lines, [l.get_label() for l in lines], loc='upper left', ncol=2)

        # others --
        ax1.set_title('SIS tuning : Lo Sweep - {}')
        ax1.grid(which='both', color='gray', ls='--')
        ax1.patch.set_facecolor('lightgray')
        ax1.patch.set_alpha(0.1)

        fig.savefig(self.savedir+'tsys_curve_Lo{}mA_{}.png'.format(bias, datetime))
        fig.show()
        return

    def Lo_recofigure(self):
        # get params --
        params = config_handler.Config_handler.load_sis_params(ret='array')
        # set bias --
        self.driver.set_sisv(Vmix=params[:, 0])
        # self.box.set_Vd(voltage=params[:, 1])
        # self.box.set_Vg1(voltage=params[:, 2])
        # self.box.set_Vg2(voltage=params[:, 3])
        self.driver.set_loatt(att=params[:, 4])
        return


# History
# -------
# written by T.Inaba
