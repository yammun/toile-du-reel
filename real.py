# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 17:46:28 2024

@author: 
"""

import csv, random

objets=6

with open('TD.csv', newline='', encoding='utf-8') as fichier:
    reader = csv.reader(fichier)
    for row in reader:
        liste=row[0].split(';')
        objets+=1
        #print(liste)
        print('<div id=item'+str(objets)+' preview_url="" class="genre scanme" scan=true style="color: #c67b1b; top: '+str(random.randint(100,700))+'px; left: '+str(random.randint(100,999))+'px; font-size: '+str(100+(9*(int(liste[7])-15)))+'%" role=button tabindex=0 onKeyDown="kb(event);" onclick="" title="'+liste[0]+'">'+liste[0]+'<a class=navlink href="" role=button tabindex=0 onKeyDown="kb(event);" onclick="event.stopPropagation();">&raquo;</a> </div>')
        
