Meaning helps us with many tasks like Q&A which may have access to knowledge bases and may contain a lot of English text. But we may as what happens when we consider things out of distribution. So far our meaning is limited to something like $dog\to dog(x)$ meaning being a dog is a property. FOL doesn't give more information than this. FOL focuses on **logical constants** and so more fuzzy content like meaning isn't covered.

### Semantics
*Sentential semantics* is good for some meaning like Who did what to whome. It also supports word meaning.

*Lexical semantics* captures the meaning of individual words. It can relate different denotations together and perform common sense inference.

##### Example Questions
A questions like '*When was Barack Obama born*' can be easily plugged into. The symbol referred two is used at a surface level unambiguous way.

##### Example Question 2
We may as *"What plants are native to Scotland*" be we need the model to discriminate between this being about the green plant rather than a chemical plant. These words have the same POS tag and so exits in the same context. If the word form and POS tag is the same and the senses are different this is a **word sense ambiguity**. For this we need to disambiguate this.

##### Example Question 3
We may as "Where did David Cameron go on vacation?" we may want to notice that "holiday" has the same meaning and so is the same as what we are asking (**synonym**)

##### Example Question 4
"Which animals love to swim?" If the text available is "Polar bear love to swim in freezing water in the artic" this is a hyponym (check this) where it is a subset of the overall category of animals. This is hard as words can either refer to a subset (**hyponym**) or a superset (**hypernym**). We need to have a database such that $A-is-a-B$ relations are captured. This is called an **ontology**.


##### Example Question 5
"What is a good ways to remove wine stains?" - there can be more than one concrete meaning for example remove completely or a little. We need to be able to stop these differences. The different sense of words can have a different intensity, this is called **gradation**.


##### Example Question 6
"Did Poland reduce its carbon emission since 1989?" - In this example there are multiple sentences which the meaning can be taken out of. We must **infer** from the sentences and combine their meaning to get our answer.

### WordNet
Sine if these problems can be solved with a good ontology e.g. **WordNet**. WordNet is a hand-built resources containing 117000 **synsets** set of synonymous words. Synsets are connected by relations such as hyponym/hypernym (IS-A chair-furniture), meronym (PART-WHOLE: leg-chair), antonym (OPPOSITED: good-bad).

### Word Sense Ambiguity
One word form, same category but more than one sense (**homonyms**). For example 

"I put my money in the bank" vs. "He rested at the bank of the river" (comes from Venice bank)
"I like playing squash" vs. "I like drinking squash"

The word being used have different meanings and these have to be known. This is different to words that exhibit sense ambiguity that fall into

![[Pasted image 20230402135910.png]]

![[Pasted image 20230402135922.png]]

![[Pasted image 20230402135933.png]]

Regular **polysemy** can be distinguished by similar words sharing these meanings. Regular polysemy itself being the productive word meaning rules where the word remains in the same category.

We can also refer to different attributes of objects in the same sentence "That book on the shelf is about syntax". The meaning is the same however unlike examples like "I like mustard on my thighs but George like sun-cream".

- Words are typically ambiguous
- There's a lot of regularity (and hence predictability) in the range of senses a words can take.
- Those senses also influence the word's syntactic behaviors
- But all regularities admit (arbitrary) exceptions
- Word senses can be **productive** making dictionary model inadequate

#### NOUN Interest

![[Pasted image 20230402144130.png]]

A questions comes up if these meanings are the same and how they get split apart.

### Lumping and Splitting
This is the choice lexicographers have, to group meanings together or split them into finer categories.

### WordNet Senses for interest
Here we give a sentence and then a words that acts as a **synonym** in the given sentence.

The **Synsets** are then in relations to each other. They are organized into a network by several relations. For example

- **Hypernymy** - IS-A hyponym {ambulance} is a kind of {car}
- **Meronomy** - PART-WHOLE: meronym {air bag} is part of a {car}

### Using WordNet
NLTK provides an excellent API for WordNet.


### Coverage in WordNet
There are 155l unique string, 118k unique synsets, 207k pairs. Nouns have on average 1.24 senses (2.79 if excluding monosemous words) Verbs have 2.17 senses (3.57 excluding monosemous words).

Then we have **idioms** which give meaning to larger sentences. These are **multiword expression** and may also include expressions, idioms etc. Then we have Neologisms; newer arising meanings.

The senses are different in different languages and so when translating we need to disambiguate these senses.

### Translation
Word senses can make translation hard as we have to move between many to one and one to many mappings. Words may be split or combined or not translatable at all.

### Naive Bayes for WSD
Here we pick out the sense that is most likely given some features. For example the word and surrounding context. We assume the feature are conditionally independent of other features give then sense **naive bayes**. Then we can train nave bayes.

We can also perform MaxEnt on custom features to get better performance. This could encode syntactically related words, syntactic role in the sentence, topic of the text etc.

### Issues with WSD
Its not always clear how fine grained the meanings and so the labeled compared to should be. It is also difficult to annotate corpora with fine-grained senses, We must also train classifier *separately* with each word. This makes it hard to use infrequent words. It also means every word must be well annotated and so this must be done for new words.

### Semantic Classes
Other approaches such as **named entity recognition** and **supersense tagging**. That is categories exits in different classes. Apple vs Apple (Corp). We don't care about the different plant apple nouns but want to distinguish at a higher level.

- We may want to disambiguate  organization vs. food.

Unlike senses which are refinement of particular words classes are groupings of words. The classes can be applied to words/names not in the lexicon.

### Named Entity Recognition
Recognizing and classifying **proper names** in text. Works as a kind of **information extraction**.



### Supersense in WordNet
![[Pasted image 20230402151730.png]]

[[Word Sense Questions]]