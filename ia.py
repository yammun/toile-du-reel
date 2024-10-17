# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 17:34:51 2024

@author: okadalzo
"""

import codecs, csv, dominate
from dominate.tags import *
from dominate.util import raw
from larousse_api import larousse

with open('TD.csv', newline='', encoding='utf-8') as fichier:
    reader = csv.reader(fichier)
    for row in reader:
        liste=row[0].split(';')
        doc = dominate.document(title=liste[0])
        with doc.head:
            link(rel='stylesheet', href='style.css')
        with doc.body:
            raw('<div class="title_container">\n<div class=title><a href="/engenremap-slayer">&nbsp; Le réel &middot;</a>\n&nbsp; <a style="color: #845ec2" href="/Individualité.html">individuel</a>\n&nbsp; <a style="color: #a178df" href="/Expression.html">expressif</a>\n&nbsp; <a style="color: #be93fd" href="/Perception.html">perceptif</a>\n&nbsp; <a style="color: #dcb0ff" href="/Collectif.html">collectif</a></div>')
            with div():
                attr(cls='def')
                h1(liste[0])
                for d in larousse.get_definitions(liste[0]):
                    p(d)
            raw('''<div id=mirror role=complementary style="width: 135em; padding: 32px 550px 16px 550px;">
<div class=canvas style="width: 399px; height: 336px; border: 4px solid #4d8076; background: #404040; top: 64px">
    <div id=mirroritem1 class="genre scanme" scan=true style="top: 29px; left: 231px; font-size: '''+str(80*(int(liste[4])-1))+'''%" role=button tabindex=0 onKeyDown="kb(event);" title="Les traces">Les traces<a class=navlink href="/Les traces.html" role=button tabindex=0 onKeyDown="kb(event);" onclick="event.stopPropagation();" target=artistprofile>&raquo;</a> </div>
    <div id=mirroritem2 class="genre scanme" scan=true style="top: 51px; left: 69px; font-size: '''+str(80*(int(liste[3])-1))+'''%" role=button tabindex=0 onKeyDown="kb(event);" title="L'art">L'art<a class=navlink href="/L'art.html" role=button tabindex=0 onKeyDown="kb(event);" onclick="event.stopPropagation();" target=artistprofile>&raquo;</a> </div>
    <div id=mirroritem3 class="genre scanme" scan=true style="top: 118px; left: 64px; font-size: '''+str(80*(int(liste[2])-1))+'''%" role=button tabindex=0 onKeyDown="kb(event);" title="L'apparence vestimentaire">L'apparence vestimentaire<a class=navlink href="/L'apparence vestimentaire.html" role=button tabindex=0 onKeyDown="kb(event);" onclick="event.stopPropagation();" target=artistprofile>&raquo;</a> </div>
    <div id=mirroritem4 class="genre scanme" scan=true style="top: 183px; left: 21px; font-size: '''+str(80*(int(liste[1])-1))+'''%" role=button tabindex=0 onKeyDown="kb(event);" title="Les gestes">Les gestes<a class=navlink href="/Les gestes.html" role=button tabindex=0 onKeyDown="kb(event);" onclick="event.stopPropagation();" target=artistprofile>&raquo;</a> </div>
    <div id=mirroritem5 class="genre scanme" scan=true style="top: 236px; left: 129px; font-size: '''+str(80*(int(liste[5])-1))+'''%" role=button tabindex=0 onKeyDown="kb(event);" title="La nature et l'animalité">La nature et l'animalité<a class=navlink href="/La nature et l'animalité.html" role=button tabindex=0 onKeyDown="kb(event);" onclick="event.stopPropagation();" target=artistprofile>&raquo;</a> </div>
    <div id=mirroritem6 class="genre scanme" scan=true style="top: 287px; left: 67px; font-size: '''+str(80*(int(liste[6])-1))+'''%" role=button tabindex=0 onKeyDown="kb(event);" title="Les espaces">Les espaces<a class=navlink href="/Les espaces.html" role=button tabindex=0 onKeyDown="kb(event);" onclick="event.stopPropagation();" target=artistprofile>&raquo;</a> </div>
</div></div>''')
        print(unicode(doc))
        f = codecs.open(liste[0]+".html", "w", "utf-8")
        f.write(unicode(doc))
        f.close()