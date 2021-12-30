# -*- coding: utf-8 -*-
'''
@ File         : setting.py
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
from tableconfig import TableConfigEvent
from setting_handle import *

# ===================================================


class DBCSettingGui(Toplevel):
    def _create(self):
        # ========================= create image code =========================
        
        # ========================= create widget code ========================
        self.WindowWidth   = 284
        self.WindowHeight  = 227
        self.WindowX       = int((self.winfo_screenwidth() - self.WindowWidth)*0.5)
        self.WindowY       = int((self.winfo_screenheight() - self.WindowHeight)*0.3)
        
        self.title('设置')
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
        self.style.configure(
            'ButtonConfig.TButton',
            foreground      = '#000000',
            background      = '#ECECEC',
            font            = ('Arial', 11, 'normal', 'roman'),
            anchor          = 'center',
            justify         = 'center',
            relief          = 'raised'
        )
        self.ButtonConfig = ttk.Button( 
            self.TopFrame,
            textvariable    = self.ButtonConfigLabel,
            image           = '',
            compound        = 'bottom',
            cursor          = 'hand2',
            takefocus       = True,
            command         = self.ButtonConfig_buttoncommand,
            style           = 'ButtonConfig.TButton'
        )
        self.style.configure(
            'ButtonSettingOk.TButton',
            foreground      = '#000000',
            background      = '#ECECEC',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            anchor          = 'center',
            justify         = 'center',
            relief          = 'raised'
        )
        self.ButtonSettingOk = ttk.Button( 
            self.TopFrame,
            textvariable    = self.ButtonSettingOkLabel,
            image           = '',
            compound        = 'center',
            cursor          = 'hand2',
            takefocus       = True,
            command         = self.ButtonSettingOk_buttoncommand,
            style           = 'ButtonSettingOk.TButton'
        )
        self.style.configure(
            'ButtonSettingCancel.TButton',
            foreground      = '#000000',
            background      = '#ECECEC',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            anchor          = 'center',
            justify         = 'center',
            relief          = 'raised'
        )
        self.ButtonSettingCancel = ttk.Button( 
            self.TopFrame,
            textvariable    = self.ButtonSettingCancelLabel,
            image           = '',
            compound        = 'center',
            cursor          = 'hand2',
            takefocus       = True,
            command         = self.ButtonSettingCancel_buttoncommand,
            style           = 'ButtonSettingCancel.TButton'
        )
        self.Labelframe01 = LabelFrame(
            self.TopFrame,
            text            = '表头配置',
            labelanchor     = 'nw',
            cursor          = 'arrow',
            takefocus       = False,
            foreground      = '#000000',
            background      = '#ECECEC',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            relief          = 'groove'
        )
        self.style.configure(
            'RadiobuttonManual.TRadiobutton',
            foreground      = '#000000',
            background      = '#ECECEC',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            anchor          = 'center',
            justify         = 'center',
            relief          = 'flat'
        )
        self.RadiobuttonManual = ttk.Radiobutton( 
            self.Labelframe01,
            textvariable    = self.RadiobuttonManualLabel,
            variable        = self.ConfigStyleGroup,
            value           = '手动配置',
            image           = '',
            compound        = 'center',
            cursor          = 'arrow',
            takefocus       = True,
            command         = self.RadiobuttonManual_buttoncommand,
            style           = 'RadiobuttonManual.TRadiobutton'
        )
        self.style.configure(
            'RadiobuttonAuto.TRadiobutton',
            foreground      = '#000000',
            background      = '#ECECEC',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            anchor          = 'center',
            justify         = 'center',
            relief          = 'flat'
        )
        self.RadiobuttonAuto = ttk.Radiobutton( 
            self.Labelframe01,
            textvariable    = self.RadiobuttonAutoLabel,
            variable        = self.ConfigStyleGroup,
            value           = '自动配置',
            image           = '',
            compound        = 'center',
            cursor          = 'hand2',
            takefocus       = True,
            command         = self.RadiobuttonAuto_buttoncommand,
            style           = 'RadiobuttonAuto.TRadiobutton'
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
        self.ButtonConfig.place(
            x      = self.ButtonConfig_x,
            y      = self.ButtonConfig_y,
            width  = self.ButtonConfig_w,
            height = self.ButtonConfig_h,
            anchor = 'nw'
        )
        self.ButtonSettingOk.place(
            x      = self.ButtonSettingOk_x,
            y      = self.ButtonSettingOk_y,
            width  = self.ButtonSettingOk_w,
            height = self.ButtonSettingOk_h,
            anchor = 'nw'
        )
        self.ButtonSettingCancel.place(
            x      = self.ButtonSettingCancel_x,
            y      = self.ButtonSettingCancel_y,
            width  = self.ButtonSettingCancel_w,
            height = self.ButtonSettingCancel_h,
            anchor = 'nw'
        )
        self.Labelframe01.place(
            x      = self.Labelframe01_x,
            y      = self.Labelframe01_y,
            width  = self.Labelframe01_w,
            height = self.Labelframe01_h,
            anchor = 'nw'
        )
        self.RadiobuttonManual.place(
            x      = self.RadiobuttonManual_x,
            y      = self.RadiobuttonManual_y,
            width  = self.RadiobuttonManual_w,
            height = self.RadiobuttonManual_h,
            anchor = 'nw'
        )
        self.RadiobuttonAuto.place(
            x      = self.RadiobuttonAuto_x,
            y      = self.RadiobuttonAuto_y,
            width  = self.RadiobuttonAuto_w,
            height = self.RadiobuttonAuto_h,
            anchor = 'nw'
        )


    def _size(self):
        self.ButtonConfig_x = 194
        self.ButtonConfig_y = 34
        self.ButtonConfig_w = 70
        self.ButtonConfig_h = 30
        self.ButtonSettingOk_x = 28
        self.ButtonSettingOk_y = 169
        self.ButtonSettingOk_w = 100
        self.ButtonSettingOk_h = 30
        self.ButtonSettingCancel_x = 156
        self.ButtonSettingCancel_y = 169
        self.ButtonSettingCancel_w = 100
        self.ButtonSettingCancel_h = 30
        self.Labelframe01_x = 23
        self.Labelframe01_y = 15
        self.Labelframe01_w = 150
        self.Labelframe01_h = 100
        self.RadiobuttonManual_x = 17
        self.RadiobuttonManual_y = 9
        self.RadiobuttonManual_w = 100
        self.RadiobuttonManual_h = 30
        self.RadiobuttonAuto_x = 17
        self.RadiobuttonAuto_y = 44
        self.RadiobuttonAuto_w = 100
        self.RadiobuttonAuto_h = 34


class DBCSettingEvent(DBCSettingGui):
    def __init__(self, master):
        super().__init__(master)
        self.style = master.style
        # appearance variables
        self.ButtonConfigLabel = StringVar(value='配  置')
        self.ButtonSettingOkLabel = StringVar(value='确  认')
        self.ButtonSettingCancelLabel = StringVar(value='取  消')
        self.RadiobuttonManualLabel   = StringVar(value='手动配置')
        self.ConfigStyleGroup  = StringVar(value='自动配置')
        self.RadiobuttonAutoLabel   = StringVar(value='自动配置')
        self._create()
        # wing initial
        # ===================================================
        self.setting_configure = master.setting_configure

        if self.setting_configure.get('Configure Style') == 'Auto':
            self.ButtonConfig.configure(state='disabled')
            self.ConfigStyleGroup.set(value='自动配置')
        elif self.setting_configure.get('Configure Style') == 'Manual':
            self.ButtonConfig.configure(state='normal')
            self.ConfigStyleGroup.set(value='手动配置')
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


    def ButtonConfig_buttoncommand(self):
        # wing buttoncommand 705523
        # ===================================================
        TableConfigEvent(self).show()
        
        # ===================================================


    def ButtonSettingOk_buttoncommand(self):
        # wing buttoncommand 715113
        # ===================================================
        self.master.setting_configure = self.setting_configure
        # write_setting(self.setting_configure)
        self.destroy()
        
        # ===================================================


    def ButtonSettingCancel_buttoncommand(self):
        # wing buttoncommand 984778
        # ===================================================
        self.destroy()
        
        # ===================================================


    def RadiobuttonManual_buttoncommand(self):
        # wing buttoncommand 478918
        # ===================================================
        if self.ConfigStyleGroup.get() == '自动配置':
            self.setting_configure['Configure Style'] = 'Auto'
            self.ButtonConfig.configure(state='disabled')
        elif self.ConfigStyleGroup.get() == '手动配置':
            self.setting_configure['Configure Style'] = 'Manual'
            self.ButtonConfig.configure(state='normal')

        # ===================================================


    def RadiobuttonAuto_buttoncommand(self):
        # wing buttoncommand 729833
        # ===================================================
        if self.ConfigStyleGroup.get() == '自动配置':
            self.setting_configure['Configure Style'] = 'Auto'
            self.ButtonConfig.configure(state='disabled')
        elif self.ConfigStyleGroup.get() == '手动配置':
            self.setting_configure['Configure Style'] = 'Manual'
            self.ButtonConfig.configure(state='normal')
        
        # ===================================================
    

    