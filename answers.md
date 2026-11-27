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

**Maximum depth:** $\lceil \log_d((d-1)n + 1) \rceil - 1 = O(\log_d n)$ for a heap with $n$ elements, counting the root as depth 0.

A $d$-ary tree has at most $d^i$ nodes at depth $i$, and by the shape property every level except possibly the last is full. A heap of depth $h$ therefore satisfies $\frac{d^h - 1}{d - 1} < n \le \frac{d^{h+1} - 1}{d - 1}$. Solving for $h$ gives the expression above.


- **3b. (4 pts)** What is the work done by
`delete-min` and `insert` operations in a $d$-ary heap?

**`delete-min`:** $O(d \log_d n)$. When swapping downward, each level requires finding the smallest of up to $d$ children, which costs $O(d)$, over $O(\log_d n)$ levels.

**`insert`:** $O(\log_d n)$. When swapping upward, each level requires only one comparison with the parent, which costs $O(1)$, over $O(\log_d n)$ levels.


- **3c. (5 pts)** What is the work done by Dijkstra's algorithm using a $d$-ary heap?

**Work:** $O(|V| \, d \log_d |V| + |E| \log_d |V|)$

This assumes the heap keeps at most one entry per vertex, and lowers that entry's key (by swapping upward, the same cost as `insert`) when a shorter path is found.

- `delete-min`: at most $|V|$ operations at $O(d \log_d |V|)$ each, for $O(|V| \, d \log_d |V|)$.
- `insert` (including key decreases): at most $|E|$ operations at $O(\log_d |V|)$ each (plus one insert for the source), for $O(|E| \log_d |V|)$.


- **3d. (6 pts)** What value of $d$ yields an overall running time of $O(|E|)$?

**Choose** $d = |E| / |V| = |V|^{\epsilon}$ (rounded up to an integer, and at least 2).

This balances the two terms, since $|V| \, d = |E|$. Then $\log_d |V| = \log_{|V|^{\epsilon}} |V| = 1/\epsilon$, so the total work is

$$O(|V| \, d \log_d |V| + |E| \log_d |V|) = O(|E| / \epsilon) = O(|E|)$$

because $\epsilon$ is a constant greater than 0.


**4. Spanning trees**

- **4a. (3 pts)** Is a solution to MST guaranteed to be a solution to MMET?

**Yes**, every MST is also an MMET.

Suppose $T$ is an MST whose heaviest edge $e$ has weight $w$, and that some spanning tree $T'$ has all of its edges lighter than $w$. Removing $e$ from $T$ splits $T$ into two components. Since $T'$ is spanning, it has an edge $e'$ connecting those two components, and $e'$ is lighter than $e$. Then $T - e + e'$ is a spanning tree with lower total weight than $T$, which contradicts $T$ being an MST. So no spanning tree has a smaller maximum edge than $T$.


- **4b. (3 pts)** Describe algorithm for next best MST.

A next best tree can be obtained from the MST $T$ by swapping a single edge: add one edge that is not in $T$, and remove one edge of $T$ from the cycle this creates. The goal is to find the swap that increases the total weight the least.

1. For each vertex $u$, run a DFS on $T$ starting at $u$. For every vertex $v$ reached, record $M[u][v]$, the heaviest edge on the tree path from $u$ to $v$. When moving from $x$ to $y$, $M[u][y]$ is the heavier of $M[u][x]$ and edge $(x, y)$.
2. For each edge $(u, v)$ not in $T$, compute the increase $w(u, v) - w(M[u][v])$.
3. Pick the edge $(u, v)$ with the smallest increase.
4. Return $T - M[u][v] + (u, v)$. If there are no edges outside $T$, then $T$ is the only spanning tree and there is no next best one.

The increase is never negative, since otherwise $T$ would not be an MST. It is zero when another tree ties with $T$.


- **4c. (2 pts)** What is the work of your algorithm?

**Work:** $O(|V|^2)$

- Step 1: $|V|$ searches of the tree, each costing $O(|V|)$ because a tree has $|V| - 1$ edges, for $O(|V|^2)$.
- Steps 2 and 3: $O(1)$ for each edge outside $T$, for $O(|E|)$.
- Step 4: $O(|V|)$.

The total is $O(|V|^2 + |E|) = O(|V|^2)$, since $|E| \le |V|^2$.
