

## Minimum Edit Distance
Here we want to find the minimum numbers of edits from one string to another. This can be through of as a search problem. There are many strings and many edit sequences lead to the same string. So we can just keep track of the minimum to any given string.

The **minimum edit distance algorithm** allows the edit distance to be found between two strings efficiently. We do this by noting that if a word appears in the sequence of edits between one word and another then the sequence between that word and the other two will also be the minimum number of edits. If we have two strings $X$ and $Y$ then the edits distance $D[i,j]$ is the edit distance between $X[1...i]$ and $Y[1...j]$. So if $|X|=n$ and $|Y|=m$ then we are looking to find $D[n,m]$. 

The **base case** occurs when either $i$ or $j$ is 0. In this case we set $D[i,j]=\max(i,j)$. If we are at a portion $D[i,j]$ then we could have moved from $D[i-1,j]$. We think of $Y$ as the **target** word and $X$ as the **source** word. Then we can make the rule

![[Pasted image 20230415160253.png]]

With **del-cost** and **ins-cost** equal to 1 and sub-cost = 2 (if different else 0). We get 

![[Pasted image 20230415160435.png]]

