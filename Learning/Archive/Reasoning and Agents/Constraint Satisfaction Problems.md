# Constraint Satisfaction Problems
[[Search]] strategies use **atomic** states that are indivisible here states and the actions taking us between them are more expressive and reasoned. A **Constraint Satisfaction Problem** has three parts

1. **Variables** -> we use $X$ to be the set of variables $\{X_1, X_2 ... X_n\}$ in a CPS
2. **Domains** -> we use $D$ to be the set of domains for the variables $\{D_1, D-2...D_n\}$ each $D_i=\{v_1,v_2...v_k\}$
3. **Constraints** -> we use $C$ to be the set of constraints the describe what combinations of assignments fulfill the problem.

A variables $X_i$ can be assigned to any of the values from its domain so if $D_i=\{v_1,v_2...v_k\}$ we can say $X_i=v_u$ for any $u\in [1,k]$. We must assign all variables to have a solution to the **CSP**. But this must also satisfy the **Constraints** they are made out of two parts. $C_i=\langle scope, rel\rangle$. The $scope$ is a tuple of variables and $rel$ is a relation that says if a combination of the variables in the $scope$ is allowed. An example would be a map coloring problem. We can make each section a variables then their domains will be the colors we can choose. The constraints will be that any adjacent states don't have the same color. Below the variables are nodes and the constraints are edges.

![[Pasted image 20220212094441.png]]

A **binary CSP** is a CSP where every constraint is between two variables for example $\langle (\textrm{WA}, \textrm{NT}), \textrm{WA}\neq \textrm{NT} \rangle$. These are easy to work with and any higher order CPS can be converted to a binary CSP with the addition of new variables. There are also **unary** constraints which have a single variables as their $scope$. There is also **global** constraints where a constrains relates all variables.  For example with **cryptarithmetic** puzzles. Here there is a hypergraph instead of a binary graph.

![[Pasted image 20220212100108.png]]

**CSP** works better for specific problems as we can avoid exploring certain paths knowing they will never be a solution as a given constraint is not met. In regular search we just ask if we have found a goal we have no concept of some states never leading to the goal. 

We can also have **preference constraints** which indicate what solutions are preferred. We can use them to guide the search to an optimal solution. A problem that isn't solved or not that has some preferred solution is called a **constraint optimization problem**.

## Inference
When we are searching for a solution we can do two things. Either we assign a value to a variable. Or we reduce the number of possible values for a variable based on previous assignments. This is a type of **inference** called **constrains propagation**. The idea here is we enforce **local consistency**. That is if we look at our problem as a graph we make sure any possible assignments satisfy the constrains to neighboring nodes. There are two types of **local consistency**

1. **Node Consistency** -> This is when the domain of a variable is consistently with that variables **unary constraint** at this point we call the node **node consistent**. We remove all unary constrains by following this rule of elimination (inference).
2. **Arc Consistency** -> This is when every value in the domain of a variable satisfiers that variables **binary constraints**. We say $X_i$ is consistent with another variable $X_j$ if for every value in the current domain of $X_i$ there is a value in $X_j$ that would satisfy the binary constraint between the two. If for some value for $X_i$ there is no value in $X_j$ we can remove this value as it can never be a solution. We would then say $X_i$ is arc consistent with respect to $X_j$. We may later have to make the reverse true.

## AC-3 Algorithm
This attempts to make every variable **arc consistent**. It maintains a queue of arcs (binary constraints) though the order of removal doesn't matter. An arc between some $X_i$ and $X_j$ is Revised making it consistent. If the domain of $X_i$ is unchanged we move onto the next constraint. But if it is reduced we need to add all the arcs to $X_i$ that is for all $k$ $X_k$ to $X_i$ arc must be re examined.  As if we have previously checked them the values making that allowed them to be consistent could have been removed from $X_i$ hence we need to do another pass.

![[Pasted image 20220212102520.png]]

If the domain of $X_i$ is reduced to $\emptyset$ then there are not possible values that for the assignment we have given to AC-3 so it returns false. We can continue to search after using AC-3 as the domains will be reduced this will make the search faster as well as pruning many dead end paths.  

#### Complexity
We consider the complexity for a CPS with $n$ variables, each with a domain size at most $d$ with $c$ binary arc. We know any given ark can be queued at most $d$ times since some $X_i$ only has at most $d$ variables that can be removed. Checking consistency for a single arc can be done in $O(d^2)$ time as we will check over every value each time the arc is added as we have to compare every combination of values. In total it will take $O(cd^3)$ then since $c$ arcs can be enqueued at most $d$ times.

## Backtracking Search
This approach is simple we just assign a random variable to some value making a new node. We can perform inference on this to check its values ahead of time. If its still consistent when we assign another variable and if not we go back and try the next value. If we run out of values we go back the the previous consistently assigned value and try another. This is basically **DFS** but we use inference to prune options. Each **state** is a **partial assignment of variables**.

![[Pasted image 20220212105022.png]]

This ignores the **commutativity** of a **CPS** problem meaning the order of the actions doesn't matter to the solution. We can also have the values be commutative for example with the coloring version the colors are different in how we apply the constraints to them so we need not consider different combinations of colors only valid solutions. This will mean we have $d^n$ possible assignments (ignoring consistency) for $d$ values over $n$ variables.

![[Pasted image 20220212111101.png]]

## Variable and Value Ordering
We are simply using "select-unassigned-variable" simply in some order they are given but is there a way to select values that will reduce the amount we have to search. If we pick values that have the most values to assign we remove options later to make our solution consistent. The idea is instead to use a **heuristic** to find values that will keep our options the least open if we don't choose them. So we might as well constrain them now. This is called the **MRV** **minimum-remaining-values** heuristic. The order we assign variables is always to the one with the least possible values. We can also combine this with a **most constrained** tie-breaker. So we always select the variable that will lead to the fewest consistent partial assignment so branching is reduced.

We also have "order-domain-values" we could again just go with whatever order but is there a way to order that will ensure we run into the least dead ends. We can use the **LCV** heuristic or **least constraining value** that is we pick the value that leaves us with the most possible values later hence we keep our options open reducing the chance of us reducing a domain to $\emptyset$.

[[Constraint Satisfaction Problems Questions]]