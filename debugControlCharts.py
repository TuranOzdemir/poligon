# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 17:05:03 2021

@author: TURAN
"""

import numpy as np
import matplotlib.pyplot as plt
data = [35.5,27.2, 27.6, 26.8, 27.2, 27.1, 
            26.6, 27.6, 27.7, 27.5, 26.6, 
            27.2, 26.7, 25.9, 27.1, 27.6, 
            27.5, 28.3, 26.5, 29.0, 27.2]
class getFactorVals:
    facVals = {
  "d2": [1.128,1.693,2.059,2.326,2.534],
  "D3": [0,0,0,0,0],
  "D4": [3.267,2.574,2.282,2.114,2.004]
}
#factors = getFactorVals()
#d2 = factors.facVals.get("d2")[0]
class IndMR:
    
    def __init__(self, data):
        factors = getFactorVals()
        self.d2 = factors.facVals.get("d2")[0]
        self.data = data
        
    def mRort(self):
        mR = [round(abs(self.data[i+1]-self.data[i]),2) for i in range(len(self.data)-1)]
        mRtop = 0
        for j in range(len(mR)):
            mRtop += mR[j] 
        return mRtop/len(mR)
    
    def Iort(self):
        Itop = 0
        for z in range(len(self.data)):
            Itop += self.data[z]
        return Itop/len(self.data)
    
    def UCLI(self):
        return Iort + 3*(mRort/self.d2)
    
    def CLI(self):
        return Iort
    
    def LCLI(self):
        return Iort - 3*(mRort/self.d2)
    def outlier(self):
        outlier = []
        for i in self.data:
            if i>UCLI or  i<LCLI:
                outlier.append(i)
        return outlier
class goster:
    def __init__(self, data):
        gr = IndMR(data)
        self.mRort = gr.mRort()
        self.Iort = gr.Iort()
        self.UCLI = gr.UCLI()
        self.CLI = gr.CLI()
        self.LCLI = gr.LCLI()
        self.data = data
    def hesapGoster(self):
        print("mRort = {}\nIort = {}".format(round(self.mRort,6),round(self.Iort,6)))
        print("--------------------------------")
        print("UCLı = {}\nCLı = {}\nLCLı = {}".format(self.UCLI,self.CLI,self.LCLI))
        z = IndMR(self.data)
        if len(z.outlier())>0:
            print("aykırı değerler vardır bu nedenle özel nedenlerden kaynaklanan varyasyon bulunmaktadır olarak yorum yapabiliriz\nAykırı Değerler = {}".format(z.outlier()))

        else:
            print("veride aykırı değer bulunmamaktadır varyasyon doğal nedenlerden kaynaklanmaktadır.")

class visualise:
    def __init__(self, data):
        self.data = data
        IndMr = IndMR(self.data)        
        self.UCLI = IndMr.UCLI()
        self.CLI = IndMr.CLI()
        self.LCLI = IndMr.LCLI()
        
    def showI(self):
        plt.figure(figsize=(15,5))
        plt.plot(self.data,marker="o",color="k",label="data")
        plt.plot([self.UCLI]*len(self.data),color="r",label="UCLı={}".format(round(self.UCLI,2)))
        plt.plot([self.LCLI]*len(self.data),color="r",label="LCLı={}".format(round(self.LCLI,2)))
        plt.plot([self.CLI]*len(self.data),color="b",label="CLı={}".format(round(self.UCLI,2)))
        plt.title("I Chart")
        plt.xticks(np.arange(len(self.data)))
        plt.legend()
        plt.show()
        

ImR = IndMR(data)
ImR.mRort()
ImR.Iort()
g = goster(data)
g.hesapGoster()
vis = visualise(data)
vis.showI()



