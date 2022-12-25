## Edit Distance
This is the difference between two strings. It is used to see how common DNA strings are. We as long the second under the first then we count how many edits we have to add to the string to get the other. The three types are **insertion**, **deletion** and **substitution**. Insertions and deletions are when new characters are added or removed respectively. We can then say they can undo each other. Then a change can also undo another change. Hence The edit distance from $a$ to $b$ is the same as from $b$ to $a$. The edit distance is then the the fewest number of changes possible between the two strings.

**Alignment** can be defined as the being made our of insertions and deletions between two strings to change what part of them correspond to each other. The **optimal alignment** is the one that minimizes the number of dashes + the number of changes. So the edit distance is the minimum custom the alignments.

Be can get a recurrence relationship by noting if for two strings $T$ and $S$ then the alignment must end in -- with $t_m$ below, $s_n$ with $t_m$ bellow or $s_n$ with -- below. In the first and last case this last one will cost one. Then the middle one will only cost is $s_n\ne t_m$. Then it will take the distance for up to $t_{m-1}$ and to $s_{n-1}$ in the third case. Then it will take to $t_{m-1}$ and $s_{n-1}$ in the middle case.

![[Pasted image 20220124160740.png]]

If we blindly do a recurrence we will get a very exponential recursive tree.
![[Pasted image 20220124161855.png]]
We can not however that the inputs to d are always prefixes of $S$ and $T$ hence we will at most have $m+1$ by $n+1$ space for all the $d$ values. We can then also keep a list of what action our $d$ took to get it form the previous table in table $a$.
![[Pasted image 20220124162307.png]]
Note like before the work done for each $i$, $j$ is $O(1)$ since we are simply looking up values in an array. The overall runtime will the $O(nm)$ for two lists of size $n$ and $m$.

**Reading** CLRS: 15.3-4