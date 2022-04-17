#Import
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
import sys

#form
from mpl_toolkits.mplot3d import axes3d
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox

class OpenRocketCSV:

    def __init__(self):
        self.Time = []
        self.Altitude = []
        self.PositionUpwind = []
        self.PositionParallerToWind = []
        self.Roll = []
        self.Pitch = []
        self.Yaw = []
        self.Len = []
        self.Heg = []
        self.CCP = []
        self.CGP = []
        
        self.Setup()
        self.FilghtLine3D()
        self.LunchAndFallLocation()

    def Setup(self):
        FileName = ''
        print(len(sys.argv))
        if len(sys.argv) >= 2:
            FileName = str(sys.argv[1])
        else:
            FileName = ''

        if FileName == '':          
            File = open(str(input("File Name: ")), "r")

            while True:
                Line = File.readline()         
                if Line != "":
                    if Line[0] != "#":
                        SPS = Line.split(",")
                        self.Time.append(float(SPS[0]))
                        self.Altitude.append(float(SPS[1]))
                        self.PositionUpwind.append(float(SPS[2]))                 
                else:
                    break
        else:
            File = open(str(FileName), "r")
            while True:
                Line = File.readline()         
                if Line != "":
                    if Line[0] != "#":
                        SPS = Line.split(",")
                        self.Time.append(float(SPS[0]))
                        self.Altitude.append(float(SPS[1]))
                        self.PositionUpwind.append(float(SPS[2]))
                else:
                    break

    def FilghtLine3D(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(self.Time, self.PositionUpwind, self.Altitude)
        plt.show()
        
    def LunchAndFallLocation(self):
        LunchX = 0
        LunchY = 0
        FallX = 0
        FallY = 0
        X = []
        index = -500
        for x in range(-500,500):
            Y = []
            indey = -500
            for y in range(-500,500):
                if index == 0 and indey == 0:
                    Y.append(10)
                elif index == int(self.PositionUpwind[len(self.PositionUpwind)-1]) and indey == int(self.PositionUpwind[len(self.PositionUpwind)-1]):
                    Y.append(10)
                else:
                    Y.append(0)
                indey+=1
            X.append(Y)
            index+=1
        fig, ax = plt.subplots()
        ax.imshow(X)
        numrows = 1
        numcols = 1
        #ax.format_coord = self.format_coord
        plt.show()
            
    def format_coord(self, x, y):
        print("L")
        #col = int(int(x) + 0,5)
        #row = int(int(y) + 0,5)
        #if 0 <= col < numcols and 0 <= row < numrows:
            #z = X[row, col]
            #return 'x=%7f, y=%7f, z=%7f' % (x, y, z)
        #else:
            #return 'x=%5f, y=%5f' % (x, y)
            #return x,y

Test = OpenRocketCSV()





