import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Container;
import java.awt.Graphics;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.util.Random;
import java.util.Vector;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class Fenetre extends JFrame implements ActionListener {
	JButton start;
	JButton plus;
	JButton moins;
	JLabel horloge;
	JLabel score;
	Ball test;
	Ball test2;
	public boolean pause;
	Vector<Ball> dessins = new Vector<Ball>() ;
	double minx , miny , maxx , maxy;
	Container contentPane = getContentPane();
	JPanel ballzone = new JPanel() ;
	JPanel buttonzone = new JPanel(new GridLayout(1,10));
	int time;
	int ball_size;
	int score_value;

	public Fenetre(String titre ){
		super(titre);
		setLocation(10,150);
		setVisible(true);
		setSize(1600,900);
		ball_size = 10;
		start = new JButton("Pause");
		plus = new JButton("+");
		moins = new JButton("-");
		horloge = new JLabel("00:00");
		score = new JLabel("0");
		start.addActionListener(this);
		plus.addActionListener(this);
		moins.addActionListener(this);
		pause = false;
		contentPane.add(buttonzone,BorderLayout.SOUTH);
		contentPane.add(ballzone,BorderLayout.CENTER);
		ballzone.setBackground(new Color(0.5f,0.5f,0.5f));
		buttonzone.add(start);
		buttonzone.add(plus);
		buttonzone.add(moins);
		buttonzone.add(horloge);
		buttonzone.add(score);
		minx = contentPane.getBounds().getMinX();
		miny = contentPane.getBounds().getMinY();
		maxx = contentPane.getBounds().getMaxX();
		maxy = contentPane.getBounds().getMaxY();


	    score_value = 0;

		time = 0;
		repaint();

	}


	
	@Override
	public void paint(Graphics g){
		super.paint(g);
		score.setText("" + score_value);
		horloge.setText("00:" + time);
		for(int i=0;i<dessins.size();i++){
		dessins.get(i).draw(g);
		}
	}

	
	@Override
	public void actionPerformed(ActionEvent e) {

		Object source = e.getSource();
		if(source == plus){
			Random test = new Random();
			
			int newx = (int) (minx + (test.nextInt((int) maxx) - minx));
			int newy = (int) (miny + (test.nextInt((int) maxy) - miny));

			float red = (float)test.nextInt((int)10)/10;
			float green= (float)test.nextInt((int)10)/10;
			float blue= (float)test.nextInt((int)10)/10;
			Color color = new Color(red,green,blue);
			
			int newvx = (int) (-5 + (test.nextInt((int) 5) ));
			int newvy = (int) (-5 + (test.nextInt((int) 5) ));
			dessins.addElement(new Ball(newx,newy,newvx,newvx,10 , minx , miny , maxx , maxy , color));
		}
	
		if(source == moins){
			dessins.remove(dessins.size()-1);
		}
		if(source == start){
			pause = !pause;
			if(pause){
				start.setText("Start");
			}
			else{
				start.setText("Pause");
			}
		}		
	}
}