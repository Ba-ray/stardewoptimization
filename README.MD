# Using ILP (Integer Linear Programming) to solve as combinatorial optimization problem

## Defining the Problem

The input for this problem will be a grid representing the farmland we need to distribute sprinklers on:

$ F(r,c) \in \{0,1 \}$
- $F(r,c) = 1$ : Farmable Land
- $F(r,c) = 0$ : Unfarmable Land

### Problem variables

**Sprinklers:**
$$
S(r,c) \in \{0,1\} \\
- 0 : No\ sprinkler\ placed \\
- 1 : Sprinkler\ placed 
$$

**Watered cells:**
$$
W(r,c) \in \{0,1\} \\
- 0 : Unwatered \\
- 1 : Watered
$$

**Objective:**
Maximize number of watered farmable cells while minimizing number of sprinklers used (fine tune the punishment for placing a sprinkler depending on your needs)
$$
\displaystyle\sum_{r=1}^{rows}\sum_{c=1}^{cols} W(r,c)\ .\ F(r,c)\ -\ \displaystyle\sum_{r=1}^{rows}\sum_{c=1}^{cols} S(r,c)
$$

For example, having a very high punishment for placing a sprinkler (-30 for each sprinkler) will surely prevent the placement of sprinklers since you will never be able to water enough crops with a sprinkler(iridium provides 24 watered crops at best) to get a positive reward.

### Constraints

**For a farmable cell \((i, j)\):**
$$
W(i, j) \leq \sum_{(di,dj) \in N} S(di, dj)\ .\ F(di,dj)
$$
where:
- N is the set of points in the 5x5 area around $F_{ij}$ (areas where an iridium sprinkler can reach the point)

**If a sprinkler is placed in a cell, that cell cannot be marked as watered:**
$$
W(i, j) \leq 1 - S(i, j)
$$