# Coin-changing problem
Here we want to give out the least number of coins to sum to a particular sum. The denominations are the different values of the coins and we want them to sum to a value $v$. We assume some solution exists for $v$. We return a *multiset* that sums to $v$ made out of numbers of each denomination.

We know for some solution there will be a $c_i$ coin then there must also be a solution to $v-c_i$ since we defined $c_i$ as part of the solution. The solution for $v$ is 1 plus the solution to $v-c_i$ (as it is just this solution plus the coin $c_i$) so we just need to find $c_i$. We can look at all possible coins and find every combination of coins that sum to $v$. Then we take the number with the minimum number of coins.

![[Pasted image 20220120190316.png]]

We have to look at the *subproblems* for this recursive solution. We know all the calls will be for values less than $v$. So we can store all values up to $v$ and we can work up solving . Since we are ordering the problems so that for any recursion on a $v$ we already know its solution we can easily cut to the chase and not search all possible solutions.

![[Pasted image 20220120214905.png]]

**So for dynamic programming we want to cut out large searches and instead save a set of problems that could make up our recursive problem**. This is why it can be thought of as working up from the bottom of a recursive  tree.
