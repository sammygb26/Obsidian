**Morphology** is the study of the structure of words. English has a relatively impoverished morphology. Languages with rich morphology include: Turkish, Arabic, Hungarian, Korean

For example Turkish is an **agglutinative** language and tends to express concepts in complex words constructed by concatenating *morphemes* each expressing some simple component

![[Pasted image 20230217121545.png]]

'Whole' words constructed by combining

**Stems** (house, combine, eat walk) the base dictionary word

**Affixes** (prefixes, suffixes, infixes and circumfixes), Prefix goes at the start, suffix after the stem, infix middle of the step and circumfix reduces the stem.

#### Four Methods for combining them
**Inflectional** (stem + grammar affix): no change to grammatical meaning (walk -> walking)

**Derivation** (stem + grammar affix): change to grammatical category (combine -> combination)

**Compounding (stems together)**: doghouse

**Cliticization**  I've, we're, he's

Morphology can be concatenative or non-concatenative. **Blocking** is a major problem with these methods. If we have a word that already fills a role we can't apply rules to fill that role. Which explains why we can t say glutinosity as we have the work glory (curious - curiosity) (glorious -> glory).

### Different Inflections in Different Languages
In **English** nouns are inflected for number; verbs for person and tense

![[Pasted image 20230217122544.png]]

In **German** nouns are inflected for a number and case

![[Pasted image 20230217122617.png]]

**Spanish** - inflects depending on gender (el sol , la luna)

**Luganda**: nouns have ten genders

### Agglutination and compounding

![[Pasted image 20230217122709.png]]

In most extreme examples the meaning of the word is the meaning of a sentence.

### Morphological parsing: the problem
English has concatenative morphology. Words can be made up of a main **stem** plus one or more *affixes* carrying grammatical information.

![[Pasted image 20230217122840.png]]

We want a word represented with this structure as it helps us parse these words. This is called the **lexical form**. The other form is called the **surface form**. 

Some trips are:

**Irregular forms** - (goose -> geese)
**Systemic rules** ('e' is inserted before suffix 's' after s,x,z,ch,sh) fox-> foxes
**Things that look like affixes b aren't** (proactive vs. protect)
**Blocking**: semi-productivity of morphological rules (glorious glutinosity)

### Why Bother
Any NLP task involving **grammatical parsing** will typically involve morphology parsing as a prerequisite. **Search engines** like search for fox should return documents containing foxes. This can also be useful for **spell checking**.

### Why an exhaustive word list isn't adequate
This might work in English but in many other languages there are too many possible ways to extend a word. Similarly for noun compounding in German. We also need to break up words as we may not always know when the word breaks are.

### How expressive is morphology
Morphemes are tacked together in a rather regular way, but there are no long range dependencies. So finite-state machines are a good way to model morphology.

### Parsing and generation
In **parsing** we want to break a surface form into its lexical form. In **generation** we go in the opposite way. FSMs give a path to all lexical forms but this won't rank which is the best.  This processing is done through intermediate forms.

![[Pasted image 20230217123835.png]]

## Nondeterministic Finite State Automatons (NFAs)
This is a FM where a state can have more than one ongoing ark.

![[Pasted image 20230217123944.png]]

There are two or more start and end states. There are outgoing arrows that give a direction (next node) given a string.

### Finite-state Transduces
Here we both generate and consume a string at the same time.

![[Pasted image 20230217124143.png]]

We can also input and output nothing. There are multiple possible outputs in many cases.

##### Forma definition
A **FST**  $T$ with inputs from $\Sigma$ and outputs $\Pi$. Consists of $Q$ states, $S$ (for start) and $F$ (for finish). A transition relation $\Delta\subseteq Q\times (\Sigma\cup\{\epsilon\})\times(\Pi\cup\{\epsilon\})\times Q$. This defines a **many-step transition relation.

- $(q,x,y,q')\in\hat\Delta$ means "starting from state $q$, the input string $x$ can be translated into the output string $y$, ending in state $q$"
A FST can be run in either direction! From $T$ you can obtain another traducer $\bar T$ by swapping inputs and outputs.

## Stage 1: From lexical to intermediate form
Here we convert 'fox+N+PL' to 'fox ^ s #'.

![[Pasted image 20230217124754.png]]

We can reverse this by flipping arrows and start and ends states. We treat +N, +SG, +PL as a single symbol. 

The left hand part of the preceding diagram is an abbreviation for something like this

![[Pasted image 20230217124959.png]]

The full form would be 

![[Pasted image 20230217125023.png]]

## Stage 2: From intermediate to surface form
To convert a sequence of morphemes to surface form we apply a number of **orthographic rules**:

![[Pasted image 20230217125117.png]]

We want say a form that (ignoring ch and sh cases) turns some stem work into a plural with +s.

![[Pasted image 20230217125210.png]]

![[Pasted image 20230217125318.png]]

Here ? may stand for any symbol except z,s,x,^,#.

...

### Putting it all together
FSTs can ve **cascaded** output form one can be input to another.

![[Pasted image 20230217125415.png]]

...

### The Porter Stemmer
Lexicon can be quite large with FSTs. Sometimes need to extract the stem in a very efficient fashion (such as in IR). The Porter stemmer: a lexicon-free method for getting the stem of a given word

![[Pasted image 20230217125518.png]]

It makes errors but it quick and easy

![[Pasted image 20230217125537.png]]

### Learning Morphological Parsers
Here we learn these in an unsupervised or supervised parsing. Results make errors but it works very well for English's. With more complicated languages we need to add in inductive biases.

[[Morphology Questions]]


