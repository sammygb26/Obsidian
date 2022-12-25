# Introduction to Computability Theory
We have analyzed how well algorithms work in terms of asymptotic. But can we also look at problems that can be solved better than the solutions we have found. So example it is proved that we will never find a sorting algorithm that works in better than $O(n\cdot log\hspace{2pt}n)$ . Similarly it is believed that 3-Sat $O(n^d)$ may not be solved polynomial time. We still even haven't proven it can take place in linear time. But instead we can look at problems that can't be solve by any algorithm taking any amount of time and space.

The **Church-Turing computable** functions which are generally accepted as being the same as "algorithmically computable" functions (ignoring time and space limitations). 

We focus on partial functions $f:N\to N$ (after all all data could just be one number we perform computation on). Where *partial* means it doesn't work on all inputs (so may not terminate on all inputs). This also extends to functions on multiple number $f:N\times N\to N$.

## Church-Turing Computable
This was reached by many roads. One from the $\lambda$ calculus and one form FSM called (*Turing machines*). We can instead look at *register machines* a version made by *Marvin Minsky*.

**Register Machine** - A register machine have a fixes finite set of *registers* (A, B ... I ) each can store any *natural number* (not memory constrained). We build machines by plugging together trivial components.

![[Pasted image 20220329001346.png]]

So the first one adds one to $C$ , the second removes a number from $E$ the third is a branch an splits it path based on a test of $F$. Then we have a merge which is really just ensuring that two paths becomes one. Finally we have an example where we can decrease $B$ while increasing $A$ until $B=0$. So adds $B$ to $A$. We can once we have made these simple components make larger machines using them as parts.

![[Pasted image 20220329002134.png]]

A register machine has $M$ computes a partial function $f:N\times N\to N$ if, for any $m,n\in N$ the following works. With $A=m$, and $B=n$ $C=D...=0$ then run $M$. The computation will terminate iff $f(m,n)$ is defined. If it does the final value in $A$ will be the value of $f(m,n)$. But this is just convention.

We can then say some function $f:N\times N\to N$ is *RM-computable* iff there's some register machine that computes $f$. This can also be done for 1 argument functions. We say +, - can be computed.

## Church-Turing Thesis
If we look out at the class of *RM-computable* functions they coincide with all function computable via $\lambda$ calculus and *Turing machines* or even any language (with unlimited memory and time). This is as these formalisms can simulate the others. That is we can write an interpreter for RMs in python (or even the other way around). This class is the class of **Church-Turing computable** functions.

The **church-Turing** thesis is the claim that this class is the same as a recognized class of *functions computable by an algorithm*. We understand this informally (as algorithm isn't defined, hence we cannot prove it). We can only really take this apart philosophically. We define algorithms as a sequence of actions we don't have choice in doing that in the end computes some output.

**Reasons** - there are many reason people believe the *CT-thesis*.
1. No one has ever come up with an obviously 'mechanical' algorithm that computes anything outside of CT
2. Very many attempts at defining a concept of 'computable' functions reduced to the same class.
3. *Turing's Argument* this about what a human calculator could in principle do with (finitely many (distinguishable) mind states, unlimited paper but finitely many (distinguishable) symbols, finitely many 'fingers on the page') gives the *Turing machines* model.
 
## Universal Machine
We can look at two observations with register machines. First a complete *set of register values* can be coded up as a single *natural number*, e.g. the 9-tuple might becomes

![[Pasted image 20220329003826.png]]

$200000000350000000$ knowing the code we could retrieve the original nine numbers (same amount of information). Second an entire *RM flowchart* can also be coded up as a *natural number*. The detail are unimportant. 

The idea of a *universal machine* is if you were given two numbers register machine and register values. You would be able to decode the two numbers to get a flowchart and the numbers at the values. We could then also simulate the machine and get its finial output value. Then this could all be done via an algorithmic process and so we could build a machine to do this. This would be a *universal machine U*.

![[Pasted image 20220329004554.png]]

We call the machine being simulated the *object machine*. Out universal machine would start with the A being a description of the object machine then in B we would encode the values for the input register to the object. Then in the output our A would be again the description of the object machine and B would describe the output registers of the object.

## General-purpose Computer
This gives the idea of general purpose computers. Since a values in the A register can program any universal machine (even another universal machine). So we can reuse the same machine for multiple algorithms. We program it with suitable inputs hence programmable computers that can do many things at once. The *hardware* is the universal machine and the *software* is the encoding of the program.

[[Introduction to Computability Theory Questions]]