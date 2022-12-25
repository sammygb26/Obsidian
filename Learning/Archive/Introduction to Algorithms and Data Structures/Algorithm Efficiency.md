# Algorithm Efficiency
We want to know what makes and [[Algorithm]] efficient and inefficient. We will do this mathematically. The idea here is we are given a task and we want to find an efficient way of computing the answer.

*Example* : Take for example A N M exponential modulation problem. Here you take three numbers a, n, and m (usually with large a, n and m) then you take a^n mod m. What is the most efficient way to calculate this? Doing it in a literal since would take up a large amount of data and become impossible for large numbers so we need a more efficient algorithm.

Another way can be described in pseudo code. We note for 

$$
a^n\textrm{ mod }m = a^2{\lfloor n/2 \rfloor} \textrm{ mod }m
$$ 
If n is even

$$
a^n\textrm{ mod }m = a\cdot a^2{\lfloor n/2 \rfloor} \textrm{ mod }m
$$
If n is odd

This allows us to solve the problem recursively by breaking it into a version of the problem with a smaller n then keeping all the recursive returns smaller than m.

### Types of Efficiency
There are two types of efficiency **temporal** and **spatial**.

**Temporal** is how long an algorithm takes to execute a given task, how long we have to wait before we get our answer, this is often very important in modern computing as memory is more available than computing power.

**Spatial** is how much memory an algorithm takes up in the process of finding the answer. It doesn't matter how fast an algorithm is if it can't fit on a computer then it can't be run at all.

#### In-place algorithms
This is how much space needed for the algorithm grows with the size of the problem. An algorithm is in-place if it has a special complexity of $\Theta(n)$

### [[Sorting]]
Another application of efficiency is sorting. In sorting we want a fast and space efficient algorithm that can sort a given list into order.  A simple but inefficient implementation of this is the [[Insert Sort]] algorithm. Where for each element in the list we check if the number to the left is smaller. If not we swap them we then move on to the left. Another more efficient way is [[Merge Sort]] in this version we split the original list into two smaller lists (the splitting goes on until we read a trivial case with either 2 or 1 element subsists) then sort them and them merge the two sorted lists. The time saving comes since merging of sorted lists is far more efficient that sorting the entire list all together.

### [[Asymptotic Analysis]]
We will look at example of efficient and inefficient algorithms and how can we say a algorithm is good or bad for this we will use [[Asymptotic Analysis]].

## Best case, worst case, average case
We what an estimate of how long our algorithm will take for a problem. We we can't know all possible runtimes so we can either look at $T_{\textrm{worst}}$, $T_{\textrm{best}}$ or $T_{\textrm{average}}$.
![[Pasted image 20220120224758.png]]

[[Algorithmic Efficiency Questions]]