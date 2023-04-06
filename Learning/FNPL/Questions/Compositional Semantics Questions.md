What is semantics? #flashcard #FNLP #question 
	Semantics defines the meaning of sentences, how a sentences **relates to the world**. It is important to be able to process this to have AI that can understand natural language and what it signifies.

---
What are the who types of relation a sentences can have the world semantically? #flashcard #FNLP #question 
	Semantically a sentence can either related in terms of **truth condition and denotation** - here it is a logical statement that is either true or false. Then **connotations** which are other assertions, implied meanings and metaphors.

---
How would a question answering agent need to interact with its knowledge base? #flashcard #FNLP #question 
	A question answering agent need to have some knowledge base. Either text or a database of some sort. Then when it receives a question it needs to properly parse the sentence in the way a human would understand it and use that to relate to its knowledge base. The *meaning* must be captured as a way to query the KB.

---
When we have some sort of database as a KB what is the text generation task called? #flashcard #FNLP #question 
	This is called **context-to-text** generation.

---
What is sentential semantics? #flashcard #FNLP #question 
	Sentential semantics capture the meaning of well formed sentences. It allows the meaning of individual phrases to be build up with recursion to form an overall meaning.

---
What is lexical semantics? #flashcard #FNLP #question 
	This is the meaning of individual words. It tells you things like what a man and how it relates to the world.

---
How does the resolution of syntactic ambiguity affect sentential semantic meaning? #flashcard #FNLP #question 
	The structure of the syntax tree informs how word meanings are combined. A change here therefore will change the meaning of the final sentence (sententially).

---
What are three non syntax ambiguities? #flashcard #FNLP #question 
	1) Word sense ambiguity 2) Semantic scope 3) Anaphoric expressions.

---
What is an example of semantic scope ambiguity? #flashcard #FNLP #question 
	The classic example is **every man loves some woman** does *some* outscope *every* meaning some refers to the exact same woman or the other way around and every man loves a possibly different woman.

---
How can scope ambiguity be resolved? #flashcard #FNLP #question 
	 A level of how likely the sentences are can help. Every man loving some different woman is more likely. Then other sentences can also disambiguate. "She is very pretty" would collapse some to mean just a single woman.

---
How is compositionality used to derive sentential meaning? #flashcard #FNLP #question 
	The key thing is the meaning of the whole sentence is a function of its parts. The compositionality of semantic components it used to ensure we get valid sentence then we define rules to combine the subsentences for these parts.

---
What is the aim for how derived sentence meaning should behave, what logical construct most easily fits this? #flashcard #FNLP #question 
	Derived sentence meanings should be **unambiguous**, **verifiable** and should allow **automated inference**. The logical construct therefore used is First Order Logic.

---
How is logical different than common sense inference? #flashcard #FNLP #question 
	In logical inference we can use **logical constants** like *someone* to replace a subject of a verb. But in common sense inference we apply more knowledge to get an idea of what parts of sentences mean the expanded meanings in our mind are then operated on. Therefore this implication requires we understand the relation between words.

---
How does sentential semantics resolve semantic scope ambiguity? #flashcard #FNLP #question 
	It can either be built into the language giving sentences that OR the two options. Or we can force on by excluding options.

---
How are tense modifiers added with Davidsonian semantics? #flashcard #FNLP #question 
	With Davidsonian semantics we add tense modifies by creating an event. This event is incorporated into the old sentence as a new argument. We then conjoin on modifiers which can specify other attributes of th event. Like modifiers and times.

---
What is the benefit of event variables when it comes to modifiers? #flashcard #FNLP #question 
	They add an easy way to add on an unbounded number of modifiers to an event. Then each can be derived form the final sentence via AND elimination.

---
What two rules must be defined to allow sentential semantics to be built using a syntax tree? #flashcard #FNLP #question 
	We want **lexical rules** which give logical forms for words then we want **compositional rules** which define for non-terminals how the daughter nodes should be combined to give their logical form.

---
How is lambda calculus used to define lexical and compositional rules? #flashcard #FNLP #question 
	Lambda calculus allows us to define substitution rules in a variety of ways. We define these via **lambda abstraction** then once we pass in other logical forms as arguments we arrive at a bottomed out meaning through beta reduction.

---
What is the lambda abstraction beta reduction rule? #flashcard #FNLP #question 
	If we have a statements $\psi$ which is well formed with a variable $x$. Then $\lambda x\psi$ is a well formed FoL expression. It is a function where $$\lambda x\psi(a)=\psi[x/a]$$where be substitute the arguments $a$ into $x$'s place.

---
How is compositional rules defined with lambda calculus? #flashcard #FNLP #question 
	Compositional rules define which daughter logical form will be the functor and argument to that functor. Then once all is reduced a new logical form is given. This never leaves an error as compositionality means logical forms must have commonalities for the same Tags allowing all to be handled with the same rules.

---
How simply would a compositional rules be define, what is its form? #flashcard #FNLP #question 
	We would say something like say for a $S$ phrase $VP.sem(NP.sem)$ where the daughters nodes a $VP$ and a $NP$. But this exact way is problematic when it comes to quantified noun phrases. Then that is also problematic and requires resolution with higher order functions.

---
Why must noun phrases be treated as functors in FoL? #flashcard #FNLP #question 
	They must have arguments passed in and be treated as functors. This is to allow quantified nouns. But this conflicts with transitive verbs and requires the verb to first move its remaining argument to the outside before continuing.

---
Why must higher order functions be used for sentential semantics what in general may the form be? #flashcard #FNLP #question 
	For nouns and verbs we must have a $VP.sem(NP.sem)$ but VP will have a form like $$\lambda R\lambda x.R(sem(x))$$ this means the Noun phrase $R$ is treated as a functor within allowing both transitive verbs to extract their arguments and quantified nouns to be well formed.

---
What is the problem with just listing scope interpretations? #flashcard #FNLP #question 
	If we just list scope interpretations we will get an exponential number. Instead semantic underspecification is used.

---
How are logical forms specified in semantic underspecification? #flashcard #FNLP #question 
	Here we list different $l$ terms and also $h$ terms. The rule is each $h$s must equal a unique $l$ with no free variables. We then specify the $h$'s as the ambiguous components of $l$s and add in some rules on what the $h$s can be leading to a finite number of interpretations.

---
What does semantic underspecification capture? #flashcard #FNLP #question 
	This captures the commonalities in all operation trees that lead to the final sentences without concretizing a single one. Then we can work out instance by applying the resolution rules to get a single tree.

---