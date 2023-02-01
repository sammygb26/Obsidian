# First-Order Logic
We have tried to use **Propositional Logic** in  [[Logical Agents]] but the language is too weak and not expressive enough to allow for true inference in a complex environment. It became very hard to use when we took into account  **fluents** things that changed in the world. **First-Order Logic** is a more expressive language that will allow us to create a true **Logical Agent**.

**Programming Languages** are general they only allow really descriptions of computation and lack any inbuilt way to derive facts form what they already know. Instead we need to program domain specific inference into them, as well as trouble showing partial information. Then in **propositional logic** which is a **declarative language** we just say the rules and **domain independent** inference take place to infer facts given the basics. We have to define the **semantics** for any programmed solution but when we use a logic the **semantics** are already set up we just have to follow the rules to perform inference. Another benefit of **propositional logic** is **compositionality** meaning we can combine sentences together to get more complicated sentences and the meaning is just a composition of the meaning of the smaller sentences. This allows us to build up from simple descriptions of how to world works to an arbitrary level of complexity. But a problem with **propositional logic** was that we couldn't state anything that was universally true instead we had to add in little pieces for every possible combination. We could use **natural** language but its is very **context** dependent and being given a sentence doesn't along give us enough information to do inference, but we could have to store and represent this context. We also have the problem of **ambiguity** meaning one sentence can be interpreted in different ways.

The idea behind **First-Order logic** is to take the best parts form **propositional logic** (**context-independent**, **unambiguous**, **declarative**, **compositional semantics**) and combine them with the expressivity of **Natural Languages** . We want to use some of the main features of **Natural Language** such as **Objects** (being able to refer to things in the world and their attributes given by **properties**) and **relations** single object for **properties** or n-ary for among objects that are evaluated to true or false. Then **functions** which describe new objects from old ones. **First-Order Logic** implements these elements as well as being able to give relations of *some* or *all* objects. This allows statements to be general and not restated over and over again.

## Syntax and Semantics
In **propositional logic** link symbols to predefined truth values, this describes the possible worlds or models that we consider. In **First-Order Logic** we instead consider things about **objects**. The **objects** are defined in the **domain** of a model that is the set of **domain elements** contained within the model. A **domain** bus not be empty the world must contain at least 1 objects. Take the example below with 5 objects.

![[Pasted image 20220213124128.png]]

The objects would be Richard, John, Richard's left leg, John's left leg and John's Crown. The objects are **related** in various ways. For example Richard and John are brothers. This can be defined as a set of tuples defining the brotherhood relation. When these objects are put into the relation we could look this up and give true or false to whether they are brothers $\{\langle Richard, John\rangle, \langle John, Richard\rangle\}$. The brother and one head relations are binary relations so can be defined by a set of binary tuples $\{\langle Crown, John\rangle\}$. There are also **unary relations** which are **properties** these could be defined as a set of objects that have the property $person=\{Richard, John\}$. We can also use **functions** to describe relations between objects. This way they can only be related in one way and to one object, note the definition of function as a relation that is many to one. An example of this is the **left leg** function since each person can have only one left leg. This does 

![[Pasted image 20220213125327.png]]

There is the peculiarity that functions are required to be **total** meaning the must have a relation for every object  so a the crown must have  left leg. This can be solved with *invisible* objects. This is an object that relates anything that doesn't have a left leg to itself, including itself.

## Symbols and Interpretations
We will now look at how to construct **first-order logic** sentences. The basic elements of **FOL** are symbols for **objects**, **functions** and **relations**. So there are three kinds of symbols.

1. **Constant Symbols** -> Which are objects
2. **Predicate Symbols** -> Which are relations
3. **Function Symbols** -> Which are functions (wow)

The convention is for these symbols to start with upper case letters, but the names are completely up to the user. Each **predicate** and **function** symbol has an **arity** meaning the number of arguments. Any **model** (as in propositional logic) must give the information required to determine if a sentence is $true$ or $false$. This means a **model** requires an **interpretation** which defines what relations, objects and functions translate to which constant, predicate and function symbols (defining the interpretation). So your example can have the following interpretation that is the **intended interpretation** in this case.

![[Pasted image 20220213130712.png]]

We don't have to have this interpretation however we can have completely different interpretations that to us make no sense but still are valid within the logic. The syntax gives the mapping from the symbols to the objects. For instance that. The rules for the syntax are given bellow

![[Pasted image 20220213143411.png]]

We now define **entailment** the same way as in **propositional logic** as relating to all possible models (interpretations), we can get an idea of what all possible interpretations looks like below. Different interpretations have different numbers of objects and different mappings between objects.

![[Pasted image 20220213143841.png]]

This flexibility does mean since we can have unnamed objects and even with few objects there are many possible relations it becomes impossible to check via enumeration like with **propositional logic**.

### Terms
A **term** is a logical expression that refers to an object. So **constant** symbols refer to objects. But also **functions** of constant symbols ($LeftLeg(John)$) the object the function refers to has no name even though it is an object in the same way $John$ is, this isn't returning a $leg$ the function is the leg. This is similar to functional languages where functions themselves are objects. So both $John$ and $LeftLeg(John)$ are **terms** referring to objects.

### Atomic Sentences
We have **predicate symbols** that can define relations between objects and we have **terms** that refer to these Objects. We can not form **Atomic Sentences** which are **predicate symbols** followed optionally by a list of **terms** (so **terms** are like arguments). So an example could be $Married(Father(Richard),Mother(Richard))$ here the **terms** are $Mother(Richard)$ and $Father(Richard)$. Where both are function symbols applied to the constant symbol $Richard$. $Married$ is the predicate symbol.

*An atomic sentence is* **true** *in a given model if the relation referred to by the predicate symbol holds among the objects referred to by the arguments*

So we can evaluate an **atomic sentence** in an **interpretation/model** by looking up if the relation (predicate symbol) has the terms given as a relation within it.

### Complex Sentences
We add **logical connectives** to allow more complex sentences. They use the same syntax and semantics as **propositional calculus** but can be though of as relations (predicate symbols) themselves as the evaluate to a $true$ or $false$ value.

### Quantifiers
We want our sentences to be general and refer to not just one set of objects at a time. That is refer to groups of objects rather than just one case. 

**Universal Quantification** -> We can say things like "all king are people" as follows (the all is what allows us to be expressive and general)
$$
\forall x. King(x)\implies Person(x)
$$
We use the *predicate symbols* $King$ and $Person$ but with a **variable** instead of an object. Variables are lower case letters by convention. A **variable** is a **term** in itself, so $LeftLeg(x)$ is a **term** just as $LeftLeg(John)$ is. If a **term** has no variables it is a **ground term**. The meaning of $\forall$ is as follows. We say that $\forall x. P$ where $p$ is any logical expression (sentence) means for every object $x$, $P$ evaluates to true. So $\forall x. P$ is true is a model if all possible **extended interpretations**. An **extended interpretation** gives a **domain element** to which $x$ refers. So the above example can have many interpretations for which object $x$ refers to. They must all be true for the sentence overall to be true. So the following must all be true in our example.

![[Pasted image 20220213151345.png]]

The first one is true because both parts of the argument for the implicating predicate are true. But since $King(x)$ is false for the remaining interpretations they are all true as well. The truth table meaning of $\implies$ is where its names comes from as it gives this effect where when applies over all objects we can say something natural like the above quantified sentence. Note note to use $\land$ instead of $\implies$ since $\land$ would mean all objects are both $King$ and $Person$.

**Existential Quantification** -> We can make statements about something in our world using the **existential quantifier**. To say "king John has a crown on his head" we would write
$$
\exists x. Crown(x)\land OnHead(x, John)
$$
That says there exists some object $x$ in the world such that $x$ is both a $Crown$ and is $OnHead$ of $John$. There could also be a crown that is not on Johns head but for this to be true when we look at all the **extended interpretations** (that make $x$ some **domain element**) at least one must evaluate to true. When we say $\exists x. P$ for the sentence $P$ this means  $P$ is true for at least one object $x$ so we get all the following interpretations

![[Pasted image 20220213152800.png]]

Only the final one is true, but it makes the overall sentence true. So $\exists$ is like taking the **disjunction** of all **extended interpretations** and $\forall$ is like taking the **conjunction** of all  extended interpretations. Just as with $\land$ with $\forall$, we want to make sure not to confuse $\implies$ when using $\exists$. For example using this in the sentence above would mean there is some object such that when if it is $Crown$ it is also $OnHead$ of $John$. But $John$ is not crown but he is also not on his head. So the statement must be true for him too which doesn't give the intended effect.

**Nested Quantifiers** -> We can use these to express more complicated sentences that with just one **quantifier**. For example what about all pairs of objects. So to say "all brother are siblings" we could write
$$
\forall x. \forall y. Brother(x,y)\implies Sibling(x,y)
$$
If two quantifiers in a row are the same they can be written with just 1 quantifiers so $\forall x. \forall y$ is the same as $\forall x, y$. But there can also be a mix so "everybody loves somebody" can be written as
$$
\forall x. \exists y. Loves(x, y)
$$
But we can't flip the **quantifiers** so 
$$
\exists y.\forall x. Loves(x,y)
$$
Would mean "there exists someone everyone loves" this is clearer with parenthesis $\forall x.(\exists y. Loves(x,y))$ so in we can create **extended interpretations** for the $\forall x. P$ part then for each of these we can evaluate $\exists y. Loves(x,y)$

**Connections between $\forall$ and $\exists$** -> The two quantifiers are quite similar through negation and this comes from **De Morgan's Laws** It is that case that if for all $x$ $P$ is true then there does not exists $x$ for which $P$ is false. Then if there exits an $x$ for which $P$ is it not the case the for all $x$, $P$ is false.

![[Pasted image 20220213154936.png]]

## Equality
Equality is slightly different from pure logical equality ($\iff$). Here the **equality symbol** says that two **terms** refer to the same object. So we can say
$$
Father(John)=Henry
$$
So the object $Father(John)$ and $Henry$ must be the same object in the **interpretation**. This can also be combined with **negation** to make two objects. So if we wanted to say $John$ has two brothers we can write
$$
\exists x, y, Borhter(x, John)\land Brother(x, John)
$$ As one of the **extended evaluations** has $x$ and $y$ as the same value. Instead we can write
$$
\exists x, y, Brother(x, John)\land Borhter(y, John)\land\neg(x=y)
$$
## Using First-Order Logic
We will look at this from a simple $Tell$, $Ask$ interface. We can add **assertions** to our knowledge base as follows

![[Pasted image 20220213161233.png]]

Then we can ask the knowledge base questions, so the following would return true.

![[Pasted image 20220213161318.png]]

These questions asked are called **queries** or **goals**. If this would also return true for anything entailed by our previous **assertions**. So we can say 

![[Pasted image 20220213161558.png]]

Which would return true. We can also have quantified queries such as which involve quantifiers such as $\exists$ or $\forall$ but if we say

![[Pasted image 20220213161722.png]]

We would get just $true$ but we might want to know what $x$ fulfills this. We want another function that does this $AskVars$. So we can say

![[Pasted image 20220213161849.png]]

This would give us a stream of answers. Like for example $\{x/John\}$ and $\{x/Richard\}$. This types of answer is called a **substitution** or **binding list**. Sometimes this can't be found however as say if we asserted $King(John)\lor King(Richard)$ is is true that $\exists x. King(x)$ but we can't return either answer.

When we have a **domain** (area of knowledge) we create **axioms** define the logic our a given **domain**. One type of **axiom** is a **definition** which gives a value for a **predicate symbol** based on other **predicate symbols**, this will eventually get down to pure **predicate symbols** however. All the information in an **interpretation** will therefore come from these ground level truths. **Definitions** are similar to how we might build up functions from basic language library functions. Not all logical sentences that are purely about a **domain** are **axioms** some are also **theorems** which are entailed by the **axioms** necessarily, even before we have added some. We will never need the **theorems** however since they are always implied by the **axioms** they add no information to the knowledge base. But they can help with common requests as otherwise we have to prove something from first principles every times.

## Wumpus World
We can now define the Wumpus World with **First-Order Logic** in a much more concise way than previously with **propositional logic**. First we can bridge the connection between our Wumpus Agent the the world with percepts.

![[Pasted image 20220213170104.png]]

Each percept states a predicate describing the percept in a given time is true. We can the build rules on top of this that define what this means to our knowledge base.

![[Pasted image 20220213170222.png]]

We could also find out the best action by saying for example.

![[Pasted image 20220213171151.png]]

Then we can encode the logic for the agent as

![[Pasted image 20220213171240.png]]

Instead of defining objects for each square we can instead  say given the $x$ and $y$ of two squares we can define what it means to be adjacent. Then we can define adjacency as follows.

![[Pasted image 20220213171703.png]]

So we can encode where the pits are with a unary predicate $Pit$. It is unary since the square can be an array $[2,1]$ for the square $x$, $y$. We can use a unary predicate or a constant for the Wumpus as it is only in one place. The we can have a predicate $At$ which takes in some says some agent is at a given square at a point in time $t$.
$$
At(A, s, t)
$$
Would be true if the agent $A$ was at the $s$ square at the time $t$. We can finally start encoding the logic of the world like follows.

![[Pasted image 20220213172642.png]]

Then if we want to quantify anything over time we can just say something like

![[Pasted image 20220213172737.png]]

The quantifiers allow us to be more general. Then objects let us write rules generally.

## Knowledge Engineering
So we can represent knowledge in **First-Order Logic** but how do we get it there. A **knowledge Engineer** is someone who investigates a specific domain learns about it and creates a formal representations of the objects and relations in the domain.

[[First-Order Logic Questions]]