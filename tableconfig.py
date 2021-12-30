# -*- coding: utf-8 -*-
'''
@ File         : tableconfig.py
@ Project      : 
@ Author       : 
@ Contact      : 
@ Date         : 2021-12-21 10:36:09
@ Description  : 
'''

import os, sys
from tkinter import *
from tkinter import ttk

# wing import
# ===================================================

# ===================================================


class TableConfigGui(Toplevel):
    def _create(self):
        # ========================= create image code =========================
        
        # ========================= create widget code ========================
        self.WindowWidth   = 317
        self.WindowHeight  = 557
        self.WindowX       = int((self.winfo_screenwidth() - self.WindowWidth)*0.5)
        self.WindowY       = int((self.winfo_screenheight() - self.WindowHeight)*0.3)
        
        self.title('表头配置')
        self.geometry(
            '{}x{}+{}+{}'.format(
                self.WindowWidth, 
                self.WindowHeight,
                self.WindowX,
                self.WindowY
            )
        )
        self.resizable(False, False)
        self.TopFrame = Frame(self, background='#ECECEC')
        self.Label10 = Label(
            self.TopFrame,
            textvariable    = self.Label10Label,
            image           = '',
            compound        = 'center',
            cursor          = 'arrow',
            takefocus       = False,
            foreground      = '#000000',
            background      = '#ECECEC',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            anchor          = 'center',
            justify         = 'center',
            relief          = 'flat'
        )
        self.Label08 = Label(
            self.TopFrame,
            textvariable    = self.Label08Label,
            image           = '',
            compound        = 'center',
            cursor          = 'arrow',
            takefocus       = False,
            foreground      = '#000000',
            background      = '#ECECEC',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            anchor          = 'center',
            justify         = 'center',
            relief          = 'flat'
        )
        self.EntryByteOrder = Entry(
            self.TopFrame,
            textvariable    = self.EntryByteOrderValue,
            show            = '',
            state           = 'normal',
            exportselection = True,
            cursor          = 'xterm',
            takefocus       = True,
            foreground      = '#000000',
            background      = '#FFFFFF',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            justify         = 'center',
            relief          = 'flat'
        )
        self.Label09 = Label(
            self.TopFrame,
            textvariable    = self.Label09Label,
            image           = '',
            compound        = 'center',
            cursor          = 'arrow',
            takefocus       = False,
            foreground      = '#000000',
            background      = '#ECECEC',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            anchor          = 'center',
            justify         = 'center',
            relief          = 'flat'
        )
        self.Label12 = Label(
            self.TopFrame,
            textvariable    = self.Label12Label,
            image           = '',
            compound        = 'center',
            cursor          = 'arrow',
            takefocus       = False,
            foreground      = '#000000',
            background      = '#ECECEC',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            anchor          = 'center',
            justify         = 'center',
            relief          = 'flat'
        )
        self.Label04 = Label(
            self.TopFrame,
            textvariable    = self.Label04Label,
            image           = '',
            compound        = 'center',
            cursor          = 'arrow',
            takefocus       = False,
            foreground      = '#000000',
            background      = '#ECECEC',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            anchor          = 'center',
            justify         = 'center',
            relief          = 'flat'
        )
        self.EntryStartBit = Entry(
            self.TopFrame,
            textvariable    = self.EntryStartBitValue,
            show            = '',
            state           = 'normal',
            exportselection = True,
            cursor          = 'xterm',
            takefocus       = True,
            foreground      = '#000000',
            background      = '#FFFFFF',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            justify         = 'center',
            relief          = 'flat'
        )
        self.EntryMsgLen = Entry(
            self.TopFrame,
            textvariable    = self.EntryMsgLenValue,
            show            = '',
            state           = 'normal',
            exportselection = True,
            cursor          = 'xterm',
            takefocus       = True,
            foreground      = '#000000',
            background      = '#FFFFFF',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            justify         = 'center',
            relief          = 'flat'
        )
        self.Label13 = Label(
            self.TopFrame,
            textvariable    = self.Label13Label,
            image           = '',
            compound        = 'center',
            cursor          = 'arrow',
            takefocus       = False,
            foreground      = '#000000',
            background      = '#ECECEC',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            anchor          = 'center',
            justify         = 'center',
            relief          = 'flat'
        )
        self.EntryMsgName = Entry(
            self.TopFrame,
            textvariable    = self.EntryMsgNameValue,
            show            = '',
            state           = 'normal',
            exportselection = True,
            cursor          = 'xterm',
            takefocus       = True,
            foreground      = '#000000',
            background      = '#FFFFFF',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            justify         = 'center',
            relief          = 'flat'
        )
        self.Label14 = Label(
            self.TopFrame,
            textvariable    = self.Label14Label,
            image           = '',
            compound        = 'center',
            cursor          = 'arrow',
            takefocus       = False,
            foreground      = '#000000',
            background      = '#ECECEC',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            anchor          = 'center',
            justify         = 'center',
            relief          = 'flat'
        )
        self.EntryMinv = Entry(
            self.TopFrame,
            textvariable    = self.EntryMinvValue,
            show            = '',
            state           = 'normal',
            exportselection = True,
            cursor          = 'xterm',
            takefocus       = True,
            foreground      = '#000000',
            background      = '#FFFFFF',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            justify         = 'center',
            relief          = 'flat'
        )
        self.EntrySignalName = Entry(
            self.TopFrame,
            textvariable    = self.EntrySignalNameValue,
            show            = '',
            state           = 'normal',
            exportselection = True,
            cursor          = 'xterm',
            takefocus       = True,
            foreground      = '#000000',
            background      = '#FFFFFF',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            justify         = 'center',
            relief          = 'flat'
        )
        self.Label02 = Label(
            self.TopFrame,
            textvariable    = self.Label02Label,
            image           = '',
            compound        = 'center',
            cursor          = 'arrow',
            takefocus       = False,
            foreground      = '#000000',
            background      = '#ECECEC',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            anchor          = 'center',
            justify         = 'center',
            relief          = 'flat'
        )
        self.style.configure(
            'ButtonTableCancel.TButton',
            foreground      = '#000000',
            background      = '#ECECEC',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            anchor          = 'center',
            justify         = 'center',
            relief          = 'raised'
        )
        self.ButtonTableCancel = ttk.Button( 
            self.TopFrame,
            textvariable    = self.ButtonTableCancelLabel,
            image           = '',
            compound        = 'center',
            cursor          = 'hand2',
            takefocus       = True,
            command         = self.ButtonTableCancel_buttoncommand,
            style           = 'ButtonTableCancel.TButton'
        )
        self.Label05 = Label(
            self.TopFrame,
            textvariable    = self.Label05Label,
            image           = '',
            compound        = 'center',
            cursor          = 'arrow',
            takefocus       = False,
            foreground      = '#000000',
            background      = '#ECECEC',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            anchor          = 'center',
            justify         = 'center',
            relief          = 'flat'
        )
        self.EntryMsgCycleTime = Entry(
            self.TopFrame,
            textvariable    = self.EntryMsgCycleTimeValue,
            show            = '',
            state           = 'normal',
            exportselection = True,
            cursor          = 'xterm',
            takefocus       = True,
            foreground      = '#000000',
            background      = '#FFFFFF',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            justify         = 'center',
            relief          = 'flat'
        )
        self.Label07 = Label(
            self.TopFrame,
            textvariable    = self.Label07Label,
            image           = '',
            compound        = 'center',
            cursor          = 'arrow',
            takefocus       = False,
            foreground      = '#000000',
            background      = '#ECECEC',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            anchor          = 'center',
            justify         = 'center',
            relief          = 'flat'
        )
        self.EntryMaxv = Entry(
            self.TopFrame,
            textvariable    = self.EntryMaxvValue,
            show            = '',
            state           = 'normal',
            exportselection = True,
            cursor          = 'xterm',
            takefocus       = True,
            foreground      = '#000000',
            background      = '#FFFFFF',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            justify         = 'center',
            relief          = 'flat'
        )
        self.Label11 = Label(
            self.TopFrame,
            textvariable    = self.Label11Label,
            image           = '',
            compound        = 'center',
            cursor          = 'arrow',
            takefocus       = False,
            foreground      = '#000000',
            background      = '#ECECEC',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            anchor          = 'center',
            justify         = 'center',
            relief          = 'flat'
        )
        self.EntryBitLen = Entry(
            self.TopFrame,
            textvariable    = self.EntryBitLenValue,
            show            = '',
            state           = 'normal',
            exportselection = True,
            cursor          = 'xterm',
            takefocus       = True,
            foreground      = '#000000',
            background      = '#FFFFFF',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            justify         = 'center',
            relief          = 'flat'
        )
        self.EntryUnit = Entry(
            self.TopFrame,
            textvariable    = self.EntryUnitValue,
            show            = '',
            state           = 'normal',
            exportselection = True,
            cursor          = 'xterm',
            takefocus       = True,
            foreground      = '#000000',
            background      = '#FFFFFF',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            justify         = 'center',
            relief          = 'flat'
        )
        self.EntryMsgID = Entry(
            self.TopFrame,
            textvariable    = self.EntryMsgIDValue,
            show            = '',
            state           = 'normal',
            exportselection = True,
            cursor          = 'xterm',
            takefocus       = True,
            foreground      = '#000000',
            background      = '#FFFFFF',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            justify         = 'center',
            relief          = 'flat'
        )
        self.EntryResolution = Entry(
            self.TopFrame,
            textvariable    = self.EntryResolutionValue,
            show            = '',
            state           = 'normal',
            exportselection = True,
            cursor          = 'xterm',
            takefocus       = True,
            foreground      = '#000000',
            background      = '#FFFFFF',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            justify         = 'center',
            relief          = 'flat'
        )
        self.style.configure(
            'ButtonTableOk.TButton',
            foreground      = '#000000',
            background      = '#ECECEC',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            anchor          = 'center',
            justify         = 'center',
            relief          = 'raised'
        )
        self.ButtonTableOk = ttk.Button( 
            self.TopFrame,
            textvariable    = self.ButtonTableOkLabel,
            image           = '',
            compound        = 'center',
            cursor          = 'hand2',
            takefocus       = True,
            command         = self.ButtonTableOk_buttoncommand,
            style           = 'ButtonTableOk.TButton'
        )
        self.EntryOffset = Entry(
            self.TopFrame,
            textvariable    = self.EntryOffsetValue,
            show            = '',
            state           = 'normal',
            exportselection = True,
            cursor          = 'xterm',
            takefocus       = True,
            foreground      = '#000000',
            background      = '#FFFFFF',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            justify         = 'center',
            relief          = 'flat'
        )
        self.Label03 = Label(
            self.TopFrame,
            textvariable    = self.Label03Label,
            image           = '',
            compound        = 'center',
            cursor          = 'arrow',
            takefocus       = False,
            foreground      = '#000000',
            background      = '#ECECEC',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            anchor          = 'center',
            justify         = 'center',
            relief          = 'flat'
        )
        self.Label06 = Label(
            self.TopFrame,
            textvariable    = self.Label06Label,
            image           = '',
            compound        = 'center',
            cursor          = 'arrow',
            takefocus       = False,
            foreground      = '#000000',
            background      = '#ECECEC',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            anchor          = 'center',
            justify         = 'center',
            relief          = 'flat'
        )
        
        # ========================= create bind code ==========================
        self.protocol('WM_DELETE_WINDOW', self.quit_window_command)


    def _lay(self):
        self.TopFrame.place(
            relx=0, 
            rely=0, 
            relwidth=1, 
            relheight=1, 
            anchor='nw'
        )
        self.Label10.place(
            x      = self.Label10_x,
            y      = self.Label10_y,
            width  = self.Label10_w,
            height = self.Label10_h,
            anchor = 'nw'
        )
        self.Label08.place(
            x      = self.Label08_x,
            y      = self.Label08_y,
            width  = self.Label08_w,
            height = self.Label08_h,
            anchor = 'nw'
        )
        self.EntryByteOrder.place(
            x      = self.EntryByteOrder_x,
            y      = self.EntryByteOrder_y,
            width  = self.EntryByteOrder_w,
            height = self.EntryByteOrder_h,
            anchor = 'nw'
        )
        self.Label09.place(
            x      = self.Label09_x,
            y      = self.Label09_y,
            width  = self.Label09_w,
            height = self.Label09_h,
            anchor = 'nw'
        )
        self.Label12.place(
            x      = self.Label12_x,
            y      = self.Label12_y,
            width  = self.Label12_w,
            height = self.Label12_h,
            anchor = 'nw'
        )
        self.Label04.place(
            x      = self.Label04_x,
            y      = self.Label04_y,
            width  = self.Label04_w,
            height = self.Label04_h,
            anchor = 'nw'
        )
        self.EntryStartBit.place(
            x      = self.EntryStartBit_x,
            y      = self.EntryStartBit_y,
            width  = self.EntryStartBit_w,
            height = self.EntryStartBit_h,
            anchor = 'nw'
        )
        self.EntryMsgLen.place(
            x      = self.EntryMsgLen_x,
            y      = self.EntryMsgLen_y,
            width  = self.EntryMsgLen_w,
            height = self.EntryMsgLen_h,
            anchor = 'nw'
        )
        self.Label13.place(
            x      = self.Label13_x,
            y      = self.Label13_y,
            width  = self.Label13_w,
            height = self.Label13_h,
            anchor = 'nw'
        )
        self.EntryMsgName.place(
            x      = self.EntryMsgName_x,
            y      = self.EntryMsgName_y,
            width  = self.EntryMsgName_w,
            height = self.EntryMsgName_h,
            anchor = 'nw'
        )
        self.Label14.place(
            x      = self.Label14_x,
            y      = self.Label14_y,
            width  = self.Label14_w,
            height = self.Label14_h,
            anchor = 'nw'
        )
        self.EntryMinv.place(
            x      = self.EntryMinv_x,
            y      = self.EntryMinv_y,
            width  = self.EntryMinv_w,
            height = self.EntryMinv_h,
            anchor = 'nw'
        )
        self.EntrySignalName.place(
            x      = self.EntrySignalName_x,
            y      = self.EntrySignalName_y,
            width  = self.EntrySignalName_w,
            height = self.EntrySignalName_h,
            anchor = 'nw'
        )
        self.Label02.place(
            x      = self.Label02_x,
            y      = self.Label02_y,
            width  = self.Label02_w,
            height = self.Label02_h,
            anchor = 'nw'
        )
        self.ButtonTableCancel.place(
            x      = self.ButtonTableCancel_x,
            y      = self.ButtonTableCancel_y,
            width  = self.ButtonTableCancel_w,
            height = self.ButtonTableCancel_h,
            anchor = 'nw'
        )
        self.Label05.place(
            x      = self.Label05_x,
            y      = self.Label05_y,
            width  = self.Label05_w,
            height = self.Label05_h,
            anchor = 'nw'
        )
        self.EntryMsgCycleTime.place(
            x      = self.EntryMsgCycleTime_x,
            y      = self.EntryMsgCycleTime_y,
            width  = self.EntryMsgCycleTime_w,
            height = self.EntryMsgCycleTime_h,
            anchor = 'nw'
        )
        self.Label07.place(
            x      = self.Label07_x,
            y      = self.Label07_y,
            width  = self.Label07_w,
            height = self.Label07_h,
            anchor = 'nw'
        )
        self.EntryMaxv.place(
            x      = self.EntryMaxv_x,
            y      = self.EntryMaxv_y,
            width  = self.EntryMaxv_w,
            height = self.EntryMaxv_h,
            anchor = 'nw'
        )
        self.Label11.place(
            x      = self.Label11_x,
            y      = self.Label11_y,
            width  = self.Label11_w,
            height = self.Label11_h,
            anchor = 'nw'
        )
        self.EntryBitLen.place(
            x      = self.EntryBitLen_x,
            y      = self.EntryBitLen_y,
            width  = self.EntryBitLen_w,
            height = self.EntryBitLen_h,
            anchor = 'nw'
        )
        self.EntryUnit.place(
            x      = self.EntryUnit_x,
            y      = self.EntryUnit_y,
            width  = self.EntryUnit_w,
            height = self.EntryUnit_h,
            anchor = 'nw'
        )
        self.EntryMsgID.place(
            x      = self.EntryMsgID_x,
            y      = self.EntryMsgID_y,
            width  = self.EntryMsgID_w,
            height = self.EntryMsgID_h,
            anchor = 'nw'
        )
        self.EntryResolution.place(
            x      = self.EntryResolution_x,
            y      = self.EntryResolution_y,
            width  = self.EntryResolution_w,
            height = self.EntryResolution_h,
            anchor = 'nw'
        )
        self.ButtonTableOk.place(
            x      = self.ButtonTableOk_x,
            y      = self.ButtonTableOk_y,
            width  = self.ButtonTableOk_w,
            height = self.ButtonTableOk_h,
            anchor = 'nw'
        )
        self.EntryOffset.place(
            x      = self.EntryOffset_x,
            y      = self.EntryOffset_y,
            width  = self.EntryOffset_w,
            height = self.EntryOffset_h,
            anchor = 'nw'
        )
        self.Label03.place(
            x      = self.Label03_x,
            y      = self.Label03_y,
            width  = self.Label03_w,
            height = self.Label03_h,
            anchor = 'nw'
        )
        self.Label06.place(
            x      = self.Label06_x,
            y      = self.Label06_y,
            width  = self.Label06_w,
            height = self.Label06_h,
            anchor = 'nw'
        )


    def _size(self):
        self.Label10_x = 5
        self.Label10_y = 314
        self.Label10_w = 150
        self.Label10_h = 30
        self.Label08_x = 5
        self.Label08_y = 240
        self.Label08_w = 150
        self.Label08_h = 30
        self.EntryByteOrder_x = 160
        self.EntryByteOrder_y = 203
        self.EntryByteOrder_w = 150
        self.EntryByteOrder_h = 30
        self.Label09_x = 4
        self.Label09_y = 277
        self.Label09_w = 150
        self.Label09_h = 30
        self.Label12_x = 5
        self.Label12_y = 388
        self.Label12_w = 150
        self.Label12_h = 30
        self.Label04_x = 5
        self.Label04_y = 92
        self.Label04_w = 150
        self.Label04_h = 30
        self.EntryStartBit_x = 160
        self.EntryStartBit_y = 240
        self.EntryStartBit_w = 150
        self.EntryStartBit_h = 30
        self.EntryMsgLen_x = 160
        self.EntryMsgLen_y = 129
        self.EntryMsgLen_w = 150
        self.EntryMsgLen_h = 30
        self.Label13_x = 5
        self.Label13_y = 351
        self.Label13_w = 150
        self.Label13_h = 30
        self.EntryMsgName_x = 160
        self.EntryMsgName_y = 18
        self.EntryMsgName_w = 150
        self.EntryMsgName_h = 30
        self.Label14_x = 5
        self.Label14_y = 462
        self.Label14_w = 150
        self.Label14_h = 30
        self.EntryMinv_x = 160
        self.EntryMinv_y = 425
        self.EntryMinv_w = 150
        self.EntryMinv_h = 30
        self.EntrySignalName_x = 160
        self.EntrySignalName_y = 166
        self.EntrySignalName_w = 150
        self.EntrySignalName_h = 30
        self.Label02_x = 5
        self.Label02_y = 18
        self.Label02_w = 150
        self.Label02_h = 30
        self.ButtonTableCancel_x = 180
        self.ButtonTableCancel_y = 515
        self.ButtonTableCancel_w = 100
        self.ButtonTableCancel_h = 30
        self.Label05_x = 5
        self.Label05_y = 129
        self.Label05_w = 150
        self.Label05_h = 30
        self.EntryMsgCycleTime_x = 160
        self.EntryMsgCycleTime_y = 92
        self.EntryMsgCycleTime_w = 150
        self.EntryMsgCycleTime_h = 30
        self.Label07_x = 5
        self.Label07_y = 203
        self.Label07_w = 150
        self.Label07_h = 30
        self.EntryMaxv_x = 160
        self.EntryMaxv_y = 388
        self.EntryMaxv_w = 150
        self.EntryMaxv_h = 30
        self.Label11_x = 5
        self.Label11_y = 425
        self.Label11_w = 150
        self.Label11_h = 30
        self.EntryBitLen_x = 160
        self.EntryBitLen_y = 277
        self.EntryBitLen_w = 150
        self.EntryBitLen_h = 30
        self.EntryUnit_x = 160
        self.EntryUnit_y = 462
        self.EntryUnit_w = 150
        self.EntryUnit_h = 30
        self.EntryMsgID_x = 160
        self.EntryMsgID_y = 55
        self.EntryMsgID_w = 150
        self.EntryMsgID_h = 30
        self.EntryResolution_x = 160
        self.EntryResolution_y = 314
        self.EntryResolution_w = 150
        self.EntryResolution_h = 30
        self.ButtonTableOk_x = 45
        self.ButtonTableOk_y = 515
        self.ButtonTableOk_w = 100
        self.ButtonTableOk_h = 30
        self.EntryOffset_x = 160
        self.EntryOffset_y = 351
        self.EntryOffset_w = 150
        self.EntryOffset_h = 30
        self.Label03_x = 5
        self.Label03_y = 55
        self.Label03_w = 150
        self.Label03_h = 30
        self.Label06_x = 5
        self.Label06_y = 166
        self.Label06_w = 150
        self.Label06_h = 30


class TableConfigEvent(TableConfigGui):
    def __init__(self, master):
        super().__init__(master)
        self.style = master.style
        # appearance variables
        self.Label10Label   = StringVar(value='精度')
        self.Label08Label   = StringVar(value='起始位')
        self.EntryByteOrderValue   = StringVar(value='')
        self.Label09Label   = StringVar(value='信号长度')
        self.Label12Label   = StringVar(value='最大值')
        self.Label04Label   = StringVar(value='报文周期时间')
        self.EntryStartBitValue   = StringVar(value='')
        self.EntryMsgLenValue   = StringVar(value='')
        self.Label13Label   = StringVar(value='偏移量')
        self.EntryMsgNameValue   = StringVar(value='')
        self.Label14Label   = StringVar(value='单位')
        self.EntryMinvValue   = StringVar(value='')
        self.EntrySignalNameValue   = StringVar(value='')
        self.Label02Label   = StringVar(value='报文名称')
        self.ButtonTableCancelLabel = StringVar(value='取  消')
        self.Label05Label   = StringVar(value='报文长度')
        self.EntryMsgCycleTimeValue   = StringVar(value='')
        self.Label07Label   = StringVar(value='排列格式')
        self.EntryMaxvValue   = StringVar(value='')
        self.Label11Label   = StringVar(value='最小值')
        self.EntryBitLenValue   = StringVar(value='')
        self.EntryUnitValue   = StringVar(value='')
        self.EntryMsgIDValue   = StringVar(value='')
        self.EntryResolutionValue   = StringVar(value='')
        self.ButtonTableOkLabel = StringVar(value='确  认')
        self.EntryOffsetValue   = StringVar(value='')
        self.Label03Label   = StringVar(value='报文标识符')
        self.Label06Label   = StringVar(value='信号名称')
        self._create()
        # wing initial
        # ===================================================
        
        self.EntryMsgNameValue.set(value=self.master.setting_configure['Table Configure']['MsgName'])
        self.EntryMsgIDValue.set(value=self.master.setting_configure['Table Configure']['MsgID'])
        self.EntryMsgCycleTimeValue.set(value=self.master.setting_configure['Table Configure']['MsgCycleTime'])
        self.EntryMsgLenValue.set(value=self.master.setting_configure['Table Configure']['MsgLen'])
        self.EntrySignalNameValue.set(value=self.master.setting_configure['Table Configure']['SignalName'])
        self.EntryByteOrderValue.set(value=self.master.setting_configure['Table Configure']['ByteOrder'])
        self.EntryStartBitValue.set(value=self.master.setting_configure['Table Configure']['StartBit'])
        self.EntryBitLenValue.set(value=self.master.setting_configure['Table Configure']['BitLen'])
        self.EntryResolutionValue.set(value=self.master.setting_configure['Table Configure']['Resolution'])
        self.EntryOffsetValue.set(value=self.master.setting_configure['Table Configure']['Offset'])
        self.EntryMaxvValue.set(value=self.master.setting_configure['Table Configure']['Maxv'])
        self.EntryMinvValue.set(value=self.master.setting_configure['Table Configure']['Minv'])
        self.EntryUnitValue.set(value=self.master.setting_configure['Table Configure']['Unit'])

        # ===================================================
        

    def show(self, parameter=None):
        # wing preshow
        # ===================================================
        
        # ===================================================
        self._size()
        self._lay()


    def quit_window_command(self):
        # wing quitcommand
        # ===================================================
        
        # ===================================================
        self.destroy()


    def ButtonTableCancel_buttoncommand(self):
        # wing buttoncommand 584767
        # ===================================================
        self.destroy()
        
        # ===================================================


    def ButtonTableOk_buttoncommand(self):
        # wing buttoncommand 916853
        # ===================================================
        self.master.setting_configure['Table Configure']['MsgName'] = int(self.EntryMsgNameValue.get())
        self.master.setting_configure['Table Configure']['MsgID'] = int(self.EntryMsgIDValue.get())
        self.master.setting_configure['Table Configure']['MsgCycleTime'] = int(self.EntryMsgCycleTimeValue.get())
        self.master.setting_configure['Table Configure']['MsgLen'] = int(self.EntryMsgLenValue.get())
        self.master.setting_configure['Table Configure']['SignalName'] = int(self.EntrySignalNameValue.get())
        self.master.setting_configure['Table Configure']['ByteOrder'] = int(self.EntryByteOrderValue.get())
        self.master.setting_configure['Table Configure']['StartBit'] = int(self.EntryStartBitValue.get())
        self.master.setting_configure['Table Configure']['BitLen'] = int(self.EntryBitLenValue.get())
        self.master.setting_configure['Table Configure']['Resolution'] = int(self.EntryResolutionValue.get())
        self.master.setting_configure['Table Configure']['Offset'] = int(self.EntryOffsetValue.get())
        self.master.setting_configure['Table Configure']['Maxv'] = int(self.EntryMaxvValue.get())
        self.master.setting_configure['Table Configure']['Minv'] = int(self.EntryMinvValue.get())
        self.master.setting_configure['Table Configure']['Unit'] = int(self.EntryUnitValue.get())
        self.destroy()
        # ===================================================
    

    