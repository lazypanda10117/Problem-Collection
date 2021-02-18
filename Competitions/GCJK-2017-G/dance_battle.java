// Google CodeJam Kickstart - 2017 Round G
// Question: Dance Battle
// https://code.google.com/codejam/contest/7254486/dashboard#s=p1&a=1

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
		Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
		int t = in.nextInt();  // Scanner has functions to read ints, longs, strings, chars, etc.
		for (int i = 0; i < t; i ++) {
			ArrayList<Integer> arr = new ArrayList<Integer>();
			int e = in.nextInt();
			int r = in.nextInt();

			boolean ba = true;
			
			energy = e;
			honour = 0;

			for(int j = 0; j < r; j ++) {
				int a = in.nextInt();
				arr.add(a);
			}
			
			Integer[] tL = new Integer[arr.size()];
			tL = arr.toArray(tL);
			Arrays.sort(tL); 
			 
			ArrayList<Integer> ac = new ArrayList<Integer>();
			for(int k = 0; k < tL.length; k ++) {
				ac.add(tL[k]);
			}			

			for(int p = 0; p < ac.size(); p ++) {
				if(energy > sumOfArray(ac)) {
					break;
				}else{
					if(ac.get(p) >= energy) {
						if(honour > 0) {
							if(ac.size() > 1) {
								energy += ac.get(ac.size()-1);
								ac.remove(ac.size()-1);
								honour -= 1;
							}else {
								ba = false;
								break;
							}
						}else {
							ba = false;
							break;
						}
					} else {
						energy -= ac.get(p);
						ac.remove(p);
						honour += 1;
					}
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
			sum += aL.get(i);
		}
		return sum;
	}
}
