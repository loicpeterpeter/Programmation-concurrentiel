#importation des bibliotheque
from tkinter import *
from threading import Thread, RLock
from random import *
from math import *
import time
from parametre import *
from fenetre import *

#classe des balles
class ball(object):
	liste=list()#liste contenant les balles afficher
	def __init__(self,name,x,y,col=choice(color)):
		ball.liste.append(self)#quand une balle est créer, l'ajouter dans la liste
		self.name = name
		#coordonnée de la balle
		self.x = x
		self.y = y
		#couleur
		self.col=col
		#direction de la balle
		self.dirx=randint(-1,0)
		self.diry=randint(-1,0)
		if self.dirx==0:self.dirx=1
		if self.diry==0:self.diry=1