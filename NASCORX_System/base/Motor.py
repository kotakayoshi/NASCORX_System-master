# ! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
DESCRIPTION
================
This module controls the motor relation.
It is conposed of following three classes.

INCLUDED CLASS
================
1. slider class: 
   This class controls the slider.
2. M4 class:
   This class controls the M4.
3. chopper class:
   This class controls the chopper.
"""

import os, time, datetime, linecache
import NASCORX_System.base.libMotor as lib
import NASCORX_System.device.CPZ7415V as CPZ7415V

class slider(object):
    """
    DESCRIPTION
    ================
    This class controls the slider.

    ARGUMENTS
    ================
    1. board: name of the motion controller registered in the IP_table.
        Type: string
        Default: 'CZP7415Va'
    2. device_table: file path of the IP table
        Type: string
        Default: '/home/amigos/NASCORX-master/base/IP_table_115.txt'
    """

    def __init__(self, board='CPZ7415Va', device_table='/home/amigos/NASCORX_System-master/NASCORX_System/base/device_table_115.txt'):
        self.board = board
        self.device_table = device_table
        # self.nboard = self._board_search_(device=self.board)
        # self.mtnc = CPZ7415V.cpz7415v(dev=self.nboard[1])
        self.mtnc = CPZ7415V.cpz7415v(dev=1)

    '''
    def _board_search_(self, device):
        f = open(self.device_table, 'r')
        for line in f:
            dev = line.strip().split(',')
            if device in dev:
                info1 = int(dev[1].strip())
                break
            else:
                pass
        f.close()
        ret = [device, info1]
        return ret
    '''

    def slide_cw(self, strk=1, axis='X'):
        """
        DESCRIPTION
        ================
        This function slides the slider.
        (Cw means the motor derection.)
        
        ARGUMENTS
        ================
        1. strk: slide length [mm]
            Number: 0 - 150
            Type: list[float]
            Default: 1

        2. axis: selection of the control device.
            Type: string
            Default: lib.MOTOR_XAXIS
        
        RETURNS
        ================
        """
        '''
        if self.board == 'CPZ7415Va' and axis == X:
            axis = lib.MOTOR_XAXIS_1
        elif self.board == 'CPZ7415Vb' and axis == X:
            axis = lib.MOTOR_XAXIS_2
        else: pass
        '''
        if 0 < strk < 150:
            self.mtnc.move_cw(strk=[strk,1,1,1], axis=axis)
            return
        else:
            print('!!!!ERROR!!!!\n'
                  'Please input invalid parameter.\n'
                  '0 < strk < 150')

    def slide_ccw(self, strk=1, axis='X'):
        """
        DESCRIPTION
        ================
        This function slides the slider.
        (Ccw means the oppsite motor derection.)
        
        ARGUMENTS
        ================
        1. strk: slide length [mm]
            Number: 0 - 150
            Type: list[float]
            Default: 1

        2. axis: selection of the control device.
            Type: string
            Default: lib.MOTOR_XAXIS
        
        RETURNS
        ================
        """
        '''
        if self.board == 'CPZ7415Va' and axis == X:
            axis = lib.MOTOR_XAXIS_1
        elif self.board == 'CPZ7415Vb' and axis == X:
            axis = lib.MOTOR_XAXIS_2
        else: pass
        '''
        if 0 < strk < 150:
            self.mtnc.move_ccw(strk=[strk,1,1,1], axis=axis)
            return
        else:
            print('!!!!ERROR!!!!\n'
                  'Please input invalid parameter.\n'
                  '0 < strk < 150')

    def return_org(self, out=lib.RETURN_ORIGIN_XAXIS):
        """        
        DESCRIPTION
        ================
        This function let the slider return origin.
        
        ARGUMENTS
        ================
        1. out: output pin
            Type: int(bit)
            Derault: RETURN_ORIGIN_XAXIS

        RETURNS
        ================
        Nothing.
        """
        cnt = 5
        for i in range(cnt):
            self.mtnc.output_do(out=out)
            time.sleep(0.5)
        return

    def reset_alarm(self):
        """        
        DESCRIPTION
        ================
        This function resets alarm of 
        all motion driver controlled by the motion controller board.
        
        ARGUMENTS
        ================
        Nothing.

        RETURNS
        ================
        Nothing.
        """
        out = lib.INITIAL_STATE
        self.mtnc.output_do(out=out)
        return

    def query_position(self, pos=lib.MOTOR_XAXIS_POS):
        """        
        DESCRIPTION
        ================
        This function queries the slider position.
        
        ARGUMENTS
        ================
        1. pos: select the slider
            Type: int
            Default: MOTOR_XAXIS_1_POS
        
        RETURNS
        ================
        1. position [mm]
            Type: fault
            About: position is destance from the slider origin.
        """
        ret = self.mtnc.query_position()
        if pos == 0: p2l = 0.01
        elif pos == 1: p2l = -0.01
        position = ret[pos] * p2l
        return position

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
        self.mtnc.close_board()
        return

class M4(object):
    """
    DESCRIPTION
    ================
    This class controls the M4.

    ARGUMENTS
    ================
    1. board: M4 class is oprated by board of 'CPZ7415Va'
        Type: string
        board: 'CZP7415Va'
    """
    def __init__(self):
        dev = 1 # CPZ7415Va
        LIMIT = 130
        axis = lib.MOTOR_ZAXIS
        log_file = M4_log.txt
        self.mtnc = CPZ7415V.cpz7415v(dev=dev)

    def _log(self, con='HOT'):
        """        
        DESCRIPTION
        ================
        This function logs the M4 state means UP or DOWN in the logfile.
        
        ARGUMENTS
        ================
        1. con: M4 state
            Type: str
            Default: HOT

        RETURNS
        ================
        Nothing.
        """
        da = ['{0:%Y-%m-%d %H:%M:%S}'.format(datatime.datetime.now()), ' ' , '{0}\n'.format(con)]
        os.chdir('/home/amigos/NASCORX_System-master/NASCORX_System/base/Motor_log')
        f = open('{0}'.format(log_file), 'a')
        f.writelines(da)
        f.close()
        os.chdir('/home/amigos/NASCORX_System-master/NASCORX_System/base')
        return

    def _state(self):
        """        
        DESCRIPTION
        ================
        This function logs the M4 state means UP or DOWN in the logfile.
        
        ARGUMENTS
        ================
        Nothing.

        RETURNS
        ================
        Nothing.
        """
        f = open('{0}'.format(log_file), 'r')
        num = sum(1 for line in open(('{0}'.format(log_file))))
        ret = linecache.getline('{0}'.format(log_file), int(num))
        return ret
        
    def move_up(self):
        """
        DESCRIPTION
        ================
        This function moves the M4 to UP.
        
        ARGUMENTS
        ================
        State of the M4 up passes the RFsignal to the NASCORX.

        RETURNS
        ================
        Nothing.
        """
        if self._state.split()[2] == 'DOWN':
            self.mtnc.move_ccw(strk=[LIMIT,1,1,1], axis=axis)
            self._log(con='UP')
            return
        else:
            print('!!!!ERROR!!!!\n'
                  'M4 has already moved to UP.')
                  
    def move_down(self):
        """
        DESCRIPTION
        ================
        This function moves the M4 to DOWN.
        
        ARGUMENTS
        ================
        State of the M4 down passes the RFsignal to the SMART.

        RETURNS
        ================
        Nothing.
        """
        if self._state.split()[2] == 'UP':
            self.mtnc.move_cw(strk=[LIMIT,1,1,1], axis=axis)
            self._log(con='DOWN')
            return
        else:
            print('!!!!ERROR!!!!\n'
                  'M4 has already moved to DOWN.')
            
    def query_position(self):
        """        
        DESCRIPTION
        ================
        This function queries the M4 position.
        (The M4 positino means state of the M4 is UP or DOWN.)
        
        ARGUMENTS
        ================
        Nothing.

        RETURNS
        ================
        Nothing.
        """
        ret = self._state()
        print('THE PRESENT STATE OF THE M4\n'
              '[{0}]'.format(ret))
        return

    def close_box(self):
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
        self.mtnc.close_board()
        return

class chopper(object):
    """
    DESCRIPTION
    ================
    This class controls the chopper.

    ARGUMENTS
    ================
    1. board: chopper class is oprated by board of 'CPZ7415Vb'
        Type: string
        board: 'CZP7415Vb'
    """

    def __init__(self):
        self.dev = 1 # CPZ7415Va
        self.ROT = 2.5
        self.spd = 100
        # axis = lib.MOTOR_ZAXIS
        self.axis = 'Y'
        self.log_file = 'chopper_log.txt'
        self.mtnc = CPZ7415V.cpz7415v(dev=self.dev)

    def _log(self, con='HOT'):
        """        
        DESCRIPTION
        ================
        This function logs the chopper state means HOT or COLD in the logfile.
        
        ARGUMENTS
        ================
        1. con: chopper state
            Type: str
            Default: HOT

        RETURNS
        ================
        Nothing.
        """
        da = ['{0:%Y-%m-%d %H:%M:%S}'.format(datatime.datetime.now), ' ' , '{0}\n'.format(con)]
        os.chdir('/home/amigos/NASCORX_System-master/NASCORX_System/base/Motor_log')
        f = open('{0}'.format(self.log_file), 'a')
        f.writelines(da)
        f.close()
        os.chdir('/home/amigos/NASCORX_System-master/NASCORX_System/base')
        return

    def _state(self):
        """        
        DESCRIPTION
        ================
        This function logs the chopper state means HOT or COLD in the logfile.
        
        ARGUMENTS
        ================
        Nothing.

        RETURNS
        ================
        Nothing.
        """
        f = open('{0}'.format(log_file), 'r')
        num = sum(1 for line in open(('{0}'.format(log_file))))
        ret = linecache.getline('{0}'.format(log_file), int(num))
        return ret
        
    def move_hot(self):
        """
        DESCRIPTION
        ================
        This function moves the chopper to HOT.
        
        ARGUMENTS
        ================
        Nothing.

        RETURNS
        ================
        Nothing.
        """
        if self._state().split()[2] == 'COLD':
            self.mtnc.move_ccw(strk=[self.ROT,1,1,1], axis=self.axis)
            self._log(con='HOT')
            return
        else:
            print('!!!!ERROR!!!!\n'
                  'Chopper has already moved to HOT.')
                  
    def move_cold(self):
        """
        DESCRIPTION
        ================
        This function moves the chopper to COLD.
        
        ARGUMENTS
        ================
        Nothing.

        RETURNS
        ================
        Nothing.
        """
        if self._state().split()[2] == 'HOT':
            self.mtnc.move_cw(strk=[self.ROT,1,1,1], axis=self.axis)
            self._log(con='COLD')
            return
        else:
            print('!!!!ERROR!!!!\n'
                  'Chopper has already moved to COLD.')
            
    def query_position(self):
        """        
        DESCRIPTION
        ================
        This function queries the chopper position.
        (The M4 positino means state of the chopper is HOT or COLD.)
        
        ARGUMENTS
        ================
        Nothing.

        RETURNS
        ================
        Nothing.
        """
        ret = self._state()
        print(ret)
        return

    def close_box(self):
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
        self.mtnc.close_board()
        return

    def rot_chopper(self, spd=100): # for Mr.s_masahiro
        self.mtnc.move_ccw(strk=[self.ROT,1,1,1], spd=[spd,100,100,100], axis=self.axis)
        return
