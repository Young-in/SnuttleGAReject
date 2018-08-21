import random
import math

class RequestGenerator() :
    # requests : locations and time windows of requests [tuple of 4 positive integers(timeS, stationS, timeD, stationD)]
    # n : the number of requests
    # T : the maximum time of the simulation
    def __init__(self, Map, typ = 'AR', reqN = 1000, T = 1440):
        self.reqN = reqN
        self.T = T

        self.staNap = Map
        self.staN = Map.staN
        self.dists = Map.dists

        self.requests = []
        if(typ == 'AR') :
            self.requests = self.rand()
        elif(typ == 'CS') :
            self.requests = self.cluster()
        elif(typ == 'CS2'):
            self.requests = self.cluster2(0.8)
        else :
            print("ERROR : Requests Type Unavailable")
        pass

    def __str__(self):
        ret = ""
        ret += "The number of requests : {n}\n".format(n=self.reqN)
        for request in self.requests: ret += "{r}\n".format(r=request)
        ret += "------------------------------------\n"
        return ret

    def rand(self):
        lst = []
        for i in range(self.reqN):
            # new version without using loop
            sta0 = random.randrange(self.staN) + 1
            sta1 = (sta0 + random.randrange(1, self.staN)) % self.staN + 1
            # change index 1~m to 0~m-1 for easy access of dist[][]

            d = self.dists[sta0][sta1] * (
                        1 + random.random())  # make time interval random value between distance and 2*distance
            t0 = random.randrange(math.floor(self.T - d))
            t1 = math.floor(t0 + d)
            lst.append((t0, sta0, t1, sta1))
            # To ensure two stations, times are different
        return lst

    def cluster(self):
        lst = []
        for i in range(self.reqN//2):
            # new version without using loop
            sta0 = random.randrange(self.staN//2) + 1
            sta1 = (sta0 + random.randrange(1, self.staN//2)) % (self.staN//2) + 1
            # change index 1~m to 0~m-1 for easy access of dist[][]

            d = self.dists[sta0][sta1] * (1 + random.random())
            # make time interval random value between distance and 2*distance
            t0 = random.randrange(math.floor(self.T - d))
            t1 = math.floor(t0 + d)
            lst.append((t0, sta0, t1, sta1))
            
        for i in range(self.reqN//2, self.reqN):
            # new version without using loop
            sta0 = random.randrange(self.staN//2) + (self.staN//2) + 1
            sta1 = (sta0 + random.randrange(1, self.staN//2)) % (self.staN//2) + (self.staN//2) + 1
            # change index 1~m to 0~m-1 for easy access of dist[][]

            d = self.dists[sta0][sta1] * (1 + random.random())
            # make time interval random value between distance and 2*distance
            t0 = random.randrange(math.floor(self.T - d))
            t1 = math.floor(t0 + d)
            lst.append((t0, sta0, t1, sta1))
        return lst

    def cluster2(self, p):
        np = int(self.reqN*p)
        RG = RequestGenerator(self.staNap, 'CS', np, self.T)
        requests1 = RG.requests
        requests2 = []

        for i in range(np, self.reqN) :
            sta0 = random.randrange(self.staN // 2) + (self.staN // 2)*(i%2) + 1
            sta1 = (sta0 + random.randrange(1, self.staN // 2)) % (self.staN // 2) + (self.staN // 2)*((i+1)%2) + 1
            # change index 1~m to 0~m-1 for easy access of dist[][]

            d = self.dists[sta0][sta1] * (1 + random.random())
            # make time interval random value between distance and 2*distance
            t0 = random.randrange(math.floor(self.T - d))
            t1 = math.floor(t0 + d)
            requests2.append((t0, sta0, t1, sta1))

        return requests1+requests2

