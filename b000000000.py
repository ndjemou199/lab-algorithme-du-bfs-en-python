# -*- coding: utf-8 -*-



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
   return name == 'zoureni'

def search(name):
   from collections import deque
   visitees = []
   search_queue = deque()
   search_queue+=eleves[name]
   while search_queue:
      personne = search_queue.popleft()
      if not personne in visitees:
         if personne_elue(personne):
            print(personne + " a le fameux Mac")
            return True
         search_queue += eleves[personne]
         visitees.append(personne)
   return False
if __name__== "__main__":
  search("Boris")


