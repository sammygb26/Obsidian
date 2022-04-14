# Classical Planning
Planning has been managed with search and logic. But search can be hard to implement well without numerical evaluations which can be hard to find. Here we will look at an approach which allows us to represent planning problems that handles this limitation.

## Planning Domain Definition Language
**PDDL** is a language representation that is a simpler, less expressive version of **FOL**. We can use it to describe planning problems while avoiding the pitfalls of inference with **FOL**. A **PDDL** description has 4 parts

1. *Initial state* -> This is the state we start in
2. *Actions* -> This is the possible actions we can take at a state $Actions(s)$.
3. *Results* -> This is the outcome of taking a particular action $Result(s,a)$.
4. *Goal(s)* - This is a description of a state we want to reach.

A **state** is represented as a conjunction of positive fluents that are ground (no variables) and functionless. For example
$$Happy\land Respected$$
Might represent the state of some recently promoted agent. Then $$At(Bus_1, Lighthouse)\land At(Bus_2, Castle)$$Is the state where $Bus_1$ is at the $Lighthouse$ and $Bus_2$ is at the $Castle$. We assume a **closed world** and so every fluent not mentioned is assumed to be false. Overall **database semantics** are used.

**Actions** and **Results** are defined in the same schema and individual action defines when it can be taken as well as when what the outcome of taking the action will be.

![[Pasted image 20220228201951.png]]

The **precondition** is the requirements that need to be met by the current state. The **effect** overcomes the *frame problem* and states the exact changes to literals (only these ones will change). The *variables* used in this scheme are universally quantified and can refer to what we choose. The above actions represents the idea of a plane flying from somewhere to somewhere else. The variables will be quantified for example giving

![[Pasted image 20220228202919.png]]

Both the **precondition** and the **effect** are conjunctions of literals that can be positive or negative. The **precondition** must be true in the state for the action to be a valid choice, it will be called *applicable*. All the literals mentioned in effect will have their corresponding fluents set to that value. So any negative ones will be removed and any positives added (so we can also think of the effect as a *delete list* and *add list*).

![[Pasted image 20220228203903.png]]

No **times** are mentioned in **PDDL** all references implicitly refer to the current state. The **initial state** is just a conjunction of ground atoms so is represented just as any other state. The **goal** states are represented as a conjunction of positive and negative literals just like the precondition. This makes sense as the only reason we would want to be in a goal is to be able to accomplish something hence why we are using **PDDL** to find a plan.

## Block World
This is a domain consisting of a set of cube shaped blocks on a table. Our goal is to stack them in various ways. An arms can pick up a block as long as no block are on top of it. It can then be moved to the table or onto another block that doesn't haven anything on top of it. Here are the rules specifying a simple problem.

![[Pasted image 20220228205226.png]]

This is the representation of the problem

![[Pasted image 20220228205317.png]]

$On(x,y)$ would mean $x$ is on $y$ where $y$ can be either a block or a table. We have to take some care here however. For example if we put a block on the table with the above rules we get $¬Clear(Table)$ but the table will always have room on it as it isn't a block. Hence we need to add the following rule.

![[Pasted image 20220228205519.png]]

## Algorithms for Planning as State-Space Search
In *state-space* search we represent the space we are searching through as either states that can be reached by a sequence of action or the partial states that can reach after a sequence of action our goal state. These are called **forward (progression)** search and **backward (regression) search**.

![[Pasted image 20220304130723.png]]

Forward is shown as $(a)$ and backwards is shown as $(b)$

## Forward (progression) state-space search
Forward search is often considered impractical, this is due to the large branching factors we can quickly get due to the combinatorial nature of the *action schemas*. This also leads to us exploring *irrelevant actions* which have nothing to do with our goal state (but perhaps they may be needed later?). Overall this leads to large state spaces making both depth bases approaches and breadth based approaches expensive. Uninformed search is therefore very costly with *progression search*.

## Backward (regression) state-space search
In this we start with the *goal* being true (which is a partial description of a state). Then we reverse the actions so if the results meet the conditions met by a partial description we can apply that action in reverse making the preconditions true in a new partial state. 

![[Pasted image 20220304132107.png]]

We keep doing this until we find some partial state that matches our start state. This is also called *relevant state-space search* since we only consider actions that are relevant to the goal and needed to reach it form some state. The partial states are a list of literals that can be both false and true. We match the start state when all the positive literals of some state match those in the start state and the negatives ones are not in the start state. Any fluent not mentioned in the partial state can have any value.

*Backward* search gets even more powerful when we consider partially uninstantiated actions and states (not just ground ones). Take the example we want to deliver some cargo to an airport. We know we will need to $unload$ it at the end. Now we could try this will all possible planes bun instead we can use an uninstantiated plane (we don't care which one it is). This comes from the definition of $unload$.

![[Pasted image 20220304132543.png]]

We take care to *standardize apart* to avoid confusion like in [[Inference in First-Order Logic]]. But this will give a partial description describing that our cargo is in $p'$ and some plane $p'$ is at $SFO$ et.

![[Pasted image 20220304132933.png]]

We say an action is *applicable* if it can be the next step in some plan. We call an action *relevant* if it could be the last step in a plan leading to the current goal state. That is *applicable* actions link forward but *relevant* can link backwards fitting the partial description in the goal state. They must fit it completely to be *relevant*. We can use the *most general unifier* when regressing backwards reduce our branching factor. This helps cut down considering irrelevant substitutions as we combine them to be one then the final unification with the start state will give us our action sequence.

## Heuristics

## Planning as Refinement of Partially Ordered Plans
Previous approaches construct a linear sequence of actions as the final plan. The *POP* approach takes into account that some parts of the plan are independent and instead of having a strict order allows us to take many different sequences in the end. Instead of a list of actions in a sequence a *Partial Ordered Plan* is a set of actions with a set of sequence constraints that define that some will have to happen after others. We prefer to search through the space of plans rather than the space of actions sequences.

![[Pasted image 20220304172750.png]]

We start with and empty plan $(a)$ consisting of a start state and a goal state. The algorithm then finds a *flaw* in this plan. An action is them made to correct for the flaw. For example we need $At(Space, Axle)$ to be true so we add the $PutOn(Space, Axle)$ as this is the only action that can make that true. This add more *open conditions* that do not resolve to an action from the start state. We add an ordering constrain that the new $PutOn$ action must be done before $Finish$ (although usually this is left out as of course everything is done before the end). If there is no correction for a *flaw* then the algorithm will backtrack and try another earlier option.

Every step adding a new action we choose the *least commitment* possible to fix the flaw. For example when adding $Remove(Spare, Trunk)$ we require it to happen before $PutOn$ but no other action hence we keep our options as open as possible. Then also if there is a variable we leave it unbound or possible reduce its scope the least we can.