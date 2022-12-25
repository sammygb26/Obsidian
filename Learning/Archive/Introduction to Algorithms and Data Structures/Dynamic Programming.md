# Dynamic Programming
This is a technique use for **optimization** where we want to find the **best** solution to a problem. Hence these algorithms are more computationally difficult. The idea is to structure the problem in terms of a recurrence relation, this breaks our problem down into subproblems. If we can then find an [[Algorithm]] to *compute* and *store* all the subproblems we **may** need for our solution in polynomial time $O(n^k)$

Divide and Conquer another problem solving tequniques where we split up some $n$ size problem into smaller ones. We can recursively do this and then we can take the smaller parts together to get the solution. The splitting up increases efficiency if the pieces are *proportionally* small enough. But if they are not these algorithms can be very costly taking exponential time $O(k^n)$

## Common Features in Dynamic Programming
1. Understand the problem well enough to understand the structure so that we can find solutions for smaller problems and bring them together. So we generalize so that we will compute **items we do not need** but are still less than the problem we are solving.
2. We need to find a way to write it in a recursive way such that the problems are strictly smaller. This is what allows us to build up in terms of smaller versions up to the larger one.
3. We need a way to organize the result for subproblems that is polynomial bounded by the size of the problem that is meaningful enough to help us for the final solution.
4. Need an algorithm that controls the order of solving subproblems so the right hand side of a recurrence is solved before the left hand side is needed.



**Memoization** can be used to implement a dynamic approach over a recursive solution. In this we simply check if we have already calculated a solution to a recursion and if we have we just return that. We just keep track of what we have calculated. This can be implemented with a wrapper
![[Pasted image 20220120185037.png]]
You can just check if a program is suffering from recursion based inefficiency by running a memoized version.

## Problems
Many problems can be solved via dynamic programming such as [[Coin Change]], [[Fibonacci Numbers]], [[Seam Carving]], [[Edit Distance]], [[Viterbi Algorithm]] and [[All-pairs shortest paths]].

[[Dynamic Programming Questions]]
