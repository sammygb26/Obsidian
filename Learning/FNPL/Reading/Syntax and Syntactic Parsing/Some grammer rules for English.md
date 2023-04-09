### Sentence Level Construction
These are constructions that come from the $S$ symbol. These can come in different flavors for examples **declarative** structures have a subject noun phrase followed by a verb phrase for example "I eat apples". Some examples in the ATIS domain are

![[Pasted image 20230408155322.png]]

Sentences with an **imperative** structure have no subject and often begin with a *noun phrase*. For example

![[Pasted image 20230408155413.png]]

These are modeled with the structure $S\to VP$. Sentences with a **yes-no question** structure are often used to ask questions and begin with an **auxiliary verb**, followed by a subject $NP$ and then a $VP$. For exaple

![[Pasted image 20230408160123.png]]

These can also have **pragmatic** meanings like how the third sentence is really a command. The rule for generating will be $S\to Aux\space NP\space VP$. There are also **wh**-structures. These are so named because one of their constituents is a **wh-phrase** and includes a **wh-word** (who, whose, when, where, what, which, how, why). These are broadly grouped into two classes of sentence-level structures. The **wh-subject-question** structure just like the *declarative* structure accept the first noun phrase contains some wh-word.

![[Pasted image 20230408161146.png]]

The rule is $S\to Wh-NP\space VP$. In the **wh-non-subject question** structure, the wh-phrase is not the subject of the sentence, and so the sentence includes another subject. In these types of sentence an auxiliary appears before the subject $NP$ as in the yes-no-question structure. The rule will be $S\to Wh-Np\space Aux\space NP\space VP$. An examples sentences could be

![[Pasted image 20230408161609.png]]

Here we have a **long-distance dependency** as the $Wh-NP$ "what flights" is far away from the predicate that is semantically related to the main verb *have*. This relation has a **semantic meaning**.

### The Noun Phrase
We have seen noun phrases in three flavors: pronouns, proper-nouns and $NP\to Det\space Nominal$ construction. We will look as the Det Nominal as it is the most grammatically complex.

##### The Determiner
Noun phrases can begin with lexical determiners as in:

![[Pasted image 20230408163331.png]]

This role can also be filled by more complex expressions for example

![[Pasted image 20230408163415.png]]

In this case we have a **possessive expression** where a noun phrase is followed by a 's as a possessive marker. The rule would be $Det\to NP's$. In some cases in English determiners are optional like with plurals.

![[Pasted image 20230408163703.png]]

**Mass nouns** also don't require determination. These don't take the indefinite article "a" as they are a collective substance. Many abstract nouns are *mass nouns* like *music, homework, breakfast, lunch and dinner*.

##### The Nominal
The nominal construction follows the determiner. It contains any pre- and post-head noun modifiers. The simplest form is $Nominal\to Noun$. More complex nominal recursive rules use this to bottom out.

##### Before the Head Noun
Different kinds of words classes can appear after the determiner but before the head noun. For examples **cardinal numbers, ordinal numbers** and **quantifiers**. Cardinal numbers:

![[Pasted image 20230408164657.png]]

Ordinals:

![[Pasted image 20230408164717.png]]

Some *quantifiers* only occur in with plural count nouns like "many fares". While other quantifiers like *many* and *a little* only occur with noncount nouns. 

**Adjectives** occur after quantifiers but before nouns.

![[Pasted image 20230408165244.png]]

They can also be grouped into a phrase called an **Adjective phrase** ($AP$). These can have an adverb before the adjective 

![[Pasted image 20230408165300.png]]

The final rule is given as

![[Pasted image 20230408165323.png]]

This has a flatter structure and is simpler than most mode generative theories of grammar give.

##### After the Head Noun
A head noun can be followed by **postmodifiers** of which there are three kinds common in English.

![[Pasted image 20230408165541.png]]

Here are some examples with the $PP$ labeled []. Then also multiple can be chained together.

![[Pasted image 20230408165728.png]]

We add a Nominal rule to account for this. It will be $Nominal\to Nominal\space PP$. There three most common kinds of **non-finite** postmodifiers are gerundive and infinitive forms.

**Gerundive** postmodifiers contain a verb phrase that begins with a gerundive verb.

![[Pasted image 20230408170236.png]]

The rule that allows this is $Nominal\to Nominal\space Gerund VP$ and we can make rule for this by replacing $V$ with $Gerund V$ in all $VP$ productions. Then $GerundV$ is defined as

![[Pasted image 20230408170416.png]]

The other non-finite clauses, infinitives and -ed forms are like:

![[Pasted image 20230408170855.png]]

A postnominal relative clauses is a clause that begins with a **relative pronoun** (that and who are common). This *relative pronoun* functions as a pronoun for the noun in the same sentence. It is the subject of the embedded verb.

![[Pasted image 20230408171411.png]]

To add in these phrases we could add rules like

![[Pasted image 20230408171446.png]]

The **relative pronoun** can also be the object as in "The earliest LoganAir flight that I can get".

##### Before the Noun Phrase
Word classes that modify and appear before NPs are called **predeterminers**. Many of these have to do with number or amount; for example

![[Pasted image 20230408171900.png]]

![[Pasted image 20230408172801.png]]

### Agreement
English's inflectional morphology means most verbs appear in two forms in the present tense. One for third-person singular subjects and the form for all other subjects. Here are some examples with "do".

![[Pasted image 20230408172451.png]]

**Agreement** occurs when there is some noun that has some verb acting as its subject. The sentences in which the subject doesn't agree with the verb are ungrammatical.

![[Pasted image 20230408172729.png]]

There are different ways to expand our grammar to handle this. One way is to have different rules for different 3gs and non-3gs subjects. We then add rules like 

![[Pasted image 20230408173138.png]]

Then we also need 3sg and Non-3gs Noun phrases will have to duplicate all their rules.

![[Pasted image 20230408173343.png]]

The issue is we have to keep doubling the size of the grammar and this is only the start of agreement phrases. This can be combated by **parameterizing** each non-terminal of the grammar with **feature structures** and **unification** but for small grammars we don't need to worry too much.

### The Verb Phrase Subcategorization
The verb phrase is made our of a **verb** and a number of other constituents like NPs and PPs.

![[Pasted image 20230408173844.png]]

Many constituents can follow the verb including whole sentences these are called **sentential complements**.

![[Pasted image 20230408174011.png]]

The rule is simply $VP\to Verb\space S$. Verbs can also be followed by **particles** like "take off" the particle here is considered to be part of the word. Not every verb is compatible with every verb phrase. For example there are **transitive** verbs like "find" which take a direct object and **intransitive** verbs like "disappear" (I found a flight vs I disappeared a flight). But modern grammars use as many as 100 **subcategories**. We would say "find" **subcategorizes for** an NP, while "want" subcategorizes for either a NP or a non-finite VP. These constituents are also called the **compliments** of the verb. Another way to think about this is as the verbs as a logical predicate taking the constituents as arguments. $$FIND(I, A\space FLIGHT)\hspace{64pt}WANT(I, TO\space FLY)$$To account for these rules we could add in more non-terminal types but this would explode the size of our grammar. Instead **feature structure** is used.

### Auxiliaries
These are basically special verbs also called **helping verbs**. They have particular syntactic constraints that give their meaning. There are four kinds **modal** verbs (*can, could, might, must, will, would, shall and should*), the **perfect** auxiliary *have*, the **progressive** *be* and the **passive** auxiliary *be*.

Each of these place a constraint on the form of the following verb and can combine in a particular order. 

1. **Modal verbs** subcategorize for a VP whose head verb is a bare stem. (*can go in the morning, will try to find a flight*)
2. **Perfect verb** (have) subcategorizes for a VP whose head verb is the past participle form. (*have booked*)
3. **Progressive verb** (be) subcategorizes for a VP whose head verb is the gerundive participle (*am going from Aberdeen*)
4. **Passive verb** (be) subcategorizes for a VP whose head verb is the past participle (*delayed by inclement weather*)

A sentence can have multiple auxiliary verbs, but they must occur in a particular order *modal < progressive < passive*. Some examples are

![[Pasted image 20230408205944.png]]

The special order can be captured by a **verb group** whose sub constituents include all auxiliaries as well as the main verb.

### Coordination
The major phrase types discussed can be **conjoined** with **conjunctions** like *and*, *or* and *but* to form larger constructions of the same type. For example a **coordinate noun phrase** is made our of two other noun phrases seperated by a conjunction

![[Pasted image 20230408210217.png]]

The rule will be $NP\to NP\text{ and }NP$. This is often used as a **test for constituency**. For example

![[Pasted image 20230408210443.png]]

With the determiner the is evidence for an underling $Nominal$ constituent with the rules $Nominal\to Nominal\text{ and }Nominal$. Here are some examples with $VP$s and $S$s

![[Pasted image 20230408210622.png]]

All the major phrase types can be conjoined in the fashion and so it is possible to represent this more generally with **metarules** such as $$X\to X\text{ and }X$$Where $X$ is not a non-terminal but rather can represent any nonterminal we wish for.

[[Syntax and Parsing Questions]]