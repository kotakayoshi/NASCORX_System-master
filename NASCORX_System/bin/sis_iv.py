#! /usr/bin/env python

# import modules
import time
import numpy
import matplotlib.pyplot

from NASCORX_System.base import config_handler
from NASCORX_System.base import sis


class IV_curve(object):
    method = 'IV Curve Measurement'
    ver = '2017.12.21'
    savedir = '/home/amigos/NASCORX_Measurement/SIStune/'

    def __init__(self):
        pass

    def run(self, initV=0.0, finV=8.0, interval=0.1, onoff='cnf', lo=None, filefmt='csv'):

        # Print Welcome massage
        # ----------------------
        print('\n\n'
              ' =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'
              '   NASCO RX : SIS IV curve Measurement  \n'
              ' =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'
              ' ver - {}\n'
              '\n\n'.format(self.ver))

        # Input value check
        # -----------------
        repeat = self.input_value_check(initV=initV, finV=finV, interval=interval)

        # Check available unit
        # --------------------
        if onoff == 'cnf':
            onoff = config_handler.Config_handler.check_sis_state()
        else:
            pass

        # Set Driver
        # ----------
        self.driver = sis.multi_box()
        print('\n'
              ' PCI board drivers are set.\n'
              '\n')

        # == Main ========

        # Lo setting
        # ----------
        if lo is None: pass
        else: self.driver.set_loatt(att=lo)

        # Measurement part
        # ----------------
        AD_data = self.measure(repeat=repeat, initV=initV, interval=interval, onoff=onoff)

        # Data saving part
        # ----------------
        datetime = time.strftime('%Y%m%d-%H%M')
        filename = self.savedir + 'SISIV_{}.{}'.format(datetime, filefmt)
        header = 'D/A-SISV,' \
                 '1L-V,1L-I,1R-V,1R-I,2L-V,2L-I,2R-V,2R-I,' \
                 '3L-V,3L-I,3R-V,3R-I,4L-V,4L-I,4R-V,4R-I,' \
                 'LCP-USB-V,LCP-USB-I,LCP-LSB-V,LCP-LSB-I,' \
                 'RCP-USB-V,RCP-USB-I,RCP-LSB-V,RCP-LSB-I'
        numpy.savetxt(filename, AD_data, fmt='%.5f', header=header, delimiter=',')

        # close sis driver
        # ----------------
        self.driver.close_box()

        # Data loading
        # ------------
        AD_data = numpy.loadtxt(filename, skiprows=1, delimiter=',')

        # Plot part
        # ---------
        self.ttlplot(AD_data=AD_data, initV=initV, finV=finV, datetime=datetime)

        # Output information on terminal
        # ------------------------------
        print('\n'
              ' ======== SIS IV Curve MEASUREMENT ========\n'
              ' Time Stamp    : {}\n'
              ' Start SISV    : {} [mV]\n'
              ' Finish SISV   : {} [mV]\n'
              ' Lo Attenuation: !!coming soon!! [mA]\n\n'.format(datetime, initV, finV))
        return

    def input_value_check(self, initV, finV, interval):
        Vmix_limit = 30  # [mv]
        if -Vmix_limit <= initV <= finV <= Vmix_limit:
            pass
        else:
            msg = '{0}\n{1}\n{2}'.format('-- Input Invalid Value Error --',
                                         '    !!! Invalid Voltage !!!',
                                         'Available Voltage: -30 -- 30 [mV]')
            raise ValueError(msg)
        repeat = int(abs(initV - finV) / interval)
        return repeat

    def plot_options(self, ax, initV, finV):
        [_ax.set_xticklabels('') for i, _ax in enumerate(ax) if i/2<1]
        [_ax.set_yticklabels('') for i, _ax in enumerate(ax) if i%2!=0]
        [_ax.set_xlabel('SIS V [mV]') for i, _ax in enumerate(ax) if i/2>=1]
        [_ax.set_ylabel('SIS I [uA]') for i, _ax in enumerate(ax) if i%2==0]
        [_ax.set_xlim([initV, finV]) for _ax in ax]
        [_ax.legend(loc='upper left', prop={'size': 7}, numpoints=1) for _ax in ax]
        [_ax.grid(color='gray', linestyle='--') for _ax in ax]
        return

    def divplot(self, AD_data, initV, finV, datetime):
        ## figure 1: Beam 1-2
        #### list-comprehension
        fig = matplotlib.pyplot.figure()
        ax = [fig.add_subplot(2, 2, i+1) for i in range(4)]
        labels = ['Beam1-LCP', 'Beam1-RCP', 'Beam2-LCP', 'Beam2-RCP']
        [_ax.plot(AD_data[:, 1+2*i], AD_data[:, 2+2*i], label=labels[i]) for i, _ax in enumerate(ax)]
        self.plot_options(ax=ax, initV=initV, finV=finV)

        fig.tight_layout()
        fig.subplots_adjust(top=0.9)
        fig.suptitle('SIS IV Curve: Beam 1-2\n{}'.format(datetime), fontsize=13)
        figname = self.savedir + 'SIS-IVcurve_Beam1-2_{}.png'.format(datetime)
        fig.savefig(figname)
        fig.show()

        ## figure 2: Beam 3-4
        fig = matplotlib.pyplot.figure()
        ax = [fig.add_subplot(2, 2, i+1) for i in range(4)]
        labels = ['Beam3-LCP', 'Beam3-RCP', 'Beam4-LCP', 'Beam4-RCP']
        [_ax.plot(AD_data[:, 9+2*i], AD_data[:, 10+2*i], label=labels[i]) for i, _ax in enumerate(ax)]
        self.plot_options(ax=ax, initV=initV, finV=finV)

        fig.tight_layout()
        fig.subplots_adjust(top=0.9)
        fig.suptitle('SIS IV Curve: Beam 3-4\n{}'.format(datetime), fontsize=13)
        figname = self.savedir + 'SIS-IVcurve_Beam3-4_{}.png'.format(datetime)
        fig.savefig(figname)
        fig.show()

        ## figure 3: 230GHz - 2 Pol x 2SB
        fig = matplotlib.pyplot.figure()
        ax = [fig.add_subplot(2, 2, i+1) for i in range(4)]
        labels = ['230GHz-LCP-USB', '230GHz-LCP-LSB', '230GHz-RCP-USB', '230GHz-RCP-LSB']
        [_ax.plot(AD_data[:, 17+2*i], AD_data[:, 18+2*i], label=labels[i]) for i, _ax in enumerate(ax)]
        self.plot_options(ax=ax, initV=initV, finV=finV)

        fig.tight_layout()
        fig.subplots_adjust(top=0.9)
        fig.suptitle('SIS IV Curve: 230GHz\n{}'.format(datetime), fontsize=13)
        figname = self.savedir + 'SIS-IVcurve_230GHz_{}.png'.format(datetime)
        fig.savefig(figname)
        fig.show()
        return

    def ttlplot(self, AD_data, initV, finV, datetime):
        fig = matplotlib.pyplot.figure(figsize=(9, 7))
        ax = [fig.add_subplot(3, 4, i+1) for i in range(12)]
        labels = ['Beam2-LCP', 'Beam2-RCP', 'Beam3-LCP', 'Beam3-RCP',
                  'Beam4-LCP', 'Beam4-RCP', 'Beam5-LCP', 'Beam5-RCP',
                  'Beam1-LCP-USB', 'Beam1-LCP-LSB', 'Beam1-RCP-USB', 'Beam1-RCP-LSB']
        [_ax.plot(AD_data[:, 1+2*i], AD_data[:, 2+2*i], label=labels[i]) for i, _ax in enumerate(ax)]
        [_ax.set_xlim([initV, finV]) for _ax in ax]
        [_ax.set_ylim([-800, 800]) for _ax in ax]
        [_ax.set_xticklabels('') for i, _ax in enumerate(ax) if i/4<2]
        [_ax.set_yticklabels('') for i, _ax in enumerate(ax) if i%4!=0]
        [_ax.set_xlabel('SIS V [mV]') for i, _ax in enumerate(ax) if i/4>=2]
        [_ax.set_ylabel('SIS I [uA]') for i, _ax in enumerate(ax) if i%4==0]
        [_ax.legend(loc='upper left', prop={'size': 7}, numpoints=1) for _ax in ax]
        [_ax.grid(color='gray', linestyle='--') for _ax in ax]

        fig.tight_layout()
        fig.subplots_adjust(top=0.9)
        fig.suptitle('SIS IV Curve Measurement: {}'.format(datetime), fontsize=15)
        figname = self.savedir + 'sis-iv_{}.png'.format(datetime)
        fig.savefig(figname)
        fig.show()
        return

    def measure(self, repeat, initV=0.0, interval=0.1, onoff=[0]*12):
        AD_data = []
        setV_list = [0] * 12

        # Measurement part
        # ----------------
        for i in range(repeat+1):
            temp = []

            # set bias --
            setV = initV + i * interval
            for j in range(12):
                if onoff[j] == 1: setV_list[j] = setV
                else: pass
            self.driver.set_sisv(Vmix=setV_list)

            time.sleep(0.2)

            # get data --
            ret = self.driver.monitor_sis()

            # data arrangement
            # ----------------
            temp.append(setV)
            # scaling --
            for j in range(24):
                if j % 2 == 0:
                    temp.append(ret[j]*1e+1)  # AD[V] --> bias [mV]
                elif j % 2 == 1:
                    temp.append(ret[j]*1e+3)  # AD[V] --> current [uA]
            AD_data.append(temp)
        return AD_data


# History
# -------
# written by T.Inaba
# 2017/12/21 T.Inaba : restructure.
