We want to understand language to do something useful with it. In the end we want to distil what natural language describes into a representation that will help us operate in the world. One way to do this is to build a representation of the meaning as a structured object we can later manipulate to help us operate. Some things this could help perform

1. Answering essay questions in an exam
2. Deciding what to order at a restaurant by reading a menu
3. Learning to use a new piece of software by reading the manual (ew)
4. realizing you've been insulted (time to throw hands)
5. Following recipes (yum!)

We have already build representation of sentences but these aren't sufficient for these purposes. In **semantic analysis** these meaning representations are build up and assigned to linguistic inputs. These representations describes here will be the **literal meaning** and wont capture idioms, metaphors or more complex structure in natural language.

## Computational Desiderata for Representations
We can cover some of the different properties we want from our meaning representation.

#### Verifiability
We want our meaning representation to have a relationship to the world that is **verifiable** meaning we can test is it is true or false. If we are asked a question "Does Mary serve Greek food?" we want a representation of the statement $Serves(Mary, Greek food)$ for example in our KB. This way we can check and return Yes, No, or we don't know (if we suspect our information isn't complete).

#### Unambiguous Representations
Much of language is **ambiguous** but we want to make inferences and statements to help us operate in the world. The meaning therefore has to be free of ambiguity freeing us up to do those things.

A closely related concept is **vagueness**. Here a statement may not have multiple interpretations but instead there is an ambiguity to the resolution behind the statement, how much information is provided to divine for example the requirement on a sentence.

#### Canonical Form
We may have many sentences that say a similar thing or at least we want them to resolve to the same knowledge or part of our word model in the end.

![[Pasted image 20230422212012.png]]

All these sentences are different but we want their knowledge representation to be the same. But the actual words used are different. These common representations are called **canonical forms**. We don't want to collapse all sentences together and have no range it what we can say. One way to combine these sentences is to note that "food", "dishes" and "fare" are different words but they can all be resolved to the same **word sense**. Getting the correct sense for the word is called **word sense disambiguation**.

#### Inference and Variables
We may get asked a question like "Can vegetarians eat at Maharani?". With the knowledge $Serve(Maharani, Vegiterian Food)$. We don't want to resolve the sentence to have the same form as our knowledge, for example as we would for "Does Maharani have vegetarian dishes?" instead there is a connection between what vegetarians eat and vegetarian food being served that allows them to dine. We need to use these facts to connect the two statements. This connection is called **inference**.

We may also have the case there we want to fill in some blank. Take the question "I'd like to find a restaurant where I can get vegetarian food." In this case we will be finding $x$ values that match the statement $Serves(x, Vegetarian Food)$

#### Expressiveness
We want a system that allows us to represent anything we might say. This is pretty hard but [[First-Order Logic]] comes close.

## Model-Theoretic Semantics
We want some way of mapping our knowledge to some representation (**model**) of the world which can help guarantee that the translation makes sense. This model will be made our of two things **non-logical vocabulary** and **logical vocabulary**. The non-logical vocabulary is a set of element that have a **denotation** in the model, meaning it corresponds to a well defined part of the model. For example there will be a collection of *objects* called the **domain** of our model. Object can be referred to by multiple elements from our *non-logical vocabulary* for example $Mary, WifeOf(Abe)$ might mean the same thing.

When we have **properties** like $WifeOf$ we represent these as sets of object all of whome share the same property. **Relations** can similarly be represented as set of tuples of objects, examples where the relationship applies. This approach to properties and relations is called an **extensional** one. We also need a mapping from our meaning representation to denotations of the model. This is called an **interpretation**.

An example of this would be

![[Pasted image 20230423102913.png]]

But there are more complex sentences like "Katie likes the Rio and Matthew likes the Med" how can we translate these into our model format? One way we could do this is with **truth conditional semantics**. We can basically look up the truth of smaller statement and then consult a truth table (like for and) to see if the overall statement is true.

## First-Order Logic
![[Pasted image 20230423105503.png]]

This is the grammar for FOL. There are **constants** which refer to specific objects, these are generally capitalized words (Camal case). **Functions** corresponds to a genitive concept in English and basically like to objects together. So $$LocationOf(Mary)$$ gives some object. **Variables** are represented with lower case letters and act to underspecify objects. They can either refer to some object with the quantifier $\exists$ or all object with the quantifier $\forall$. 

**Predicates** can either be properties or relations. But either way they are basically sets of tuples. Each one an example where some relation holds. For example $$Serves(Maharani, VegiterianFood)$$or $$Restaurant(Maharani)$$From this we can express more complicated expressions. For example ""I only have five dollars and I don't have a lot of time". Would equate to $$Have(Speaker, FiveDollars)\land¬Have(Speaker,LotOfTime)$$

#### Variables and Quantifiers
So as I said there are tow quantifiers which inform what a variables refers to. Either $\exists$ which means there is at least one instance which fulfills the coming statement. Then $\forall$ which means everything fulfills the coming statement. For example "a restaurant that servers Mexican food near ICSI" we could make a FOL statement equivalent as $$\exists x Restaurant(x)\land Serves(x,MexicanFood)\land Near(x, ICSI)$$So $\exists$ basically says out of all the substitutions we could make for $x$ at least one of them makes the statement true. $\forall$ has a similar interpretation and instead says all substitutions make the statement true. For example "All vegetarian restaurant serve vegetarian food" would be translated to $$\forall x.VegiterianRestaurant(x)\implies Serves(x, VegiterianFood)$$For course if we substituted some random symbol like $Whale$ into $x$ the first part would be false making the statement true regardless. This means the statement basically only applies to $VegiterianRestaurant$s as we wanted.

#### Lambda Notation
This is an extension of FOL with the **lambda calculus** of Church. For example $$\lambda x.P(x)$$We can basically give this expression an argument to derive a new FOL expression. For example $$\lambda x. P(x)(A)=P(A)$$But we can also have multiple layers of $\lambda$ expressions. For example $$\lambda x.\lambda y.Near(x,y)(Centro)=\lambda y.Near(Centro,y)$$This technique is called **Currying**. This technique allows arguments to be slowly gathered to fill a predicate from daughter of a predicate in a parse tree.

#### The Semantics of First Order Logic
We can use the same framework as in **Mode-Theoretic Semantics** basically atomic statement corresponds to some property or predicate. Then our **constants** corresponds to objects in our domain. We then combine atomic statements to get more complicated sentences. We do this with logical connectives.

![[Pasted image 20230423125153.png]]

#### Inference
This is one of the most important considerations we wanted from our logical system. We want to add valid propositions based on our starting statements. **Modus ponens** is one of the simples rules that allows this. It can be written as

![[Pasted image 20230423125425.png]]

This just states if the left hand side of a rule is true we can infer the right. For example

![[Pasted image 20230423125516.png]]

In **forward chaining** we perform this kind of inference and one after another add new knowledge to our KB. Of course this can be an issue if we make to many statements we don't need, but of course we might need all this knowledge base don what we get asked.

In **backward chaining** we move in the opposite direction searching from a query by adding new antecedents to get to the point where these match up with facts we do know.

One problem is both of these reasoning methods though sound (never creating false inferences) are not complete (wont find all true statements). **Resolution** is another technique that is sound and complete. But this method is less computationally tractable.

## Event and State Representations
Semantics for language need to capture states and events. **States** are conditions or properties that are true for some period of time. **Events** denote changes in some state.

The representations we have employed so far just take as many arguments as are needed. So "Leaf serves vegetarian food" leads to a predicate with two symbols $Serves(x, y)$. This assumes the predicate for a given verb always takes the same number of arguments. But this has some problems

- Determining the correct number of roles for a given event
- Representing facts about roles associated with an event
- Ensuring that all the correct inferences can be derived directly from the representation of an event (splitting)
- Ensuring that no incorrect inferences can be derived from the representation of an event

For example 

![[Pasted image 20230423130950.png]]

These all denote the same event. But all events have the same *arity* and so we need different predicates for each event.

![[Pasted image 20230423131134.png]]

This is a bit of a brute force approach. We also need to infer the other relations from the different times. For example $Eating_7$ implies all other statements. We can solve this with **meaning postulates** for example

![[Pasted image 20230423131456.png]]

This approach has some **scalability problems**. Another approach is to treat the smaller example as underspecified larger ones. For example we could rewrite as

![[Pasted image 20230423131646.png]]

This does work and we no longer need **meaning postulates**, however a problem is it locks us into certain assumptions about a situation. For example now that someone has eaten "for lunch" we now need every instance of eating to be associated with a meal, but this doesn't reflect eating as this isn't always the case. So it fails to properly **individuate events**. For example take 

![[Pasted image 20230423132000.png]]

If we knew the first two formulas were referring to the same event we could conclude the third. But there is not way to represent this. We can solve this by adding an **event variable**. For example we could say $$\exists e. Easting(e)\land Eater(e, speaker)\land Eaten(e, TurkeySandwich)\land Meal(e,lunch)$$and so on. Adding additional facts with this notation is known as **Davidsonian** event representation but splitting the event into each individual role like this is called **neo-Davidsonian** event representations. This automatically includes all the meaning postulates thanks to and elimination.

#### Representing Time
We will need to parse tense information in order to represent events. Generally we represent events with a start, end point in the temporal sequence. Then we say one event precedes another if  the temporal evolution leads form one to the other. But we need to incorporate this into our FOL system. For example "I am arriving in New York" would would translate as $$\exists e. Arriving(e)\land Arriver(e, Speaker)\land Destination(e, NewYork)$$But this has no **temporal information**, to add this in we include temporal variables. For examples the interval $i$, the end point $n$ then we also use the constant $Now$. Hence $$\exists e. Arriving(e)\land \dots\land IntervalOf(e,i)\land MemberOf(i,Now)$$Then we could use $Preceeds(e,Now)$ to say something happened in the past and $Preceeds(Now,e)$ for the future. But this doesn't capture all temporal information. For example we might refer to something happening around some time "Flight 1902 had arrived". We can use a **reference point** that is separate from the true time of the utterance and specifies the time of the event.

![[5-Figure2-1.png]]

#### Aspect
This is a clustering of related topics that concerns if an event took some interval and if an event has  ended or is ongoing. There are four general groups of aspect

- **Stative**: I know my departure gate
- **Activity** John is flying
- **Accomplishment** Sally booked her flight
- **Achievement** She found her gate

**Stative expressions** - These basically state something is true but not if it was or will be. For example

![[Pasted image 20230423143032.png]]

We can performs some tests to check whether some statement is a stative. For example using a verb in the progressive form generally makes an odd sentence.

![[Pasted image 20230423143129.png]]

Imparities also make strange statements

![[Pasted image 20230423143216.png]]

And they cannot be easily modified with adjectives.

![[Pasted image 20230423143256.png]]

**Activity Expressions** - Here the activity is carried out by a participant without a definite end.

![[Pasted image 20230423143354.png]]

Unlike **statives** these work in both imperative and progressive forms.

![[Pasted image 20230423143503.png]]

But these statements seem odd when we add in some temporal modification of the form "in"

![[Pasted image 20230423143615.png]]

But we can state is happened for some temporal period

![[Pasted image 20230423143646.png]]

**Accomplishment Expressions** - These describe events with a natural end point resulting in a particular state.

![[Pasted image 20230423143756.png]]

So some event has taken place over a period of time whose ending cuased some state change. Many tests can be used again one is using *stop*.

![[Pasted image 20230423144350.png]]

**Achievement Expressions** - These are just expressions that result in some state.

![[Pasted image 20230423144407.png]]

## Description Logics
Many representational schemes have been used to capture the meaning of language. Other than FOL the most popular is **semantic networks** and **frames**. In **semantic networks** objects are nodes in a graph and relations between objects are represented by named-links. In **frame-based** system objects are features structures. Both these representations can be converted to FOL. Different versions of these systems are studied as **description logics** and they may often be restricted forms of FOL to make inference of particular types more tractable. Then they are often used to model specific domains.

These logics reside over categories, individuals belonging to those categories and relationships amongst individuals. The set of **categories**, or **concepts** that make up a specific application domain are called the **terminology** of the domain. The area describing relations between these classes is called the **TBox**. By contrast the **ABox** contains facts about individuals and their relations. The terminology can be organized into a hierarchy called an **ontology** that captures.

The most common way to capture the relationship between classes (i.e. an ontology) is to assert **subsumption** relations between concepts. Here $C \sqsubseteq D$ is read as $C$ is subsumed in $D$. For example we could write $$Restaurant\sqsubseteq ComercialEstablishment$$$$ItalianRestaurant\sqsubseteq Restaurant$$etcetera. One thing we cannot state with this kind of relation is a bit vague. We cannot tell is a list of classes is disjoint or exhaustive. We can't state if one object can belong to multiple classes for example. One option is to state disjoint relations explicitly. For example $$ChineseRestaurant\textbf{ not}\sqsubseteq ItalianRestaurant$$ or $$Restaurant\sqsubseteq(\textbf{or }ItalianRestaurant\space ChineseRestaurant\space MexicanRestaurant)$$The hierarchy here can be given as follows.

![[Pasted image 20230425122013.png]]

This hierarchy however doesn't describe what it means to be a particular type of restaurant / thing.  Instead we might add cuisines ad then describe an $ItalianRestaurant$ as $$\forall x ItalianRestaurant(x)\to Restaurant(x)\land(\exists y.Serves(x,y)\land ItalianCuisine(y))$$Which is the FOL translation of $$ItalianRestaurant\sqsubseteq Restaurant\space\sqcap\space\exists hasCuisine.ItalianCuisine$$The FOL makes it clear a restaurant can serve multiple cuisines and so be an Italian and Greek restaurant for example. From this we can also see we can just define what these things are. For example $$ItalianRestaurant\equiv Restaurant\space\sqcup\space\exists hasCuisine.ItalianCuisine$$These kind of expressions provide the necessary and sufficient conditions.

#### Inference
**Subsumption** is a form of inference for determining whether a superset/subset relation exists between two concepts. Alternatively **instance checking** asks if a particular individual can be a member of a category given the facts we know about it.
