import pandas as pd
import random as rd
import math as mt

class Frequencia:
    def __init__(self, prop) -> None:
        pass
        #self.prop = prop
        #print(self.prop)

    #Generates a Quantitative sample
    def RandomNumbers(self, num : int):
        
        self.num = num
        self.sam : list = rd.sample(range(150), k = self.num)
        Frequencia.Classes(self, self.sam)

    #Generates a Quanlitative sample
    def RandomQualitative(self, num : int):
        pass
    
    def Classes(self, sample : list):
        self.sample = sample

        #Sort Rol
        self.sample.sort()

        #Sturges
        self.sturges : float = 1+ mt.log2(len(self.sample))
        self.k = round(self.sturges)
        

        #Range = Highest value - Lowest value
        self.r = max(self.sample) - min(self.sample)
        

        #Class Size = Ramge / k
        self.classsize = self.r / self.k
        self.c = round(self.classsize)

        #debug
        print(self.sample)
        print(self.k) 
        print(self.r)
        print(self.c)
        pass
    
    #consertar calculo de sturges
    