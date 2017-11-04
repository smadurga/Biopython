#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "gelpi"
__date__ = "$02-nov-2017 8:21:31$"

import math

SIG=3.4
EPS=0.09

class System():
    def __init__(self,dmin):
        self.parts = []
        self.d = dmin
        for x in range(-1,2):
            for y in range(-1,2):
                for z in range(-1,2):
                    self.parts.append(Particle(x,y,z,0.))
    
    def calcEnergy(self):
        eint = 0.
        evdw = 0.
        for p1 in sys.parts:
            for p2 in sys.parts:
                if p1 == p2:
                    continue
                eint = eint + p1.elecInt(p2,self.d)
                evdw = evdw + p1.vdwInt(p2,self.d)
        return [evdw,eint]
    
                    
class Particle():
    def __init__(self,x,y,z,c):
        self.x=x
        self.y=y
        self.z=z
        self.c=c
    
    def distance(self,other):
        return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2+(self.z-other.z)**2)
    
    def vdwInt(self,other,dmin):
        f = SIG/self.distance(other)/dmin
        return 4.*EPS * (pow(f,12)-pow(f,6))
    
    def elecInt(self,other,dmin):
        d = self.distance(other)*dmin
        return 332.16*self.c*other.c/d
    
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y and self.z == other.z

#if __name__ == "__main__":
sys = System(3.8)
[evdw,eint] = sys.calcEnergy()
print ("Evdw=", evdw)
p0 = Particle(0,0,0,0)
evdw0 = 0
for pi in sys.parts:
    if pi != p0:
        evdw0 = evdw0 + p0.vdwInt(pi,sys.d)
print ("Evdw=", evdw-evdw0)
for pi in sys.parts:
    pi.c = 1.
(evdw1,eint1) = sys.calcEnergy()
print (evdw/eint1)
    
    
    
