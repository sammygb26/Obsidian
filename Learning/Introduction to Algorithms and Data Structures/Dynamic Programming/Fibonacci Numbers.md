# Fibonacci Numbers
**Fibonacci numbers** are easily coded up as a recursive algorithm
![[Pasted image 20220120184624.png]]
but if we look at a tree for a simple implementation is grows very quickly
![[Pasted image 20220120183853.png]]
But we call the same function many times so it is clear this isn't very efficient. It in fact takes exponential time and it will take time proportional to the size of $F_n$. It grows at about $1.6^n$. Since the left and the right tree means for each $n$ we are doing more and more calls. This can be solved through **dynamic programming**.

We instead keep an [[Array]] and we start with the smallest versions first. By building up form small values we discount the repetition. 
![[Pasted image 20220120184659.png]]
The hard problem here is designing a way to structure the sub calls you have already worked out so you can easily work up.