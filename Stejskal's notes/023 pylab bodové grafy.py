﻿# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 08:24:01 2012

@author: Martin
"""
"""
Styly čar
ro  - červená kolečka
bs  - modré čtverečky
g^  - zelené trojúhelníky
y-  - žlutá plná čára
--  - čárkovaná čára
:   - tečkovaná
""" 

from pylab import *


x=[1,2,3,4]
y=[1,4,9,16]

#plot(x,y,"g-") #vložení bodů do grafu 'barvatvar'
#axis([0, 10, 0, 10]) #rozsah os x a y

#plot(x,y,'ro') #vložení bodů do grafu 'barvatvar'
#plot(x,y,'bo') #vložení bodů do grafu 'barvatvar'

#plot(x,y,color="green")
plot(x,y,'g--',color="#004437") #vložení bodů do grafu 'barvatvar'


show()

"""
Úkol:
1) Vykreslete graf funkce y=x**3-2*x**2+x-1 do 
   jednoho grafu - jednou jako plnou čáru a podruhé 
   jako kulaté body
2) Vygenerujte seznam 20-ti náhod. bodů v rovině (0,20)
   a zobrazte jej pomocí čtverečků.   
3) Načtěte z klávesnice souřadnice tří bodů a zobrazte 
   trojúhelník. 
""" 






  
