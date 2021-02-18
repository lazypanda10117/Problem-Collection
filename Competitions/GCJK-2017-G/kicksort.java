// Google CodeJam Kickstart - 2017 Round G
// Question: Kicksort
// https://code.google.com/codejam/contest/7254486/dashboard#s=p0&a=0

import java.util.*;
import java.io.*;
import java.lang.Math;
import java.util.ArrayList;

/*

4
4
1 4 3 2
4
2 1 3 4
2
2 1
3
1 2 3
 
 */
public class Test1 {

	static boolean bo = true;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		 Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
		 int t = in.nextInt();  // Scanner has functions to read ints, longs, strings, chars, etc.
		 for (int i = 0; i < t; i++) {
			 int p = in.nextInt();
			 ArrayList<Integer> arr = new ArrayList<Integer>();
			 bo = true;
			 for(int j=0; j<p; j++) {
				 int q = in.nextInt();
				 arr.add(q);
			 }
			 tryKicksort(arr);
			 if(bo) {
				 System.out.println("Case #" + (i+1) + ": YES");
			 }else {
				 System.out.println("Case #" + (i+1) + ": NO");
			 }
		 }
	}
	
	public static void tryKicksort(ArrayList<Integer> arr) {
		if(arr.size() <= 1) {
		}else{
			int k = (int) Math.floor((arr.size()-1)/2.0);
			int p = arr.get((int) Math.floor((arr.size()-1)/2.0));
			ArrayList<Integer> a = new ArrayList();
			ArrayList<Integer> b = new ArrayList();			
			if((checkSmall(p,arr)) || checkBig(p,arr)) {
				for(int j =0; j<arr.size(); j++) {
					if(j!=k) {
						if(arr.get(j) <=  p) {
							a.add(arr.get(j));
						}else {
							b.add(arr.get(j));
						}
					}
				}
				tryKicksort(b);
			}else {
				bo = false;
			}	
		}
	}
	public static boolean checkSmall(int a, ArrayList<Integer> arr) {
		for(int i=0; i<arr.size(); i++) {
			if(a > arr.get(i)) {
				return false;
			}
		}
		return true;
	}
	public static boolean checkBig(int a, ArrayList<Integer> arr) {
		for(int i=0; i<arr.size(); i++) {
			if(a < arr.get(i)) {
				return false;
			}
		}
		return true;
	}
}
