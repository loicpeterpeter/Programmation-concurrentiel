#importation des bibliotheque
from tkinter import *
from threading import Thread, RLock
from random import *
from math import *
import time
from parametre import *
from ball import *

#thread pour la fenetre
class affichage(Thread):
	x=None
	nb=0 #nombre de balle
	score = 0 #score
	do=True
	
	def __init__(self):
		Thread.__init__(self)
		self.fenetre=Tk()
		affichage.x=self
		self.daemon=True 		
		self.temps=0
		self.recall=0
		#texte nombre de balle
		self.nb_ball=Label(self.fenetre,text="nombre de balle: {}".format(self.nb))
		self.nb_ball.pack()

		#texte score
		self.n_score=Label(self.fenetre,text="score: {}".format(self.score))
		self.n_score.pack() 

		self.temps=Label(self.fenetre,text="temps: {}".format(self.temps))
		self.temps.pack()
		#Canvas
		self.canvas = Canvas(self.fenetre, width=largeur, height=hauteur, background='white')
		self.canvas.pack()
		#boutton quitter
		self.bouton_quitter = Button(self.fenetre, text="Quitter", command=self.close)
		self.bouton_quitter.pack(side="bottom")
		
		self.Frame_balle=Frame(self.fenetre, borderwidth=2, relief=GROOVE)
		self.Frame_balle.pack()

		#boutton ajout
		self.ajout= Button(self.Frame_balle,text="+",command=self.ajout)
		self.ajout.pack(side=LEFT)
		#boutton retirer
		self.retrait= Button(self.Frame_balle,text="-",command=self.retrait)
		self.retrait.pack(side=RIGHT)
		#boutton pause
		self.pause= Button(self.fenetre,text="STOP",command=self.pause)
		self.pause.pack()

	# thread pour actualiser la fenetre
	def run(self):
		while 1:
			temps=int(time.clock())-self.recall
			for i in ball.liste: #deplacement des balles
				self.canvas.coords(i.name,i.x+i.dirx,i.y+i.diry,i.x+i.dirx+taille,i.y+i.diry+taille)
			#actualisation des textes
			self.nb_ball["text"]=("nombre de balle: {}".format(affichage.nb))
			self.n_score["text"]=("score: {}".format(affichage.score))
			#controle du timer
			if affichage.do:
				self.temps["text"]=("temps: {}".format(temps))
			else:
				self.recall=int(time.clock())-temps

	#fonction qui active ou desactive le thread de calcul
	def pause(self):
		if affichage.do:
			affichage.do=False
			self.pause["text"]=("START")
		else:
			affichage.do=True
			self.pause["text"]=("STOP")

	#fonction qui ajoute les balles
	def ajout(self):
		if self.nb<5:
			#selectionne des coordonnée aleatoires pour la balle
			x=randint(taille,hauteur-taille)
			y=randint(taille,largeur-taille)
			#selection d'une couleur aleatoire
			col=choice(color)
			#creation de la balle
			name=self.canvas.create_oval(x,y,x+taille,y+taille,fill=col)
			ball(name,x,y,col)
			#actualiser l'affichage
			affichage.nb+=1
			self.nb_ball["text"]=("nombre de balle: {}".format(self.nb))
	
	#fonction qui retire la balles
	def retrait(self):
		#si il y a des balles dans la liste
		if ball.liste!=[]:
			#supprime la derniere balle de la liste
			supp=self.canvas.find_all()
			self.canvas.delete(supp[len(supp)-1])
			ball.liste.pop(len(ball.liste)-1)
			#actualisation de l'affichage
			affichage.nb-=1
			self.nb_ball["text"]=("nombre de balle: {}".format(self.nb))

	#fonction qui gere les collisions
	def collision(self,p,q):
		#detection de la collision
		x=q.x-p.x
		y=q.y-p.y
		dist=x*x+y*y

		if (sqrt(dist))<=(taille):
			#si collision, supprimer les deux balles
			affichage.nb-=2
			affichage.score+=2
			ball.liste.remove(p)
			ball.liste.remove(q)
			self.canvas.delete(p.name)
			self.canvas.delete(q.name)

	#fonction qui ferme la fenetre
	def close(self):
		self.fenetre.quit()
