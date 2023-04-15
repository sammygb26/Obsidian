One way to capture **structural dependencies** which standard PCFGs is to **split** non-terminals. One way is **parent annotation** where we split into different forms based on their parents. For example $NP$ with an $S$ parent will be $NP\hat\space S$ and $NP$ with a $VP$ parent will be $NP\hat\space VP$. 

![[Pasted image 20230410180322.png]]

The issues with **splitting** is it increases the size of our grammar and so effectively reduces the size of our training data.