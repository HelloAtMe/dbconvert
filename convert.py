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

ExcelRowNum = {
    1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G",
    8:"H", 9:"I", 10:"J", 11:"K", 12:"L", 13:"M", 14:"N",
    15:"O", 16:"P", 17:"Q", 18:"R", 19:"S", 20:"T",
    21:"U", 22:"V", 23:"W", 24:"X", 25:"Y", 26:"Z", 
    27:"AA", 28:"AB", 29:"AC", 30:"AD", 31:"AE", 32:"AF", 33:"AG",
    34:"AH", 35:"AI", 36:"AJ", 37:"AK", 38:"AL", 39:"AM", 40:"AN",
    41:"AO", 42:"AP", 43:"AQ", 44:"AR", 45:"AS", 46:"AT"
}


def read_excel(self, filename="", password=""):
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
        return False, {}

    for sheet in workbook.Sheets:
        shtName = sheet.Name
        shtContent = sheet.UsedRange.Value
        all_sheet_content.update({shtName:shtContent})

    workbook.Close()
    xlsApp.Visible = True
    xlsApp.DisplayAlerts = True
    xlsApp.Quit()
    pythoncom.CoUninitialize()
    return True, all_sheet_content


""" 
vaild value:
{
    msgid:{
        cycle:
        length:
        node:
        signals:{
            id : {
                signalname:
                byteorder:
                startbit:
                bitlen:
                resolution:
                offset:
                maxv:
                minv:
                unit:
                receiver:[]
            }
        }
    }
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
    def check_worksheet(self, worksheet):
        column_miss_count = 0
        error_message = []

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

        if column_miss_count == 0:
            return ERROR_SHEET_OK, None
        elif column_miss_count > 0 and column_miss_count < 3:
            return ERROR_SHEET_TITLE_UNMATCH, error_message[:]
        else:
            return ERROR_SHEET_ERROR, None


    # extract the key info like msgid msgname ... 
    # put them into self.extract_contents and self.error_contents
    def extract_information(self, row):
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

        if row_status == ERROR_ROW_OK:
            self.extract_contents.append(
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
            new_value = str(new_value)
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
        if new_value in ['Motorola LSB', 'Intel']:
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
            new_value = str(new_value)
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
            new_value = str(new_value)
        return status, new_value


    def resolution_check(self, old_value):
        new_value = str(old_value).strip()
        try:
            new_value = float(new_value)
        except:
            status = False
        else:
            status = True
            new_value = str(new_value)
        return status, new_value


    def offset_check(self, old_value):
        new_value = str(old_value).strip()
        try:
            new_value = float(new_value)
        except:
            status = False
        else:
            status = True
            new_value = str(new_value)
        return status, new_value


    def maxv_check(self, old_value):
        new_value = str(old_value).strip()
        try:
            new_value = float(new_value)
        except:
            status = False
        else:
            status = True
            new_value = str(new_value)
        return status, new_value


    def minv_check(self, old_value):
        new_value = str(old_value).strip()
        try:
            new_value = float(new_value)
        except:
            status = False
        else:
            status = True
            new_value = str(new_value)
        return status, new_value


    def unit_check(self, old_value):
        if old_value:
            new_value = str(old_value).strip()
        else:
            new_value = ''
        return None, new_value


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
                error_out_message.extend(['{:4}{:>2d}.{}'.format('', i, e) for i, e in enumerate(error_content)])
            error_out_message.append('')
            self.error_messages.extend(error_out_message)


    def handle_data(self, worksheet_with_name):
        self.error_contents   = {}
        self.extract_contents = []
        self.error_messages   = []

        for sheetname, worksheet in worksheet_with_name.items():
            sheet_status, error_message = self.check_worksheet(worksheet)
            if sheet_status == ERROR_SHEET_OK:
                self.error_contents.update(
                    {
                        sheetname : {
                            'type'  : 'row',
                            'error' : {}
                        }
                    }
                )
                for row, row_content in enumerate(worksheet[1:]):
                    row_status, error_message = self.extract_information(row_content)
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


DEFULT_VAL = "Vector__XXX"
class DBCGen(object):
    def __init__(self) -> None:
        super().__init__()
        self.excel_data_handle  = ExcelDataHandle()


    def gen_version_code(self):
        self.version_code = """VERSION "" """


    def gen_ns_code(self):
        self.ns_code = """
NS_ :
    NS_DESC_
    CM_
    BA_DEF_
    BA_
    VAL_
    CAT_DEF_
    CAT_
    FILTER
    BA_DEF_DEF_
    EV_DATA_
    ENVVAR_DATA_
    SGTYPE_
    SGTYPE_VAL_
    BA_DEF_SGTYPE_
    BA_SGTYPE_
    SIG_TYPE_REF_
    VAL_TABLE_
    SIG_GROUP_
    SIG_VALTYPE_
    SIGTYPE_VALTYPE_
    BO_TX_BU_
    BA_DEF_REL_
    BA_REL_
    BA_DEF_DEF_REL_
    BU_SG_REL_
    BU_EV_REL_
    BU_BO_REL_
    SG_MUL_VAL_
"""

    def gen_bs_code(self):
        self.bs_code = "BS_:\n"

    def gen_bu_code(self):
        self.bu_code = "BU_: "
        for n in self.node_list:
            self.bu_code += n + " "
        self.bu_code += "\n"

    def gen_bo_code(self, msg_attr=[]):
        tx_node_list = msg_attr[4]

        _id   = self.filter_msgid(msg_attr[0])
        _name = self.filter_msgname(msg_attr[1])
        _len  = self.filter_msglen(msg_attr[3])
        _node = ""

        if len(tx_node_list) > 0:
            _node = self.filter_node(tx_node_list[0])
        else:
            _node = DEFULT_VAL
        if self.temp_msgid_error:
            self.fatal_error_msg = True
            self.fatal_error_info_msg.append(_id)
            return ""
        else:
            return "BO_ {} {}: {} {}\n".format(self.caculate_msgid(_id), _name, _len, _node)

    def gen_sg_code(self, msgid="", signal_attr=[]):
        self.fatal_error_signal = False
        _name   = self.filter_signalname(signal_attr[0])
        _start  = self.filter_startbit(signal_attr[2])
        _len    = self.filter_bitlen(signal_attr[3])
        if signal_attr[1] == "Motorola LSB":
            _order  = "0"
        elif signal_attr[1] == "Intel":
            _order  = "1"
        _type   = "+"
        _factor = self.filter_factor(signal_attr[4])
        _offset = self.filter_offset(signal_attr[5])
        _min    = self.filter_min(signal_attr[7])
        _max    = self.filter_max(signal_attr[6])
        _unit   = self.filter_unit(signal_attr[10])
        _node   = ""
        rx_node_list   = signal_attr[12]
        temp_rx_nodes = []
        if len(rx_node_list) > 1:
            for n in rx_node_list:
                n = self.filter_node(n)
                temp_rx_nodes.append(n)
            _node = ", ".join(temp_rx_nodes)
        elif len(rx_node_list) == 1:
            _node = self.filter_node(rx_node_list[0])
        else:
            _node = DEFULT_VAL

        temp_error_info = []
        if self.temp_startbit_error:
            self.fatal_error_signal = True
            temp_error_info.append("Start Bit -> "+_start)
        if self.temp_bitlen_error:
            self.fatal_error_signal = True
            temp_error_info.append("Bit Length -> "+_len)
        if self.temp_factor_error:
            self.fatal_error_signal = True
            temp_error_info.append("Resolution -> "+_factor)
        if self.temp_offset_error:
            self.fatal_error_signal = True
            temp_error_info.append("Offset -> "+_offset)

        if not (self.fatal_error_signal):
            _start = self.caculate_startbit(_start, _len)
            return """ SG_ {} : {}|{}@{}{} ({},{}) [{}|{}] "{}" {}\n""".format( _name,
                _start, _len ,_order, _type ,_factor, _offset, _min, _max, _unit, _node)
        else:
            self.fatal_error_info_signal.append([msgid, signal_attr[0], temp_error_info])
            return ""
        
    def gen_bosg_code(self):
        self.bosg_code = ""
        for msgid in self.msg_id_list:
            temp_msg_code = ""
            msg_attr = self.msg_attr_dict[msgid]
            sgs_attr = self.msg_signal_dict[msgid]
            temp_msg_code = self.gen_bo_code(msg_attr)
            if not (self.fatal_error_msg):
                self.bosg_code += temp_msg_code
                for sg_attr in sgs_attr:
                    temp_signal_code = ""
                    temp_signal_code = self.gen_sg_code(msgid, sg_attr)
                    if not (self.fatal_error_signal):
                        self.bosg_code += temp_signal_code
                self.bosg_code += "\n"
        self.bosg_code += "\n"

    def gen_bedef_def_code(self):
        self.bedef_def_code = """
BA_DEF_  "BusType" STRING ;
BA_DEF_DEF_  "BusType" "CAN";
        """

    def filter_msgid(self, msgid=""):
        self.temp_msgid_error = False
        characters = "xX0123456789abcdefABCDEF"
        for c in msgid:
            if c not in characters:
                self.temp_msgid_error = True
                break
        return msgid
    def filter_msgname(self, msgname=""):
        characters  =  "abcdefghijklmnopqrstuvwxyz\
ABCDEFGHIJKLMNOPQRSTUVWXYZ\
0123456789_"
        _msgname = ""
        for c in msgname:
            if c in characters:
                _msgname += c
        return _msgname
    def filter_msglen(self, msglen=""):
        characters  =  "0123456789."
        _msglen = ""
        for c in msglen:
            if c in characters:
                if c == ".":
                    break
                _msglen += c
        if _msglen == "":
            _msglen = "8"
        return _msglen
    def filter_signalname(self, signalname=""):
        characters  =  "abcdefghijklmnopqrstuvwxyz\
ABCDEFGHIJKLMNOPQRSTUVWXYZ\
0123456789_"
        _signalname = ""
        for c in signalname:
            if c in characters:
                _signalname += c
        return _signalname
    def filter_startbit(self, startbit=""):
        characters  =  "0123456789."
        self.temp_startbit_error = False
        _startbit = ""
        if startbit != "":
            for c in startbit:
                if c not in characters:
                    self.temp_startbit_error = True
                    break
        else:
            self.temp_startbit_error = True
        if not(self.temp_startbit_error):
            _startbit = str(int(float(startbit)))
        return _startbit
    def filter_bitlen(self, bitlen=""):
        characters  =  "0123456789."
        self.temp_bitlen_error = False
        _bitlen = ""
        if bitlen != "":
            for c in bitlen:
                if c not in characters:
                    self.temp_bitlen_error = True
                    break
        else:
            self.temp_bitlen_error = True
        if not(self.temp_bitlen_error):
            _bitlen = str(int(float(bitlen)))
        return _bitlen
    def _Int_Check(self, strings=""):
        int_flag = False
        temp2 = ""
        temp_l = []
        if "." in strings:
            temp_l = strings.split(".")
            if len(temp_l) == 2:
                temp2 = temp_l[1]
                if int(temp2) > 0:
                    int_flag = False
                else:
                    int_flag = True
        return int_flag
    def filter_factor(self, factor=""):
        characters  =  "0123456789."
        self.temp_factor_error = False
        for c in factor:
            if c not in characters:
                self.temp_factor_error = True
                break
        if not(self.temp_factor_error):
            if self._Int_Check(factor):
                factor = factor.split(".")[0]
        if factor == "":
            factor = "1"
        return factor
    def filter_offset(self, offset=""):
        characters  =  "0123456789-."
        self.temp_offset_error = False
        for c in offset:
            if c not in characters:
                self.temp_offset_error = True
                break
        if not(self.temp_offset_error):
            if self._Int_Check(offset):
                offset = offset.split(".")[0]
        if offset == "":
            offset = "0"
        return offset
    def filter_min(self, minv=""):
        characters  =  "0123456789-."
        _minv = ""
        for c in minv:
            if c in characters:
                _minv += c
        if self._Int_Check(_minv):
            _minv = _minv.split(".")[0]
        if _minv == "":
            _minv = "0"
        return _minv
    def filter_max(self, maxv=""):
        characters  =  "0123456789-."
        _maxv = ""
        for c in maxv:
            if c in characters:
                _maxv += c
        if self._Int_Check(_maxv):
            _maxv = _maxv.split(".")[0]
        if _maxv == "":
            _maxv = "0"
        return _maxv
    def filter_unit(self, uint=""):
        characters  =  "abcdefghijklmnopqrstuvwxyz\
ABCDEFGHIJKLMNOPQRSTUVWXYZ\
0123456789_/"
        _uint = ""
        for c in uint:
            if c in characters:
                _uint += c
        return _uint
    def filter_node(self, _node=""):
        characters  =  "abcdefghijklmnopqrstuvwxyz\
ABCDEFGHIJKLMNOPQRSTUVWXYZ\
0123456789_"
        __node = ""
        for c in _node:
            if c in characters:
                __node += c
        return __node
    def caculate_startbit(self, startbit="", bitlen=""):
        bitlen = int(bitlen)
        mot_startbit = ""
        bitbox = []
        for i in range(8):
            for j in range(8):
                bitbox.append(str((7-i)*8+j))
        mot_startbit = str(bitbox[bitbox.index(startbit)+bitlen-1])
        return mot_startbit
    def caculate_msgid(self, msgid=""):
        return str(int(msgid, 16))

    def gen_dbc_content(self):

        self.gen_version_code()
        self.gen_ns_code()
        self.gen_bs_code()
        self.gen_bu_code()
        self.gen_bosg_code()
        self.gen_bedef_def_code()

        self.dbc = self.version_code + \
                    "\n" + \
                    self.ns_code + \
                    "\n" + \
                    self.bs_code + \
                    "\n" + \
                    self.bu_code + \
                    "\n" + \
                    self.bosg_code + \
                    "\n" + \
                    self.bedef_def_code + \
                    "\n"
                    
    def get_signal_error_info(self):
        return self.fatal_error_info_signal

    def get_msg_error_info(self):
        return self.fatal_error_info_msg

    def get_dbc(self):
        self.initial_out_info()
        self.gen_dbc_content()
        return self.dbc


class FileHandle(object):
    def set_file_path(self, path=""):
        self.path = path


    def set_file_name(self, _name=""):
        self._name = _name


    def write_dbc(self, dbc=""):
        with open(os.path.join(self.path, self._name), "w") as f:
            f.write(dbc)
            f.close()


if __name__ == "__main__":
    
    xlsxname  = r"D:\Yun\Codes\Python\DBConvertor\can.xlsx"
    password = ''

    exceldataextract = ExcelDataExtract()
    exceldatahandle  = ExcelDataHandle()

    exceldataextract.read_excel(xlsxname, password)
    exceldatahandle.handle_data(exceldataextract.all_sheet_content)

    print('\n'.join(exceldatahandle.error_messages))

