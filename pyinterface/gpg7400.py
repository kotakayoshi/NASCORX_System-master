
import ctypes
import pyinterface
import pyinterface.libgpg7400 as lib
pIE = pyinterface.IdentiferElement


# Identifier Wrapper
# =================

class AxisConfig(pyinterface.BitIdentifer):
    size = 16
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    bits[0].set_params('X', 'OFF', 'ON')
    bits[1].set_params('Y', 'OFF', 'ON')
    bits[2].set_params('Z', 'OFF', 'ON')
    bits[3].set_params('U', 'OFF', 'ON')
    pass

class OpenFlag(pyinterface.Identifer):
    MTR_FLAG_NORMAL = pIE('MTR_FLAG_NORMAL', lib.MTR_FLAG_NORMAL)
    MTR_FLAG_OVERLAPPED = pIE('MTR_FLAG_OVERLAPPED', lib.MTR_FLAG_OVERLAPPED)
    MTR_ILOCK_RESET_OFF = pIE('MTR_ILOCK_RESET_OFF', lib.MTR_ILOCK_RESET_OFF)
    MTR_EXT_RESET_OFF = pIE('MTR_EXT_RESET_OFF', lib.MTR_EXT_RESET_OFF)
    MTR_FLAG_SHARE = pIE('MTR_FLAG_SHARE', lib.MTR_FLAG_SHARE)
    pass

class ResetMode(pyinterface.Identifer):
    MTR_RESET_CTL = pIE('MTR_RESET_CTL', lib.MTR_RESET_CTL)
    MTR_RESET_MOTION = pIE('MTR_RESET_MOTION', lib.MTR_RESET_MOTION)
    pass

class PulseOutConfigSection(pyinterface.Identifer):
    MTR_METHOD = pIE('MTR_METHOD', lib.MTR_METHOD)
    MTR_IDLING = pIE('MTR_IDLING', lib.MTR_IDLING)
    MTR_FINISH_FLAG = pIE('MTR_FINISH_FLAG', lib.MTR_FINISH_FLAG)
    MTR_SYNC_OUT = pIE('MTR_SYNC_OUT', lib.MTR_SYNC_OUT)
    pass

class PulseOutMethod(pyinterface.BitIdentifer):
    size = 16
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    bits[0].set_params('PULSE', 'OFF', 'ON')
    bits[1].set_params('OUT', 'OFF', 'ON')
    bits[2].set_params('DIR', 'OFF', 'ON')
    bits[3].set_params('WAIT', 'OFF', 'ON')
    bits[4].set_params('DUTY', 'OFF', 'ON')
    pass

class FinishFlag(pyinterface.Identifer):
    MTR_PULSE_OUT = pIE('MTR_PULSE_OUT', lib.MTR_PULSE_OUT)
    MTR_INP = pIE('MTR_INP', lib.MTR_INP)
    MTR_PULSE_OFF = pIE('MTR_PULSE_OFF', lib.MTR_PULSE_OFF)
    pass

class SyncOutMode(pyinterface.Identifer):
    MTR_SYNC_OFF = pIE('MTR_SYNC_OFF', lib.MTR_SYNC_OFF)
    MTR_COMP1 = pIE('MTR_COMP1', lib.MTR_COMP1)
    MTR_COMP2 = pIE('MTR_COMP2', lib.MTR_COMP2)
    MTR_COMP3 = pIE('MTR_COMP3', lib.MTR_COMP3)
    MTR_COMP4 = pIE('MTR_COMP4', lib.MTR_COMP4)
    MTR_COMP5 = pIE('MTR_COMP5', lib.MTR_COMP5)
    MTR_ACC_START = pIE('MTR_ACC_START', lib.MTR_ACC_START)
    MTR_ACC_FINISH = pIE('MTR_ACC_FINISH', lib.MTR_ACC_FINISH)
    MTR_DEC_START = pIE('MTR_DEC_START', lib.MTR_DEC_START)
    MTR_DEC_FINISH = pIE('MTR_DEC_FINISH', lib.MTR_DEC_FINISH)
    pass

class LimitConfigSection(pyinterface.Identifer):
    MTR_MASK = pIE('MTR_MASK', lib.MTR_MASK)
    MTR_LOGIC = pIE('MTR_LOGIC', lib.MTR_LOGIC)
    MTR_SD_FUNC = pIE('MTR_SD_FUNC', lib.MTR_SD_FUNC)
    MTR_SD_ACTIVE = pIE('MTR_SD_ACTIVE', lib.MTR_SD_ACTIVE)
    MTR_ORG_FUNC = pIE('MTR_ORG_FUNC', lib.MTR_ORG_FUNC)
    MTR_ORG_ACTIVE = pIE('MTR_ORG_ACTIVE', lib.MTR_ORG_ACTIVE)
    MTR_ORG_EZ_COUNT = pIE('MTR_ORG_EZ_COUNT', lib.MTR_ORG_EZ_COUNT)
    MTR_ALM_FUNC = pIE('MTR_ALM_FUNC', lib.MTR_ALM_FUNC)
    MTR_SIGNAL_FILTER = pIE('MTR_SIGNAL_FILTER', lib.MTR_SIGNAL_FILTER)
    MTR_EL_FUNC = pIE('MTR_EL_FUNC', lib.MTR_EL_FUNC)
    MTR_EZ_ACTIVE = pIE('MTR_EZ_ACTIVE', lib.MTR_EZ_ACTIVE)
    MTR_LTC_FUNC = pIE('MTR_LTC_FUNC', lib.MTR_LTC_FUNC)
    MTR_CLR_FUNC = pIE('MTR_CLR_FUNC', lib.MTR_CLR_FUNC)
    MTR_PCS_FUNC = pIE('MTR_PCS_FUNC', lib.MTR_PCS_FUNC)
    MTR_PCS_ACTIVE = pIE('MTR_PCS_ACTIVE', lib.MTR_PCS_ACTIVE)
    pass

class LimitConfigLogic(pyinterface.BitIdentifer):
    size = 16
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    bits[0].set_params('SD', 'OFF', 'ON')
    bits[2].set_params('EL', 'OFF', 'ON')
    bits[5].set_params('ORG', 'OFF', 'ON')
    bits[6].set_params('ALM', 'OFF', 'ON')
    bits[8].set_params('INP', 'OFF', 'ON')
    bits[9].set_params('PCS', 'OFF', 'ON')
    pass

class SDFunc(pyinterface.Identifer):
    MTR_CHANGE_SD_SPEED = pIE('MTR_CHANGE_SD_SPEED', lib.MTR_CHANGE_SD_SPEED)
    MTR_DEC_STOP_SIGNAL = pIE('MTR_DEC_STOP_SIGNAL', lib.MTR_DEC_STOP_SIGNAL)
    MTR_SD_OFF = pIE('MTR_SD_OFF', lib.MTR_SD_OFF)
    pass

class SDActive(pyinterface.Identifer):
    MTR_SIGNAL_LEVEL = pIE('MTR_SIGNAL_LEVEL', lib.MTR_SIGNAL_LEVEL)
    MTR_SIGNAL_LATCH = pIE('MTR_SIGNAL_LATCH', lib.MTR_SIGNAL_LATCH)
    pass

class ORGFunc(pyinterface.Identifer):
    MTR_ORG_STOP = pIE('MTR_ORG_STOP', lib.MTR_ORG_STOP)
    MTR_ORG_DEC_EZ_STOP = pIE('MTR_ORG_DEC_EZ_STOP', lib.MTR_ORG_DEC_EZ_STOP)
    MTR_ORG_EZ_STOP = pIE('MTR_ORG_EZ_STOP', lib.MTR_ORG_EZ_STOP)
    MTR_ORG_REVERSAL = pIE('MTR_ORG_REVERSAL', lib.MTR_ORG_REVERSAL)
    MTR_ORG_REV_EZ_STOP = pIE('MTR_ORG_REV_EZ_STOP', lib.MTR_ORG_REV_EZ_STOP)
    MTR_ORG_STOP_ZERO = pIE('MTR_ORG_STOP_ZERO', lib.MTR_ORG_STOP_ZERO)
    MTR_ORG_EZ_STOP_ZERO = pIE('MTR_ORG_EZ_STOP_ZERO', lib.MTR_ORG_EZ_STOP_ZERO)
    MTR_ORG_REV_EZ_ZERO = pIE('MTR_ORG_REV_EZ_ZERO', lib.MTR_ORG_REV_EZ_ZERO)
    pass

class ALMFunc(pyinterface.Identifer):
    MTR_ALM_STOP = pIE('MTR_ALM_STOP', lib.MTR_ALM_STOP)
    MTR_ALM_DEC_STOP = pIE('MTR_ALM_DEC_STOP', lib.MTR_ALM_DEC_STOP)
    pass

class SignalFilter(pyinterface.Identifer):
    MTR_OFF = pIE('MTR_OFF', lib.MTR_OFF)
    MTR_ON = pIE('MTR_ON', lib.MTR_ON)
    pass

class ELFunc(pyinterface.Identifer):
    MTR_EL_STOP = pIE('MTR_EL_STOP', lib.MTR_EL_STOP)
    MTR_EL_DEC_STOP = pIE('MTR_EL_DEC_STOP', lib.MTR_EL_DEC_STOP)
    pass

class EZActive(pyinterface.Identifer):
    MTR_DOWN_EDGE = pIE('MTR_DOWN_EDGE', lib.MTR_DOWN_EDGE)
    MTR_UP_EDGE = pIE('MTR_UP_EDGE', lib.MTR_UP_EDGE)
    pass

class LTCFunc(pyinterface.Identifer):
    MTR_DOWN_EDGE = pIE('MTR_DOWN_EDGE', lib.MTR_DOWN_EDGE)
    MTR_UP_EDGE = pIE('MTR_UP_EDGE', lib.MTR_UP_EDGE)
    pass

class CLRFunc(pyinterface.Identifer):
    MTR_DOWN_EDGE = pIE('MTR_DOWN_EDGE', lib.MTR_DOWN_EDGE)
    MTR_UP_EDGE = pIE('MTR_UP_EDGE', lib.MTR_UP_EDGE)
    MTR_LOW_LEVEL = pIE('MTR_LOW_LEVEL', lib.MTR_LOW_LEVEL)
    MTR_HIGH_LEVEL = pIE('MTR_HIGH_LEVEL', lib.MTR_HIGH_LEVEL)
    pass

class PCSFunc(pyinterface.Identifer):
    MTR_OFF = pIE('MTR_OFF', lib.MTR_OFF)
    MTR_ON = pIE('MTR_ON', lib.MTR_ON)
    MTR_EXT_START = pIE('MTR_EXT_START', lib.MTR_EXT_START)
    pass

class CounterConfigSection(pyinterface.Identifer):
    MTR_ENCODER_MODE = pIE('MTR_ENCODER_MODE', lib.MTR_ENCODER_MODE)
    MTR_ENCODER_CLEAR = pIE('MTR_ENCODER_CLEAR', lib.MTR_ENCODER_CLEAR)
    MTR_COUNTER_CLEAR_ORG = pIE('MTR_COUNTER_CLEAR_ORG', lib.MTR_COUNTER_CLEAR_ORG)
    MTR_COUNTER_CLEAR_CLR = pIE('MTR_COUNTER_CLEAR_CLR', lib.MTR_COUNTER_CLEAR_CLR)
    MTR_LATCH_MODE = pIE('MTR_LATCH_MODE', lib.MTR_LATCH_MODE)
    MTR_DECLINO_MODE = pIE('MTR_DECLINO_MODE', lib.MTR_DECLINO_MODE)
    MTR_SOFT_LATCH = pIE('MTR_SOFT_LATCH', lib.MTR_SOFT_LATCH)
    pass

class EncoderMode(pyinterface.Identifer):
    MTR_SINGLE = pIE('MTR_SINGLE', lib.MTR_SINGLE)
    MTR_DOUBLE = pIE('MTR_DOUBLE', lib.MTR_DOUBLE)
    MTR_QUAD = pIE('MTR_QUAD', lib.MTR_QUAD)
    MTR_UP_DOWN = pIE('MTR_UP_DOWN', lib.MTR_UP_DOWN)
    pass

class CounterClearORG(pyinterface.BitIdentifer):
    size = 16
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    bits[0].set_params('CU1R', 'OFF', 'ON')
    bits[1].set_params('CU2R', 'OFF', 'ON')
    bits[2].set_params('CU3R', 'OFF', 'ON')
    pass

class CounterClearCLR(pyinterface.BitIdentifer):
    size = 16
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    bits[0].set_params('CU1C', 'OFF', 'ON')
    bits[1].set_params('CU2C', 'OFF', 'ON')
    bits[2].set_params('CU3C', 'OFF', 'ON')
    pass

class LatchMode(pyinterface.Identifer):
    MTR_OFF = pIE('MTR_OFF', lib.MTR_OFF)
    MTR_ORG = pIE('MTR_ORG', lib.MTR_ORG)
    MTR_LTC = pIE('MTR_LTC', lib.MTR_LTC)
    MTR_COMP4 = pIE('MTR_COMP4', lib.MTR_COMP4)
    MTR_COMP5 = pIE('MTR_COMP5', lib.MTR_COMP5)
    pass

class DeclinoMode(pyinterface.Identifer):
    MTR_DECLINO = pIE('MTR_DECLINO', lib.MTR_DECLINO)
    MTR_SPEED = pIE('MTR_SPEED', lib.MTR_SPEED)
    pass

class Comparator(pyinterface.Identifer):
    MTR_COMP1 = pIE('MTR_COMP1', lib.MTR_COMP1)
    MTR_COMP2 = pIE('MTR_COMP2', lib.MTR_COMP2)
    MTR_COMP3 = pIE('MTR_COMP3', lib.MTR_COMP3)
    MTR_COMP4 = pIE('MTR_COMP4', lib.MTR_COMP4)
    MTR_COMP5 = pIE('MTR_COMP5', lib.MTR_COMP5)
    pass

class SyncSection(pyinterface.Identifer):
    MTR_START_MODE = pIE('MTR_START_MODE', lib.MTR_START_MODE)
    MTR_EXT_STOP = pIE('MTR_EXT_STOP', lib.MTR_EXT_STOP)
    MTR_START_LINE = pIE('MTR_START_LINE', lib.MTR_START_LINE)
    MTR_STOP_LINE = pIE('MTR_STOP_LINE', lib.MTR_STOP_LINE)
    pass

class StartMode(pyinterface.Identifer):
    MTR_NO = pIE('MTR_NO', lib.MTR_NO)
    MTR_X = pIE('MTR_X', lib.MTR_X)
    MTR_Y = pIE('MTR_Y', lib.MTR_Y)
    MTR_Z = pIE('MTR_Z', lib.MTR_Z)
    MTR_U = pIE('MTR_U', lib.MTR_U)
    MTR_SYNC_X = pIE('MTR_SYNC_X', lib.MTR_SYNC_X)
    MTR_SYNC_Y = pIE('MTR_SYNC_Y', lib.MTR_SYNC_Y)
    MTR_SYNC_Z = pIE('MTR_SYNC_Z', lib.MTR_SYNC_Z)
    MTR_SYNC_U = pIE('MTR_SYNC_U', lib.MTR_SYNC_U)
    MTR_SYNC_EXT = pIE('MTR_SYNC_EXT', lib.MTR_SYNC_EXT)
    pass

class ExtStop(pyinterface.Identifer):
    MTR_OFF = pIE('MTR_OFF', lib.MTR_OFF)
    MTR_CSTP_STOP = pIE('MTR_CSTP_STOP', lib.MTR_CSTP_STOP)
    MTR_CSTP_DEC_STOP = pIE('MTR_CSTP_DEC_STOP', lib.MTR_CSTP_DEC_STOP)
    pass

class StartLine(pyinterface.Identifer):
    SYN0 = pIE('SYN0', 0x00)
    SYN1 = pIE('SYN1', 0x01)
    SYN2 = pIE('SYN2', 0x02)
    SYN3 = pIE('SYN3', 0x03)
    SYN4 = pIE('SYN4', 0x04)
    SYN5 = pIE('SYN5', 0x05)
    SYN6 = pIE('SYN6', 0x06)
    SYN7 = pIE('SYN7', 0x07)
    pass

class StopLine(pyinterface.Identifer):
    SYN0 = pIE('SYN0', 0x00)
    SYN1 = pIE('SYN1', 0x01)
    SYN2 = pIE('SYN2', 0x02)
    SYN3 = pIE('SYN3', 0x03)
    SYN4 = pIE('SYN4', 0x04)
    SYN5 = pIE('SYN5', 0x05)
    SYN6 = pIE('SYN6', 0x06)
    SYN7 = pIE('SYN7', 0x07)
    pass

class ReviseSection(pyinterface.Identifer):
    MTR_PULSE = pIE('MTR_PULSE', lib.MTR_PULSE)
    MTR_REVISE_MODE = pIE('MTR_REVISE_MODE', lib.MTR_REVISE_MODE)
    MTR_COUNTER_MODE = pIE('MTR_COUNTER_MODE', lib.MTR_COUNTER_MODE)
    MTR_REST_RT = pIE('MTR_REST_RT', lib.MTR_REST_RT)
    MTR_REST_FT = pIE('MTR_REST_FT', lib.MTR_REST_FT)
    pass

class ReviseMode(pyinterface.Identifer):
    MTR_REVISE_OFF = pIE('MTR_REVISE_OFF', 0x00)
    MTR_BACK = pIE('MTR_BACK', lib.MTR_BACK)
    MTR_SLIP = pIE('MTR_SLIP', lib.MTR_SLIP)
    pass

class ReviseCounterMode(pyinterface.BitIdentifer):
    size = 16
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    bits[0].set_params('CU1B', 'OFF', 'ON')
    bits[1].set_params('CU2B', 'OFF', 'ON')
    bits[2].set_params('CU3B', 'OFF', 'ON')
    pass

class ERCConfigSection(pyinterface.Identifer):
    MTR_AUTO = pIE('MTR_AUTO', lib.MTR_AUTO)
    MTR_LOGIC = pIE('MTR_LOGIC', lib.MTR_LOGIC)
    MTR_WIDTH = pIE('MTR_WIDTH', lib.MTR_WIDTH)
    MTR_OFF_TIMER = pIE('MTR_OFF_TIMER', lib.MTR_OFF_TIMER)
    MTR_SIGNAL_ON = pIE('MTR_SIGNAL_ON', lib.MTR_SIGNAL_ON)
    MTR_SIGNAL_OFF = pIE('MTR_SIGNAL_OFF', lib.MTR_SIGNAL_OFF)
    pass

class ERCAuto(pyinterface.BitIdentifer):
    size = 16
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    bits[0].set_params('EROE', 'OFF', 'ON')
    bits[1].set_params('EROR', 'OFF', 'ON')
    pass

class ERCLogic(pyinterface.Identifer):
    MTR_ACTIVE_LOW = pIE('MTR_ACTIVE_LOW', lib.MTR_ACTIVE_LOW)
    MTR_ACTIVE_HIGH = pIE('MTR_ACTIVE_HIGH', lib.MTR_ACTIVE_HIGH)
    pass

class ERCWidth(pyinterface.Identifer):
    MTR_12MICRO = pIE('MTR_12MICRO', lib.MTR_12MICRO)
    MTR_102MICRO = pIE('MTR_102MICRO', lib.MTR_102MICRO)
    MTR_409MICRO = pIE('MTR_409MICRO', lib.MTR_409MICRO)
    MTR_1600MICRO = pIE('MTR_1600MICRO', lib.MTR_1600MICRO)
    MTR_13M = pIE('MTR_13M', lib.MTR_13M)
    MTR_52M = pIE('MTR_52M', lib.MTR_52M)
    MTR_104M = pIE('MTR_104M', lib.MTR_104M)
    MTR_LEVEL = pIE('MTR_LEVEL', lib.MTR_LEVEL)
    pass

class ERCOffTimer(pyinterface.Identifer):
    MTR_ZERO = pIE('MTR_ZERO', lib.MTR_ZERO)
    MTR_12MICRO = pIE('MTR_12MICRO', lib.MTR_12MICRO)
    MTR_1600MICRO = pIE('MTR_1600MICRO', lib.MTR_1600MICRO)
    MTR_104M = pIE('MTR_104M', lib.MTR_104M)
    pass

class MotionSection(pyinterface.Identifer):
    MTR_JOG = pIE('MTR_JOG', lib.MTR_JOG)
    MTR_ORG = pIE('MTR_ORG', lib.MTR_ORG)
    MTR_PTP = pIE('MTR_PTP', lib.MTR_PTP)
    MTR_TIMER = pIE('MTR_TIMER', lib.MTR_TIMER)
    MTR_SINGLE_STEP = pIE('MTR_SINGLE_STEP', lib.MTR_SINGLE_STEP)
    MTR_ORG_SEARCH = pIE('MTR_ORG_SEARCH', lib.MTR_ORG_SEARCH)
    MTR_ORG_EXIT = pIE('MTR_ORG_EXIT', lib.MTR_ORG_EXIT)
    MTR_ORG_ZERO = pIE('MTR_ORG_ZERO', lib.MTR_ORG_ZERO)
    MTR_PTP_REPEAT = pIE('MTR_PTP_REPEAT', lib.MTR_PTP_REPEAT)
    MTR_REPEAT_CLEAR = pIE('MTR_REPEAT_CLEAR', lib.MTR_REPEAT_CLEAR)
    MTR_START_MODE_OFF = pIE('MTR_START_MODE_OFF', lib.MTR_START_MODE_OFF)
    pass

class MotionLineSection(pyinterface.Identifer):
    MTR_LINE_NORMAL = pIE('MTR_LINE_NORMAL', lib.MTR_LINE_NORMAL)
    MTR_LINE_REPEAT = pIE('MTR_LINE_REPEAT', lib.MTR_LINE_REPEAT)
    MTR_REPEAT_CLEAR = pIE('MTR_REPEAT_CLEAR', lib.MTR_REPEAT_CLEAR)
    MTR_START_MODE_OFF = pIE('MTR_START_MODE_OFF', lib.MTR_START_MODE_OFF)
    pass

class MotionArcSection(pyinterface.Identifer):
    MTR_ARC_NORMAL = pIE('MTR_ARC_NORMAL', lib.MTR_ARC_NORMAL)
    MTR_ARC_REPEAT = pIE('MTR_ARC_REPEAT', lib.MTR_ARC_REPEAT)
    MTR_REPEAT_CLEAR = pIE('MTR_REPEAT_CLEAR', lib.MTR_REPEAT_CLEAR)
    MTR_START_MODE_OFF = pIE('MTR_START_MODE_OFF', lib.MTR_START_MODE_OFF)
    pass

class StartMotion(pyinterface.Identifer):
    MTR_ACC = pIE('MTR_ACC', lib.MTR_ACC)
    MTR_CONST = pIE('MTR_CONST', lib.MTR_CONST)
    MTR_CONST_DEC = pIE('MTR_CONST_DEC', lib.MTR_CONST_DEC)
    pass

class MotionMode(pyinterface.Identifer):
    MTR_JOG = pIE('MTR_JOG', lib.MTR_JOG)
    MTR_ORG = pIE('MTR_ORG', lib.MTR_ORG)
    MTR_PTP = pIE('MTR_PTP', lib.MTR_PTP)
    MTR_TIMER = pIE('MTR_TIMER', lib.MTR_TIMER)
    MTR_SINGLE_STEP = pIE('MTR_SINGLE_STEP', lib.MTR_SINGLE_STEP)
    MTR_ORG_SEARCH = pIE('MTR_ORG_SEARCH', lib.MTR_ORG_SEARCH)
    MTR_ORG_EXIT = pIE('MTR_ORG_EXIT', lib.MTR_ORG_EXIT)
    MTR_ORG_ZERO = pIE('MTR_ORG_ZERO', lib.MTR_ORG_ZERO)
    MTR_LINE = pIE('MTR_LINE', lib.MTR_LINE)
    MTR_SYNC_LINE = pIE('MTR_SYNC_LINE', lib.MTR_SYNC_LINE)
    MTR_ARC = pIE('MTR_ARC', lib.MTR_ARC)
    MTR_CP = pIE('MTR_CP', lib.MTR_CP)
    MTR_LIMIT = pIE('MTR_LIMIT', lib.MTR_LIMIT)
    MTR_ABSOLUTE = pIE('MTR_ABSOLUTE', lib.MTR_ABSOLUTE)
    pass

class StopMotion(pyinterface.Identifer):
    MTR_DEC_STOP = pIE('MTR_DEC_STOP', lib.MTR_DEC_STOP)
    MTR_IMMEDIATE_STOP = pIE('MTR_IMMEDIATE_STOP', lib.MTR_IMMEDIATE_STOP)
    pass

class RepeatMoveMode(pyinterface.Identifer):
    MTR_PTP = pIE('MTR_PTP', lib.MTR_PTP)
    MTR_IP = pIE('MTR_IP', lib.MTR_IP)
    MTR_IP_SPEED = pIE('MTR_IP_SPEED', lib.MTR_IP_SPEED)
    pass

class OutputSync(pyinterface.Identifer):
    MTR_EXT_START = pIE('MTR_EXT_START', lib.MTR_EXT_START)
    MTR_EXT_STOP = pIE('MTR_EXT_STOP', lib.MTR_EXT_STOP)
    MTR_SYNC_NORMAL = pIE('MTR_SYNC_NORMAL', lib.MTR_SYNC_NORMAL)
    MTR_SYNC_SLAVE = pIE('MTR_SYNC_SLAVE', lib.MTR_SYNC_SLAVE)
    MTR_SYNC_MASTER = pIE('MTR_SYNC_MASTER', lib.MTR_SYNC_MASTER)
    pass

class ChangeSpeed(pyinterface.Identifer):
    MTR_IMMEDIATE_CHANGE = pIE('MTR_IMMEDIATE_CHANGE', lib.MTR_IMMEDIATE_CHANGE)
    MTR_ACCDEC_CHANGE = pIE('MTR_ACCDEC_CHANGE', lib.MTR_ACCDEC_CHANGE)
    MTR_LOW_SPEED = pIE('MTR_LOW_SPEED', lib.MTR_LOW_SPEED)
    MTR_DEC_LOW_SPEED = pIE('MTR_DEC_LOW_SPEED', lib.MTR_DEC_LOW_SPEED)
    pass

class StatusSection(pyinterface.Identifer):
    MTR_BUSY = pIE('MTR_BUSY', lib.MTR_BUSY)
    MTR_FINISH_STATUS = pIE('MTR_FINISH_STATUS', lib.MTR_FINISH_STATUS)
    MTR_LIMIT_STATUS = pIE('MTR_LIMIT_STATUS', lib.MTR_LIMIT_STATUS)
    MTR_INTERLOCK_STATUS = pIE('MTR_INTERLOCK_STATUS', lib.MTR_INTERLOCK_STATUS)
    MTR_PRIREG_STATUS = pIE('MTR_PRIREG_STATUS', lib.MTR_PRIREG_STATUS)
    MTR_SYNC_STATUS = pIE('MTR_SYNC_STATUS', lib.MTR_SYNC_STATUS)
    MTR_PTP_REPEAT_NUM = pIE('MTR_PTP_REPEAT_NUM', lib.MTR_PTP_REPEAT_NUM)
    MTR_IP_REPEAT_NUM = pIE('MTR_IP_REPEAT_NUM', lib.MTR_IP_REPEAT_NUM)
    pass

class StatusBusy(pyinterface.BitIdentifer):
    size = 32
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    bits[0].set_params('BUSY', 'NO', 'YES')
    bits[1].set_params('ACC', 'NO', 'YES')
    bits[2].set_params('DEC', 'NO', 'YES')
    bits[3].set_params('WAIT', 'NO', 'YES')
    bits[4].set_params('SYNC', 'NO', 'YES')
    bits[5].set_params('STOP', 'OFF', 'ON')
    bits[6].set_params('INP', 'NO', 'YES')
    bits[7].set_params('CSTA', 'NO', 'YES')
    bits[8].set_params('BACK', 'NO', 'YES')
    bits[10].set_params('CMD', 'NO', 'YES')
    bits[12].set_params('ERC', 'NO', 'YES')
    bits[13].set_params('DIR', 'NO', 'YES')
    bits[14].set_params('OTH', 'NO', 'YES')
    pass

class StatusFinish(pyinterface.BitIdentifer):
    size = 32
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    bits[0].set_params('FNS', 'NO', 'YES')
    bits[3].set_params('CMP1', 'NO', 'YES')
    bits[4].set_params('CMP2', 'NO', 'YES')
    bits[5].set_params('CMP3', 'NO', 'YES')
    bits[6].set_params('CMP4', 'NO', 'YES')
    bits[7].set_params('CMP5', 'NO', 'YES')
    bits[8].set_params('SD', 'NO', 'YES')
    bits[10].set_params('+EL', 'NO', 'YES')
    bits[11].set_params('-EL', 'NO', 'YES')
    bits[12].set_params('CSTP', 'NO', 'YES')
    bits[13].set_params('EA/EB', 'NO', 'YES')
    bits[14].set_params('ALM', 'NO', 'YES')
    bits[15].set_params('ERR', 'NO', 'YES')
    bits[16].set_params('OVER', 'NO', 'YES')
    pass

class StatusLimit(pyinterface.BitIdentifer):
    size = 32
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    bits[0].set_params('SD', 'NOINPUT', 'INPUT')
    bits[2].set_params('+EL', 'NOINPUT', 'INPUT')
    bits[3].set_params('-EL', 'NOINPUT', 'INPUT')
    bits[5].set_params('ORG', 'NOINPUT', 'INPUT')
    bits[6].set_params('ALM', 'NOINPUT', 'INPUT')
    bits[8].set_params('INP', 'NOINPUT', 'INPUT')
    bits[9].set_params('CLR', 'NOINPUT', 'INPUT')
    bits[10].set_params('LTC', 'NOINPUT', 'INPUT')
    bits[11].set_params('CTSA', 'NOINPUT', 'INPUT')
    bits[12].set_params('CSTP', 'NOINPUT', 'INPUT')
    bits[13].set_params('PCS', 'NOINPUT', 'INPUT')
    bits[14].set_params('ERC', 'NOOUTPUT', 'OUTPUT')
    bits[15].set_params('EZ', 'NOINPUT', 'INPUT')
    pass

class StatusInterlock(pyinterface.Identifer):
    MTR_ILOCK_OFF = pIE('MTR_ILOCK_OFF', lib.MTR_ILOCK_OFF)
    MTR_ILOCK_ON = pIE('MTR_ILOCK_ON', lib.MTR_ILOCK_ON)
    pass

class StatusSync(pyinterface.BitIdentifer):
    size = 32
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    bits[0].set_params('IPLx', 'NONE', 'SET')
    bits[1].set_params('IPLy', 'NONE', 'SET')
    bits[2].set_params('IPLz', 'NONE', 'SET')
    bits[3].set_params('IPLu', 'NONE', 'SET')
    bits[4].set_params('IPEx', 'NONE', 'SET')
    bits[5].set_params('IPEy', 'NONE', 'SET')
    bits[6].set_params('IPEz', 'NONE', 'SET')
    bits[7].set_params('IPEu', 'NONE', 'SET')
    bits[8].set_params('IPSx', 'NONE', 'SET')
    bits[9].set_params('IPSy', 'NONE', 'SET')
    bits[10].set_params('IPSz', 'NONE', 'SET')
    bits[11].set_params('IPSu', 'NONE', 'SET')
    bits[12].set_params('IPFx', 'NONE', 'SET')
    bits[13].set_params('IPFy', 'NONE', 'SET')
    bits[14].set_params('IPFz', 'NONE', 'SET')
    bits[15].set_params('IPFu', 'NONE', 'SET')
    bits[16].set_params('IPL', 'NOT', 'APPLY')
    bits[17].set_params('IPE', 'NOT', 'APPLY')
    bits[18].set_params('IPCW', 'NOT', 'APPLY')
    bits[19].set_params('IPCC', 'NOT', 'APPLY')
    bits[20].set_params('SDM0', 'OFF', 'ON')
    bits[21].set_params('SDM1', 'OFF', 'ON')
    bits[22].set_params('SED0', 'OFF', 'ON')
    bits[23].set_params('SED1', 'OFF', 'ON')
    pass

class CounterType(pyinterface.Identifer):
    MTR_ENCODER = pIE('MTR_ENCODER', lib.MTR_ENCODER)
    MTR_COUNTER = pIE('MTR_COUNTER', lib.MTR_COUNTER)
    MTR_REMAINS = pIE('MTR_REMAINS', lib.MTR_REMAINS)
    MTR_DECLINO = pIE('MTR_DECLINO', lib.MTR_DECLINO)
    MTR_ABSOLUTE = pIE('MTR_ABSOLUTE', lib.MTR_ABSOLUTE)
    MTR_LATCH = pIE('MTR_LATCH', lib.MTR_LATCH)
    pass

class SampleStatus(pyinterface.Identifer):
    MTR_REPEAT = pIE('MTR_REPEAT', lib.MTR_REPEAT)
    MTR_SAMPLE_FINISHED = pIE('MTR_SAMPLE_FINISHED', lib.MTR_SAMPLE_FINISHED)
    MTR_NOW_SAMPLING = pIE('MTR_NOW_SAMPLING', lib.MTR_NOW_SAMPLING)
    MTR_WAITING_BUSY = pIE('MTR_WAITING_BUSY', lib.MTR_WAITING_BUSY)
    MTR_FULL_BUFFER = pIE('MTR_FULL_BUFFER', lib.MTR_FULL_BUFFER)
    MTR_EMPTY_DATA = pIE('MTR_EMPTY_DATA', lib.MTR_EMPTY_DATA)
    pass

class CMDBufferSection(pyinterface.Identifer):
    MTR_CMD_MOVE = pIE('MTR_CMD_MOVE', lib.MTR_CMD_MOVE)
    MTR_CMD_CLOCK = pIE('MTR_CMD_CLOCK', lib.MTR_CMD_CLOCK)
    MTR_CMD_LOW_SPEED = pIE('MTR_CMD_LOW_SPEED', lib.MTR_CMD_LOW_SPEED)
    MTR_CMD_SPEED = pIE('MTR_CMD_SPEED', lib.MTR_CMD_SPEED)
    MTR_CMD_ACC = pIE('MTR_CMD_ACC', lib.MTR_CMD_ACC)
    MTR_CMD_DEC = pIE('MTR_CMD_DEC', lib.MTR_CMD_DEC)
    MTR_CMD_ACC_SPEED = pIE('MTR_CMD_ACC_SPEED', lib.MTR_CMD_ACC_SPEED)
    MTR_CMD_DEC_SPEED = pIE('MTR_CMD_DEC_SPEED', lib.MTR_CMD_DEC_SPEED)
    MTR_CMD_STEP = pIE('MTR_CMD_STEP', lib.MTR_CMD_STEP)
    MTR_CMD_CENTER = pIE('MTR_CMD_CENTER', lib.MTR_CMD_CENTER)
    MTR_CMD_START_MODE = pIE('MTR_CMD_START_MODE', lib.MTR_CMD_START_MODE)
    pass

class CMDMode(pyinterface.Identifer):
    MTR_CMD_JOG_P = pIE('MTR_CMD_JOG_P', lib.MTR_CMD_JOG_P)
    MTR_CMD_JOG_M = pIE('MTR_CMD_JOG_M', lib.MTR_CMD_JOG_M)
    MTR_CMD_ORG_P = pIE('MTR_CMD_ORG_P', lib.MTR_CMD_ORG_P)
    MTR_CMD_ORG_M = pIE('MTR_CMD_ORG_M', lib.MTR_CMD_ORG_M)
    MTR_CMD_ORG_EXIT_P = pIE('MTR_CMD_ORG_EXIT_P', lib.MTR_CMD_ORG_EXIT_P)
    MTR_CMD_ORG_EXIT_M = pIE('MTR_CMD_ORG_EXIT_M', lib.MTR_CMD_ORG_EXIT_M)
    MTR_CMD_ORG_SEARCH_P = pIE('MTR_CMD_ORG_SEARCH_P', lib.MTR_CMD_ORG_SEARCH_P)
    MTR_CMD_ORG_SEARCH_M = pIE('MTR_CMD_ORG_SEARCH_M', lib.MTR_CMD_ORG_SEARCH_M)
    MTR_CMD_PTP = pIE('MTR_CMD_PTP', lib.MTR_CMD_PTP)
    MTR_CMD_ORG_ZERO = pIE('MTR_CMD_ORG_ZERO', lib.MTR_CMD_ORG_ZERO)
    MTR_CMD_SINGLE_STEP_P = pIE('MTR_CMD_SINGLE_STEP_P', lib.MTR_CMD_SINGLE_STEP_P)
    MTR_CMD_SINGLE_STEP_M = pIE('MTR_CMD_SINGLE_STEP_M', lib.MTR_CMD_SINGLE_STEP_M)
    MTR_CMD_TIMER = pIE('MTR_CMD_TIMER', lib.MTR_CMD_TIMER)
    MTR_CMD_LINE = pIE('MTR_CMD_LINE', lib.MTR_CMD_LINE)
    MTR_CMD_ARC_CW = pIE('MTR_CMD_ARC_CW', lib.MTR_CMD_ARC_CW)
    MTR_CMD_ARC_CCW = pIE('MTR_CMD_ARC_CCW', lib.MTR_CMD_ARC_CCW)
    MTR_CMD_ACC_SIN = pIE('MTR_CMD_ACC_SIN', lib.MTR_CMD_ACC_SIN)
    MTR_CMD_FH_OFF = pIE('MTR_CMD_FH_OFF', lib.MTR_CMD_FH_OFF)
    MTR_CMD_SP_COMPOSE = pIE('MTR_CMD_SP_COMPOSE', lib.MTR_CMD_SP_COMPOSE)
    pass

class CMDStartMode(pyinterface.Identifer):
    MTR_CMD_CONST = pIE('MTR_CMD_CONST', lib.MTR_CMD_CONST)
    MTR_CMD_ACC_DEC = pIE('MTR_CMD_ACC_DEC', lib.MTR_CMD_ACC_DEC)
    MTR_CMD_CONST_DEC = pIE('MTR_CMD_CONST_DEC', lib.MTR_CMD_CONST_DEC)
    pass

class StartCMDBuffer(pyinterface.Identifer):
    MTR_CMD_AUTO_START = pIE('MTR_CMD_AUTO_START', lib.MTR_CMD_AUTO_START)
    MTR_CMD_STEP_START = pIE('MTR_CMD_STEP_START', lib.MTR_CMD_STEP_START)
    pass

# for structures
# - - - - - - - -
class CompConfig(pyinterface.Identifer):
    MTR_NO = pIE('MTR_NO', lib.MTR_NO)
    MTR_EQ = pIE('MTR_EQ', lib.MTR_EQ)
    MTR_EQ_UP = pIE('MTR_EQ_UP', lib.MTR_EQ_UP)
    MTR_EQ_DOWN = pIE('MTR_EQ_DOWN', lib.MTR_EQ_DOWN)
    MTR_LT = pIE('MTR_LT', lib.MTR_LT)
    MTR_GT = pIE('MTR_GT', lib.MTR_GT)
    MTR_SOFT_LIMIT = pIE('MTR_SOFT_LIMIT', lib.MTR_SOFT_LIMIT)
    pass

class CompMotion(pyinterface.Identifer):
    MTR_NO = pIE('MTR_NO', lib.MTR_NO)
    MTR_STOP = pIE('MTR_STOP', lib.MTR_STOP)
    MTR_DEC = pIE('MTR_DEC', lib.MTR_DEC)
    MTR_CHG_REG = pIE('MTR_CHG_REG', lib.MTR_CHG_REG)
    pass

class CompCntType(pyinterface.Identifer):
    MTR_CMP_COUNTER = pIE('MTR_CMP_COUNTER', lib.MTR_CMP_COUNTER)
    MTR_CMP_ENCODER = pIE('MTR_CMP_ENCODER', lib.MTR_CMP_ENCODER)
    MTR_CMP_DECLINO = pIE('MTR_CMP_DECLINO', lib.MTR_CMP_DECLINO)
    MTR_CMP_SPEED = pIE('MTR_CMP_SPEED', lib.MTR_CMP_SPEED)
    pass

class MotionAccMode(pyinterface.Identifer):
    MTR_ACC_NORMAL = pIE('MTR_ACC_NORMAL', lib.MTR_ACC_NORMAL)
    MTR_ACC_SIN = pIE('MTR_ACC_SIN', lib.MTR_ACC_SIN)
    MTR_FH = pIE('MTR_FH', lib.MTR_FH)
    pass

class LineMode(pyinterface.Identifer):
    MTR_LINE = pIE('MTR_LINE', lib.MTR_LINE)
    MTR_LINE_JOG = pIE('MTR_LINE_JOG', lib.MTR_LINE_JOG)
    pass

class LineAccMode(pyinterface.Identifer):
    MTR_ACC_NORMAL = pIE('MTR_ACC_NORMAL', lib.MTR_ACC_NORMAL)
    MTR_ACC_SIN = pIE('MTR_ACC_SIN', lib.MTR_ACC_SIN)
    MTR_SP_COMPOSE = pIE('MTR_SP_COMPOSE', lib.MTR_SP_COMPOSE)
    pass

class CounterClearCLR(pyinterface.BitIdentifer):
    size = 16
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    bits[0].set_params('CU1C', 'OFF', 'ON')
    bits[1].set_params('CU2C', 'OFF', 'ON')
    bits[2].set_params('CU3C', 'OFF', 'ON')
    pass

class ARCMode(pyinterface.Identifer):
    MTR_ARC_CW = pIE('MTR_ARC_CW', lib.MTR_ARC_CW)
    MTR_ARC_CCW = pIE('MTR_ARC_CCW', lib.MTR_ARC_CCW)
    MTR_SP_COMPOSE = pIE('MTR_SP_COMPOSE', lib.MTR_SP_COMPOSE)
    pass

class EventPulseOut(pyinterface.BitIdentifer):
    size = 16
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    bits[0].set_params('STOP', 'OFF', 'ON')
    bits[1].set_params('ACC-START', 'OFF', 'ON')
    bits[2].set_params('ACC-FINISH', 'OFF', 'ON')
    bits[3].set_params('DEC-START', 'OFF', 'ON')
    bits[4].set_params('DEC-FINISH', 'OFF', 'ON')
    bits[5].set_params('NEXT', 'OFF', 'ON')
    bits[6].set_params('WRITE', 'OFF', 'ON')
    pass

class EventComparator(pyinterface.BitIdentifer):
    size = 16
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    bits[0].set_params('CMP1', 'OFF', 'ON')
    bits[1].set_params('CMP2', 'OFF', 'ON')
    bits[2].set_params('CMP3', 'OFF', 'ON')
    bits[3].set_params('CMP4', 'OFF', 'ON')
    bits[4].set_params('CMP5', 'OFF', 'ON')
    pass

class EventSignal(pyinterface.BitIdentifer):
    size = 16
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    bits[0].set_params('SD', 'OFF', 'ON')
    bits[1].set_params('ORG', 'OFF', 'ON')
    bits[2].set_params('CLR', 'OFF', 'ON')
    bits[3].set_params('LTC', 'OFF', 'ON')
    bits[4].set_params('ILOCK', 'OFF', 'ON')
    bits[5].set_params('EXT', 'OFF', 'ON')
    bits[6].set_params('CSTA', 'OFF', 'ON')
    pass

class SampleFreqMode(pyinterface.Identifer):
    MTR_ENCODER = pIE('MTR_ENCODER', lib.MTR_ENCODER)
    MTR_COUNTER = pIE('MTR_COUNTER', lib.MTR_COUNTER)
    MTR_DECLINO = pIE('MTR_DECLINO', lib.MTR_DECLINO)
    MTR_BUSY_SAMP = pIE('MTR_BUSY_SAMP', lib.MTR_BUSY_SAMP)
    MTR_REPEAT = pIE('MTR_REPEAT', lib.MTR_REPEAT)
    pass    

# 27: MtrOutputDO
# ---------------
class OutputDO(pyinterface.BitIdentifer):
    size = 32
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    bits[0].set_params('OUT1', 'HIGH', 'LOW')
    bits[1].set_params('OUT2', 'HIGH', 'LOW')
    bits[2].set_params('OUT3', 'HIGH', 'LOW')
    bits[3].set_params('OUT4', 'HIGH', 'LOW')
    bits[4].set_params('OUT5', 'HIGH', 'LOW')
    bits[5].set_params('OUT6', 'HIGH', 'LOW')
    bits[6].set_params('OUT7', 'HIGH', 'LOW')
    bits[7].set_params('OUT8', 'HIGH', 'LOW')
    pass

# 28: MtrInputDI
# ---------------
class InputDI(pyinterface.BitIdentifer):
    size = 32
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    bits[0].set_params('IN1', 'HIGH', 'LOW')
    bits[1].set_params('IN2', 'HIGH', 'LOW')
    bits[2].set_params('IN3', 'HIGH', 'LOW')
    bits[3].set_params('IN4', 'HIGH', 'LOW')
    bits[4].set_params('IN5', 'HIGH', 'LOW')
    bits[5].set_params('IN6', 'HIGH', 'LOW')
    bits[6].set_params('IN7', 'HIGH', 'LOW')
    bits[7].set_params('IN8', 'HIGH', 'LOW')
    bits[8].set_params('IN8', 'HIGH', 'LOW')
    bits[9].set_params('IN8', 'HIGH', 'LOW')
    bits[10].set_params('IN8', 'HIGH', 'LOW')
    bits[11].set_params('IN8', 'HIGH', 'LOW')
    pass

# Error Wrapper
# =============
class ErrorGPG7400(pyinterface.ErrorCode):
    MTR_ERROR_SUCCESS = pIE('MTR_ERROR_SUCCESS', lib.MTR_ERROR_SUCCESS)
    MTR_ERROR_NOT_DEVICE = pIE('MTR_ERROR_NOT_DEVICE', lib.MTR_ERROR_NOT_DEVICE)
    MTR_ERROR_NOT_OPEN = pIE('MTR_ERROR_NOT_OPEN', lib.MTR_ERROR_NOT_OPEN)
    MTR_ERROR_INVALID_DEVICE_NUMBER = pIE('MTR_ERROR_INVALID_DEVICE_NUMBER', lib.MTR_ERROR_INVALID_DEVICE_NUMBER)
    MTR_ERROR_ALREADY_OPEN = pIE('MTR_ERROR_ALREADY_OPEN', lib.MTR_ERROR_ALREADY_OPEN)
    MTR_ERROR_NOT_SUPPORTED = pIE('MTR_ERROR_NOT_SUPPORTED', lib.MTR_ERROR_NOT_SUPPORTED)
    MTR_ERROR_NOW_MOVING = pIE('MTR_ERROR_NOW_MOVING', lib.MTR_ERROR_NOW_MOVING)
    MTR_ERROR_NOW_STOPPED = pIE('MTR_ERROR_NOW_STOPPED', lib.MTR_ERROR_NOW_STOPPED)
    MTR_ERROR_NOW_SAMPLING = pIE('MTR_ERROR_NOW_SAMPLING', lib.MTR_ERROR_NOW_SAMPLING)
    MTR_ERROR_NOW_STOP_SAMPLING = pIE('MTR_ERROR_NOW_STOP_SAMPLING', lib.MTR_ERROR_NOW_STOP_SAMPLING)
    MTR_ERROR_NOW_BUSY_CMD_BUFF = pIE('MTR_ERROR_NOW_BUSY_CMD_BUFF', lib.MTR_ERROR_NOW_BUSY_CMD_BUFF)
    MTR_ERROR_NOW_STOP_CMD_BUFF = pIE('MTR_ERROR_NOW_STOP_CMD_BUFF', lib.MTR_ERROR_NOW_STOP_CMD_BUFF)
    MTR_ERROR_EEPROM_BUSY = pIE('MTR_ERROR_EEPROM_BUSY', lib.MTR_ERROR_EEPROM_BUSY)
    MTR_ERROR_WRITE_FAILED = pIE('MTR_ERROR_WRITE_FAILED', lib.MTR_ERROR_WRITE_FAILED)
    MTR_ERROR_READ_FAILED = pIE('MTR_ERROR_READ_FAILED', lib.MTR_ERROR_READ_FAILED)
    MTR_ERROR_INVALID_DEVICE = pIE('MTR_ERROR_INVALID_DEVICE', lib.MTR_ERROR_INVALID_DEVICE)
    MTR_ERROR_INVALID_AXIS = pIE('MTR_ERROR_INVALID_AXIS', lib.MTR_ERROR_INVALID_AXIS)
    MTR_ERROR_INVALID_SPEED = pIE('MTR_ERROR_INVALID_SPEED', lib.MTR_ERROR_INVALID_SPEED)
    MTR_ERROR_INVALID_ACCDEC = pIE('MTR_ERROR_INVALID_ACCDEC', lib.MTR_ERROR_INVALID_ACCDEC)
    MTR_ERROR_INVALID_PULSE = pIE('MTR_ERROR_INVALID_PULSE', lib.MTR_ERROR_INVALID_PULSE)
    MTR_ERROR_INVALID_PARAMETER = pIE('MTR_ERROR_INVALID_PARAMETER', lib.MTR_ERROR_INVALID_PARAMETER)
    MTR_ERROR_INVALID_INDEX = pIE('MTR_ERROR_INVALID_INDEX', lib.MTR_ERROR_INVALID_INDEX)
    MTR_ERROR_REPEAT_LINE_ARC = pIE('MTR_ERROR_REPEAT_LINE_ARC', lib.MTR_ERROR_REPEAT_LINE_ARC)
    MTR_ERROR_NOW_INTERLOCKED = pIE('MTR_ERROR_NOW_INTERLOCKED', lib.MTR_ERROR_NOW_INTERLOCKED)
    MTR_ERROR_IMPOSSIBLE = pIE('MTR_ERROR_IMPOSSIBLE', lib.MTR_ERROR_IMPOSSIBLE)
    MTR_ERROR_WRITE_FAILED_EEPROM = pIE('MTR_ERROR_WRITE_FAILED_EEPROM', lib.MTR_ERROR_WRITE_FAILED_EEPROM)
    MTR_ERROR_READ_FAILED_EEPROM = pIE('MTR_ERROR_READ_FAILED_EEPROM', lib.MTR_ERROR_READ_FAILED_EEPROM)
    MTR_ERROR_NOT_ALLOCATE_MEMORY = pIE('MTR_ERROR_NOT_ALLOCATE_MEMORY', lib.MTR_ERROR_NOT_ALLOCATE_MEMORY)
    MTR_ERROR_NOW_WAIT_STA = pIE('MTR_ERROR_NOW_WAIT_STA', lib.MTR_ERROR_NOW_WAIT_STA)
    MTR_ERROR_EMPTY_DATA = pIE('MTR_ERROR_EMPTY_DATA', lib.MTR_ERROR_EMPTY_DATA)
    MTR_ERROR_FULL_PRIREG = pIE('MTR_ERROR_FULL_PRIREG', lib.MTR_ERROR_FULL_PRIREG)
    MTR_ERROR_FAILED_CREATE_THREAD = pIE('MTR_ERROR_FAILED_CREATE_THREAD', lib.MTR_ERROR_FAILED_CREATE_THREAD)
    MTN_ERROR_NOT_ALLOCATE_MEMORY = pIE('MTN_ERROR_NOT_ALLOCATE_MEMORY', lib.MTN_ERROR_NOT_ALLOCATE_MEMORY)
    
    _success = MTR_ERROR_SUCCESS
    pass



# ==========================
# GPG-7400 Python Controller
# ==========================

# ---
class gpg7400(object):
    def __init__(self, ndev=1, remote=False):
        initialize = not remote
        self.ctrl = gpg7400_controller(ndev, initialize=initialize)
        pass

    def move(self, speed, count, axis, clock=[4095,4095,4095,4095],
             low_speed=[5,5,5,5], acc=[100,100,100,100], dec=[100,100,100,100],
             accspeed=[0,0,0,0], decspeed=[0,0,0,0]):
        self.ctrl.set_pulse_out()
        self.ctrl.set_motion(axis=axis, mode="MTR_PTP", clock=clock, 
	                     accmode=["MTR_ACC_NORMAL","MTR_ACC_NORMAL","MTR_ACC_NORMAL","MTR_ACC_NORMAL"], 
			     lowspeed=low_speed, speed=speed, acc=acc, dec=dec,accspeed=accspeed, decspeed=decspeed, step=count)
        self.ctrl.start_motion(axis=axis, mode="MTR_PTP")
        return

    def get_position(self, axis='XYZU', cntmode="MTR_ENCODER_MODE"):
        ret = self.ctrl.get_counter(axis=axis, cntmode=cntmode)
        return ret
# ---

class gpg7400_controller(object):
    ndev = int()
    
    def __init__(self, ndev=1, initialize=True):
        self.ndev = ndev
        if initialize: self.initialize()
        return
    
    def _log(self, msg):
        print('Interface GPG7400(%d): %s'%(self.ndev, msg))
        return
        
    def _error_check(self, error_no):
        ErrorGPG7400.check(error_no)
        return
        
    def initialize(self):
        self.open()
        #self.get_device_info()
        return
        
    def open(self, open_flag='MTR_FLAG_NORMAL'):
        """
        1. MtnOpen
        """
        self._log('open')
        open_flag = OpenFlag.verify(open_flag)
        ret = lib.MtnOpen(self.ndev, open_flag)
        self._error_check(ret)
        return
    
    def close(self):
        """
        2. MtnClose
        """
        self._log('close')
        ret = lib.MtnClose(self.ndev)
        self._error_check(ret)
        return
    
    def reset(self, axis='XYZU', mode='MTR_RESET_CTL'):
        """
        3. MtnReset
        """
        self._log('reset')
        axis = AxisConfig(axis)
        mode = ResetMode.verify(mode)
        ret = lib.MtnReset(self.ndev, axis, mode)
        self._error_check(ret)
        return
    
    def set_pulse_out(self, axis='XYZU', mode='MTR_METHOD', config=''):
        """
        4. MtnSetPulseOut
        """
        self._log('set_pulse_out')
        axis = AxisConfig(axis)
        mode = PulseOutConfigSection.verify(mode)
        if mode=='MTR_METHOD': config = PulseOutMethod(config)
        elif mode=='MTR_IDLING': config = int(config)
        elif mode=='MTR_FINISH_FLAG': config = FinishFlag.verify(config)
        elif mode=='MTR_SYNC_OUT': config = SyncOutMode.verify(config)
        ret = lib.MtnSetPulseOut(self.ndev, axis, mode, config)
        self._error_check(ret)
        return
    
    def set_limit_config(self, axis='XYZU', mode='MTR_METHOD', config=''):
        """
        5. MtnSetLimitConfig
        """
        self._log('set_limit_config')
        axis = AxisConfig(axis)
        mode = LimitConfigSection.verify(mode)
        if mode=='MTR_LOGIC': config = LimitConfigLogic(config)
        elif mode=='MTR_SD_FUNC': config = SDFunc.verify(config)
        elif mode=='MTR_SD_ACTIVE': config = SDActive.verify(config)
        elif mode=='MTR_ORG_FUNC': config = ORGFunc.verify(config)
        elif mode=='MTR_ORG_EZ_COUNT': config = int(config)
        elif mode=='MTR_ALM_FUNC': config = ALMFunc.verify(config)
        elif mode=='MTR_SIGNAL_FILTER': config = SignalFilter.verify(config)
        elif mode=='MTR_EL_FUNC': config = ELFunc.verify(config)
        elif mode=='MTR_EZ_ACTIVE': config = EZActive.verify(config)
        elif mode=='MTR_LTC_FUNC': config = LTCFunc.verify(config)
        elif mode=='MTR_CLR_FUNC': config = CLRFunc.verify(config)
        elif mode=='MTR_PCS_FUNC': config = PCSFunc.verify(config)
        elif mode=='MTR_PCS_ACTIVE': config = None
        ret = lib.MtnSetLimitConfig(self.ndev, axis, mode, config)
        self._error_check(ret)
        return
    
    def set_counter_config(self, axis='XYZU', mode='MTR_ENCODER_MODE', config='MTR_SINGLE'):
        """
        6. MtnSetCounterConfig
        """
        self._log('set_counter_config')
        axis = AxisConfig(axis)
        mode = CounterConfigSection.verify(mode)
        if mode=='MTR_ENCODER_MODE': config = EncoderMode.verify(config)
        elif mode=='MTR_COUNTER_CLEAR_ORG': config = CounterClearORG(config)
        elif mode=='MTR_COUNTER_CLEAR_CLR': config = CounterClearORG(config)
        elif mode=='MTR_LATCH_MODE': config = LatchMode.verify(config)
        elif mode=='MTR_DECLINO_MODE': config = DeclinoMode.verify(config)
        elif mode=='MTR_SOFT_LATCH': config = None
        ret = lib.MtnSetCounterConfig(self.ndev, axis, mode, config)
        self._error_check(ret)
        return
    
    def set_comparator(self, axis='XYZU', comp_no='MTR_COMP1', config=None, motion=None,
                       counter=None, cont_type=None):
        """
        7. MtnSetComparator
        """
        self._log('set_comparator')
        axis = AxisConfig(axis)
        comp_no = Comparator.verify(comp_no)
        comp = (lib.MTNCOMP * 4)()
        for i, ax in enumerate(axis.get_ind_on()):
            comp[ax].wConfig = CompConfig.verify(config[i])
            comp[ax].wMotion = CompMotion.verify(motion[i])
            comp[ax].lCounter = int(counter[i])
            comp[ax].wCntType = CompCntType.verify(cont_type[i])
            continue
        ret = lib.MtnSetComparator(self.ndev, axis, comp_no, comp)
        self._error_check(ret)
        return
    
    def set_sync(self, axis='XYZU', mode='MTR_START_MODE', config='MTR_NO'):
        """
        8. MtnSetSync
        """
        self._log('set_sync')
        axis = AxisConfig(axis)
        mode = SyncSection.verify(mode)
        if mode=='MTR_START_MODE': config = StartMode.verify(config)
        elif mode=='MTR_EXT_STOP': config = ExtStop.verify(config)
        elif mode=='MTR_START_LINE': config = StartLine.verify(config)
        elif mode=='MTR_STOP_LINE': config = StopLine.verify(config)
        ret = lib.MtnSetSync(self.ndev, axis, mode, config)
        self._error_check(ret)
        return
    
    def set_revise(self, axis='XYZU', mode='MTR_PULSE', config=1):
        """
        9. MtnSetRevise
        """
        self._log('set_revise')
        axis = AxisConfig(axis)
        mode = ReviseSection.verify(mode)
        if mode=='MTR_PULSE': config = int(config)
        elif mode=='MTR_REVISE_MODE': config = ReviseMode.verify(config)
        elif mode=='MTR_COUNTER_MODE': config = ReviseCounterMode(config)
        elif mode=='MTR_REST_RT': config = int(config)
        elif mode=='MTR_REST_FT': config = int(config)
        ret = lib.MtnSetRevise(self.ndev, axis, mode, config)
        self._error_check(ret)
        return
    
    def set_erc_config(self, axis='XYZU', mode='MTR_AUTO', config=0):
        """
        10. MtnSetERCConfig
        """
        self._log('set_erc_config')
        axis = AxisConfig(axis)
        mode = ERCConfigSection.verify(mode)
        if mode=='MTR_AUTO': config = ERCAuto(config)
        elif mode=='MTR_LOGIC': config = ERCLogic.verify(config)
        elif mode=='MTR_WIDTH': config = ERCWidth.verify(config)
        elif mode=='MTR_OFF_TIMER': config = ERCOffTimer.verify(config)
        elif mode=='MTR_SIGNAL_ON': config = None
        elif mode=='MTR_SIGNAL_OFF': config = None
        ret = lib.MtnSetERCConfig(self.ndev, axis, mode, config)
        self._error_check(ret)
        return
    
    def set_motion(self, axis='XYZU', mode='MTR_JOG', 
                   clock=[], accmode=[], lowspeed=[], speed=[], acc=[], dec=[],
                   accspeed=[], decspeed=[], step=[]):
        """
        11. MtnSetMotion
        """
        self._log('set_motion')
        axis = AxisConfig(axis)
        mode = MotionSection.verify(mode)
        motion = (lib.MTNMOTION * 4)()
        for i, ax in enumerate(axis.get_ind_on()):
            motion[ax].wClock = int(clock[i])
            motion[ax].wAccMode = MotionAccMode.verify(accmode[i])
            motion[ax].fLowSpeed = float(lowspeed[i])
            motion[ax].fSpeed = float(speed[i])
            motion[ax].ulAcc = int(acc[i])
            motion[ax].ulDec = int(dec[i])
            motion[ax].fSAccSpeed = float(accspeed[i])
            motion[ax].fSDecSpeed = float(decspeed[i])
            motion[ax].lStep = int(step[i])
            continue
        ret = lib.MtnSetMotion(self.ndev, axis, mode, motion)
        self._error_check(ret)
        return
    
    def set_motion_line(self, mode='MTR_LINE_NORMAL', 
                        axis='XYZU', clock=4095, linemode='MTR_LINE',
                        accmode='MTR_ACC_NORMAL', lowspeed=1.0, speed=1.0, acc=1,
                        dec=1, accspeed=0.0, decspeed=0.0, step=[0,0,0,0]):
        """
        12. MtnSetMotionLine
        """
        self._log('set_motion_line')
        mode = MotionLineSection.verify(mode)
        line = lib.MTNLINE()
        line.wAxis = AxisConfig(axis)
        line.wClock = int(clock)
        line.wMode = LineMode(linemode)
        line.wAccMode = LineAccMode(accmode)
        line.fLowSpeed = float(lowspeed)
        line.fSpeed = float(speed)
        line.ulAcc = int(acc)
        line.ulDec = int(dec)
        line.fSaccSpeed = float(accspeed)
        line.fSDecSpeed = float(decspeed)
        for i, ax in enumerate(axis.get_ind_on()):
            line.lStep[ax] = int(step[i])
            continue
        ret = lib.MtnSetMotionLine(self.ndev, mode, line)
        self._error_check(ret)
        return
    
    def set_sync_line(self, maxstep=1000, axis='XYZU', clock=4095, linemode='MTR_LINE',
                      accmode='MTR_ACC_NORMAL', lowspeed=1.0, speed=1.0, acc=1,
                      dec=1, accspeed=0.0, decspeed=0.0, step=[0,0,0,0]):
        """
        13. MtnSetSyncLine
        """
        self._log('set_sync_line')
        maxstep = int(maxstep)
        line = lib.MTNLINE()
        line.wAxis = AxisConfig(axis)
        line.wClock = int(clock)
        line.wMode = LineMode(linemode)
        line.wAccMode = LineAccMode(accmode)
        line.fLowSpeed = float(lowspeed)
        line.fSpeed = float(speed)
        line.ulAcc = int(acc)
        line.ulDec = int(dec)
        line.fSaccSpeed = float(accspeed)
        line.fSDecSpeed = float(decspeed)
        for i, ax in enumerate(axis.get_ind_on()):
            line.lStep[ax] = int(step[i])
            continue
        ret = lib.MtnSetSyncLine(self.ndev, maxstep, line)
        self._error_check(ret)
        return
    
    def set_motion_arc(self, mode='MTR_ARC_NORMAL', axis='XYZU', clock=4095,
                       arcmode='MTR_ARC_CW', speed=1.0,
                       centerx=0, centery=0, endx=0, endy=0):
        """
        14. MtnSetMotionArc
        """
        self._log('set_motion_arc')
        mode = MotionArcSection(mode)
        arc = lib.MTNARC()
        arc.wAxis = AxisConfig(axis)
        arc.wClock = int(clock)
        arc.wMode = ARCMode(arcmode)
        arc.fSpeed = float(speed)
        arc.lCenterX = int(centerx)
        arc.lCenterY = int(centery)
        arc.lEndX = int(endx)
        arc.lEndY = int(endy)
        ret = lib.MtnSetMotionArc(self.ndev, mode, arc)
        self._error_check(ret)
        return
    
    def set_motion_cp(self, axis='X', num=2,
                      clock=[], accmode=[], lowspeed=[], speed=[], acc=[], dec=[],
                      accspeed=[], decspeed=[], step=[]):
        """
        15. MtnSetMotionArc
        """
        self._log('set_motion_cp')
        axis = AxisConfig(axis)
        motion = (lib.MTNMOTION * num)()
        for i in range(num):
            motion[i].wClock = int(clock[i])
            motion[i].wAccMode = MotionAccMode.verify(accmode[i])
            motion[i].fLowSpeed = float(lowspeed[i])
            motion[i].fSpeed = float(speed[i])
            motion[i].ulAcc = int(acc[i])
            motion[i].ulDec = int(dec[i])
            motion[i].fSAccSpeed = float(accspeed[i])
            motion[i].fSDecSpeed = float(decspeed[i])
            motion[i].lStep = int(step[i])
            continue
        ret = lib.MtnSetMotionCp(self.ndev, axis, num, motion)
        self._error_check(ret)
        return

# ---
    def start_motion(self, axis="XYZU", startmode="MTR_CONST", mode="MTR_PTP"):
        """
        28. MtnStartMotion
        """
        self._log("start_motion")
        startmode = StartMotion.verify(startmode)
        axis = AxisConfig(axis)
        mode = MotionSection.verify(mode)
        ret = lib.MtnStartMotion(self.ndev, axis, startmode, mode)
        self._error_check(ret)
        return


    def get_status(self, axis="XYZU", sttsmode="MTR_LIMIT_STATUS"):
        """
        35. MtnGetStatus
        ------------------
        """
        self._log("get_status")
        axis = AxisConfig(axis)
        sttsmode = StatusSection.verify(sttsmode)
        po = ctypes.c_ulong(0)
        ret = lib.MtnGetStatus(self.ndev, axis, sttsmode, po)
        self._error_check(ret)
        po = ctypes.pointer(po)
        ret = [po[0], po[1], po[2], po[3]]
        return ret

    def get_counter(self, axis="XYZU", cntmode="MTR_ENCODER_MODE"):
        """
        37. MtnReadCounter
        ------------------
        """
        self._log("read_counter")
        axis = AxisConfig(axis)
        cntmode = CounterConfigSection.verify(cntmode)
        pos = ctypes.c_long(0)
        ret = lib.MtnReadCounter(self.ndev, axis, cntmode, pos)
        self._error_check(ret)
        pos = ctypes.pointer(pos)
        ret = [pos[0], pos[1], pos[2], pos[3]]
        return ret

    def output_do(self, out):
        """
        39. MtnOutputDO
        ------------------
        """
        self._log('output_do')
        out = OutputDO(out)
        ret = lib.MtnOutputDO(self.ndev, out)
        self._error_check(ret)
        return 

    def input_di(self):
        """
        40. MtnInputDIN
        ------------------
        """
        self._log('input_di')
        din = ctypes.c_ushort(0)
        ret = lib.MtnInputDI(self.ndev, din)
        din = InputDI(din.value)
        return din

# ---
    
# .................................
# The following is not implemented.
