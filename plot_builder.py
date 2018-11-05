import matplotlib.pyplot as plt
import numpy as np

class PlotBuilder:
    @staticmethod
    def buildSolutionPlot(values, legend):
        plt.close(1)
        plt.figure(1)

        for i in values:
            plt.plot(i[0], i[1])

        plt.ylabel('Y axis')
        plt.xlabel('X axis')
        plt.legend(legend, loc='upper left')
        plt.gcf().canvas.set_window_title('Solution')
        plt.xticks(np.arange(min(values[0][0]), max(values[0][0]), 1))
        plt.show()

    @staticmethod
    def buildLocalErrorPlot(values, legend):
        plt.close(2)
        plt.figure(2)

        for i in values:
            plt.plot(i[0], i[1])

        plt.ylabel('Y axis')
        plt.xlabel('X axis')
        plt.legend(legend, loc='upper left')
        plt.gcf().canvas.set_window_title('Local Error')
        plt.xticks(np.arange(min(values[0][0]), max(values[0][0]), 1))
        plt.show()

    @staticmethod
    def buildGlobalErrorPlot(values, legend):
        plt.close(3)
        plt.figure(3)

        for i in values:
            plt.plot(i[0], i[1], marker='o')

        plt.ylabel('Y axis')
        plt.xlabel('X axis')
        plt.legend(legend, loc='upper left')
        plt.gcf().canvas.set_window_title('Global Error')
        plt.show()