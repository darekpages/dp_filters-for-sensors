# ,----,
# | DP | Copyright (C) 2022 DAREK PAGES
# '----' MIT Licence
# ==========================================================================
# File: dp_filters.py
#
# Digital average filter with adjustable precision for use with various 
# types of sensors.
# python3, micropython v1.19.1, circuitpython
#
# version: 0.3
# date: 20.11.2022 - 21.11.2022
# -------------------------------------------------------------------------
class sensorfilter:
    __dim_mean__= []
    __resbuff__= []
    
    def mean2(self, value, dim_mean):
        '''Digital Filter Means for sensors:
       args: value - of A/C, dim_mean - base mean (=>2).'''
        self.__dim_mean__.append(value)            #adding to buffor
        dmn= len(self.__dim_mean__)
        men= sum(self.__dim_mean__)/dmn            #mean
        if dmn==dim_mean:
            self.__dim_mean__= [men]               #transfer to the beginning
        return men

    def pic_correction(self, value):
        '''Mean correction for 2 level:
        args: value - of A/C'''
        if len(self.__resbuff__)<3:
            self.__resbuff__.append(value)         #adding to buffor
            dim_buff= len(self.__resbuff__)
            if dim_buff==3:                        #filter
                if(self.__resbuff__[1]>self.__resbuff__[0]) or (self.__resbuff__[1]>self.__resbuff__[2]):
                    self.__resbuff__[1]= (self.__resbuff__[0]+self.__resbuff__[2])/2
                if(self.__resbuff__[1]<self.__resbuff__[0]) or (self.__resbuff__[1]<self.__resbuff__[2]):
                    self.__resbuff__[1]= (self.__resbuff__[0]+self.__resbuff__[2])/2
                return self.__resbuff__.pop(0)
            else:
                if dim_buff==1:
                    return self.__resbuff__[dim_buff-1]
                if dim_buff==2:
                    return sum(self.__resbuff__)/2
