# Logical Agents
We have agents that can find out what to do but only for single simple tasks. They have no way to understand more than what they were programed to. We also have the problem of unknown environments. The only way one of these agents can navigate this is by assuming it is in all states which is useless for real world problems.

We want an agent with a **knowledge base**. That can incorporate **percepts** into this and then **query** the knowledge bade to get answers to questions. A **knowledge base** is made up of **sentences** (not English sentences but statements in a **knowledge representation language**). A **sentence** can be an **axiom** if it isn't derived form other sentences. The adding and querying of knowledge is called **Tell** and **Ask**. For both we use **inference** that allows us to find new sentences from old ones. The knowledge base starting with some **background knowledge** which can be used to build up to new knowledge. Take this basic **knowledge based agent** bellow

![[Pasted image 20220212153213.png]]

The implementation is hidden behind the functions $Make-Percept-Sentence$, $Tell$, $Ask$ and $Make-Action-Sentence$. We give the agent time when we are asking and telling this makes sure we are updating the world properly. The key think is the changes needed to changes needed for a new problem are at the **knowledge level** not the algorithm level. Our reasoning is independent from the actual interface with the world. 

## Wumpus World
This is a simple world that illustrates the idea. We are in a cave consisting of rooms, pits, gold and a beast called the Wumpus. If we fall it a pit or stumble across the Wumpus we die. We have an arrow we can shoot at the Wumpus if we are facing it form a neighboring room. Neighboring tiles to the Wumpus have a stench and neighboring tiles to the pits have breeze.

![[Pasted image 20220212154740.png]]

The environment is hidden so our agent is trying to deduce the state of the world. We can get an understanding of how an agent might reason by doing it ourselves.

![[Pasted image 20220212155101.png]]
![[Pasted image 20220212155127.png]]

We first conclude the lack of percepts means the cells round us are empty. We can deduce the location of the Wumpus and a pit from the lack of both in the 2,2 square. And we continue on... When we deduce something we know it to be true and we can trust this from our **logic**.

## Logic
A **logic** is a langue we can use to describe our knowledge in. It has **syntax** that defines what sentences are correctly formed. Then we have **semantics** which define the **truth** of a sentence with respect to the possible **words** used. The **semantics** define when sentences are true in a world. In standard logics sentences are either true or false in a possible world. The actual representations of this our agent has are called **models**. A **model** is a abstraction of the real world that fits into our knowledge base to make sentences either true or false. We then say if a **model** $m$ makes a **knowledge base** or **sentence** $\alpha$ true then $m$ **satisfies** $\alpha$ or $m$ is a model of $\alpha$. We also have the model of $\alpha$ the set of all models for which $\alpha$ is true which is $M(\alpha)$.

This is what builds up our logic but how can we reason with this? When we have a knowledge base there is a set of models that satisfy this knowledge base (the KB's model). If all these models fit within the model of another statement $\alpha$ then in any model that satisfies KB $\alpha$ is also true. We say $KB\models \alpha$ that is KB **entails** $\alpha$. This is illustrated bellow with the example of the Wumpus world after the first two moves in 1,1 and 2,1. The knowledge we have perceived in our KB and it rules out possibilities outside it. While the states within are the possible states.

![[Pasted image 20220212161330.png]]

This can also be said with notation as

![[Pasted image 20220212161755.png]]

$M(\alpha)$ is a subset of $M(\beta)$ is is said to rule out more worlds. We can then check if some $\beta$ is entailed by enumerating over all possible models and checking if when $\beta$ is true $\alpha$ is also always true. This is a way of performing **logical inference** called **model checking**. Many sentences might be **entailed** by a knowledge base to find them we use **inference**. We would say for inference procedure $i$ we say
$$
KB\vdash_i\alpha
$$
We read this as "$\alpha$ is derived from KB by $i$" or "$i$ derives $\alpha$ from KB". If $i$ only derived entailed sentences it is **sound** or **truth preserving**. We also say a $i$ is **complete** if it can derive any sentence that is entailed. If we have a **sound** inference and our KB is true in the real world and anything we infer is also true. Then we can find new facts about the real world by examining our KB. We know our KB is true in the real-world from it being **grounded** this comes from our percepts being true to the real world. Inferring the rules that we use for inference is called **learning** and is beyond logical agents.

## Propositional Logic
This is the simples **logic** but can still be powerful. Its **syntax** defines the allowed sentences. **Atomic sentences** are a single propositional symbol. A symbol is a proposition that can be true or false. For example we can represent if a pit is in a given position 1,2 with the proposition $P_{1,2}$. **Complex sentences** are constructed from simpler sentences and **logical connectives**. There are five common ones 

* $\neg$ **Not** -> so we can have the negation of $P_{1,2}$ which is $\neg P_{1,2}$ this is true when $P_{1,2}$ is false. This also makes up **literals** which are either a atomic sentence (positive literal) or a negation of one (negative literal)
* $\land$ **And** -> A sentence whose main connective is $\land$ such as $P\land W$ is true when both sentences $P$ and $W$ are true.
* $\lor$ **Or** -> A sentence whose main connective is $\lor$ such as $P\lor W$ is true when either sentence $P$ or $W$ is true.
* $\implies$ **Implies** -> A sentence whose main connective is $\implies$ such as $P\implies W$ is true if $P$ is false or $W$ is true.
* $\iff$ **Iff** -> A sentence whose main connective is $\iff$ such as $P\iff W$ is true if $P$ and $W$ have the same logical value, both true or both false. Said another way both $P\implies W$ and $W\implies P$

![[Pasted image 20220212170435.png]]

This is the formal grammar for **propositional logic**.The **semantics** which defines the rules for getting the truth of a sentence in a particular model. The values for **Atomic sentences** can be $true$ or $false$. So for $n$ symbols there are $2^n$ models. To find the truth of a sentence in we can just substitute in the values the propositions have in our model and evaluate according to the definition of the connectives.

![[Pasted image 20220212171249.png]]

We can now construct a simple logic base for our Wumpus world encoding the rules. For instance the following rules encode for the effect of getting a breeze percept in 1,1 or 2,1

![[Pasted image 20220212182235.png]]

## Simple Inference
If we want to check if some sentence $\alpha$ is entailed by $KB$ we need to is enumerate over all the possible combinations of the propositions involved and check if when $KB$ is true $\alpha$ is true.

![[Pasted image 20220212182503.png]]

This approach can be replicated simply with simple truth table inference algorithm.

![[Pasted image 20220212182622.png]]

Here we just assign the variables one by one and then when we have run out of variable we check if $KB\implies \alpha$ for all these leaves. We and them all together getting our final answer.

## Theorem Proving
Here the idea is that we can simplify our KB bringing it all down to a simple form which is easy to add new percepts to. We need to describe some more concepts to understand **theorem proving**.

1. **Equivalence** is a property between two sentences. Two sentences are **equivalent** if they are true in the set of models. That is $M(\alpha)=M(\beta)$ means $\beta\equiv\alpha$.
2. **Validity** means a sentence is true in all models so $\neg P\lor P$ is **valid**. These are also called tautologies. $\alpha\equiv\beta$ iff $\alpha\iff\beta$ is valid, that is always true. 
3. **Deduction Theorem** is closely related but is said formally as: *for any sentences $\alpha$ and $\beta$, $\alpha\models\beta$ iff the sentence $(\alpha\implies\beta)$ is valid* hence we can do inference by proving some statement to be always true (this is basically what the simple check above did)
4. **Satisfiability** is when a sentence can be true in some model, there is the possibility of it being true. This can be connected to inference still as if $(KB\land \neg\alpha)$ is **unsatisfiable** so always false then $KB\models\alpha$.

![[Pasted image 20220212185329.png]]

These equivalences are proven and are the basis of **theorem proving**. 

## Inference
We also need **inference rules** which are more relaxed versions of equivalences that can be used one way but not the other (although all equivalences function as inferences). We have **modus pones** meaning "mode that affirms" in Latin.

![[Pasted image 20220212190157.png]]

Then we also have **And-Elimination** which basically means if we know the **conjunction** of two variables is true we can conclude the are bot individually true.

![[Pasted image 20220212190419.png]]

Now that we have these rules we can find a proof bringing us from our knowledge base to an inference and we can formulate it as a search with **Initial State** (KB), **Actions** (inferences), **Results** (inferences), **Goal** (inferred sentence). The benefit of doing it this way is we don't concern ourselves with propositions that aren't relevant.  We can also say propositional logic has **monotonicity** meaning that as we add information to our knowledge base we only increase information. A logic can be **nonmonotonic** if this isn't the case.

We also need **resolution** in our inference. This is when we have some **disjunction** of literals but we know one of them to be false.
![[Pasted image 20220212192038.png]]
here $l_i$ and $m$ are complementary literals meaning one is the negation of the other. This really means we are combining the two statements sentences which are both true and reducing the total size. The general rule is called **resolution**
![[Pasted image 20220212192627.png]]
Where $m_j$ is the dual of $m_i$. To perform resolution we need to have a disjunction of literals without repetition. But repartition can be easily removed with a trivial inference where $(A\lor A)\models A$. The **resolution** rules makes sense as if two literals are duals one or the other is true. If this is the case either one sentence of the other is true without these literals as the sentence would only need to be true if the literal was false. If we ever find two dual literals in the same **disjunction** we know it will always be true so we can discard this statement.

## Conjunctive Normal Form
We know resolution can be applied to **disjunctions** of literals also called **clauses** the while knowledge base can be made out of a **conjunction** of these clauses giving us **CNF**. So we just need to convert our KB to CNF then we can reduce it to get inference. There are four steps to this

1. **Eliminate $\iff$** We replace all $A\iff B$ with $(A\implies B)\land(B\implies A)$
2. **Eliminate $\implies$** We replace all $A\implies B$ with $\neg A \lor B$ 
3. **Move $\neg$ Inwards** This is since CNF requires only negations of literals
4. **Distribute $\lor$ and $\land$** This is to get us into our final CNF form

We can then use **proof by contradiction** where we prove $KB \land \neg\alpha$ is unsatisfiable to prove that $KB\models\alpha$ the algorithm is given below

![[Pasted image 20220212195154.png]]

The idea is we convert $(KB\land\alpha)$ to a CNF then we attempt to resolve any clauses that share predicates either there are no clauses that can resolve in which case there must be a model for which $\neg(KB\implies \alpha)$ or two clauses resolve to an empty clause (disjunction of nothing equivalent to false) which is a contradiction hence $\neg(KB\land\alpha)$ is a contradiction so $KB\models\alpha$.

This method is **complete** as there are only finitely many resolutions that can be made as each time the number of literals decreases so eventually it must resolve to some **CNF** with no duals. This gives us the **ground resolution theorem** which states that if a CNF is unsatisfiable then it's resolution contains the empty clause

## DPLL Algorithm
This is an improvement of the TT-Entails? algorithm seen above. It take in a CNF and tells us if it is satisfiable. It is more efficient than TT-Entails however for three reasons

1. **Early Termination** -> The algorithm can detect whether a clause must be true quickly as if any of its literals are set to true the whole thing is true so the rest can be ignored as the values will not effect the outcome. Then if any clause has to be false the whole thing must be false there is no recovery.
2. **Pure Symbol Heuristic** -> A **pure symbol** always appears with the same sign in every clause. Then an **impure** symbol must be negated in one an unnegated in another. If there is a model then either these pure symbols are true in it or they can be. So there is no harm in setting them true as early as possible. It will only make the problem easier.
3. **Unit Clause Heuristic** -> A unit clause in this context is a clause with either one literal or only false values and a literal hence this literal must be set to true. Doing so early will reduce complexity again.

These heuristic prioritize assigning values to certain literals. It can also happen that this assigning causes another heuristic to apply so we go back again, this is called **unit propagation**. This gives the **DPLL Algorithm** below

![[Pasted image 20220212204602.png]]

This is the skeleton of the search process but it gives the idea we repeat the process and when the heuristics don't apply we branch. Note unit clauses aren't included but just checking for if a clause is true or false at the start has the same effect as the branch we wouldn't go down gets caught anyway.

## WalkSAT
This is a local search algorithm so functions in a semi greedy manor. It loops each time picking a false clause it then with a 50% change either picks the variable to flip that would maximize the number of satisfied clauses or randomly changes a variable. We we loop forever we will find a solution, unfortunately if there is no solution we will never stop. So WalkSAT is best when we know there is a solution and we want to find one.

![[Pasted image 20220212210319.png]]

The number of literals in a clause defines how **constrained** a problem is. Problems that are **unconstrained** and have few literals in clauses are easily solved by greedy methods like WalkSat as solutions are dense in the space of assignments. This is even if there are many different propositions. Hence WalkSat works well for these problems. We can randomly generate CNFs and test WalkSAT and DPLL against them. The **satisfiability threshold conjecture** states that for every number of clauses greater than 3 there is some threshold ratio between the number of clauses and the number of symbols where we see the probability of satisfiability drops of. So we can use this to determines when to use WalkSat and when not to.

![[Pasted image 20220212211958.png]]

This is useful if we look at the right graph which shows how much faster WalkSat is.

## Making an Agent
We want to use all we have seen to actually build a **logical agent**. We start by collecting **axioms** which are sentences we know to be true in all possible models of the world. These define how we understand the world and given what percepts what we can derive. In the Wumpus world we need to describe all the rules of the world. We have to have pure symbols so we will need many propositions for each space saying if it has the Wumpus, a pit, gold. Then cave is 4x4 so there will be 48 pure symbols. We will also need many clauses such as one with 64 predicates saying the Wumpus is somewhere. Then we will need 120 propositions for this. We will also have to add time stamps to our proposition as well as where we are for this all to make sense. We also need a transition model to make sense of **fluents** that change with time such as our position. For this we will need to construct a **transition model**. For this we will add **effect axioms** that describe how the world changes as times does. For example the ones bellow describes one possible movement we an make. Then we would need this for every possible time step!

![[Pasted image 20220212215635.png]]

We would also need rules like this for every possible timestep. But we also need to explain how all the state will transition between two time steps. For example we need a rule to explain that if we have an arrow before we will have one after if we didn't shoot. This is the **frame problem** where we don't maintain information between states. One solution is to add many **frame axioms** that describe how we might move between frames.

![[Pasted image 20220212220140.png]]

The problem is we would need to keep adding these axioms for every possible action this is called the **representational frame problem**. This is a problem as in the real world there are very many **fluents** so it becomes impossible to describe how the real world actually functions. We can just say it only changes when a certain action is taken as follows.

![[Pasted image 20220212220609.png]]

This is called a **successor state axiom**. For example we could say having an arrow is equivalent to us having an arrow in the past and having not shot in the past. It can still be quite complicated for position however as we will require these axioms for all positions. We can also add convenience variables like $OK$ to mean $\neg P\land\neg (W\land W_{alive})$. Then give our agent a percept, action sequence as follows

![[Pasted image 20220212221207.png]]

Then we can query the knowledge base and ask it questions like $ASK(KB,OK_{2,2}^6)$ and we will actually get the answer $true$ so we know it is safe to move there. One problem is when what we expect doesn't happen for example we have missed some possibility that lead us to no longer understand the world. This is called the **qualification problem** and there is no solution in logic for this.

## Hybrid Agent
We can combine all above with a [[Search]] based agent to plan out a solution. The agent program maintains a knowledge base which it updates with its actions when it makes them. A plan it kept and as we move forward in the world we update this based on our percepts. We need to also plan to shoot if we cant find a safe tile to explore or can't accomplish our goal without further exploration.

![[Pasted image 20220212222148.png]]

A major problem with this is as time goes on and we continue to add new predicates the time taken to compute the answer to a question goes up. So the time taken to get an answer goes up with the age of our agent. Another way is to replace the old states with a **belief state**. We then update this belief state using percept in a process called **state estimation**. The problem is the size of the we need to represent this belief state is very large. There will be $2^n$ possible values described by a belief state for $n$ propositions states we could encode as proposition which means there is $2^{2^n}$ possible evaluations for this. So

[[Logical Agents Questions]]