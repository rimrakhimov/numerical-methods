#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx


class MainWindow(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.InitUI()
        self.Centre()

    def InitUI(self):
        panel = wx.Panel(self)

        sizer = wx.GridBagSizer(5, 5)

        # text1 = wx.StaticText(panel, label="Equation")
        # sizer.Add(text1, pos=(0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=15)

        icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap('equation.png'))
        sizer.Add(icon, pos=(0, 1), flag=wx.TOP | wx.BOTTOM | wx.ALIGN_CENTRE_HORIZONTAL,
                  border=5)

        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(1, 0), span=(1, 4), flag=wx.EXPAND | wx.BOTTOM, border=10)

        text2 = wx.StaticText(panel, label="x0")
        sizer.Add(text2, pos=(2, 0), flag=wx.LEFT | wx.ALIGN_CENTRE_HORIZONTAL, border=10)

        tc1 = wx.TextCtrl(panel)
        sizer.Add(tc1, pos=(2, 1), span=(1, 2), flag=wx.EXPAND | wx.RIGHT | wx.RIGHT, border=5)

        text3 = wx.StaticText(panel, label="y0")
        sizer.Add(text3, pos=(3, 0), flag=wx.TOP | wx.LEFT | wx.ALIGN_CENTRE_HORIZONTAL, border=10)

        tc2 = wx.TextCtrl(panel)
        sizer.Add(tc2, pos=(3, 1), span=(1, 2), flag=wx.EXPAND | wx.TOP | wx.RIGHT, border=5)

        # button1 = wx.Button(panel, label="Browse...")
        # sizer.Add(button1, pos=(3, 4), flag=wx.TOP | wx.RIGHT, border=5)

        text4 = wx.StaticText(panel, label="X")
        sizer.Add(text4, pos=(4, 0), flag=wx.TOP | wx.LEFT | wx.ALIGN_CENTRE_HORIZONTAL, border=10)

        tc3 = wx.TextCtrl(panel)
        sizer.Add(tc3, pos=(4, 1), span=(1, 2), flag=wx.EXPAND | wx.TOP | wx.RIGHT, border=5)

        text5 = wx.StaticText(panel, label="N")
        sizer.Add(text5, pos=(5, 0), flag=wx.TOP | wx.LEFT | wx.ALIGN_CENTRE_HORIZONTAL, border=10)

        tc4 = wx.TextCtrl(panel)
        sizer.Add(tc4, pos=(5, 1), span=(1, 2), flag=wx.EXPAND | wx.TOP | wx.RIGHT, border=5)

        # button2 = wx.Button(panel, label="Browse...")
        # sizer.Add(button2, pos=(4, 4), flag=wx.TOP | wx.RIGHT, border=5)

        button4 = wx.Button(panel, label="Solution")
        sizer.Add(button4, pos=(6, 1), flag=wx.ALIGN_RIGHT)

        button5 = wx.Button(panel, label="Local Error")
        sizer.Add(button5, pos=(6, 2), flag=wx.BOTTOM | wx.RIGHT, border=10)

        sb = wx.StaticBox(panel, label="Methods to solve Differential Equation")

        boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
        boxsizer.Add(wx.CheckBox(panel, label="Exact Solution"), flag=wx.LEFT | wx.TOP, border=5)
        boxsizer.Add(wx.CheckBox(panel, label="Euler's Method"), flag=wx.LEFT | wx.TOP, border=5)
        boxsizer.Add(wx.CheckBox(panel, label="Improved Euler Method"), flag=wx.LEFT, border=5)
        boxsizer.Add(wx.CheckBox(panel, label="Runge-Kutta Method"), flag=wx.LEFT | wx.BOTTOM, border=5)
        sizer.Add(boxsizer, pos=(7, 0), span=(1, 3), flag=wx.EXPAND | wx.TOP | wx.RIGHT | wx.LEFT, border=10)

        sizer.Add((-1, 20), pos=(8, 0))

        # button3 = wx.Button(panel, label="Help")
        # sizer.Add(button3, pos=(8, 0), flag=wx.LEFT, border=10)

        sizer.AddGrowableCol(2)
        panel.SetSizer(sizer)
        sizer.Fit(self)


def main():
    app = wx.App()
    frame = MainWindow(None, id=wx.ID_ANY, title="Differential Equations",
                       style=wx.MINIMIZE_BOX | wx.CLOSE_BOX)
    frame.Show()

    app.MainLoop()


if __name__ == '__main__':
    main()