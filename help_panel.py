# -*- coding: utf-8 -*-
'''
@ File         : Toplevel00.py
@ Project      : 
@ Author       : 
@ Contact      : 
@ Date         : 2022-10-13 14:10:13
@ Description  : 
'''

import os, sys
from tkinter import *
from tkinter import ttk

# wing import
# ===================================================
VERSION_TEXT = 'V10.0.0'
# ===================================================


class HelpPanelGui(Toplevel):
    def _create(self):
        # ========================= create image code =========================
        
        # ========================= create widget code ========================
        self.WindowWidth   = 338
        self.WindowHeight  = 403
        self.WindowX       = int((self.winfo_screenwidth() - self.WindowWidth)*0.5)
        self.WindowY       = int((self.winfo_screenheight() - self.WindowHeight)*0.3)
        
        self.title('Version Information')
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
        self.Label00 = Label(
            self.TopFrame,
            textvariable    = self.Label00Label,
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
        self.Label00.place(
            x      = self.Label00_x,
            y      = self.Label00_y,
            width  = self.Label00_w,
            height = self.Label00_h,
            anchor = 'nw'
        )


    def _size(self):
        self.Label00_x = 14
        self.Label00_y = 20
        self.Label00_w = 310
        self.Label00_h = 362


class HelpPanel(HelpPanelGui):
    def __init__(self, master):
        super().__init__(master)
        self.style = master.style
        # appearance variables
        self.Label00Label   = StringVar(
            value='''Version: {}\n
    Any bugs, contact me at 935716406@qq.com\n

Description: This applicatio is used to 
decode the dbc files from excel.
        '''.format(VERSION_TEXT)
        )
        self._create()
        # wing initial
        # ===================================================
        
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
    

    