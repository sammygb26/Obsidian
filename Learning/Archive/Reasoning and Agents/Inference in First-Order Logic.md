We will attempt to interface with **First-Order Logic**  to get to a place where we can actually perform inference with it. First we can consider **reduction to propositional logic**. The following rules are different form the **extended interpretations** used in [[First-Order Logic]] these instead refer to new sentences and symbols created as we perform inference.

**Universal Installation** -> If we have a statement with universal quantifiers we can use the rule of **universal instantiation**. This says that anything we can obtain from substituting a **ground term** into a variable within a universal statement is implied by that statement being true. This is written using **substitution** notation as seen in [[First-Order Logic]]. We can write this formally by saying that $Subst(\theta, \alpha)$ is the result of applying the substitution $\theta$ to the sentence $\alpha$. Then **universal instantiation** is the following

![[Pasted image 20220213191655.png]]

So for any variable $v$ and ground term $g$ we can infer that a forall statement for the sentence $\alpha$ with variable $v$ infers the substitution of any $g$ in the place of $v$.

**Existential Instantiation** -> The rule here is if we have an existential statement we can perform **existential instantiation** by replacing the variable that is quantified by a new constant symbol that isn't used elsewhere in the knowledge base.

![[Pasted image 20220213192326.png]]

We have to create a new symbol that is called a **Skolem Constant**. We have to create a new symbol as the rule doesn't mean it is anything that is already in the knowledge base. Existential instantiation can be applied only once. We can **discard** the existential statement once we have instantiated it as the effect of there being one object fulfilling the statement makes it always true. It isn't the same but it will cause the same inferences so anything satisfiable in the original knowledge base will also be satisfiable after this.

## Reduction to Propositional Inference
We now have rules that reduce quantified sentences to unquantified ones. We replace each existential sentence with a single instantiation then every universally quantified sentence can be an infinite set of *all possible* instantiations. So given the knowledge base 

![[Pasted image 20220213204337.png]]

We can apply **UI** to remove the universal statement. We instead get the following sentences added on.

![[Pasted image 20220213204422.png]]
 Now we have a proposition based knowledge base if we view all the **ground terms** as propositions such as $Evil(John)$. Now we can apply an algorithm such as those in [[Logical Agents]] to obtain any inference we want. There is a problem however if we have a **function symbol** we have **infinite ground terms**. For example if we have $Father(John)$ then we also have $Father(Father(John))$ and so on. None of our techniques can solve an infinite set of propositions. However there is a solution a **theorem** that if a sentence is entailed by the original first order knowledge base then there is a proof for any entailed sentence that take only a finite number of the propositionalized knowledge base. So we can solve this with a depth based approach starting with constant symbols then allowing 1 level of functions and then 2 and so on until we have found a proof. The problem is if the sentence isn't entailed the our recursion will never end! So **FOL** is **semidecidable** meaning we can tell if a sentence is entailed but not if its not entailed.

 ## Unification and Lifting
 One problem with the **propositionalization** approach is that there is not matching. For instance we all know not to generate the sentence $King(Richard)\land Greedy(Richard)\implies Evil(Richard)$ from the knowledge base in 9.1 as Richard isn't the king so we can never satisfy the preconditions. The only sentences involved are the following.

 ![[Pasted image 20220213211452.png]]

 So instead of trying our every possible $x$ we can instead find and $x$ that is both $King$ and $Greedy$ infer $x$ is evil from these. We need a **substitution** $\theta$ that makes the **conjuncts** (the parts required to make the premise true $King$ and $Greedy$) true then we can also infer conclusion is true under $\theta$. This can even work with more universal statements, for example the following still implies $John$ is greedy so how can we use it.
 
![[Pasted image 20220213212035.png]]


We need a substitution for the variables in the implication and the sentences in the knowledge base that give us the **conjuncts**. This is captured in **Generalized Modus Ponens**

**Generalized Modus Ponens** -> For atomic sentences $p_i$, $p_i'$ and $q$ where there is a substitution $\theta$ such that $Subst(\theta,p_i')=Subst(\theta,p_i)$ for all $i$  we have

![[Pasted image 20220213212854.png]]

So $p_i'$ are some sentences in our knowledge base and $p_i$ are the **conjuncts** so if we find a **substitution** to make them all true we can conclusion that when we perform this substitution on the conclusion, it is inferred. In total there are $n+1$ premises for this, $n$ atomic sentences $p_i'$ and the implication. So an example of this being used we could perform the following inference.

![[Pasted image 20220213213527.png]]

This comes from **universal instantiation** of course. We know any $p\models Subst(\theta, p)$ for any $p$ and $\theta$. So from the fact that $Subst(\theta,p_i')$ for all $p_i'$ we have $Subst(\theta,p_1')\land...\land Subst(\theta,p_n')$ can be inferred we can also infer $Subst(\theta,p_1\land...\land p_n\implies q)$ which is the same as $Subst(\theta,p_1)\land...\land Subst(\theta,p_n)\implies Subst(\theta,q)$.  Hence since  $Subst(\theta,p_i')=Subst(\theta,p_i)$ we know the premises for the second statement are true. So we can apply **modus ponens** $(\alpha\implies\beta),\alpha\models\beta$. We say **generalized modus ponens** is a **lifted** version it is raised from ground variable free propositional form to FOL form. 

## Unification
So now we need to find substitutions that make different logical expression look identical. This is called **unification**. So the $Unify$ algorithm takes in two sentences and returns a unifier for both of them if that exists. So if we wanted to know who $Knows$ $John$ we could $AskVars(Knows(John, x))$ and we can return the results of **unification** giving us the following.

![[Pasted image 20220213215619.png]]

The last one fails as we can't have $x$ be $John$ and $Elizabeth$ at the same time. We need to make sure we don't use the same variable when **unifying** this is called **standardizing apart**. Changing a variables name doesn't change the meaning of the sentence so we can do this without worry, $x$ has the same semantic meaning as $x_{69}$.  It could also be the case that the unifier can have more than one unification substitution. So $Knows(John,x)$ and $Knows(y,z)$ can unify both $\{y/John,x/z\}$ but also $\{y/John,x/John,z/John\}$. We want the **most general unifier** (**MGU**) instead. A final problem is what if we try to match a variable against a **complex term** (with a function), such as $Unify(x,S(x))$. If we try to unify this we will never get a substitution and we will loop forever. This gives the following step for a unification algorithm (we use $\stackrel{?}{=}$ to mean we are trying to unify two constants)

1. **Decomposition** -> If we are trying to unify two **predicate symbols** with variables where the predicate symbols are the **same** we can remove the predicate symbols and just unify the **terms** so $f(s_1,...,s_n)\stackrel{?}{=}f(t_1,...,t_n)$ becomes $s_1\stackrel{?}{=}t_1,...s_n\stackrel{?}{=}t_n$ 
2. **Conflict** -> If we are trying to unify two **predicate symbols** with variables where the predicate symbols are **different** we cant continue so we return a **fail**. For example $f(s_1,...,s_n)\stackrel{?}{=}g(t_1,...,t_n)$ since $f\neq g$.
3. **Eliminate** -> If we are trying to unify some $P$ and within in it we have $x$ but also $x\stackrel{?}{=}t$ and $t$ isn't a variable then we can substitute $t$ in for any $x$. So we get $x\stackrel{?}{=}t$ and $P\{x/t\}$.
4. **Delete** -> If we are trying to unify something with itself we don't need to and we can remove it from our process so $P, s\stackrel{?}{=}s$ becomes $P$
5. **Switch** -> If we are trying to unify a nonarable to a variable we just *switch* them around so $P, s\stackrel{?}{=}x$ (where $x$ is a variable but $s$ isn't) becomes $P, x\stackrel{?}{=}s$
6. **Coalesce** -> If we have two variables that occur in some $P$  and we are trying to unify them. Then we can replace all the occurrences of one in $P$ with the other. So $P, x\stackrel{?}{=}y$ becomes $P\{x/y\}, x\stackrel{?}{=}y$
7. **Occurs Check** -> If we are trying to unify $x\stackrel{?}{=}s$ and $s$ isn't a variable. Then we will continue to apply eliminate over and over again creating an infinite loop. This makes the algorithm take **quadratic time** on its own.

This together builds the $Unify$ algorithm bellow.

![[Pasted image 20220213224830.png]]

## Store and Fetch
We also need to manage our knowledge base. **Store** and **Fetch** are used to *store* and find the facts that unify to a given sentence. We can just store them all in a list and attempt unification on every element. It can be slow but it works. We can also use **predicate indexing** as we know $Knows(...)$ will never unify to $Brother(...)$. So we store different predicates in different buckets and only try to unify matching ones. We can also index by what is in the predicates. We would need an index for each possible key so in the end we get a **subsumption lattice** where we store a query base on all the locked in values it has. This allows us to split up a query into multiple searches that converge on the correct match.

![[Pasted image 20220213225736.png]]

This will take $2^n$ nodes where $n$ is the number of arguments to the predicate so this doesn't work for many indices.

Now using **unify** we will look at way of performing inference directly on **FOL** in **Forward Chaining**, **Backward Chaining** and finally **Resolution**.

## Forward Chaining
The idea here is quite simple we start with our ground truths in our knowledge base we then match those **premises** to **rules** giving us new truths. We continue like this until we reach our goal statement. This has to take place on **FOL** **definite clauses**. That is they have the structure
$$
A\land B\to C
$$
So $A$, $B$ and $C$ are literals. We could also have just a single literal as a **definite clause**. The variables in these literals can exist and are assumed to be **universally quantified**. Since there are only definite clauses this can't represent all knowledge bases. If there are no **function symbols** then the knowledge base is called a **Datalog**.

We can now look at an algorithm for it. Most of the computation is found in the "$\theta$ *such that*" part which would be a **pattern matching** part. The way it works is we continually take a rule and match it's premises against anything we can find in our KB getting the substitution $\theta$ we the apply this to the conclusion and add that to our KB hence we have found new knowledge. We try to match this against out rule we are trying to prove and continue. We stop when either we find a match from what we have inferred or we cannot find any more rules to apply. We only consider a fact new if there isn't already an instance in KB.

![[Pasted image 20220215183208.png]]

This works by brute force, we can reconstruct how it finds an answer with a graph as follows.

![[Pasted image 20220215183953.png]]

Once no new inferences can be made the **KB** is said to be at a **Fixed point**. This is a ground up approach where we build up to our conclusion form the base of our knowledge. This is **sound** and **complete** meaning first anything it implies will be entailed and secondly anything that is entailed will also be implied. If we have **function symbols** then this can generate **infinite** new facts. This does give us the same problem as **reduction to propositional inference** where we can say if something is entailed but not if it isn't.

We want to do this all efficiently, a lot of the computation comes down to matching to find new inferences. We can store our knowledge by the **predicates** and **terms** but we would still need to find an optimal solution to look at them in to solve this. This is an **NP-hard** problem but we can use heuristics like **MRV** where we use inferences with rules that give the most flexibility as in [[Constraint Satisfaction Problems]].

### Efficient Forward Changing
#### Matching Rules Against Known FacTS
This is the problem of filling out the conjuncts in the rules (a problem called *matching*). We may need to find an object for which many predicates are true. It can be inefficient to search through all objects fulfilling one predicate and then the next. Instead we can search through the predicates in the order of how many objects are in them. This will give us the least objects to search through. This would be using the *minimum remaining value* heuristic.

#### Incremental Forward Chaining
For some times step $t$ in the algorithms execution we will use all our knowledge to derive every possible new sentence. In the algorithm given we check every combination of statement every timestep. But if both statements used were present in the previous timestep then any sentence they could have derived would already be derived. Hence the only combinations worth looking at are combination containing at least one sentences derived in the previous timestep. 

The way this is implemented is we only check a rule if one of the conjuncts it unifies with was generated in the previous timestep $t-1$ for timestep $t$. With this approach we can also index rules by what types of predicates they require. This way we only check a rule if at $t-1$ a matching conjunct was derived.

#### Irrelevant Facts
The problem here is we are trying to perform inference by considering every possible combination of variables. There may be some variables that are completely irrelevant to our goal conjunct however. If we know many rules are irrelevant to our goal we can restrict the set we consider to this. 

One way to deal with this is to make new rules that are restricted to just the values we care about. We can do this by adding so called *magic facts*. Which just help with book keeping to make sure we are using facts on track. The magic set which applies to certain variables such that they can only have certain values. Hence restricting what options we can try out.



## Pattern Matching and [[Constraint Satisfaction Problems]]
There is actually a strong connection between why the **CSP** heuristics work with **forward checking**. To se this if we take the Australia example we can reduce it to a **FOL** problem where the **constants** are the colors and the **predicates** are saying the different variables for the different states are the same.

![[Pasted image 20220215185849.png]]

We get this. Now if we solve this with **forward checking** we take the input sentence at the top of (b) and work out if **colorable** is implied. To do this we will try to match the diff statements as we add new ones we are treating the variables the same as in **CPS** so the heuristics work.

## Backward Chaining
As you might expect this is the opposite of **forward chaining**. In **backward chaining** we start with our **goal** state and work out to our basic information until we can match everything.  The **recursive** algorithm is given bellow.

![[Pasted image 20220215191913.png]]

The way this works is we find a unifying conclusion $rhs$ then we attempt to match that with out goal. If we can't do that we have failed this attempt but we spray out with the recursion so it is ok for some to do this. The OR part goes over every possible rule that could possibly solve for our goal. The and part then takes the list of subgoals this rule will need (conjuncts) and find substitutions through another layer of OR search with them. Out $FOL-BC-AND$ function just splits up the premises of a definite clause and tries to backward chain them in turn. This will in turn find all possible solutions. There is a problem that we can end up in loops of recursion so this algorithm will never terminate. Since it finds all results in turn it is called a **generator**.

![[Pasted image 20220501103857.png]]

An **AND-OR** search is used as any rule could lead to the solution hence **OR** but all **premises** must be met hence **AND**. Here this works as a **Depth First Search** algorithm.

#### Logic Programming
In logic programing we define knowledge in a formal language then run inference on it to derive new knowledge to help us.

#### Efficient Implementation
Instead of managing possible results generated by each substitution through recursion. We can keep all our substitutions on a stack. This makes the code and data more accessible and allows for easier debugging.

To save space we can store with each possible variable a binding. As we navigate our search tree we add bindings when we need to. If we succeed we return all the current bindings. If we fail we can backtrack and unbind some variables. These paths where variables are bound are called *trials*.

We can also get a speed up by *compiling* our knowledge base. Here for each rule we generate a prover that can more effectively knows our knowledge base and can find what bindings can solve situations more efficiently. We build up knowledge instead of just re-interpreting the KB every time we try to infer something.

## Resolution
Resolution is the final way to do logical inference. It takes some KB in **FOL** and converts it to **FOL CNF** form. We can then use **Non-ground Binary Resolution** to perform inference.  First we will go over conversion to **CNF** there are 6 steps to this the basics of this are in [[Logical Agents]] but there are some alterations for **FOL**.

1. **Eliminate Implications** -> We replace any implication or bi-implication with its corresponding $\lor$ and $\land$ versions.
2. **Move ¬ Inwards** -> In addition to the rules from [[Logical Agents]] we also need to pay attention to the **quantifiers** here are the basic rules.

![[Pasted image 20220215195147.png]]

3. **Standardize apart** -> For any sentence that uses the same variable twice we have to make sure this isn't repeated to avoid confusion later.
4. **Skolemize** -> This is when we remove the existential quantifier. We can simple add a new constant that isn't used elsewhere. We need to take care with $\forall$ however, since the meaning of an existential statement that is within a universal statement is different we need a Skolem constant for every external variable. So we use a function for this. $\forall x. \exists y. loves(x, y)$ becomes $\forall x. loves(x,F(x))$ of course this time making sure the function isn't names elsewhere (it is called a **Skolem Function**)
5. **Drop Universal Quantifiers** -> Since we have **Skolemized** we don't need $\forall$ anymore and we can drop them. They are implicit when we are performing unification.
6. **Distribute over $\lor$ and $\land$ as** -> As in [[Logical Agents]]

### Inference Rules
We we have two complementary literals (with different signs, that unify under $\theta$) in two different clauses then we can combine, remove and implicate the remaining literals with the same substitution $\theta$

![[Pasted image 20220215200304.png]]

So the idea is we continue to add **CNF** clauses together that we can unify together until we unify to an empty clause. The reason we want this is we start by trying to unify with the negation of what we are trying to prove. Reducing to nothing means there was a inconsistency in the knowledge base hence the negation we added isn't implicated.

![[Pasted image 20220215205140.png]]

![[Pasted image 20220215205353.png]]

[[Inference in First-Order Logic Questions]]