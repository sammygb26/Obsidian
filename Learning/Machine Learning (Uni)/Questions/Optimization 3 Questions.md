What is constrained optimization? #flashcard  #MachineLearningUni #Optimization
	 In constrained optimization we attempt to optimize a given function but with added constraints on the form of the minimizer.

---
What is the simplest way to work a constraint into a function we are optimizing? #flashcard  #MachineLearningUni #Optimization 
	We can add a new function that is defined as 0 or either $\infty$ or $-\infty$ depending on whether we are minimizing or maximizing some values respectively. Then we add this function to our original function passing the constrain into it. For example $$\underset{w}\min L(w) \hspace{16pt}\text{ s.t.}||w||^2\le0$$ $$\underset{w}\min L(w)+V(||w||^2-1)$$ Where $V(s)$ defined as 0 for $s\le0$ and $\infty$ otherwise.

---
What solution is used to get around the undifferentiability of constraint functions? #flashcard  #MachineLearningUni #Optimization 
	We instead define a *Lagrangian* which is just some scaled version of the constraining values and so can be differentiated if it can.

---
What is the definition of a Lagrangian? #flashcard  #MachineLearningUni #Optimization
	Take in some function say $$\underset w\min L(w)\hspace{16pt}s.t. h(w)\le0$$ Then for some $\lambda\ge0$ the Lagrangian is defined as: $$L(w)+\lambda 
 h(w)$$

---
What is lambda called when part of the Lagrangian formula? #flashcard  #MachineLearningUni #Optimization 
	It is called the lagrangian multiplier.

---
What does it mean for some parameter to be feasible or not? #flashcard  #MachineLearningUni #Optimization
	With respect to a constraint a parameter is feasible if it fulfills that constraint.

---
With respect to whether $w$ is feasible or not what relations holds between our original function and its Lagrangian? #flashcard  #MachineLearningUni #Optimization
	If is true that if $w$ is feasible then $h(w)\le0$ and so the function we are optimizing is always greater than itself plus the lagrangian ($L(w)\ge L(w)+\lambda h(w)$) with the reverse true if $w$ not feasible.

---
	What is true of the minima of a lagrangian with respect to the minima of the function is comes from? #flashcard  #MachineLearningUni #Optimization 
		Its minima will always be less than that of the original function (with the constraint applied).

---
What is the minima of a Lagrangian a function of? #flashcard  #MachineLearningUni #Optimization 
	Is is a function of the lagrangian multiplied $\lambda$.

---
What is the dual problem of some constrained problem? #flashcard  #MachineLearningUni #Optimization 
	To find the dual of some constrained problem we start with the constrained problem: $$\underset w\min L(w)\hspace{16pt}s.t. h(w)\le0$$then we find its Lagrangian $$L(w)+\lambda h(w)$$ Then we know the minima of this will be a function of $\lambda$ and always less than or equal to the original constrained minima. So maximizing that function with respect to $\lambda$ will find the constrained minimizer $w^\star$ and minima. This maximized minimized function is called the **dual function**: $$\underset{\lambda\ge0}\max\underset x\min f(x)+\lambda h(x).$$

---
