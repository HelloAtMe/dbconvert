# -*- coding: utf-8 -*-
'''
@ File         : dbconvert.py
@ Project      : 
@ Author       : 
@ Contact      : 
@ Date         : 2021-12-13 17:01:28
@ Description  : 
'''

import os, sys
from tkinter import *
from tkinter import ttk

# wing import
# ===================================================

# ===================================================


class DBConvertorGui(Tk):
    def _create(self):
        self.style = ttk.Style()
        # For Fix Bug Treeview can't change the color in Windows OS.
        self.style.map(
            "Treeview",
            foreground=self._bugfix_style_map("foreground"),
            background=self._bugfix_style_map("background")
        )
        # ========================= create image code =========================
        
        # ========================= create widget code ========================
        self.WindowWidth   = 800
        self.WindowHeight  = 321
        self.WindowX       = int((self.winfo_screenwidth() - self.WindowWidth)*0.5)
        self.WindowY       = int((self.winfo_screenheight() - self.WindowHeight)*0.3)
        
        self.title('DBConvertor')
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
        # Create Menu 
        self.main_menubar = Menu(self)
        self.menu_cascade_File = Menu(self.main_menubar, tearoff=0)
        self.menu_cascade_File.add_command(label='Inport', command=self.menu_command_Inport_menucommand, accelerator='')
        self.menu_cascade_File.add_separator()
        self.menu_cascade_File.add_command(label='Exit', command=self.menu_command_02_menucommand, accelerator='')
        self.main_menubar.add_cascade(label='File', menu=self.menu_cascade_File)
        self.menu_cascade_Edit = Menu(self.main_menubar, tearoff=0)
        self.menu_cascade_Edit.add_command(label='Start', command=self.menu_command_Start_menucommand, accelerator='')
        self.menu_cascade_Edit.add_command(label='Setting', command=self.menu_command_Setting_menucommand, accelerator='')
        self.main_menubar.add_cascade(label='Edit', menu=self.menu_cascade_Edit)
        self.menu_cascade_Help = Menu(self.main_menubar, tearoff=0)
        self.main_menubar.add_cascade(label='Help', menu=self.menu_cascade_Help)
        self.configure(menu=self.main_menubar)
        
        self.Labelframe00 = LabelFrame(
            self.TopFrame,
            text            = '转换日志',
            labelanchor     = 'nw',
            cursor          = 'arrow',
            takefocus       = False,
            foreground      = '#000000',
            background      = '#ECECEC',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            relief          = 'groove'
        )
        self.style.configure(
            'ButtonConvert.TButton',
            foreground      = '#000000',
            background      = '#ECECEC',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            anchor          = 'center',
            justify         = 'center',
            relief          = 'raised'
        )
        self.ButtonConvert = ttk.Button( 
            self.TopFrame,
            textvariable    = self.ButtonConvertLabel,
            image           = '',
            compound        = 'center',
            cursor          = 'hand2',
            takefocus       = True,
            command         = self.ButtonConvert_buttoncommand,
            style           = 'ButtonConvert.TButton'
        )
        self.style.configure(
            'CheckbuttonShowPwdFlag.TCheckbutton',
            foreground      = '#000000',
            background      = '#ECECEC',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            anchor          = 'center',
            justify         = 'center',
            relief          = 'flat'
        )
        self.CheckbuttonShowPwdFlag = ttk.Checkbutton( 
            self.TopFrame,
            textvariable    = self.CheckbuttonShowPwdFlagLabel,
            variable        = self.CheckbuttonShowPwdFlagValue,
            offvalue        = False,
            onvalue         = True,
            image           = '',
            compound        = 'center',
            cursor          = 'hand2',
            takefocus       = True,
            command         = self.CheckbuttonShowPwdFlag_buttoncommand,
            style           = 'CheckbuttonShowPwdFlag.TCheckbutton'
        )
        self.EntryPassword = Entry(
            self.TopFrame,
            textvariable    = self.EntryPasswordValue,
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
        self.TextExcelPath = Text(
            self.TopFrame,
            wrap            = 'none',
            cursor          = 'arrow',
            takefocus       = True,
            foreground      = '#000000',
            background      = '#FFFFFF',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            relief          = 'flat'
        )
        self.Label01 = Label(
            self.TopFrame,
            textvariable    = self.Label01Label,
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
        self.ListboxLog = Listbox( 
            self.Labelframe00,
            listvariable    = self.ListboxLogListValues,
            exportselection = True,
            selectmode      = 'browse',
            cursor          = 'arrow',
            takefocus       = True,
            foreground      = '#000000',
            background      = '#ECECEC',
            font            = ('Fixdsys', 9, 'normal', 'roman'),
            justify         = 'center',
            relief          = 'flat'
        )
        self.ListboxLog_scrollbar_vertical   = ttk.Scrollbar(
            self.Labelframe00,
            orient='vertical',
            command=self.ListboxLog.yview
        )
        self.ListboxLog.configure(yscrollcommand=self.ListboxLog_scrollbar_vertical.set)
        
        # ========================= create bind code ==========================
        self.protocol('WM_DELETE_WINDOW', self.quit_window_command)
        self.ListboxLog.bind(
            '<MouseWheel>', 
            lambda event:self.ListboxLog.yview_scroll(int(-0.01*event.delta), 'units')
        )


    def _lay(self):
        self.TopFrame.place(
            relx=0, 
            rely=0, 
            relwidth=1, 
            relheight=1, 
            anchor='nw'
        )
        self.Labelframe00.place(
            x      = self.Labelframe00_x,
            y      = self.Labelframe00_y,
            width  = self.Labelframe00_w,
            height = self.Labelframe00_h,
            anchor = 'nw'
        )
        self.ButtonConvert.place(
            x      = self.ButtonConvert_x,
            y      = self.ButtonConvert_y,
            width  = self.ButtonConvert_w,
            height = self.ButtonConvert_h,
            anchor = 'nw'
        )
        self.CheckbuttonShowPwdFlag.place(
            x      = self.CheckbuttonShowPwdFlag_x,
            y      = self.CheckbuttonShowPwdFlag_y,
            width  = self.CheckbuttonShowPwdFlag_w,
            height = self.CheckbuttonShowPwdFlag_h,
            anchor = 'nw'
        )
        self.EntryPassword.place(
            x      = self.EntryPassword_x,
            y      = self.EntryPassword_y,
            width  = self.EntryPassword_w,
            height = self.EntryPassword_h,
            anchor = 'nw'
        )
        self.TextExcelPath.place(
            x      = self.TextExcelPath_x,
            y      = self.TextExcelPath_y,
            width  = self.TextExcelPath_w,
            height = self.TextExcelPath_h,
            anchor = 'nw'
        )
        self.Label01.place(
            x      = self.Label01_x,
            y      = self.Label01_y,
            width  = self.Label01_w,
            height = self.Label01_h,
            anchor = 'nw'
        )
        self.Label00.place(
            x      = self.Label00_x,
            y      = self.Label00_y,
            width  = self.Label00_w,
            height = self.Label00_h,
            anchor = 'nw'
        )
        self.ListboxLog.place(
            x      = self.ListboxLog_x,
            y      = self.ListboxLog_y,
            width  = self.ListboxLog_w,
            height = self.ListboxLog_h,
            anchor = 'nw'
        )
        self.ListboxLog_scrollbar_vertical.place(
            x      = self.ListboxLog_scrollbar_vertical_x,
            y      = self.ListboxLog_scrollbar_vertical_y,
            width  = self.ListboxLog_scrollbar_vertical_w,
            height = self.ListboxLog_scrollbar_vertical_h,
            anchor = 'nw'
        )


    def _size(self):
        self.Labelframe00_x = 300
        self.Labelframe00_y = 0
        self.Labelframe00_w = 500
        self.Labelframe00_h = 320
        self.ButtonConvert_x = 75
        self.ButtonConvert_y = 280
        self.ButtonConvert_w = 150
        self.ButtonConvert_h = 30
        self.CheckbuttonShowPwdFlag_x = 108
        self.CheckbuttonShowPwdFlag_y = 200
        self.CheckbuttonShowPwdFlag_w = 100
        self.CheckbuttonShowPwdFlag_h = 30
        self.EntryPassword_x = 5
        self.EntryPassword_y = 160
        self.EntryPassword_w = 289
        self.EntryPassword_h = 30
        self.TextExcelPath_x = 5
        self.TextExcelPath_y = 30
        self.TextExcelPath_w = 290
        self.TextExcelPath_h = 90
        self.Label01_x = 0
        self.Label01_y = 130
        self.Label01_w = 75
        self.Label01_h = 30
        self.Label00_x = 0
        self.Label00_y = 0
        self.Label00_w = 75
        self.Label00_h = 30
        self.ListboxLog_x = 0
        self.ListboxLog_y = 0
        self.ListboxLog_w = 479
        self.ListboxLog_h = 305
        self.ListboxLog_scrollbar_vertical_x = self.ListboxLog_x + self.ListboxLog_w
        self.ListboxLog_scrollbar_vertical_y = self.ListboxLog_y
        self.ListboxLog_scrollbar_vertical_w = 21
        self.ListboxLog_scrollbar_vertical_h = self.ListboxLog_h

    
    # For Fix Bug Treeview can't change the color in Windows OS.
    def _bugfix_style_map(self, option):
        return [elm for elm in self.style.map("Treeview", query_opt=option)
            if elm[:2] != ("!disabled", "!selected")]


class DBConvertorEvent(DBConvertorGui):
    def __init__(self):
        super().__init__()
        # appearance variables
        self.ButtonConvertLabel = StringVar(value='开始转换')
        self.CheckbuttonShowPwdFlagLabel   = StringVar(value='显示密码')
        self.CheckbuttonShowPwdFlagValue = BooleanVar(value=True)
        self.EntryPasswordValue   = StringVar(value='')
        self.Label01Label   = StringVar(value='Excel 密码')
        self.Label00Label   = StringVar(value='Excel 文件')
        self.ListboxLogListValues   = StringVar(value=())
        self._create()
        # wing initial
        # ===================================================
        
        # ===================================================
        self.after(20, self.periodic)


    def periodic(self):
        # wing periodcommand
        # ===================================================
        
        # ===================================================
        self.after(20, self.periodic)
        

    def show(self, parameter=None):
        # wing preshow
        # ===================================================
        
        # ===================================================
        self._size()
        self._lay()
        self.mainloop()


    def quit_window_command(self):
        # wing quitcommand
        # ===================================================
        
        # ===================================================
        self.destroy()


    def menu_command_Inport_menucommand(self):
        # wing menucommand m000001 'Inport'
        # ===================================================
        pass

        # ===================================================


    def menu_command_02_menucommand(self):
        # wing menucommand m000004 'Exit'
        # ===================================================
        pass

        # ===================================================


    def menu_command_Start_menucommand(self):
        # wing menucommand m000006 'Start'
        # ===================================================
        pass

        # ===================================================


    def menu_command_Setting_menucommand(self):
        # wing menucommand m000002 'Setting'
        # ===================================================
        pass

        # ===================================================


    def ButtonConvert_buttoncommand(self):
        # wing buttoncommand 347006
        # ===================================================
        pass
        
        # ===================================================


    def CheckbuttonShowPwdFlag_buttoncommand(self):
        # wing buttoncommand 391533
        # ===================================================
        pass
        
        # ===================================================
        
        
if __name__ == '__main__':
    DBConvertorEvent().show()


