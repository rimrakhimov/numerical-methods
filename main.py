import wx

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200, 100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()

        filemenu = wx.Menu()
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", " Information about this program")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT, "&Exit", "Terminate the program")

        menubar = wx.MenuBar()
        menubar.Append(filemenu, "&File")
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        self.Show()

    def OnAbout(self, e):
        dlg = wx.MessageDialog(self, "A small text editor", "About Sample Editor", wx.OK)
        wx.FileDialog
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self, e):
        self.Close()

app = wx.App(False)
frm = MainWindow(None, title="Hello World")

app.MainLoop()

# class HelloFrame(wx.Frame):
#     """
#     A Frame that says Hello World
#     """
#     def __init__(self, *args, **kw):
#         # ensure the parent's __init__ is called
#         super(HelloFrame, self).__init__(*args, **kw)
