Previously in [[FNPL/Reading/Compositional Semantics]] we treated word meaning as know. So the meaning of $cat$ is $CAT$. But this is accurate and words can have many different meanings. We have to define carefully what we mean by a word. A **lexeme** is a particular form with its meaning, a **lexicon** is a finite list of lexemes. Often the *lexemes* are represented by a **lemma** or **citation form**. For example "sang" is a lexeme represented by the lemma "sing". The specific forms like "sang", "sung" "sing" are **wordforms**.

Resolving a word to a lemma is called **lemmatization**. This isn't always *deterministic* can can be informed by the context the  wordform. The lemmas are also dependent on the POS of the wordform. This process can be done with FSTs as with [[Morphology Parsing]]. Generally though there are more meanings that *stem words* for example "celebration" and "celebrations" may use the same lemma but "celebrate" may not as the meaning is somewhat altered.

## Word Sense
Often words will have very many meanings for example. **Bank** can be used to mean a "financial institution" and "sopping mound". To resent this we say the **lemma** Bank has two **senses**. 

- A **word sense** is a discrete representation of one aspect of the meaning of a word!

The meaning are represented with a superscript i.e. $bank^1$ and $bank^2$. If $bank^1$ is the river bank and $bank^2$ is the financial bank then these two meaning are **homonyms** as the meanings are basically unrelated. The two senses have **homonymy**.

The meanings can be related for example $bank^3$ might mean the *biological bank* as in "blood bank", "seed bank" etc. This is similar to $bank^2$ the "financial institution" in both cases the bank is a store of something. We call this kind of relation **polysemy** rather than homonymy.

These relationships can be structured. Take for example $bank^4$ as in "The bank is on the corner by the book shop". Here $bank^4$ means the building belonging to the institution bank. But this kind of reference happens all the time with other organizations to. For example *schools, universities, hospitals etc*. There is a common rule for example $$Building\iff Organization$$This particular subtype of *polysemy* is called **metonymy**. It is the use of one aspect of a concept or entity to refer to other aspects of the entity or the entity itself. Another example would be *"The White House"* to refer to the political entity rather than the building.

![[Pasted image 20230426123231.png]]

It can be hard to decide how many meanings a word has as things like polysemy and homonomy can be hard to distinguish and in truth it is only a question of degree to which different senses are distinct. One useful technique to test if two word senses are separate is to make a **zeugma** which is a conjugation of the two meanings in a sentence.

![[Pasted image 20230426141230.png]]

Clearly the 3rd sentence doesn't make much sense suggesting there are two conflicting meanings for **serve**.

We might also ask how we should define the meanings. Often dictionaries will have circular definitions as words are defined in terms of other words. These entries are useful to humans as generally dictionaries are used to fill in holes rather than to understand and entire lexicon.

Machines can use a similar approach with word sense grouped together with **sense relations** applied between groups. For example $left$'s meaning may be the opposite to $right$'s. An example database is **WordNet**.

Another option is to create a small finite set of semantic primitives, or atomic units of meaning.  Then the sense definitions are crafted out of these primitives.

## Relations Between Senses

#### Synonymy and Antonymy
When two different words (lemmas) are identical or nearly identical we say they are **synonyms**. For example $$couch/sofa\hspace{16pt}vommit/throw\space up\hspace{16pt}filbert/hazelnut\hspace{16pt}car/automobile$$Another definition is two words are **synonymous** if they are substitutable in any sentence without changing the truth conditions. This means they have the same **propositional meaning**.

But of course any pair of course while giving the same truth conditions will have different connotations and subtle meaning differences in any case. Defining **synonyms** this exactly means likely no words will be synonymous. So generally *synonymy* refers to approximate synonymy.

Instead of words being synonymous we will look at when senses are synonymous. For example $large$ and $big$ may have the same meaning when it comes to sizes of objects and thusly can be substituted. 

- "A large plane" vs "A big plane"

But they don't always have the same meaning as for example when used to talk about siblings

- "He had a big sister" vs "He had a large sister"

But clearly the meaning is the same in the first case so we say the **senses are synonymous**.

When two words have opposite meanings they are **antonyms**. For example $$long/short\hspace{16pt}big/little\hspace{16pt}fast/slow\hspace{16pt}cold/hot\hspace{16pt}dark/light\hspace{16pt}rise/fall$$and so on. It is difficult to give a definition here as although the senses can be opposite there can be different kinds of opposite. In general we an say both words fall at the opposite ends of some scale. There are also **reversives** that describe a change in some opposite direction "rise/fall" and "up/down". Of course these antonyms are very close in terms of meaning and where they can their bahaviour in a sentence so distinguishing can be hard.

#### Hyponymy
One sense is a **hyponym** of another sense if the first sense is more specific than the second. For example "car" is a hyponym of "vehicle". In this scenario "vehicle" is the **hypernym** of "car". Another word for **hypernym** is **subordinate**.

Formally we say something is a hypernym if the class denoted by the meaning includes all the classes denoted by the hyponym. So all cars are vehicles. This can therefore be states as $A\implies B$. An **ontology** describes a grouping of these relationships between objects. These relationships are generally *transitive*. The

#### Semantic Fields
Another relation is **meronymy**, the *part-whole* relation. For example a *leg* is part of a *chair*. So "leg" is a **meronym** of "chair". Then "chair" is a **holonym** of "leg".

## WordNet: A Database of Lexical Relationships
This is a lexical database commonly used for English sense relations. There are three databases in **WordNet** for nouns, verbs and adjectives and adverbs. Closed class words are not included. Each lemma has different senses with a **gloss** for each describing its meaning in words.

![[Pasted image 20230426151250.png]]

Senses are grouped into **synsets** or sets of synonymous senses. Then the different relations as captured in the database. These are the different relations

![[Pasted image 20230426151232.png]]

