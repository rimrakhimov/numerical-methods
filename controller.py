from layout import MainWindow
from math import exp
from differential_equation import DifferentialEquation
import wx

class Controller:
    def __init__(self, equation, solution):
        self.equation = equation
        self.solution = solution
        self.app = wx.App()
        self.mainFrame = MainWindow(self, None, id=wx.ID_ANY, title="Differential Equations",
                           style=wx.MINIMIZE_BOX | wx.CLOSE_BOX)
        self.mainFrame.Show()

        self.app.MainLoop()

    def OnSolutionButton(self, event):
        x0 = float(self.mainFrame.tcx0.GetValue())
        y0 = float(self.mainFrame.tcy0.GetValue())
        X = float(self.mainFrame.tcX.GetValue())
        N = int(self.mainFrame.tcN.GetValue())
        diff = DifferentialEquation(self.equation, x0, y0, X, N, self.solution)
        exactSolution = self.mainFrame.exactSolutionCheckBox.GetValue()
        eulersMethod = self.mainFrame.eulersMethodCheckBox.GetValue()
        improvedEulerMethod = self.mainFrame.improvedEulerMethodCheckBox.GetValue()
        rungeKuttaMethod = self.mainFrame.rungeKuttaMethodCheckBod.GetValue()
        print(x0, y0, X, N, sep=" ")
        event.Skip()

def f(x, y):
    return y ** 2 * exp(x) - 2 * y

def y(x, x0, y0, eps):
    if (y0 == 0):
        return 0
    else:
        c = (1 - y0 * exp(x0)) / (y0 * exp(2 * x0))
        res = (exp(x) + c * exp(2 * x))
        resp = (exp(x + eps / 2) + c * exp(2 * (x + eps / 2)))
        resn = (exp(x - eps / 2) + c * exp(2 * (x - eps / 2)))
        if resp * resn < 0:
            return float('inf')
        return 1 / res

def main():
    Controller(f, y)

if __name__ == '__main__':
    main()