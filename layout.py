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

        equation = wx.StaticBitmap(panel, bitmap=wx.Bitmap('equation.png'))
        sizer.Add(equation, pos=(0, 1), flag=wx.TOP | wx.BOTTOM | wx.ALIGN_CENTRE_HORIZONTAL,
                  border=5)

        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(1, 0), span=(1, 4), flag=wx.EXPAND | wx.BOTTOM, border=10)

        methods = wx.StaticBox(panel, label="Methods to solve Differential Equation")

        boxsizer = wx.StaticBoxSizer(methods, wx.VERTICAL)
        boxsizer.Add(wx.CheckBox(panel, label="Exact Solution"), flag=wx.LEFT | wx.TOP, border=5)
        boxsizer.Add(wx.CheckBox(panel, label="Euler's Method"), flag=wx.LEFT | wx.TOP, border=5)
        boxsizer.Add(wx.CheckBox(panel, label="Improved Euler Method"), flag=wx.LEFT, border=5)
        boxsizer.Add(wx.CheckBox(panel, label="Runge-Kutta Method"), flag=wx.LEFT | wx.BOTTOM, border=5)
        sizer.Add(boxsizer, pos=(2, 0), span=(1, 3), flag=wx.EXPAND | wx.TOP | wx.RIGHT | wx.LEFT, border=10)

        textx0 = wx.StaticText(panel, label="x0")
        sizer.Add(textx0, pos=(4, 0), flag=wx.LEFT | wx.ALIGN_CENTRE_HORIZONTAL, border=10)

        tcx0 = wx.TextCtrl(panel)
        sizer.Add(tcx0, pos=(4, 1), span=(1, 2), flag=wx.EXPAND | wx.RIGHT | wx.RIGHT, border=5)

        texty0 = wx.StaticText(panel, label="y0")
        sizer.Add(texty0, pos=(5, 0), flag=wx.TOP | wx.LEFT | wx.ALIGN_CENTRE_HORIZONTAL, border=10)

        tcy0 = wx.TextCtrl(panel)
        sizer.Add(tcy0, pos=(5, 1), span=(1, 2), flag=wx.EXPAND | wx.TOP | wx.RIGHT, border=5)

        textX = wx.StaticText(panel, label="X")
        sizer.Add(textX, pos=(6, 0), flag=wx.TOP | wx.LEFT | wx.ALIGN_CENTRE_HORIZONTAL, border=10)

        tcX = wx.TextCtrl(panel)
        sizer.Add(tcX, pos=(6, 1), span=(1, 2), flag=wx.EXPAND | wx.TOP | wx.RIGHT, border=5)

        textN = wx.StaticText(panel, label="N")
        sizer.Add(textN, pos=(7, 0), flag=wx.TOP | wx.LEFT | wx.ALIGN_CENTRE_HORIZONTAL, border=10)

        tcN = wx.TextCtrl(panel)
        sizer.Add(tcN, pos=(7, 1), span=(1, 2), flag=wx.EXPAND | wx.TOP | wx.RIGHT, border=5)

        solutionButton = wx.Button(panel, label="Solution")
        sizer.Add(solutionButton, pos=(8, 1), flag=wx.ALIGN_RIGHT)

        localErrorButton = wx.Button(panel, label="Local Error")
        sizer.Add(localErrorButton, pos=(8, 2), flag=wx.BOTTOM | wx.RIGHT, border=10)

        globalErrorBox = wx.BoxSizer(wx.HORIZONTAL)

        textRangeFrom = wx.StaticText(panel, label="From")
        globalErrorBox.Add(textRangeFrom, proportion=0, flag=wx.RIGHT, border=10)
        tcRangeFrom = wx.TextCtrl(panel)
        globalErrorBox.Add(tcRangeFrom, proportion=1, flag=wx.RIGHT, border=10)
        textRangeTo = wx.StaticText(panel, label="To")
        globalErrorBox.Add(textRangeTo, proportion=0, flag=wx.RIGHT, border=10)
        tcRangeTo = wx.TextCtrl(panel)
        globalErrorBox.Add(tcRangeTo, proportion=1)

        sizer.Add(globalErrorBox, pos=(9, 0), span=(1, 3), flag=wx.EXPAND | wx.ALL, border=10)

        globalErrorButton = wx.Button(panel, label="Global Error")
        sizer.Add(globalErrorButton, pos=(10, 2), flag=wx.BOTTOM | wx.RIGHT, border=10)

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