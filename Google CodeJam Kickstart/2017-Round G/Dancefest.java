import java.util.*;
import java.io.*;
import java.lang.Math;

/*
2
100 1
100
10 3
20 3 15
 
 
1
10 3
20 3 15 
 
 */

public class Test2 {
	static int energy = 0;
	static int honour = 0;
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		 Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
		 int t = in.nextInt();  // Scanner has functions to read ints, longs, strings, chars, etc.
		 for (int i = 0; i < t; i++) {
			 //System.out.println("iter: " + i);
			 ArrayList<Integer> arr = new ArrayList<Integer>();
			 int e = in.nextInt();
			 //System.out.println("energy: " + e);
			 energy = e;
			 int r = in.nextInt();
			 honour = 0;
			 //System.out.println("rivals: " + r);
			 for(int j=0; j<r; j++) {
				 int a = in.nextInt();
				 //System.out.println("nxt int: " + a);
				 arr.add(a);
				 //System.out.println("arrr: " + arr.get(j));
			 }
			 Integer[] tL = new Integer[arr.size()];
			 tL = arr.toArray(tL);
			 Arrays.sort(tL);
			 
			 /*System.out.println("ab");
			 for(int h=0; h<tL.length;h++) {
				 System.out.print(tL[h] +", ");
			 }*/
			 
			 ArrayList<Integer> ac = new ArrayList<Integer>();
			 for(int k=0; k<tL.length; k++) {
				 ac.add(tL[k]);
			 }
			 boolean ba = true;
			 for(int p=0; p<ac.size(); p++) {
				 if(energy > sumOfArray(ac)) {
					 break;
				 }else{
					 if(ac.get(p) >= energy) {
						 //System.out.println(ac.get(p));
						 //recruit if not last
						 if(honour > 0) {
						 //System.out.println("h > 0");
							 if(ac.size() > 1) {
								 energy += ac.get(ac.size()-1);
								 ac.remove(ac.size()-1);
								 honour -= 1;
							 }else {
								 //System.out.println("hi");
								 ba=false;
								 break;
							 }
						 }else {
							 //System.out.println("bye");
							 ba=false;
							 break;
						 }
					 }else {
						 energy -= ac.get(p);
						 ac.remove(p);
						 honour += 1;
					 }
						 /*
					 }
					 else{
						 if(ac.get(p) >= energy) {
							 //System.out.println("hh: " + honour);
							 ba = false;
							 break;
						 }else {
							 //System.out.println("e > 0");
							 
						 }
					 }*/
				 }
				 p--;
			 }
			 if(!ba) {
				 System.out.println("Case #" + (i+1) + ": " + honour);
			 }else{
				 System.out.println("Case #" + (i+1) + ": " + (int)(honour + ac.size()));
			 }
		 }
	}
	
	public static int sumOfArray(ArrayList<Integer> aL) {
		int sum = 0;
		for(int i=0; i<aL.size(); i++){
			//System.out.println(aL.get(i));
			sum += aL.get(i);
		}
		//System.out.println("SA: " + sum);
		return sum;
	}
}


