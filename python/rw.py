import os
import numpy as np

class RW():
    
    delimiter = ','
    fmt = '%1.4e'
    directory = '../figures/'

    @classmethod
    def loadData(cls, filename):
        directory = cls.getDirectory()
        data = np.loadtxt(directory + filename, delimiter=cls.delimiter)
        return data

    @classmethod
    def saveData(cls, data, filename):
        directory = cls.getDirectory()
        np.savetxt(directory + filename, data, delimiter=cls.delimiter, fmt=cls.fmt)
        print(filename + str(' was saved.'))

    @classmethod
    def saveFigure(cls, fig, filename):
        directory = cls.getDirectory()
        fig.savefig(directory + filename, bbox_inches='tight')
        print(filename + str(' was saved.'))

    @classmethod
    def getDirectory(cls):
        if not os.path.exists(cls.directory):
            os.makedirs(cls.directory)
        return cls.directory
