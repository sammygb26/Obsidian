To start looking at **morphology** we can consider plurals as the simplest English example. Generally a **stem word** like "word" can get a plural by adding "s" on the end making "words". But there are many cases that don't follow this rule.

- "Fox" -> "Foxes"
- "Morphology" -> "Morphologies"
- "Octopus" -> "Octopi"
- "Fish" -> "Fish"

There are two kinds of rules to rules to categorize these forms. We have **orthographic** rules which tell us how to pluralize different form i.e. words ending in "x" we add "es" to the end or "y" is changed to "i" then we add "es". **Morphological rules** tell us that "fish" for example has no plural form.

Breaking down a word like "foxes" into its morphological parts i.e. "fox-es" is called **Morphological Parsing**. In general **parsing** is taking some language input and producing some structure form it. In *morphological parsing* we for example may want to take the **surface form** i.e. "going" and parse it into the different morphemes i.e. "VERB-go + GERUND-ing".

This kind of parsing is important for many applications.

1. **Searching** - It can help to search for morphologically closely related words to make search more robust. For example searching for "fox" you may be interested in an article taking about "foxes".
2. **POS-tagging** - Morphology changes the syntactic roles words can play and therefore changes their POS tags. It would be useful to be able to parse this our of the word.
3. **Translation** - Different words can have different morphologies being able to move up and down from a parsed to combined for helps make the right translation of words who change their morphological makeup (for example having a more complicated meaning in another language) between languages.

One way to capture this would be to use a dictionary. There are different reasons to not follow this path.

1. **Productivity** - Many of the rules like -ing and -s apply to every verb or every noun (almost). As new words are added we would have to constantly update our dictionaries.
2. **Rules are needed for production** - We may also want to move the opposite way form *stem* words to surface forms. We still need these rules to perform this so we can kill two birds with one stone.
3. **Scale** - It may be hard in English but in other languages which a richer morphology it is impossible i.e. Turkish.

*Turkish* - Infact has 40,000 possible surface forms for each verb and this can be made infinite if we include *causative* morphemes.

## Survey of English Morphology
**Morphemes** are thought of as the smallest unit of language. The word "fox" cannot be broken down. The word "Pianos" can be broken down into "Piano" "-s". In English we break morphemes down into **stems** and **affixes**. The stem is through of as the **main** morpheme providing the root meaning while affixes are thought of as giving additional meaning. There are different ways affixes can change stems.

1. **Prefixes** - Adds to the start of a word "fasten" -> "unfasten"
2. **Suffixes** - Adds to the end of a word "help" -> "helping"
3. **Infix** - Adds to the middle of a word "abso-bloody-lutely"
4. **Circumfix** - Adds to the start and end of a word ($null$)

Words can have multiple affixes "write" + "re-" + "-s" -> "rewrites". Or more "believe" + "un-" + "-able" + "-ly" = "Unbelievably". Languages can have many more and are called **agglutinative** languages.

There are different ways these morphemes combine to create new words.

1. **Inflection** - This adds a morpheme but doesn't change the grammatical category of a word. For example "word" -> "words" (still a noun) then "walk" -> "walked" (still a verb)
2. **Derivation** - This adds a morpheme and changes the grammatical category. For example "compute" -> "computer" or "factorize" + "-ation" = "factorization".
3. **Cliticization** - This is when a **clitic** is added onto a word. A *clitic* is a morpheme that acts syntactically like a word. For example "we" + "are" = "we're" = "we" + "-re".
4. **Compounding** - Here multiple stems are combined to give a new word. "dog" + "house" = "doghouse" or "wing" + "man" = "wingman".

#### Inflectional Morphology
English has a simple inflectional system; only nouns, verbs and some adjectives can be inflected. The number of possible inflections is also quite small.

**Nouns** - These have only three kinds of inflection. There is a **plural** "mice" and a **possessive** ("mouse's mice's") affix. So words are either bare stems and **singular** "mouse". The possessive can also be made out of a word plus an apostrophe in the case words end with "s" or "z" (Euripides' plays).

**Verbs** - Verb inflection is more complicated than nominal inflection. There are three kinds of verbs:
1. **Main verbs** - eat, sleep, impeach
2. **Modal verbs** - will, should
3. **Primary verbs** - be, have
We are mainly concerned with the **main verbs**. A large class of these are **regular** and have the same endings for the same function. 

| **Morphological Class** | **Regularly Inflected Verbs** |
| - | - | - | - | - |
| stem | walk | merge | try | map |
| -s form | walks | merges | tries | maps |
| -ing participle | walking | merging | trying | mapping |
| Past form or -ed participle | walked | merged | tried | mapped |

This form is regular as just by knowing the *stem* we can predict the surface form with the affixes. This is the **productive class** and automatically includes any new words in the language. For example the new word "fax" get "faxes" "faxed" "faxing".

The **irregular verbs** these are far fewer in number but also include most of the most common English nouns. These don't fall the rules above and can have their own rules. For example "catch" (past participle)  = "caught".

With verbs the "-s" form is the **habitual present** when concerning the third person singular ending. So "She runs" as apposed to "I, we, they, you jog". The stem is used in the *infinitive* form and so when combined with other words so "I'd rather walk" or "I want to walk". Then -ing marks a present or ongoing activity. It can also be used as a noun as in "Fishing is boring" or "Researching is hard" this is called the **gerund**.

#### Derivational Morphology
Unlike it's inflections English's derivations are quite complicated. For example **nominalization** takes verbs and converts them to nouns. For example "-ation" produces nouns form verbs often ending in -ize. (Computerize -> Computerization). There is also "-er" for example in "killer". There is "-ness" as in "fuzzy" + "-ness" = "fuzziness". Finally "-ee" as in "appoint" + "-ee" = "appointee".

We can also derive **adjectives** from *nouns* and *verbs*. For example "computation" -> "computational" or "order" -> "orderly".

##### Cliticization
One things to note here is it can be **ambiguous** in English for example "she's" could mean "she has" or "she is". Then "she-d" becomes "she would" or "she had".

#### Non-Concatenative Morphology
All the above morphology we have discussed is a string of concatenated morphemes this is called **concatenative morphology**. This doesn't always have to happen however and words can be intermingled or combined in more complex ways. For example in Hebrew there are templates which word prefabs.

#### Agreement
In English sometimes words have to match in form for example in number. This happens with "She eats" vs "She eat". It sounds wrong, instead the words must **agree**. This also happens in other language for example "el sol" as apposed to "la sol" for Spanish *genders*. **Genders** are basically equivalence classes which categorize nouns. In Spanish there are two *male* and *female*. Bantu has 20 at this point they are called **noun classes**.

## Finite-State Morphological Parsing
Now in parsing we want to move from the **surface form** to a parse where we have deconstructed the word. There is the **stem** and the **features** for example "+N" means noun, "Pl" means plural and "+Sg" means singular. We may also parse the gender as part of this.

![[Pasted image 20230416183219.png]]

Sometimes there is **ambiguity** between different parses. 

To build a morphological parser we need:

1. **Lexicon** - A list of stems and affixes along with information about them
2. **Morphotactic** - Ordering information and allowed combination rules. So which order the morphemes go in and who can go after what. 
3. **Orthographic rules** - These are **spelling rules** which are applied when morphemes combine for example "-y" + "-s" = "-ies".

## Construction of a Finite-State Lexicon
A **lexicon** is just a group of words. The simplest version of this would just have every word in the language including abbreviations. There are so many words and many are related by morphology and so it is easier to group word meaning around the stems and work out form there. We can model the **morphotactics** with a finite state automata. For example with *nominal inflection* we may only add "-s" if the noun is regular. If it is irregular plural (goose, octopus) or irregular singular (geese, mice) we will not add the "-s".  

![[Pasted image 20230416192357.png]]

We ignore the specifics of how "-s" is attacked and continue on. We will also need our base lexicon:

![[Pasted image 20230416192943.png]]

We can do the same thing for *verbal inflection*.

![[Pasted image 20230416193126.png]]

Derivation is more complicated and although subsets can have FSM that are simple overall the architecture is complicated and sometimes FSMs aren't even used. An example where we take into account the ends of words might be.

![[Pasted image 20230417100750.png]]

Another problem we want to tackle is **morphological recognition**. We will recognize if a sequence of letters make up a legitimate word. This is done by taking the **morphotactics** FSMs and expanding their arcs (e.g reg-noun-stem) to recognize all the words that belong to that group. For example with just "fox", "cat" and "goose" adding -s becomes.

![[Pasted image 20230417101214.png]]

## Finite-State Transducers
An **FST** is a finite automata that maps between two strings or tapes. We do this by adding two labels to each arc one input and one output.

![[Pasted image 20230417101425.png]]

FSTs can be used in different ways.

1. **Recognizer** - We can take in and reject a set of string just as a standard FSA would.
2. **Generator** - Here we can output a pair of strings for a language. So yes and no given a pair of strings
3. **Translator** - A machine that reads in a string and produces another one.
4. **Relater** - This machine gives a relation between sets.

In **morphological parsing** we will use the FST and a **translator** between the surface form and lexical form (morphemes). An FST is defined by seven parameters. 

- $Q$ - A finite set of $N$ states $q_0,q_1,\dots,q_{N-1}$
- $\Sigma$ - A finite set corresponding to the input alphabet
- $\Delta$ - A finite set corresponding to the output alphabet
- $q_0\in Q$ - The start state
- $F\subseteq Q$ - The set of final states
- $\delta(q,w)$ - The transition function / matrix between states. $\delta(q,w): Q\times \Sigma^*\to 2^Q$ will be a mapping from each state given a string to a set of states ($2^Q$ possible sets).
- $\sigma(q,w)$ - The output function given a string input. $\sigma(q,w): Q\times \Sigma^*\to 2^{\Delta^*}$ where $2^{\Delta^*}$ is the set of all possible sequences of symbols in $\Delta$.

FSTs are isomorphic to **regular relations** which are an extension of *regular languages* (sets of strings). These *regular relations* are closed under union but not under difference, complementation and **intersection** (so some subclasses of FSTs are, like FSTs without $\epsilon$). FSTs have two very useful closure properties. 

1. **Inversion** - The inversion of a transduce $T$ ($T^{-1}$) simply switches the input and output labels (no arc direction changes).
2. **Composition** - If $T_1$ transduces from $a\to b$ and $T_2$ transduces from $b\to c$ then $T_1\circ T_2$ transduces from $a\to c$.

Inversion means we can easily convert a parser to a generator. An example of composition could be

![[Pasted image 20230417104731.png]]

The **projection** of an FST is an FSA produced by extracting only one side of the relation.

#### Sequential Transducers and Determinism
Generally FSTs are non-deterministic and so search must be used to computer their outputs. NFSAs can always be converted to deterministic FSAs but this relationship doesn't hold for FSTs.

**Sequential transducers** are  subtype of transducers that are deterministic on their input. At any state each symbols of the input alphabet $\Sigma$ can label at most one transition out of a state.

![[Pasted image 20230417105507.png]]

These can have $\epsilon$ in the input string but not in the output. The inverse of this sequential transducer may not be sequential. We can also make **subsequential transducers** which concatenate part of their output onto the end of their input. These sequential FSTs are important as they have linear runtime in the size of their input. These can also be extended into $p$-**Transducers** which have a $p(p\ge 1)$ final output sting to be associate with each final state and these can handle a finite amount of ambiguity

![[Pasted image 20230417110213.png]]

## FSTs for Morphological Parsing
Now we want to map inputs of the form "cat + N + Pl" to their surface form "cats" for example. This is called the **lexical level** and we want to get to the **surface level**. We will use two tapes in this case which we will translate between.

![[Pasted image 20230417111258.png]]

In a **two-level morphology** we allow only a single symbols for each alphabet. each arc is annotated with a string from the new alphabet $\Sigma'\subseteq \Sigma \times \Delta$. For example with $\Sigma=\{a,b,!\}$ and $\Delta=\{a,b, !\}$ we would get $$\Sigma'=\{a:a,b:b,!:!,a:!, a:\epsilon,\epsilon:!\dots\}$$depending on what translations we make. These are called **feasible pairs**. Usually we parts $a:a$ for example, this is called a **default pair** and will just be written as $a$. We can construct a simple transducer to convert the lexical form to an intermediate.

![[Pasted image 20230417111951.png]]

This needs to be updated so that the labels "reg-noun" or "irreg-sg-noun" have  their underlying lexicon represented. We need to ensure for example the irregular single vs plural for goose and geese is parsed. We can build up the mappings needed

![[Pasted image 20230417112403.png]]

Then create a full FST

![[Pasted image 20230417112422.png]]

This will give the **intermediate form**. So this has allowed us to parse the **morphological rules**.

## Transducers and Orthographic Rules
The previous methods work for concatenation but we need different techniques for example when the spelling changes (as in **orthographic rules**). For example here are some spelling rules

![[Pasted image 20230417134343.png]]

Our transducer will take in the **intermediate form** and produce a slightly spelling modified concatenated form. For example with "fox^s" -> "foxes". We might say the rule is add "e" to surface tape when the next intermediate tape is "^s" We might write

![[Pasted image 20230417134701.png]]

Meaning write $e$ after "nothing" between $\{x,s,z\}\hat\space$ and $s\#$. The automata for this rule will be

![[Pasted image 20230417134919.png]]

q2 can be seen as detecting a potential application of the rule then q3 and q4 carry it out ensuring it fails if the s isn't at the end of the word.

## The Combination of an FST Lexicon and Rules
Now we can combine the lexicons and rule transducers. We can compose them moving from the lexical to the intermediate and then the surface forms. This is called a **cascade** we are simply running the transducers in series. Of course since we can invert these transducers easily we can also move from surface to a parsed form. Now since multiple words can map to the same one in the output we will always have ambiguity when parsing instead of generating.