#importation des bibliotheque
from tkinter import *
from threading import Thread, RLock
from random import *
from math import *
import time
from parametre import *
from fenetre import *
from ball import *

class calcul(Thread):
	do=True #boolean qui gere la boucle de calcul
	def __init__(self):
		Thread.__init__(self)
		self.daemon=True
	def run(self):
		while 1:
			self.do=affichage.do
			if self.do:
				#pour chaque balle dans la liste, deplacer les balles
				for i in ball.liste:
					i.x+=i.dirx
					i.y+=i.diry
					#si la balle touche un bord, inverser sa direction
					if i.x<=0 or i.x>=largeur-taille:
						i.dirx=-i.dirx
					if i.y<=0 or i.y>=hauteur-taille:
						i.diry=-i.diry
					for element in ball.liste:
						if element!=i:
							affichage.x.collision(element,i)
			time.sleep(0.01)

