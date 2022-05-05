What is a partial function? #flashcard #IADS #ComputabilityTheory
	A partial function $f:N\to N$ is a function that isn't defined on all possible inputs in $N$.

---
What is a register machine? #flashcard #IADS #ComputabilityTheory 
	A register machine is a simple mathematical object that perform computation. It contains a set of registers each of which can store a natural number (without memory constraint). A machine is made by plugging together smaller components that can add, subtract and test if 0. An flow can be imagined for a program pointer through the machine.

---
Describe a simple register machine that adds 1, subtracts one, tests is 0 and adds a number to another number. #flashcard #IADS #ComputabilityTheory 
	Add one is just a line with the register being added and a +. Subtract 1 is just a line with the register being subtracted and a -. A branch is just a register with a ? testing if its 0. To add a number to another $A=A+B$ we can have a loop that only breaks when $B=0$ then each time we loop we can subtract 1 from $B$ and add 1 to $A$.

---
How can we set up a truing machine to compute some function $f:N\times N\to N$ and what does that make $f$? #flashcard #IADS #ComputabilityTheory 
	We can build a machine that when the first and second registers are set to the argument for $f$ ends its computation with the result in $N$. This makes $f$ a church-Turing computable function.

---
What is the church Turing thesis? #flashcard #IADS #ComputabilityTheory 
	This says that the class of functions that can be computed by a register machine is the class of all functions that can be computed by an algorithm. 

---
What are the reasons to believe the church Turing thesis?
#flashcard #IADS #ComputabilityTheory 
	1. No one has come up with an obvious algorithm outside of CT
	2. Many attempts of defining computable functions reduce to the same class
	3. *Turing's argument* this is what a human calculator could calculate with finitely many distinguishable mind states and unlimited paper but finitely many symbols or fingers on the page (markings).

---
What observations make a universal machine possible? #flashcard #IADS #ComputabilityTheory 
	We can see that any number of register values can be encoded as one number and even an entire RM flowchart can be encoded as a flowchart hence we could encode a machine that takes in these two number an returns their result.

---
What is a universal machine? #flashcard #IADS #ComputabilityTheory 
	A universal machine is a machine that can compute any other machines output when given two strings encoding its flow chart (machinery) and initial state (registers).

---
What is the machine called that is being simulated by a universal machine? #flashcard #IADS #ComputabilityTheory 
	It is called an object machine.

---
