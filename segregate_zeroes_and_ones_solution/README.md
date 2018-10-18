# geeks-for-geeks

## Segregate 0s and 1s Solution

[Segregate 0s and 1s on Geeks for Geeks](https://practice.geeksforgeeks.org/problems/segregate-0s-and-1s/0)

You are given an array of 0s and 1s in random order. Modify the array to segregate 0s on left side and 1s on right side of the array.

### Input:
The first line of input contains an integer *T* denoting the number of test cases. For each test there will be two lines. The first line contains the size of the array *N*. The second line contains the *N* space separated elements of the array.

### Output:
Print the modified array.

### Constraints:
1 ≤ T ≤ 100<br />
1 ≤ N ≤ 107<br />
0 ≤ Ai ≤ 1<br />

### Example:
#### Input:
```bash
2
5
0 0 1 1 0
4
1 1 1 1
```

#### Output:
```bash
0 0 0 1 1
1 1 1 1
```

### Explanation:
#### Testcase 1:

All 0s are segregated to left and all 1s to right of the array. So, the modified array is 

```bash
0 0 0 1 1
```