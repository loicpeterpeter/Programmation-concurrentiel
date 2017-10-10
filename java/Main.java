public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Fenetre fenetre = new Fenetre("fenetre");
		Physique physique = new Physique(fenetre);
		Affiche affiche = new Affiche(fenetre);
		Timer timer = new Timer(fenetre);
		affiche.start();physique.start();
		timer.start();
	}

}
