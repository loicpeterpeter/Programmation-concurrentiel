#importation des bibliotheque
from tkinter import *
from threading import Thread, RLock
from random import *
from math import *
import time
from parametre import *
from fenetre import *
from ball import *
from calcul import *

#lancement du programme
main=affichage()
main.start()
c=calcul()
c.start()
main.fenetre.mainloop()