What is morphology the result of? #flashcard #FNLP #Morphology
	This is the results of the fact that words aren't the smallest unit within languages. Instead words are made up of parts themselves.

---
What are agglutinative languages? #flashcard #FNLP #Morphology 
	These are languages where words can be composed out of morphemes each of which give some concept. These are combined to make more complicated and expressive words.

---
What are stems? #flashcard #FNLP #Morphology 
	Stems are the roots of different words. A stem is a basic unit that is then modified by affixes. An example of a stem might be house, person, combine, move

---
What is an affix? #flashcard #FNLP #Morphology 
	An affix  is a modification of a stem word it adds extra meaning to the word and can modify its grammar and PoS.

---
What are the three types of affixes? #flashcard #FNLP #Morphology 
	These are **prefixes** that mortify the start of a word "pre- or post-", **suffixes** are added on the end of words "-ed or -s", **circumfixes** modify the inside of a stem word.

---
What are the four methods for combining stems and affixes? #flashcard #FNLP #Morphology 
	There is **inflection, derivation, compounding and cliticization**.

---
How does inflection combine stems and affixes? #flashcard #FNLP #Morphology 
	This combines a stem and a grammar affix and does not change the *grammatical category* (throw -> throwing)

---
How does derivation work to combine stems and affixes? #flashcard #FNLP #Morphology 
	A **derivation** changes the grammatical category the word is in. For example (combine -> combination).

---
How does compounding work to combine stems? #flashcard #FNLP #Morphology 
	Here stem words are combined together for example doghouse.

---
How does cliticization combine stem words? #flashcard #FNLP #Morphology 
	Here words are semi combined by an apostrophe is left in. For example I've, we're, he's.

---
What are inflections? #flashcard #FNLP #Morphology 
	This is one way words change with context. For example Spanish words change based on gender and plurality and tense.

---
What is the aim with morphology parsing in English? #flashcard #FNLP #Morphology 
	Morphology parsing in English we want to break words down into a main stem word plus one or more affixes giving grammatical information.

---
Can you give an example of morphological parsing applied to a simple English word? #flashcard #FNLP #Morphology
	Cats could becomes cat + N + PL while  walking could be walk + V + PresPart. Smoothest would be smooth  + Adj + Sup.

---
What are some obstacles that need to be modeled to perform morphological parsing? #flashcard #FNLP #Morphology 
	Some things making this hard are **irregular forms**, **systematic rules**, **things that are similar to affixes but aren't**, **blocking**.

---
What are irregular forms in morphology? #flashcard #FNLP #Morphology 
	In general there will be rules that we follow when adding affixes to words. Irregular forms change the word in ways these simple rules don't capture, these are edge cases.

---
What are systemic rule sin morphology? #flashcard #FNLP #Morphology 
	These are rules explaining how to apply certain affixes to words. Them may come with caveats or change their functioning depending on features of the previous word.

---
What is the problem with words that look like affixes but aren't? #flashcard #FNLP #Morphology
	These words may be caught by affix detecting methods but don't fit the semantics of these words. Therefore errors are created in the understanding.

---
What is blocking? #flashcard #FNLP #Morphology 
	This is the case where rules for expanding words are only **semi-productive** and cannot be applied in edge cases as a simpler word already exists filling the role. For example glorious -> glutinosity doesn't work as glory I blocks it.

---
What the the two forms we want to translate between in morphological parsing? #flashcard #FNLP #Morphology
	The two forms we want to transfer between are the **surface form** (the one we see) and the **lexical form** (one that gives structure / morphology).

---
Why can't morphological parsing be performed by enumerating over all words and giving the lexical form? #flashcard #FNLP #Morphology 
	This may be possible for English be languages are always changing and some are farm more complicated where each word stem may have thousands of possible surface forms.  This means to perform this we need some automated approach.

---
What are some cases where morphological parsing can be applied to IRL tasks? #flashcard #FNLP #Morphology
	Some cases are **grammatical parsing** for NLP tasks, **search engines** may want to search for similar words making the search more fuzzy. Then it is useful in **spell checking** to give similar word sugestions.

---
What is the limit of computational complexity for parsing morphology and why does it exist? #flashcard #FNLP #Morphology 
	Morphology has no long range dependencies. This way they are low on syntax complexity. FSMs are therefore enough to manage them and no unbounded memory is required.

---
What is the aim in morphology parsing? #flashcard #FNLP #Morphology 
	In parsing we want to generate a lexical form from a surface form.

---
What is the aim in morphology generation? #flashcard #FNLP #Morphology 
	In morphology generation we taking a lexical form and applying rules to turn the stem word in to a surface form.

---
Why is an intermediate form useful for parsing and generation? #flashcard #FNLP #Morphology
	The intermediate form splits up words into morphemes that have not yet been combined. This can help with **generation** and **parsing**.

---
What is the general form of the lexical form? #flashcard #FNLP #Morphology 
	The general form of the lexical form is morphemes seperated by ^ and ended by #. For example "fox ^ s #"".

---
That is an NFA? #flashcard #FNLP #Morphology 
	**Nondeterministic Finite Automata** is a FSM made our of a set of Nodes, connections between those nodes that accept possible characters then a set of start and end nodes..

---
What are finite-state transducers? #flashcard #FNLP #Morphology 
	These are similar to FSMs however each edge also has an output and this way the FST talked in a string and gives out another. Or accepts many and gives out many.

---
Mathematically how are FSTs defined? #flashcard #FNLP #Morphology 
	This is defined for a set of inputs $\Sigma$ a set of outputs $\Pi$. Then there are the state $Q$ and the subset of start and end state $S$ and $F$. The transitions are defined as a **many step-transition relation**. $$\Delta\subseteq Q\times (\Sigma\cup\{\epsilon\})\times(\Pi\cup\{\epsilon\})\times Q$$
	$(q,x,y,q')$ then defines a relation from some previous state $q$ and string $x$ to some new string $y$ and some end state $q'$.

---
What is the first step in morphological generation of a word?  #flashcard #FNLP #Morphology  
	We want to generate the intermediate form. This is done through the use of an FST. Here we need to check for irregular forms and make sure blocking rules are followed.

---
Where does the complexity for intermediate to surface form come from?  #flashcard #FNLP #Morphology 
	There are many rules and edges cases. We need a FST that accounts for all these rule sand produces the correct output.

---
What is FST cascading?  #flashcard #FNLP #Morphology 
	Here we combine many FSTs yielding a larger unit that can parse different parts ad apply many more rules.

---
How can FST cascades allow both generation and parsing?  #flashcard #FNLP #Morphology 
	By reversing the inputs and outputs and FST transforms form a parser to a generators and visa versa.

---
What is the porter stemmer?  #flashcard #FNLP #Morphology 
	This is a large FST that can strip words down to likely root stem words. Because of this it can work quickly and efficiently by make errors.

---
What are learned morphological parsers?  #flashcard #FNLP #Morphology 
	Here the parsing rules are learned by a ML methods giving hopefully more inclusive learning approaches.

---
