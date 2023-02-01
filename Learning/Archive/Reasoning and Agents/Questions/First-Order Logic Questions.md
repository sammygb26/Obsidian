What problems does **FOL** solve? #flashcard #RA #FOL 
	**FOL** its a more expressive version of **propositional logic** it allows for a wider variety of symbols that allows you to express general ideas. It also gets past the **frame problem** in propositional logic that make the world state hard to update with time. It takes the best parts of **PL** like being *context-independent*, *unambiguous*, *declarative* and *compositional* while being more expressive and closer to natural language.

---
What type of thing does **FOL** reason about? #flashcard #RA #FOL 
	**FOL** reasons about *objects*. These objects can be related and have properties. So we reason about them by name and generically to encode logic about the world. *Note:* There must be at least 1 objects in any valid model.

---
What are the three types of symbols in propositional logic? #flashcard #RA #FOL  
	There are *constant symbols*, *predicate symbols* and *function symbols*. *Constant symbols* refer the the actual ground objects. *Predicate symbols* relate objects and truth values together (can be binary, trinary etc.). *Functions symbols* describe some object from another for example $Mother(Fred)$ is an objects just like how $Fred$ is.

---
What is **entailment**? #flashcard #RA #FOL  
	We say some statement is entailed by some knowledge base when is all possible models of that knowledge base that statement is also true. that is the knowledge base being true implies that the entailed sentence is true.

---
What is a **term**, **variable** and **ground term**? #flashcard #RA #FOL 
	A term is a logical expression that refers to an objects. So both constant symbols and functions on terms are terms. So $John$ is a term and so is $LeftLeg(John)$. A term can also be a **variable** that can refer to multiple objects. If a **term** has no variable then it is a **ground term**.

---
What are **atomic sentences**? #flashcard #RA #FOL  
	*Atomic sentences* are just predicate symbols followed by a sequence of terms. For example $Married(Father(John), Mother(John))$ here $Married$ is the predicate and $Father(John)$ and $Mother(John)$ are the *terms*.

---
What are **complex sentences**? #flashcard #RA #FOL 
	Complex sentences also include *logical connectives* which allow for more expression. These connectives have the same semantics as in **PL** for example we have $\land, \lor, \implies, \iff$ etc.

---
What are **quantifiers** and what are the two quantifiers? #flashcard #RA #FOL 
	When we use *variables* we need to add semantics saying what they refer to. There are two *quantifiers* $\forall$ and $\exists$. A statement that is universally quantified is true in a model if every possible **extended interpretation** is true. We say A statement that is existential quantified is true in a model if it is true for at least one interpretation.
	
---
What is an **extended interpretation(s)**? #flashcard #RA #FOL 
	An **extended interpretation** of a sentence with variables is a possible assignment of variables to ground terms. The **extended interpretations** is the set of all possible interpretations.

---
How are nested quantifiers interpreted? #flashcard #RA #FOL 
	When we have nested quantifiers the order can effect what the sentence actually means. If we have $\forall$ or $\exists$ followed by the same quantifier then the order doesn't matter and usually the second or third etc. can be left out. Otherwise we interpret the second quantified sentence as a sub sentence this means the out quantified is assigned first. For example $\forall x. \exists y. Loves(x,y)$ would mean for every $x$ there is some $y$ such that $x$ loves $y$. But we do not day there exist one $y$ that every $x$ loves. This would have the quantifiers order switched.

---
What is the equality predicate? #flashcard #RA #FOL 
	This is different from $\iff$ that has a similar meaning. Equality uses $=$ and refers to two terms. So $x=y$ if there terms $x$ and $y$ refer to the same ground term. We can also have $\neq$ which is true in the opposite case (negation).

---
How can we build in agent that use **FOL**? #flashcard #RA #FOL 
	We encode out knowledge base into a set of **axioms** which are statement that the agent takes as red. We can then $Tell$ the agent any percepts by encoding them into statements we add to the $KB$ then we $Ask$ the $KB$ for inference we need to operate.

---
