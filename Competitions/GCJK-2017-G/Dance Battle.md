# Question 2 GCKS

### Question Details:
> Question ID: 2
> 
> Question Name: Dance Battle
> 
> Question Description: Your team is about to prove itself in a dance battle! Initially, your team has E points of energy, and zero points of honor. There are N rival teams who you must face; the i-th of these teams is the i-th in a lineup, and has a dancing skill of Si.
> 
> In each round of battle, you will face the next rival team in the lineup, and you can take one of the following actions:
> 
> - Dance: Your team loses energy equal to the dancing skill of the rival team, and that team does not return to the lineup. You gain one point of honor. You cannot take this action if it would make your energy drop to 0 or less.
> - Delay: You make excuses ("our shoes aren't tied!") and the rival team returns to the back of the lineup. Your energy and honor do not change.
> - Truce: You declare a truce with the rival team, and that team does not return to the lineup. Your energy and honor do not change.
> - Recruit: You recruit the rival team onto your team, and that team does not return to the lineup. Your team gains energy equal to the dancing skill of the rival team, but you lose one point of honor. You cannot take this action if it would make your honor drop below 0.
> 
> The battle is over when there are no more rival teams in the lineup. If you make optimal decisions, what is the maximum amount of honor you can have when the battle is over.
> Question Note:
> 
> Small dataset
> 
> ```
> 1 ≤ N ≤ 5.
> ```
> 
> Large dataset
> 
> ```
> 1 ≤ N ≤ 1000.
> ```
> Limits
> 
> ```
> 1 ≤ T ≤ 100.
> 1 ≤ E ≤ 106.
> 1 ≤ Si ≤ 106, for all i.
> ```
> Question Difficulty: 
> 
> Question Example:
> 
> ```
> Input 
> The first line of the input gives the number of test cases, T. T test cases follow; each consists of two lines. The first line consists of two integers E and N: your team's energy, and the number of rival teams. The second line consists of N integers Si; the i-th of these represents the dancing skill of the rival team that is i-th in line at the start of the battle.
> 
> Output 
> For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the maximum amount of honor you can have when the battle is over.
> ``` 
> ```
> Input
> 2
> 100 1
> 100
> 10 3
> 20 3 15 	
> 
> Output 
> Case #1: 0
> Case #2: 1
> ```
> Question Reference: [Question 2 Link](https://code.google.com/codejam/contest/7254486/dashboard#s=p1&a=1)


### Solution Details
__Solution Main Idea__:

__Solution Analysis__:
> Runtime Analysis:
> 
> Auxillary Space Analysis: 

__Solution Implementation__:

```java
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
```