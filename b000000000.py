# -*- coding: utf-8 -*-

from collections import deque
"""

@author: ndjemou99
"""
eleves = {}
eleves["Boris"]=["Amir","Franck","Nathalie","Bertrand"]
eleves["Amir"]=[]
eleves["Franck"]=[]
eleves["Nathalie"]=[]
eleves["Bertrand"]=["Erna","Hassana","Abdelkrim"]
eleves["Erna"]=[]
eleves["Hassana"]=[]
eleves["Zoureni"]=["Sekou","Auriane","Corlings"]
eleves["Sekou"]=[]
eleves["Auriane"]=[]
eleves["Corlings"]=[]
eleves["Abdelkrim"]=["Souleyman","Zack","Zoureni"]
eleves["Souleyman"]=[]
eleves["Zack"]=[]

def personne_elue(name):
   return name == 'Zoureni'


def search(name):
   search_queue = deque()
   search_queue += eleves[name]
   while search_queue:
       personne = search_queue.popleft()
       if personne_elue(personne):
           print(personne + " a le fameux Mac")
           return True
       search_queue += eleves[personne]
   return False

if __name__== "__main__":
  search("Boris")