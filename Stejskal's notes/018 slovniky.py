# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 08:48:08 2012

@author: Radek
"""
import random
DB={}
DB['Mirek']=['Mirek','Palackeho 16','Olomouc','732 675 810']
DB['Dana']=['Dana','Litovelska 7','Olomouc','775 321 405']
DB['Jana']=['Jana','Husova 7','Litovel','775 321 405']
DB['Pepa']=['Pepa','Komenskeho 9','Praha','845 207 536']
DB['Marek']=['Marek','Jarni','Olomouc','776 345 890']
DB['Michal']=['Michal','Mezice 20','Mezice','606 267 762']
DB['Petra']=['Petra','Neznama 34','Opava','731 456 789']


jmeno=0
ulice=1
mesto=2
telefon=3

for klic in DB:
    print(DB[klic])

print (DB["Jana"][telefon])

"""
for klic in DB:
    if DB[klic][telefon][0]=="7":
        print (DB[klic][jmeno],"-",DB[klic][telefon])
"""
      
"""
Úkoly:
0) Přidejte do DB 1 vlastní záznam, vypište všechny údaje    
1) Vypište seznamy údajů lidí z Olomouce
2) Všechna města Olomouc nahraďte v DB za Opavu   
3) Do každého záznamu přidejte náhodný věk 
   (15-25 let) jako 5. položku seznamu
4) Nechejte zadat uživatele jméno a pokuste se smazat záznam
   z databáze (rozlište IFem). 
"""














