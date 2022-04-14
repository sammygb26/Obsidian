# The Master Theorem
The master theorem is used to get a quick estimate of the time complexity for recursive algorithms. It take into account the proportional change in problem size between each recursion, the amount of work done and the number of recursive calls made. This comes from the idea of **divide and conquer** where we have three steps to any recursion. **Divide** where we split up problems into subproblems. **Conquer** where we solve simple base case root problems. Then **Combine** where we take these solutions and build up our full solution form them. 

To apply **divide and conquer** we need to have subproblems that are smaller than out main problem. Then we also need our subproblems to bottom out with a base case.

## Recurrences
Recurrences are helpful when talking about divide and conquer. A **recurrence** is an equation or inequality that describes a function in terms of its value on smaller inputs. For example

![[Pasted image 20220224121011.png]]

We use $\Theta(1)$ to show that there is just some constant time taken or a function that returns some constant bounded values. To **solve** a recurrence to find time-complexity we need to express the function as a single value based on the input size.

## Master Theorem
If our **recurrence** has the form

![[Pasted image 20220224123238.png]]

We can apply the **master theorem** to solve it. If we call $e=log_b\hspace{2pt}a$ then the master theorem can be given as a function giving the $\Theta$ runtime of the recurrence.

![[Pasted image 20220224123449.png]]

The way this works out is the relationship between $a$ and $b$ describes how the complexity shrinks relatively. But $k$ describes the complexity needed for each instance on its own. These forces are battling and whichever one has the creates influence will have the final say (accept if $e=k$ where there is some middle ground)