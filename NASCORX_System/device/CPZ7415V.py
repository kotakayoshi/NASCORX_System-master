# ! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys, time, pyinterface
sys.path.append('/home/amigos/NASCORX_System-master/NASCORX_System/base')
# import libMotor as lib

class cpz7415v(object):
    '''
    DESCRIPTION
    ================
    This class cntrols the CPZ-7415V.
    ////CPZ-7415V Specification////
    Function: Pulse Motion Controller
    Axises: 4
    Maximum Pulse Rate: 6.5 Mpps

    ARGUMENTS
    ================
    1. dev: device number
        Type: int
        Default: 1
    '''

    def __init__(self, dev=1):
        self.dev = dev
        self.driver = pyinterface.gpg7400.gpg7400(ndev=self.dev)
        self.ctrl = pyinterface.gpg7400.gpg7400_controller(ndev=self.dev, initialize=False)

    def query_position(self, axis='XYZU', cntmode="MTR_ENCODER_MODE"):
        """        
        DESCRIPTION
        ================
        This function queries the pulse counts.
        
        ARGUMENTS
        ================
        1. axis: slider axis 
            Type: str
            Default: XYZU
        2.cntmode: mode of pulus counts
            Type: str
            Default: MTR_ENCODER_MODE
        
        RETURNS
        ================
        list(element is the pulse counts.)
        index 0 : x-axis count
        index 1 : y-axis count
        index 2 : z-axis count
        index 3 : u-axis count
        """
        cnt = self.driver.get_position(axis=axis, cntmode=cntmode)
        return cnt

    def move_cw(self, spd=[1000,1000,1000,1000], strk=[1,1,1,1], axis="X"):
        """        
        DESCRIPTION
        ================
        This function moves the slider.
        (Cw means the motor derection.)
        
        ARGUMENTS
        ================
        1. spd: slide speed [pps]
            Number: 0 - 1000
            Type: list[int]
            Default: 1000

        2. strk: slide length [mm]
            Number: 0 - 150
            Type: list[float]
            Default: 1

        3. axis: slider axis 
            Type: string
            Default: X

        RETURNS
        ================
        Nothing.
        """
        if all(0<elem<1500 for elem in spd) and all(0<elem<150 for elem in strk):
            dd = {'U':0, 'Y':1}
            speed = spd
            cnt = list(map(lambda x: -100*x, strk))
            '''
            init_pos = round(self.query_position()[dd[axis]], 0)
            tgt_pos = round((init_pos + cnt[0]) / 10, 0)
            '''
            self.driver.move(speed=spd, count=cnt, axis=axis)
            '''

            while 1:
                time.sleep(0.5)
                crrt_pos = round(self.query_position()[dd[axis]] / 10, 0)
                print(tgt_pos)
                print(crrt_pos)
                if crrt_pos == tgt_pos:
                    break
                else:
                    continue

            return
            '''

        else:
            print('!!!!ERROR!!!!\n'
                  'Please input invalid parameter.\n'
                  '0 < spd < 1000 and 0 < strk < 150.')
        return

    def move_ccw(self, spd=[1000,1000,1000,1000], strk=[1,1,1,1], axis="X"):
        """        
        DESCRIPTION
        ================
        This function moves the slider.
        (Ccw means the opposite motor derection.)
        
        ARGUMENTS
        ================
        1. spd: slide speed [pps]
            Number: 0 - 1000
            Type: list[int]
            Default: 1000

        2. strk: slide length [mm]
            Number: 0 - 150
            Type: list[float]
            Default: 1

        3. axis: slider axis 
            Type: string
            Default: X

        RETURNS
        ================
        Nothing.
        """
        if all(0<elem<1500 for elem in spd) and all(0<elem<150 for elem in strk):

            dd = {'U':0, 'Y':1}
            speed = spd
            cnt = list(map(lambda x: 100*x, strk))
            '''
            init_pos = self.query_position()[dd[axis]]
            tgt_pos = round((init_pos + cnt[0]) / 10, 0)
            '''
            self.driver.move(speed=spd, count=cnt, axis=axis)

            '''
            while 1:
                time.sleep(0.5)
                crrt_pos = round(self.query_position()[dd[axis]] / 10, 0)
                print(tgt_pos)
                print(crrt_pos)
                if crrt_pos == tgt_pos:
                    break
                else:
                    continue

            return
            '''

        else:
            print('!!!!ERROR!!!!\n'
                  'Please input invalid parameter.\n'
                  '0 < spd < 1000 and 0 < strk < 150.')
        return

    def output_do(self, out=0):
        """        
        DESCRIPTION
        ================
        This function operates the general output.
        
        ARGUMENTS
        ================
        1. out: output pin
            Type: int(bit)
            Default: 0

        RETURNS
        ================
        Nothing.
        """
        self.ctrl.output_do(out=0)
        self.ctrl.output_do(out=out)
        self.ctrl.output_do(out=0)
        return

    def input_di(self):
        """        
        DESCRIPTION
        ================
        This function operates the general input.
        
        ARGUMENTS
        ================
        Nothing.

        RETURNS
        ================
        Nothing.
        """
        ret = self.ctrl.input_di()
        return ret

    def close_board(self):
        """        
        DESCRIPTION
        ================
        This function close the board connection.
        
        ARGUMENTS
        ================
        Nothing.
        
        RETURNS
        ================
        Nothing.
        """
        self.ctrl.close()
        return
