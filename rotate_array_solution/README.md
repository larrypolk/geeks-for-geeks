# geeks-for-geeks

## Rotate Array Solution

[Rotate Array on Geeks for Geeks](https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements/0)

Given an array of size *N*, rotate it by *D* elements. 

### Input:
The first line of the input contains *T* denoting the number of test cases. First line of test case is the number of elements *N*, next line contains *D*. Subsequent line will be the array elements.

### Output:
For each test case, in a new line, output the rotated array.

#### Constraints:
1 <= T <= 200<br />
1 <= N <= 107<br />
D <= N<br />
1 <= arr[i] <= 103<br />

### Example:
#### Input:
```bash
2
5
2
1 2 3 4 5 
10
3
2 4 6 8 10 12 14 16 18 20
```

#### Output:
```bash
3 4 5 1 2
8 10 12 14 16 18 20 2 4 6
```

### Explanation:
#### Testcase 1:
```bash
1 2 3 4 5 
```

when rotated by 2 elements, it becomes

```bash
3 4 5 1 2
```