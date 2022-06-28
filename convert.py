# -*- coding: utf-8 -*-
'''
@ File         : convert.py
@ Project      : 
@ Author       : 
@ Contact      : 
@ Date         : 2021-12-11 16:45:30
@ Description  : 
'''


from win32com.client import DispatchEx
import re, os
import pythoncom
import string


def read_excel(filename="", password=""):
    all_sheet_content = {}
    
    pythoncom.CoInitialize()
    xlsApp = DispatchEx("Excel.Application")
    xlsApp.DisplayAlerts = False
    xlsApp.Visible = False

    try:
        workbook = xlsApp.Workbooks.Open(filename, UpdateLinks=False, ReadOnly=False, Format=None, Password=password, WriteResPassword=password)
    except:
        xlsApp.DisplayAlerts = True
        xlsApp.Quit()
        pythoncom.CoUninitialize()
        return {}

    for sheet in workbook.Sheets:
        shtName = sheet.Name
        shtContent = sheet.UsedRange.Value
        all_sheet_content.update({shtName:shtContent})

    workbook.Close()
    xlsApp.Visible = True
    xlsApp.DisplayAlerts = True
    xlsApp.Quit()
    pythoncom.CoUninitialize()
    return all_sheet_content


""" 
vaild value:
{
    'msgname'       : msgname,
    'msgid'         : msgid,
    'msgcycletime'  : msgcycletime,
    'msglength'     : msglength,
    'signalname'    : signalname,
    'byteorder'     : byteorder,
    'startbit'      : startbit,
    'bitlen'        : bitlen,
    'resolution'    : resolution,
    'offset'        : offset,
    'maxv'          : maxv,
    'minv'          : minv,
    'unit'          : unit
}

invalid value:
{
    sheetname:{
        type: title, row
        error:{
            row:[ERROR_MSGNAME_EMPTY, ...]
        }
        error:[xx not found in title, ]
    }
}

"""
# define const value 
TRANSMIT_IDCODE     = "Tx"
RECEIVE_IDCODE      = "Rx"

DEFULT_VAL = "Vector__XXX"

# Signal Error
ERROR_ROW_OK                = 0
ERROR_ROW_ERROR             = 1
ERROR_ROW_EMPTY             = 2

# Sheet Error
ERROR_SHEET_OK              = 0  
ERROR_SHEET_TITLE_UNMATCH   = 1  # need record the error, which title is missing
ERROR_SHEET_ERROR           = 2  # no need to record anything.


class ExcelDataHandle(object):
    # check if there are dbc information in worksheet
    def check_worksheet(self, worksheet, setting_configure):
        configStyle = setting_configure['Configure Style']
        configInfo = setting_configure['Table Configure']
        column_miss_count = 0
        error_message = []

        if worksheet and setting_configure:

            if configStyle == 'Auto':
                
                # all column number base 0
                self.msgname_col_num        = -1
                self.msgid_col_num          = -1
                self.msgcycletime_col_num   = -1
                self.msglength_col_num      = -1
                self.signalname_col_num     = -1
                self.byteorder_col_num      = -1
                self.startbit_col_num       = -1
                self.bitlen_col_num         = -1
                self.resolution_col_num     = -1
                self.offset_col_num         = -1
                self.maxv_col_num           = -1
                self.minv_col_num           = -1
                self.unit_col_num           = -1

                first_row = worksheet[0]

                for idx, cell in enumerate(first_row):
                    if not isinstance(cell, str):
                        continue
                    msgname_match       = re.match(r".*Msg.*Name.*\s.*报文名称", cell)
                    msgid_match         = re.match(r".*Msg.*ID.*\s.*报文标识符", cell)
                    msgcycletime_match  = re.match(r".*Msg.*Cycle.*Time.*\s.*报文周期时间", cell)
                    msglength_match     = re.match(r".*Msg.*Length.*\s.*报文长度", cell)
                    signalname_match    = re.match(r".*Signal.*Name.*\s.*信号名称.*英.*", cell)
                    byteorder_match     = re.match(r".*Byte.*Order.*\s.*排列格式", cell)
                    startbit_match      = re.match(r".*Start.*Bit.*\s.*起始位", cell)
                    bitlen_match        = re.match(r".*Bit.*Length.*\s.*信号长度", cell)
                    resolution_match    = re.match(r".*Resolution.*\s.*精度", cell)
                    offset_match        = re.match(r".*Offset.*\s.*偏移量", cell)
                    maxv_match          = re.match(r".*Signal.*Max..*Value.*phys.*\s.*物理最大值", cell)
                    minv_match          = re.match(r".*Signal.*Min..*Value.*phys.*\s.*物理最小值", cell)
                    unit_match          = re.match(r".*Unit.*\s.*单位", cell)
                
                    if msgname_match:
                        self.msgname_col_num        = idx    
                    elif msgid_match:
                        self.msgid_col_num          = idx
                    elif msgcycletime_match:
                        self.msgcycletime_col_num   = idx        
                    elif msglength_match:
                        self.msglength_col_num      = idx    
                    elif signalname_match:
                        self.signalname_col_num     = idx    
                    elif byteorder_match:
                        self.byteorder_col_num      = idx    
                    elif startbit_match:
                        self.startbit_col_num       = idx    
                    elif bitlen_match:
                        self.bitlen_col_num         = idx
                    elif resolution_match:
                        self.resolution_col_num     = idx    
                    elif offset_match:
                        self.offset_col_num         = idx
                    elif maxv_match:
                        self.maxv_col_num           = idx
                    elif minv_match:
                        self.minv_col_num           = idx
                    elif unit_match:
                        self.unit_col_num           = idx
                
                if self.msgname_col_num      == -1:
                    column_miss_count += 1
                    error_message.append('{:<10} 表头未发现.'.format('报文名称'))
                if self.msgid_col_num        == -1:
                    column_miss_count += 1
                    error_message.append('{:<10} 表头未发现.'.format('报文标识符'))
                if self.msgcycletime_col_num == -1:
                    column_miss_count += 1
                    error_message.append('{:<10} 表头未发现.'.format('报文周期时间'))
                if self.msglength_col_num    == -1:
                    column_miss_count += 1
                    error_message.append('{:<10} 表头未发现.'.format('报文长度'))
                if self.signalname_col_num   == -1:
                    column_miss_count += 1
                    error_message.append('{:<10} 表头未发现.'.format('信号名称'))
                if self.byteorder_col_num    == -1:
                    column_miss_count += 1
                    error_message.append('{:<10} 表头未发现.'.format('排列格式'))
                if self.startbit_col_num     == -1:
                    column_miss_count += 1
                    error_message.append('{:<10} 表头未发现.'.format('起始位'))
                if self.bitlen_col_num       == -1:
                    column_miss_count += 1
                    error_message.append('{:<10} 表头未发现.'.format('信号长度'))
                if self.resolution_col_num   == -1:
                    column_miss_count += 1
                    error_message.append('{:<10} 表头未发现.'.format('精度'))
                if self.offset_col_num       == -1:
                    column_miss_count += 1
                    error_message.append('{:<10} 表头未发现.'.format('偏移量'))
                if self.maxv_col_num         == -1:
                    column_miss_count += 1
                    error_message.append('{:<10} 表头未发现.'.format('物理最大值'))
                if self.minv_col_num         == -1:
                    column_miss_count += 1
                    error_message.append('{:<10} 表头未发现.'.format('物理最小值'))
                if self.unit_col_num         == -1:
                    column_miss_count += 1
                    error_message.append('{:<10} 表头未发现.'.format('单位'))
            elif configStyle == 'Manual':
                self.msgname_col_num        = configInfo['MsgName']
                self.msgid_col_num          = configInfo['MsgID']
                self.msgcycletime_col_num   = configInfo['MsgCycleTime']
                self.msglength_col_num      = configInfo['MsgLen']
                self.signalname_col_num     = configInfo['SignalName']
                self.byteorder_col_num      = configInfo['ByteOrder']
                self.startbit_col_num       = configInfo['StartBit']
                self.bitlen_col_num         = configInfo['BitLen']
                self.resolution_col_num     = configInfo['Resolution']
                self.offset_col_num         = configInfo['Offset']
                self.maxv_col_num           = configInfo['Maxv']
                self.minv_col_num           = configInfo['Minv']
                self.unit_col_num           = configInfo['Unit']

            if column_miss_count == 0:
                return ERROR_SHEET_OK, None
            elif column_miss_count > 0 and column_miss_count < 3:
                return ERROR_SHEET_TITLE_UNMATCH, error_message[:]
            else:
                return ERROR_SHEET_ERROR, None
        else:
            return ERROR_SHEET_ERROR, None

    # extract the key info like msgid msgname ... 
    # put them into self.extract_contents and self.error_contents
    def extract_information(self, sheetname, row):
        row_status    = ERROR_ROW_OK
        empty_count   = 0
        error_message = []

        msgname      = row[self.msgname_col_num]
        if msgname == None:
            empty_count += 1
            row_status = ERROR_ROW_ERROR
            error_message.append('{:<10} => "" 数值为空'.format('报文名称'))
        else:
            status, msgname = self.msgname_check(msgname)
            if not status:
                row_status = ERROR_ROW_ERROR
                error_message.append('{:<10} => {} 数值无效'.format('报文名称', msgname))

        msgid        = row[self.msgid_col_num]
        if msgid == None:
            empty_count += 1
            row_status = ERROR_ROW_ERROR
            error_message.append('{:<10} => "" 数值为空'.format('报文标识符'))
        else:
            status, msgid = self.msgid_check(msgid)
            if not status:
                row_status = ERROR_ROW_ERROR
                error_message.append('{:<10} => {} 数值无效'.format('报文标识符', msgid))

        msgcycletime = row[self.msgcycletime_col_num]
        if msgcycletime == None:
            empty_count += 1
            row_status = ERROR_ROW_ERROR
            error_message.append('{:<10} => "" 数值为空'.format('报文周期时间'))
        else:
            status, msgcycletime = self.msgcycletime_check(msgcycletime)
            if not status:
                row_status = ERROR_ROW_ERROR
                error_message.append('{:<10} => {} 数值无效'.format('报文周期时间', msgcycletime))

        msglength    = row[self.msglength_col_num] 
        if msglength == None:
            empty_count += 1
            row_status = ERROR_ROW_ERROR
            error_message.append('{:<10} => "" 数值为空'.format('报文长度'))
        else:
            status, msglength = self.msglength_check(msglength)
            if not status:
                row_status = ERROR_ROW_ERROR
                error_message.append('{:<10} => {} 数值无效'.format('报文长度', msglength))

        signalname   = row[self.signalname_col_num]
        if signalname == None:
            empty_count += 1
            row_status = ERROR_ROW_ERROR
            error_message.append('{:<10} => "" 数值为空'.format('信号名称'))
        else:
            status, signalname = self.signalname_check(signalname)
            if not status:
                row_status = ERROR_ROW_ERROR
                error_message.append('{:<10} => {} 数值无效'.format('信号名称', signalname))

        byteorder    = row[self.byteorder_col_num]
        if byteorder == None:
            empty_count += 1
            row_status = ERROR_ROW_ERROR
            error_message.append('{:<10} => "" 数值为空'.format('排列格式'))
        else:
            status, byteorder = self.byteorder_check(byteorder)
            if not status:
                row_status = ERROR_ROW_ERROR
                error_message.append('{:<10} => {} 数值无效'.format('排列格式', byteorder))

        startbit     = row[self.startbit_col_num] 
        if startbit == None:
            empty_count += 1
            row_status = ERROR_ROW_ERROR
            error_message.append('{:<10} => "" 数值为空'.format('起始位'))
        else:
            status, startbit = self.startbit_check(startbit)
            if not status:
                row_status = ERROR_ROW_ERROR
                error_message.append('{:<10} => {} 数值无效'.format('起始位', startbit))
       

        bitlen       = row[self.bitlen_col_num]
        if bitlen == None:
            empty_count += 1
            row_status = ERROR_ROW_ERROR
            error_message.append('{:<10} => "" 数值为空'.format('信号长度'))
        else:
            status, bitlen = self.bitlen_check(bitlen)
            if not status:
                row_status = ERROR_ROW_ERROR
                error_message.append('{:<10} => {} 数值无效'.format('信号长度', bitlen))

        resolution   = row[self.resolution_col_num]
        if resolution == None:
            empty_count += 1
            row_status = ERROR_ROW_ERROR
            error_message.append('{:<10} => "" 数值为空'.format('精度'))
        else:
            status, resolution = self.resolution_check(resolution)
            if not status:
                row_status = ERROR_ROW_ERROR
                error_message.append('{:<10} => {} 数值无效'.format('精度', resolution))

        offset       = row[self.offset_col_num]
        if offset == None:
            empty_count += 1
            row_status = ERROR_ROW_ERROR
            error_message.append('{:<10} => "" 数值为空'.format('偏移量'))
        else:
            status, offset = self.offset_check(offset)
            if not status:
                row_status = ERROR_ROW_ERROR
                error_message.append('{:<10} => {} 数值无效'.format('偏移量', offset))

        maxv         = row[self.maxv_col_num]
        if maxv == None:
            empty_count += 1
            row_status = ERROR_ROW_ERROR
            error_message.append('{:<10} => "" 数值为空'.format('物理最大值'))
        else:
            status, maxv = self.maxv_check(maxv)
            if not status:
                row_status = ERROR_ROW_ERROR
                error_message.append('{:<10} => {} 数值无效'.format('物理最大值', maxv))

        minv         = row[self.minv_col_num]
        if minv == None:
            empty_count += 1
            row_status = ERROR_ROW_ERROR
            error_message.append('{:<10} => "" 数值为空'.format('物理最小值'))
        else:
            status, minv = self.minv_check(minv)
            if not status:
                row_status = ERROR_ROW_ERROR
                error_message.append('{:<10} => {} 数值无效'.format('物理最小值', minv))

        unit         = row[self.unit_col_num]
        status, unit = self.unit_check(unit)

        if byteorder == '0': # ''motorola is 0 intel is 1 and 0 need to be changed
            startbit_status, startbit = self.caculate_motorola_startbit(startbit, bitlen)
            if not startbit_status:
                row_status = ERROR_ROW_ERROR
                error_message.append('起始位:{} 长度:{} => 超出范围'.format(startbit, bitlen))
        
        if row_status == ERROR_ROW_OK:
            
            self.extract_contents[sheetname].append(
                {
                    'msgname'       : msgname,
                    'msgid'         : msgid,
                    'msgcycletime'  : msgcycletime,
                    'msglength'     : msglength,
                    'transmitter'   : DEFULT_VAL,
                    'signalname'    : signalname,
                    'byteorder'     : byteorder,
                    'valuetype'     : '+',          # unsigned
                    'startbit'      : startbit,
                    'bitlen'        : bitlen,
                    'resolution'    : resolution,
                    'offset'        : offset,
                    'maxv'          : maxv,
                    'minv'          : minv,
                    'unit'          : unit,
                    'receiver'      : DEFULT_VAL
                }
            )
        
        if empty_count == 12:
            row_status = ERROR_ROW_EMPTY
            error_message = []
        
        return row_status, error_message
    

    def msgname_check(self, old_value):
        new_value = str(old_value).strip()
        if set(new_value) & set(string.ascii_letters+string.digits+'_') == set(new_value):
            status = True
        else:
            status = False
        return status, new_value


    def msgid_check(self, old_value):
        new_value = str(old_value).strip()
        try:
            new_value = int(new_value, 16)
        except:
            status = False
        else:
            status = True
            new_value = str(new_value)
        return status, new_value


    def msgcycletime_check(self, old_value):
        new_value = str(old_value).strip()
        try:
            new_value = float(new_value)
        except:
            status = False
        else:
            status = True
            new_value = str(new_value)
        return status, new_value


    def msglength_check(self, old_value):
        new_value = str(old_value).strip()
        try:
            new_value = float(new_value)
        except:
            status = False
        else:
            status = True
            new_value = str(int(new_value))
        return status, new_value


    def signalname_check(self, old_value):
        new_value = str(old_value).strip()
        if set(new_value) & set(string.ascii_letters+string.digits+'_') == set(new_value):
            status = True
        else:
            status = False
        return status, new_value


    def byteorder_check(self, old_value):
        new_value = str(old_value).strip()
        if new_value == 'Motorola LSB':
            new_value = '0'
            status = True
        elif new_value == 'Intel':
            new_value = '1'
            status = True
        else:
            status = False
        return status, new_value


    def startbit_check(self, old_value):
        new_value = str(old_value).strip()
        try:
            new_value = float(new_value)
        except:
            status = False
        else:
            if -1 < new_value < 64:
                status = True
            else:
                status = False
            new_value = str(int(new_value))
        return status, new_value


    def bitlen_check(self, old_value):
        new_value = str(old_value).strip()
        try:
            new_value = float(new_value)
        except:
            status = False
        else:
            if -1 < new_value < 64:
                status = True
            else:
                status = False
            new_value = str(int(new_value))
        return status, new_value


    def resolution_check(self, old_value):
        new_value = str(old_value).strip()
        try:
            new_value = float(new_value)
        except:
            status = False
        else:
            status = True
            new_value =  str(int(new_value)) if int(new_value) == new_value else str(new_value)
        return status, new_value


    def offset_check(self, old_value):
        new_value = str(old_value).strip()
        try:
            new_value = float(new_value)
        except:
            status = False
        else:
            status = True
            new_value =  str(int(new_value)) if int(new_value) == new_value else str(new_value)
        return status, new_value


    def maxv_check(self, old_value):
        new_value = str(old_value).strip()
        try:
            new_value = float(new_value)
        except:
            status = False
        else:
            status = True
            new_value =  str(int(new_value)) if int(new_value) == new_value else str(new_value)
        return status, new_value


    def minv_check(self, old_value):
        new_value = str(old_value).strip()
        try:
            new_value = float(new_value)
        except:
            status = False
        else:
            status = True
            new_value =  str(int(new_value)) if int(new_value) == new_value else str(new_value)
        return status, new_value


    def unit_check(self, old_value):
        if old_value:
            new_value = str(old_value).strip()
        else:
            new_value = ''
        return None, new_value


    def caculate_motorola_startbit(self, startbit="", bitlen=""):
        mot_startbit = ""
        status = False
        bitlen = int(bitlen)
        bitbox = []
        for i in range(8):
            for j in range(8):
                bitbox.append(str((7-i)*8+j))
        if startbit in bitbox:
            bitpos = bitbox.index(startbit)+bitlen-1
            if bitpos in range(0, 64):
                mot_startbit = str(bitbox[bitbox.index(startbit)+bitlen-1])
                status = True
        if not status:
            mot_startbit = startbit
        return status, mot_startbit


    def format_error_message(self):
        for sheetname, error in self.error_contents.items():
            error_type          = error['type']
            error_content       = error['error']
            error_out_message   = []

            if error_type == 'row':
                for row, error_m in error_content.items():
                    error_out_message.append('  SHEET名称:{:<30} 行号:{:>3d} 行错误 ->'.format(sheetname, row))
                    error_out_message.extend(['{:4}{:0>2d}.{}'.format('', i, e) for i, e in enumerate(error_m)])
                    error_out_message.append('')
            elif error_type == 'title':
                error_out_message.append('  SHEET名称:{:<30} 表头错误 ->'.format(sheetname))
                error_out_message.extend(['{:4}{:0>2d}.{}'.format('', i, e) for i, e in enumerate(error_content)])
                error_out_message.append('')
            self.error_messages.extend(error_out_message)


    def handle_data(self, worksheet_with_name, setting_configure):
        self.error_contents   = {}
        self.extract_contents = {}
        self.error_messages   = []

        for sheetname, worksheet in worksheet_with_name.items():
            sheet_status, error_message = self.check_worksheet(worksheet, setting_configure)
            if sheet_status == ERROR_SHEET_OK:
                self.error_contents.update(
                    {
                        sheetname : {
                            'type'  : 'row',
                            'error' : {}
                        }
                    }
                )
                self.extract_contents.update(
                    {
                        sheetname : []
                    }
                )
                for row, row_content in enumerate(worksheet[1:]):
                    row_status, error_message = self.extract_information(sheetname, row_content)
                    if row_status == ERROR_ROW_ERROR:
                        self.error_contents[sheetname]['error'][row+2] = error_message
            elif sheet_status == ERROR_SHEET_TITLE_UNMATCH:
                # record the title error
                self.error_contents.update(
                    {
                        sheetname : {
                            'type'  : 'title',
                            'error' : error_message
                        }
                    }
                )
            elif sheet_status == ERROR_SHEET_ERROR:
                pass

        self.format_error_message()

        

"""
VERSION ""
NS_
BS_
BU_ node
BU_:Nodename1 Nodename2 Nodename3 ……
BO_ msg info
BO_ MessageId（10进制数表示） MessageName: MessageSize Transmitter
SG_ signal info
SG_ SignalName : StartBit|SignalSize@ByteOrder ValueType (Factor,Offset) [Min|Max] Unit Receiver

CM_ BO_ 
CM_ Object MessageId/NodeName “Comment”
BA_DEF_
BA_DEF_DEF_
BA_DEF_ Object AttributeName ValueType Min Max;
BA_DEF_DEF_ AttributeName DefaultValue;

VAL_
VAL_ MessageId SignalName N “DefineN” …… 0 “Define0”;
"""

DBC_MODULE = '''VERSION ""


NS_ : 
\tNS_DESC_
\tCM_
\tBA_DEF_
\tBA_
\tVAL_
\tCAT_DEF_
\tCAT_
\tFILTER
\tBA_DEF_DEF_
\tEV_DATA_
\tENVVAR_DATA_
\tSGTYPE_
\tSGTYPE_VAL_
\tBA_DEF_SGTYPE_
\tBA_SGTYPE_
\tSIG_TYPE_REF_
\tVAL_TABLE_
\tSIG_GROUP_
\tSIG_VALTYPE_
\tSIGTYPE_VALTYPE_
\tBO_TX_BU_
\tBA_DEF_REL_
\tBA_REL_
\tBA_DEF_DEF_REL_
\tBU_SG_REL_
\tBU_EV_REL_
\tBU_BO_REL_
\tSG_MUL_VAL_

BS_:

BU_:{nodes}


{bosg}

BA_DEF_  "BusType" STRING ;
BA_DEF_DEF_  "BusType" "CAN";

'''

class DBCGen(object):
    def __init__(self):
        super().__init__()
        self.running = False
        self.excel_sheet_number = 0
        self.excel_data_handle  = ExcelDataHandle()
        

# {
#     'msgname'       : msgname,
#     'msgid'         : msgid,
#     'msgcycletime'  : msgcycletime,
#     'msglength'     : msglength,
#     'signalname'    : signalname,
#     'byteorder'     : byteorder,
#     'startbit'      : startbit,
#     'bitlen'        : bitlen,
#     'resolution'    : resolution,
#     'offset'        : offset,
#     'maxv'          : maxv,
#     'minv'          : minv,
#     'unit'          : unit
# }
    def gen_bosg_code(self, contents:list) -> str:
        bo = []
        bosg_code = ''
        msgids = set([s.get('msgid') for s in contents])
        
        for msgid in msgids:
            firstfound = True
            for s in contents:
                if s.get('msgid') == msgid:
                    if firstfound:
                        firstfound = False
                        bosg_code += "BO_ {msgid} {msgname}: {msglength} {transmitter}\n".format(**s)
                    bosg_code += " SG_ {signalname} : {startbit}|{bitlen}@{byteorder}{valuetype} ({resolution},{offset}) [{minv}|{maxv}] \"{unit}\" {receiver}\n".format(**s)
            bosg_code += '\n'
        return bosg_code


    def generate_dbc(self, xlsxname:str, password:str, setting_configure:dict) -> None:
        self.running = True
        self.excel_sheet_number = 0
        self.dbcfilename_out = []

        path = os.path.dirname(xlsxname)

        sheets = read_excel(xlsxname, password)
        # print('open excel')

        self.excel_data_handle.handle_data(sheets, setting_configure)
        # print('handle data')

        for sheetname, contents in self.excel_data_handle.extract_contents.items():
            filename = sheetname.replace(' ', '_')+'.dbc'
            self.excel_sheet_number += 1
            self.dbcfilename_out.append(filename)

            dbc_code = DBC_MODULE
            bosg_code = self.gen_bosg_code(contents)
            dbc_code = dbc_code.format(nodes='', bosg=bosg_code)
            
            # write dbc
            with open(os.path.join(path, filename), 'w', encoding='utf-8') as f:
                f.write(dbc_code)
        self.running = False


    def generate_error_message(self):
        return self.excel_data_handle.error_messages
        

    def generate_convert_result(self):
        message = ['DBC转换完成,结果如下:',
        '  成功转换DBC文件数量: {:>2}.'.format(self.excel_sheet_number)]
        message.extend(['    {:0>2d}. {}'.format(i, m) for i, m in enumerate(self.dbcfilename_out)])
        message.extend(['', '表格内检测到一些错误:']+self.excel_data_handle.error_messages)

        return message


if __name__ == "__main__":
    
    xlsxname  = r"D:\Yun\Codes\Python\DBConvertor\can.xlsx".replace('\\', '/')
    print(xlsxname)
    # password = ''

    # dbcgen = DBCGen()
    # dbcgen.generate_dbc(xlsxname, password)
    # print(dbcgen.generate_error_message())
    # exceldatahandle  = ExcelDataHandle()

    # all_sheet_content = read_excel(xlsxname, password)
    # exceldatahandle.handle_data(all_sheet_content)

    # print('\n'.join(exceldatahandle.error_messages))

