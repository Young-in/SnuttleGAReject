import math
import random

class MapGenerator:
    # m : the number of stations
    # stations : locations of stations [tuple of 2 real numbers and name (x, y, name)] == map info
    # dists : matrix which has the distance info
    def __init__(self, staN = 20, typ = 'nomal'):
        self.staN = staN
        if typ == 'nomal' :
            self.stations = [(random.random()*100, random.random()*100, 0)] # depot
            for j in range(self.staN) :
                sta = (random.random()*100, random.random()*100, j + 1)
                while sta in self.stations :
                    sta = (random.random() * 100, random.random() * 100, j + 1)
                self.stations.append(sta)

        elif typ == 'clust' :
            self.stations = [(random.random()*100, random.random()*100, 0)] # depot
            for j in range(self.staN//2):
                sta = (random.random() * 30, random.random() * 30, j + 1)
                self.stations.append(sta)

            for j in range(self.staN//2, self.staN):
                sta = (random.random() * 30 + 70, random.random() * 30 + 70, j + 1)
                self.stations.append(sta)

        self.dists = self.getDists()
        pass

    def __str__(self):
        ret = ""
        ret += "The number of stations : {m}\n".format(m = self.staN)
        ret += "Depot: {c}\n".format(c = self.stations[0])
        for coord in self.stations[1:]: ret += "{c}\n".format(c = coord)
        ret += "------------------------------------\n"
        return ret

    def getDists(self):
        staN = self.staN # number of sta
        dists = [[None] * (staN + 1) for i in range(staN + 1)]
        for i in range(staN + 1) :
            for j in range(staN + 1) :
                d = self.getDistance(i, j)
                dists[i][j] = d
        return dists


    def getDistance(self, x, y):
        # get euclidean distance between station x and station y
        return math.sqrt((self.stations[x][0]-self.stations[y][0])**2
                         +(self.stations[x][1]-self.stations[y][1])**2)