# All Pairs Shortest path

- Floyd Warshall O(n^3)
- n-Dijkstra O($N^2logN$)
- Matrix Multiplication O($n^2.37$)

## Matrix Multiplication

### Finding no of paths of exact length i between 2 nodes

- Have a adcancey matrix `A`,denoting path exists or not [0/1].
- If A[i][j] in $A^n$ denotes path of length n between `i`,`j`

### Finding minimum distance with atmost k edges.

- B[i, j] = min{ A[i,j], mink {A[i, k] + A[k, j]}}  for two edges
- Extending this for N edges , do $A^n$

## Using Ear Decomposition

- If multiple edges exist between 2 vertex , remove everything except the shortest.

