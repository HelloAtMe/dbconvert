# -*- coding: utf-8 -*-
"""
@ File         : setting_handle.py
@ Author       : Wcy
@ Contact      : 
@ Date         : 2021-12-21 10:33:11
@ Description  : 
"""

import json
import os, sys

'''
{
    Configure Style : "Auto", "Manual",
    Table Configure : {
        "MsgName" : 0,
        "MsgID" : 0,
        "MsgCycleTime" : 0,
        "MsgLen" : 0,
        "SignalName":0,
        "ByteOrder":0,
        "StartBit":0,
        "BitLen":0,
        "Resolution":0,
        "Offset":0,
        "Maxv":0,
        "Minv":0,
        "Unit":0,
    }
}
'''

SETTING = os.path.join(os.path.abspath(sys.path[0]), 'setting.json')

def initial_setting():
    with open(SETTING, 'w', encoding='utf-8') as f:
        setting_configure = {
            'Configure Style' : "Auto",
            'Table Configure' : {
                "MsgName" : 0,
                "MsgID" : 0,
                "MsgCycleTime" : 0,
                "MsgLen" : 0,
                "SignalName" : 0,
                "ByteOrder" : 0,
                "StartBit" : 0,
                "BitLen" : 0,
                "Resolution" : 0,
                "Offset" : 0,
                "Maxv" : 0,
                "Minv" : 0,
                "Unit" : 0,
            }
        }
        json.dump(setting_configure, f, ensure_ascii=True, indent=4)


def read_setting():
    with open(SETTING, 'r', encoding='utf-8') as f:
        setting_configure = json.load(f)

    return setting_configure


def write_setting(setting_configure:dict) -> None:
    with open(SETTING, 'w', encoding='utf-8') as f:
        json.dump(setting_configure, f, ensure_ascii=True, indent=4)