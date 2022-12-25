# Insert Sort           
This works by for each element in the array we compare it to every element to its left if it is smaller that the one to the left we swap them then move to the next value to the left. We do this until we have reached the end or we have a value that is smaller than our value. This builds up a sub list that is sorted one element at a time.
![[Pasted image 20220120225121.png]]
An example of it working can be seen bellow
![[Pasted image 20220118133241.png]]
We are looking at the number of comparisons bellow this makes sense since it is the comparison part of the algorithm that will happen at least as much as every other step if not more.

In the worst case for every element we have to compare it all the way to the end of the list so for a list of size $n$ this is
$$
T_\textrm{worst}=\sum_{i=1}^ni^2=\frac{n(n+1)}{2}=\Theta(n^2)
$$
In the best case we don't have to move any items we only compare it once to its left neighbor so we have $O(n)$ time
$$
T_\textrm{best}=\sum_{i=1}^nc=cn=\Theta(n)
$$
Hence the [[Algorithm]] overall is $O(n^2)$ and $\Omega(n)$

**But what about the average case?** If we assume that for any $n$ in the list then if we assume all combinations are equally as likely (this wouldn't necessarily happen in practice) then it will be $\Theta(n^2)$
