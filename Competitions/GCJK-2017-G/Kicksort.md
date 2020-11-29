# Question 1 GCKS

### Question Details:
> Question ID: 1
> 
> Question Name: Kicksort
> 
> Question Description: Here at Kickstart, we are fans of the well-known Quicksort algorithm, which chooses a pivot value from a list, moves each other value into one of two new lists depending on how it compares with the pivot value, and then recursively sorts each of those new lists. However, the algorithm might choose a pivot that causes all of the other values to end up in only one of the two new lists, which defeats the purpose of the divide-and-conquer strategy. We call such a pivot a worst-case pivot.
>
> To try to avoid this problem, we have created our own variant, Kicksort. Someone told us that it is good to use a value in the middle as a pivot, so our algorithm works as follows:
>
```
Kicksort(A): // A is a 0-indexed array with E elements
    If E ≤ 1, return A.
    Otherwise:
      Create empty new lists B and C.
      Choose A[floor((E-1)/2)] as the pivot P.
      For i = 0 to E-1, except for i = floor((E-1)/2):
        If A[i] ≤ P, append it to B.
        Otherwise, append it to C.
    Return the list Kicksort(B) + P + Kicksort(C). 
``` 
> For practice, we are trying Kicksort out on lists that are permutations of the numbers 1 through N. Unfortunately, it looks like Kicksort still has the same problem as Quicksort: it is possible for every pivot to be a worst-case pivot!
> 
> For example, consider the list 1 4 3 2. Kicksort will choose 4 as a pivot, and all of the other values 1 3 2 will end up in one of the two new lists. Then, when Kicksort is called on that list 1 3 2, it will choose 3, and once again, all of the other values will end up in one of the two new lists. Finally, it will choose 1 from the list 1 2, and the other value 2 will of course end up in only one of the two new lists. In every case, the algorithm will choose a worst-case pivot. (Notice that when Kicksort is called on a list with 0 or 1 elements, it does not choose a pivot at all.)
> 
> Please help us investigate this further! Given a permutation of the numbers 1 through N, determine whether Kicksort will choose only worst-case pivots.
> 
> Question Note:
> 
> Small dataset
> 
> ```
> 1 ≤ T ≤ 32.
> 2 ≤ N ≤ 4.
> ```
> 
> Large dataset
> 
> ```
> 1 ≤ T ≤ 100.
> 2 ≤ N ≤ 10000.
> ```
> Limits
> 
> The values Ai are a permutation of the values from 1 to N.
> 
> Question Difficulty: 
> 
> Question Example:
> 
> ```
> Input 
> 4
> 4
> 1 4 3 2
> 4
> 2 1 3 4
> 2
> 2 1
> 3
> 1 2 3
> Output 
> Case #1: YES
> Case #2: NO
> Case #3: YES
> Case #4: NO
> ``` 
> Question Reference: [Question 1 Link](https://code.google.com/codejam/contest/7254486/dashboard#s=p0&a=0)


### Solution Details
__Solution Main Idea__:

__Solution Analysis__:
> Runtime Analysis: O(nlog(n))?, it is fundementally quicksort but on one side. `T(n) = T(n/2) + O(n)`
> 
> Auxillary Space Analysis: 

__Solution Implementation__:

```java
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
```