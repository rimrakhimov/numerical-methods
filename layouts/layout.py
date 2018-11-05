#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx


class MainWindow(wx.Frame):

    def __init__(self, controller, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.Controller = controller

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
        self.exactSolutionCheckBox = wx.CheckBox(panel, label="Exact Solution")
        boxsizer.Add(self.exactSolutionCheckBox, flag=wx.LEFT | wx.TOP, border=5)
        self.eulersMethodCheckBox = wx.CheckBox(panel, label="Euler's Method")
        boxsizer.Add(self.eulersMethodCheckBox, flag=wx.LEFT | wx.TOP, border=5)
        self.improvedEulerMethodCheckBox = wx.CheckBox(panel, label="Improved Euler Method")
        boxsizer.Add(self.improvedEulerMethodCheckBox, flag=wx.LEFT, border=5)
        self.rungeKuttaMethodCheckBox = wx.CheckBox(panel, label="Runge-Kutta Method")
        boxsizer.Add(self.rungeKuttaMethodCheckBox, flag=wx.LEFT | wx.BOTTOM, border=5)
        sizer.Add(boxsizer, pos=(2, 0), span=(1, 3), flag=wx.EXPAND | wx.TOP | wx.RIGHT | wx.LEFT, border=10)

        textx0 = wx.StaticText(panel, label="x0")
        sizer.Add(textx0, pos=(4, 0), flag=wx.LEFT | wx.ALIGN_CENTRE_HORIZONTAL, border=10)

        self.tcx0 = wx.TextCtrl(panel, style=wx.TE_RICH)
        sizer.Add(self.tcx0, pos=(4, 1), span=(1, 2), flag=wx.EXPAND | wx.RIGHT | wx.RIGHT, border=5)
        self.tcx0.Bind(wx.EVT_CHAR, self.OnKeyPressCheckFloat)

        texty0 = wx.StaticText(panel, label="y0")
        sizer.Add(texty0, pos=(5, 0), flag=wx.TOP | wx.LEFT | wx.ALIGN_CENTRE_HORIZONTAL, border=10)

        self.tcy0 = wx.TextCtrl(panel, style=wx.TE_RICH)
        sizer.Add(self.tcy0, pos=(5, 1), span=(1, 2), flag=wx.EXPAND | wx.TOP | wx.RIGHT, border=5)
        self.tcy0.Bind(wx.EVT_CHAR, self.OnKeyPressCheckFloat)

        textX = wx.StaticText(panel, label="X")
        sizer.Add(textX, pos=(6, 0), flag=wx.TOP | wx.LEFT | wx.ALIGN_CENTRE_HORIZONTAL, border=10)

        self.tcX = wx.TextCtrl(panel, style=wx.TE_RICH)
        sizer.Add(self.tcX, pos=(6, 1), span=(1, 2), flag=wx.EXPAND | wx.TOP | wx.RIGHT, border=5)
        self.tcX.Bind(wx.EVT_CHAR, self.OnKeyPressCheckFloat)

        textN = wx.StaticText(panel, label="N")
        sizer.Add(textN, pos=(7, 0), flag=wx.TOP | wx.LEFT | wx.ALIGN_CENTRE_HORIZONTAL, border=10)

        self.tcN = wx.TextCtrl(panel, style=wx.TE_RICH)
        sizer.Add(self.tcN, pos=(7, 1), span=(1, 2), flag=wx.EXPAND | wx.TOP | wx.RIGHT, border=5)
        self.tcN.Bind(wx.EVT_CHAR, self.OnKeyPressCheckInt)

        solutionButton = wx.Button(panel, label="Solution")
        sizer.Add(solutionButton, pos=(8, 1), flag=wx.ALIGN_RIGHT)
        solutionButton.Bind(wx.EVT_BUTTON, self.OnSolutionButton)

        localErrorButton = wx.Button(panel, label="Local Error")
        sizer.Add(localErrorButton, pos=(8, 2), flag=wx.BOTTOM | wx.RIGHT, border=10)
        localErrorButton.Bind(wx.EVT_BUTTON, self.OnLocalErrorButton)

        globalErrorBox = wx.BoxSizer(wx.HORIZONTAL)

        textRangeFrom = wx.StaticText(panel, label="From")
        globalErrorBox.Add(textRangeFrom, proportion=0, flag=wx.RIGHT, border=10)
        self.tcRangeFrom = wx.TextCtrl(panel, style=wx.TE_RICH)
        globalErrorBox.Add(self.tcRangeFrom, proportion=1, flag=wx.RIGHT, border=10)
        self.tcRangeFrom.Bind(wx.EVT_CHAR, self.OnKeyPressCheckInt)
        textRangeTo = wx.StaticText(panel, label="To")
        globalErrorBox.Add(textRangeTo, proportion=0, flag=wx.RIGHT, border=10)
        self.tcRangeTo = wx.TextCtrl(panel, style=wx.TE_RICH)
        self.tcRangeTo.Bind(wx.EVT_CHAR, self.OnKeyPressCheckInt)
        globalErrorBox.Add(self.tcRangeTo, proportion=1)

        sizer.Add(globalErrorBox, pos=(9, 0), span=(1, 3), flag=wx.EXPAND | wx.ALL, border=10)

        globalErrorButton = wx.Button(panel, label="Global Error")
        sizer.Add(globalErrorButton, pos=(10, 2), flag=wx.BOTTOM | wx.RIGHT, border=10)
        globalErrorButton.Bind(wx.EVT_BUTTON, self.OnGlobalErrorButton)

        sizer.AddGrowableCol(2)
        panel.SetSizer(sizer)
        sizer.Fit(self)

    def OnSolutionButton(self, event):
        if not self.isMethodsGridFilled():
            event.Skip()
        elif not self.isDataGridFilled():
            event.Skip()
        else:
            self.Controller.OnSolutionButton(event)

    def OnLocalErrorButton(self, event):
        if not self.isMethodsGridFilled(exactSolution=False):
            event.Skip()
        elif not self.isDataGridFilled():
            event.Skip()
        else:
            self.Controller.OnLocalErrorButton(event)

    def OnGlobalErrorButton(self, event):
        if not self.isMethodsGridFilled(exactSolution=False):
            event.Skip()
        elif not self.isDataGridFilled(N=False):
            event.Skip()
        elif not self.isRangeGridFilled():
            event.Skip()
        else:
            self.Controller.OnGlobalErrorButton(event)

    def OnKeyPressCheckInt(self, event):
        keycode = event.GetKeyCode()
        ctrlKeys = (wx.WXK_LEFT, wx.WXK_RIGHT, wx.WXK_UP, wx.WXK_DOWN, wx.WXK_CONTROL_A, wx.WXK_CONTROL_B,
                    wx.WXK_CONTROL_C, wx.WXK_CONTROL_D, wx.WXK_CONTROL_E, wx.WXK_CONTROL_F, wx.WXK_CONTROL_G,
                    wx.WXK_CONTROL_H, wx.WXK_CONTROL_I, wx.WXK_CONTROL_J, wx.WXK_CONTROL_K, wx.WXK_CONTROL_L,
                    wx.WXK_CONTROL_M, wx.WXK_CONTROL_N, wx.WXK_CONTROL_O, wx.WXK_CONTROL_P, wx.WXK_CONTROL_Q,
                    wx.WXK_CONTROL_R, wx.WXK_CONTROL_S, wx.WXK_CONTROL_T, wx.WXK_CONTROL_U, wx.WXK_CONTROL_V,
                    wx.WXK_CONTROL_W, wx.WXK_CONTROL_X, wx.WXK_CONTROL_Y, wx.WXK_CONTROL_Z, wx.WXK_BACK,
                    wx.WXK_TAB, wx.WXK_ESCAPE, wx.WXK_DELETE, wx.WXK_SHIFT, wx.WXK_END, wx.WXK_HOME)
        object = event.GetEventObject()
        object.SetBackgroundColour(wx.NullColour)
        if ord('0') <= keycode <= ord('9') or keycode in ctrlKeys:
            event.Skip()

    def OnKeyPressCheckFloat(self, event):
        keycode = event.GetKeyCode()
        ctrlKeys = (wx.WXK_LEFT, wx.WXK_RIGHT, wx.WXK_UP, wx.WXK_DOWN, wx.WXK_CONTROL_A, wx.WXK_CONTROL_B,
                    wx.WXK_CONTROL_C, wx.WXK_CONTROL_D, wx.WXK_CONTROL_E, wx.WXK_CONTROL_F, wx.WXK_CONTROL_G,
                    wx.WXK_CONTROL_H, wx.WXK_CONTROL_I, wx.WXK_CONTROL_J, wx.WXK_CONTROL_K, wx.WXK_CONTROL_L,
                    wx.WXK_CONTROL_M, wx.WXK_CONTROL_N, wx.WXK_CONTROL_O, wx.WXK_CONTROL_P, wx.WXK_CONTROL_Q,
                    wx.WXK_CONTROL_R, wx.WXK_CONTROL_S, wx.WXK_CONTROL_T, wx.WXK_CONTROL_U, wx.WXK_CONTROL_V,
                    wx.WXK_CONTROL_W, wx.WXK_CONTROL_X, wx.WXK_CONTROL_Y, wx.WXK_CONTROL_Z, wx.WXK_BACK,
                    wx.WXK_TAB, wx.WXK_ESCAPE, wx.WXK_DELETE, wx.WXK_SHIFT, wx.WXK_END, wx.WXK_HOME)
        object = event.GetEventObject()
        object.SetBackgroundColour(wx.NullColour)
        if ord('0') <= keycode <= ord('9') or keycode in ctrlKeys:
            event.Skip()
        elif keycode == ord('-'):
            val = object.GetValue()
            insertionPoint = object.GetInsertionPoint()
            if  insertionPoint == 0 and '-' not in val:
                event.Skip()
        elif keycode == ord('.'):
            val = object.GetValue()
            insertionPoint = object.GetInsertionPoint()
            if '.' not in val and insertionPoint > 0:
                event.Skip()

        def NotifyNothingToShow(self):
            wx.MessageBox('Cannot solv  e equation by specified methods with given value N', 'Error',
                      wx.OK | wx.ICON_ERROR)

    def isMethodsGridFilled(self, exactSolution=True):
        result = (exactSolution and self.exactSolutionCheckBox.GetValue()) or \
               self.eulersMethodCheckBox.GetValue() or \
               self.improvedEulerMethodCheckBox.GetValue() or \
               self.rungeKuttaMethodCheckBox.GetValue()

        if not result:
            wx.MessageBox('Choose at least one solution method', 'Not filled',
                          wx.OK | wx.ICON_ERROR)
        return result

    def isDataGridFilled(self, N=True):
        result = True
        if len(self.tcx0.GetValue()) == 0 or self.tcx0.GetValue() == '-':
            self.tcx0.SetBackgroundColour((255, 204, 204, 0))
            result = False
        if len(self.tcy0.GetValue()) == 0 or self.tcy0.GetValue() == '-':
            self.tcy0.SetBackgroundColour((255, 204, 204, 0))
            result = False
        if len(self.tcX.GetValue()) == 0 or self.tcX.GetValue() == '-':
            self.tcX.SetBackgroundColour((255, 204, 204, 0))
            result = False
        if (N and len(self.tcN.GetValue()) == 0):
            self.tcN.SetBackgroundColour((255, 204, 204, 0))
            result = False

        return result

    def isRangeGridFilled(self):
        result = True
        if len(self.tcRangeTo.GetValue()) == 0:
            self.tcRangeTo.SetBackgroundColour((255, 204, 204, 0))
            result = False
        if len(self.tcRangeFrom.GetValue()) == 0:
            self.tcRangeFrom.SetBackgroundColour((255, 204, 204, 0))
            result = False
        return result

def main():
    app = wx.App()
    frame = MainWindow(None, id=wx.ID_ANY, title="Differential Equations",
                       style=wx.MINIMIZE_BOX | wx.CLOSE_BOX)
    frame.Show()

    app.MainLoop()

if __name__ == '__main__':
    main()