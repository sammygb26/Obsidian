# Quick-Sort
Quick sort is another sorting algorithm. The way it works is so quicksort some section on an array we pick some pivot and sort everything bigger into  one side of the array and everything smaller into the other. The pivot is then placed back into the order. We then recursively do this for each subsection.

![[Pasted image 20220428111035.png]]

The main algorithm is given like this where $Partition$ performs the pivoting of the array form $p$ to $r$. It is given as follows.
          
![[Pasted image 20220428111131.png]]

It give the following invariant. $i$ is less that the leftmost > pivot value in the range $p...j$ (or is $j-1$ if no > pivot is there). The way partition works is $i$ keeps track of the end of the elements smaller then the pivot. So if one is found where $j$ is (as $j$ is always greater than $i$) we increase $i$ to make room for the new element and swap. The worst case of  partition is we get a smallest or greatest value as the pivot. In this case the future partitions will be of the same scale as the original. So the worst case we have to perform partition $n$ times each time taking $O(n)$ hence we have $O(n^2)$.