Generally words are represented as string of letters. One of the simplest ways to convert a word to its meaning is to just create an object for it. This is often used in logic  for example

![[Pasted image 20230411143337.png]]

But instead we want a representation that captures the similarities and differences between words and even a structure that can capture the logical modeling words do like the relationship between *buy*, *sell* and *pay*.

### Lemmas and Senses
One possible representation is with a dictionary for example

![[Pasted image 20230411143628.png]]

where we store the meaning of some *stem word* **mouse** which is referred to as the **lemma**. The other forms like mice are called **wordforms**. A since **lemma** as can be seen above has different possible meaning called **word senses**. They are **polysemous** when they have multiple senses. Distinguishing between these meanings is needed for example "How to grow grass?" is this referring to the one we run around on or the psychoactive plant? For this we require **word sense disambiguation**.

### Synonymy
If two words senses have the same meaning they are **synonyms**. For example "bike" and "bicycle". As a definition two words are synonymous if they are substitutable for one another in any sentence without changing the *truth conditions* (logical/propositional meaning) of the sentence.

But often the meaning isn't preserved when synonyms are substituted. These words being different defines a difference is meaning. For example "automobile" and "car" are the same but would be used differently. The **principle of contrast** state that a differen't lexical form always gives different semantics. Generally only *rough synonymy* is used.

### Word Similarity
Not all words have many synonyms but often words are **similar**. Generally this is defined between words and not between their senses. This can be measured by asking people to rank a word pair's similarity between 0 and 10.

![[Pasted image 20230411145103.png]]

### Word Relatedness
But again *similarity* isn't the only way to capture the meaning  similarity between words. One other way is with **relatedness** / *association* (in psychology). For example *hammer* and *builder* refer to completely different *dissimilar* things. But they are related as builders often use hammers.

One way to capture this is with a **semantic field** which is a set of words which cover a particular semantic domain and have a structural relation to each other. For example *worker, hammer, nail, scaffold, building-site, construction* and so on.

### Semantic Frames and Roles
This is related to semantic fields. A **Semantic frame** denotes participants or perspectives in a particular type of event. For example a transaction we might use words like *buy*, *sell* and *pay*. Then we might have **roles** like *buyer, seller, goods and money*. We need to capture that the sentences "Greg bought the orange from Frank" and "Frank sold the orange to Greg" have th same meaning.

### Connotation
We will take this to mean the aspect of meaning given by the reader's emotions, sentiment, opinions and evaluation. For example there can be positive "rainbow" and negative "war" connotations. Words can have the same meanings but different connotations *innocent* (positive) and *naive* (negative). Positive and negative evaluation is called **sentiment**.

Early work found three main dimensions words varied on

1. **valence** - the pleasantness or painfulness
2. **arousal** - the intensity of emotion provoked
3. **dominance** - the degree of control something has

So *happy* and *calm* are both high on valence but opposite on arousal.

![[Pasted image 20230411151000.png]]

This means a words meaning could be represented using 3 numbers given a point in space. This lead to [[Vector Semantics]].