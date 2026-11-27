# CMPS 2200 Assignment 6
## Answers

**Name:** Chuong Hoang Pham
_________________________


Place all written answers from `assignment-06.md` here for easier grading.


**1. Shortest shortest paths**

- **1b. (2 pts)** Work and span of `shortest_shortest_path`

**Work:** $O((|V| + |E|) \log |V|)$, which is $O(|E| \log |V|)$ when every vertex is reachable from the source.

The algorithm is Dijkstra's algorithm with heap entries ordered by (weight, number of edges). Each vertex is finalized at most once, so each edge is scanned at most once and causes at most one `heappush`. The heap therefore holds $O(|E|)$ entries, and each `heappush` or `heappop` costs $O(\log |E|) = O(\log |V|)$, since $|E| \le |V|^2$. Comparing the tuples takes $O(1)$, so tracking the number of edges does not change the bound.

**Span:** $O((|V| + |E|) \log |V|)$, the same as the work.

The algorithm is sequential: each `heappop` depends on the pushes made before it, and the edges are processed one at a time.



**3. Improving Dijkstra**

- **3a. (4 pts)** What is the maximum
depth of a $d$-ary heap?


- **3b. (4 pts)** What is the work done by
`delete-min` and `insert` operations in a $d$-ary heap?


- **3c. (5 pts)** What is the work done by Dijkstra's algorithm using a $d$-ary heap?


- **3d. (6 pts)** What value of $d$ yields an overall running time of $O(|E|)$?


**4. Spanning trees**

- **4a. (3 pts)** Is a solution to MST guaranteed to be a solution to MMET?


- **4b. (3 pts)** Describe algorithm for next best MST.


- **4c. (2 pts)** What is the work of your algorithm?
