import os
import matplotlib.pyplot as plt
import time

class Jump:
    def __init__(self, img_dir='/Users/yangyikang/Desktop/Images'):
        self.Img_dir = img_dir
        self.Img = None
        self.distance = None
        self.time = None
        self.coord = None

        self.ratio = 1.7

        #
        self.fig = None
        self.ax = None

    def main_execution_part1(self):
        # get image from phone
        self.getImg(path=self.Img_dir)
        self.Img = plt.imread(self.Img_dir+'/tmp.png')

        #
        self.coord = self.getCoord(self.Img)

    def main_execution_part2(self):
        plt.close()
        self.distance = sum(map(lambda x: (x[1]-x[0])**2, zip(*self.coord)))**(1/2)
        self.time = self.getTime(self.distance)
        self.sendJump(self.time)

    def getImg(self, path):
        os.system('adb shell screencap /sdcard/tmp.png')
        os.system('adb pull /sdcard/tmp.png ' + path)

    def getCoord(self, img):
        if not self.fig or self.ax:
            self.fig, self.ax = plt.subplots()
        self.ax.imshow(img)
        # auxiliary function
        self.coord = []
        def onclick(event):
            global x, y
            x, y = event.xdata, event.ydata
            self.coord.append((x, y))
            self.ax.plot([x[0] for x in self.coord], [y[1] for y in self.coord],"ro-")
            if len(self.coord) == 2:
                self.fig.canvas.mpl_disconnect(cid)

        cid = self.fig.canvas.mpl_connect('button_press_event', onclick)
        return self.coord

    def getTime(self, distance):
        return self.ratio * distance

    def sendJump(self, time):
        os.system('adb shell input swipe 1 1 1 1 %d' % time)

# other auxiliary functions
# fetch screencap and plot it
def fun1():
    test.main_execution_part1()

# send swipe request to phone with time
def fun2():
    test.main_execution_part2()
    time.sleep(1)
    fun1()


if __name__ == '__main__':
    test = Jump()
    fun1()
