What does the halting problem mean? #flashcard #IADS #UnsolvableProblems
	The halting problem means there are some questions that an algorithm can't answer.

---
Why can there be no halting tester algorithm? #flashcard #IADS #UnsolvableProblems 
	If there was a halting tester program call it $h$ that is given a program just says whether it halts or loops forever. We could construct another program $h+$ that is an extension of $h$. It will loop if $h$ says the program given does loop and it will not loop if the program says it will loop. Then if we feed the object code for $h+$ into $h+$ we have if $h+$ loops then it means the object given doesn't loop hence $h+$ doesn't loop. Then if $h+$ doesn't loop it means $h+$ does loop. This machine contradicts itself and is impossible.

---
What are Diophantine Equations? #flashcard #IADS #ComputabilityTheory 
	Diophantine Equations are of the form of a multivariable polynomial equation where the variables can be positive and negative real numbers. We cannot decide if an equation has a negative solution as the search in unbounded.

---
What is the Post word problem? #flashcard #IADS #ComputabilityTheory 
	The problem is if we have two sets ($A$ and $B$) of strings made from a finite alphabet. Is there a common list of indexes from $A$ and $B$ such that the concatenation of the strings from both is the same. This problem is undecidable as the search can go on forever.
 
---
