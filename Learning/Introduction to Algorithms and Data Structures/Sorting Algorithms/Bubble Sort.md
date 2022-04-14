# Bubble Sort
**Bubble Sort** is a simple sorting algorithm. The way it works is we go through every element in the array and for each we go down all the element behind it in the array and check it against its right element if it is larger we swap the two.
![[Pasted image 20220211115454.png]]

## Proof of correctness
We can prove this with a **loop invariant**. To do this we want to show that something about the array is maintained throughout all the loops and that this by the end will  lead to a sorted array. What we want by the end is to go from a list $A$ to a new list $A'$ where 
$$
A'[1]\le A'[2]\le ...\le A'[n]
$$
Where $n=A.\textrm{length}$. We need a loop invariant and we need to show how termination of this ensures the above property.

**Loop Invariant** -> We would like for each loop the loop up to $A'[i]$ to be in order. That is for each loop we want 
$$
A[1]\le ...\le A[i+1]
$$
Then if this is true when $i=n-1$ when the final condition must hold. We also want is so that all $\forall j\in(i+1,n). A[j]\ge A[i+1]$.

**Initialization** -> There is some smallest $A[x]$ that $\forall i\in[1,n]. A[x]\le A[i]$. In the first loop $j$ will vary from $n$ all the way down to $j=2$. This means that every adjacent pair in the list is checked over. Once $x=j$ that is $A[j]$ is the smallest element then $A[j]<A[j-1]$ is always true. Hence the value in $A[x]$ will be swapped continuously until it is swapped into $A[1]$. Then $i=1$ so the loop invariant only matters over $A[1]$ and $A[2]$ hence since $A[1]$ contains the smallest value for which all other $A$ values are larger or equal this must be true. The second condition must also be true as if wasn't true this would mean there is some element in $A$ that is smaller than $A[1]$ that  isn't $A[1]$ but this contradicts that $A[x]$ was the smallest value in $A$ at the start of the loop.

**Maintenance** -> If for some $i$ at the start of the loop $A[1]\le...A[i]$. Then there will be some element $A[x]$ where $x\in [i+1,n]$ that for for which it is the case that $\forall y\in[i+1,n]. A[x]\le A[y]$. Then in our secondary loop once $j=x$ we will always have the condition for the if statement be true. Hence the value in $A[x]$ will move down to $A[i+1]$. Now we know form the loop invariant that all the values from $\forall y\in(i,n).  A[y]\ge A[i]$ was true at the start of the loop. Since $x\in(i,n)$ the condition must also hold when $y=x$ Hence once the value in $A[x]$ has moved to $A[i+1]$ it must still be the case that the value that was in $A[x]\ge A[i]$ hence $A[i]\le A[i+1]$ at then end of the loop since the value in $x$ must go to $A[i+1]$. So the first part of the invariant is met. The second part must be true as if we take the inverse $\exists j\in(i+1,n). A[j]<A[i+1]$ contradicts $A[x]$ being the smallest value in the array from $i+1$ unto $n$ this is a condition so cannot be the case so the second condition is met.

**Termination** -> In the last cycle $i=n-1$, so $i+1=n$ but after the loop executes we know it must be the case that
$$
A[1]\le...\le A[i+1]
$$
therefore it must be the case that
$$
A[1]\le...\le A[n]
$$
So by definition the array must be sorted.