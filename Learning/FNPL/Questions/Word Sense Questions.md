Why is word sense understanding require for QA & to understand language? #flashcard #FNLP #WordSense
	In general many questions or statements may use different words but mean the same or similar things. For a model to understand language it must capture when statements overlap to understand the meaning behind the words.

---
How is word sense meaning limited in FOL? #flashcard #FNLP #WordSense 
	FOL contains basically no word sense meaning. It can have things as properties but doesn't model how things are related or similar to each other.

---
Where do sentential semantics and lexical semantics differ? #flashcard #FNLP #WordSense 
	Sentential semantics can tell **Who did what to whome, when, how and why** and perform logical inference on these statements. But **lexical semantics** can relate different denotations of words together and apply commonsense inference over the top.

---
What are difference sense of a word? #flashcard #FNLP #WordSense 
	This is one things that is hard for sentential semantics. The idea is words can mean different things. Bank on a river bank you put your money in.

---
What are synonyms for words? #flashcard #FNLP #WordSense 
	**Synonyms** are two words with the same meaning. For example *holiday* and *vacation*. The words are different but refer to the same things. This can be hard for sentential semantics to capture.

---
What are hyponyms and hypernyms? #flashcard #FNLP #WordSense 
	A **hyponym** refers to a subset of as apposed to the entered set. While a **hypernym** refers to a superset as apposed to some set. For example Beaver is a hyponym of Manal and Planet is a hypernym of Earth.

---
What is needed to capture hypo-hypernym structure? #flashcard #FNLP #WordSense 
	A database like structure describe $A-is-a-B$ would be needed. This is called an **ontology**.

---
What are hypo-hypernyms hard for sentential semantics system? #flashcard #FNLP #WordSense 
	Sentential semantic would find it hard to capture this kind of information and perform logical inference on it. Many different words can relate in very many ways and this can become computationally hard and in general complicated.

---
What is gradation in word sense? #flashcard #FNLP #WordSense 
	In word sense gradation refers to how different sense of a word can have different intensities. For example *remove* can mean *eliminate*, *annihilate* or *take away*. This is hard for sententia semantics to capture as many meanings are said at once.

---
What is WordNet? #flashcard #FNLP #WordSenses
	WordNet is an ontology of relations between words in English (mostly). It is made up of 117000 **synsets** which are word sense groupings.

---
What are some relations between synsets in WordNet? #flashcard #FNLP #WordSenses 
	**hyponym** - IS-A relations for example chair - furniture. Then **meronym** - PART-WHOLE led-chair and **antonym** opposites good-bad.

---
What is a meronym?  #flashcard #FNLP #WordSenses 
	A meronym is a a relationship between word senses. It defers a part to a whole. For example leg-chair. 

---
What is a synset in WordNet?  #flashcard #FNLP #WordSenses 
	A Synset is a set of synonymous words.

---
What is word sense ambiguity?  #flashcard #FNLP #WordSenses 
	This is only an ambiguity is a particular word exhibits some word sense difference within one syntactic category e.g. Noun.

---
What are homonyms?  #flashcard #FNLP #WordSenses 
	**Homonyms** are word senses that have the same word (same word) but different meanings for example bank (river) and bank (money). If they are homonyms then the meaning is **unrelated**! This is holonomy.

---
What is regular polysemy?  #flashcard #FNLP #WordSenses 
	This is where the two senses ambiguity of words results from semi-productive rules which allow their sense to be expanded . For example "I drank the bottle" doesn't mean the glass was drunk but instead the contents of the bottle. But this is a rule and can be applied to Jars, Mugs etc.

---
Can you give an example of a regular polysemy rule?  #flashcard #FNLP #WordSenses 
	A good example is animals and fur/hide. With "she wore anaconda" easily referring to the skin instead of the anaconda instead of the animal.

---
What is an example of regular polysemy when it comes to animal personalities?  #flashcard #FNLP #WordSenses 
	We can use reference to archetypal animal personalities to people. "You're a sheep", "He's a pig" etc. This is a metaphorical mapping. But the personality isn't easily predicted.

---
What is an example of regular polysemy being blocked?  #flashcard #FNLP #WordSenses 
	An example would be meats. Any animal without a meat word can be referred to as a meat with its name. But words like beef and pork block this.

---
What lessons are drawn from the extensive productivity in rules for word meaning?  #flashcard #FNLP #WordSenses 
	This makes the language model approach inadequate as there will be far too many meanings . Dictionaries don't capture the factorization inherent in these rules.

---
How are synsets found? #flashcard #FNLP #WordSenses 
	Word senses are found in synsets sets of synonymous words. We can check this with substitutability. Once all the meanings are hashed out synsets can be related by relationships.

---
What are some short comings word WordNet? #flashcard #FNLP #WordSenses 
	Some short comings of word net are it can't capture **multi-word expressions**. It finds it hard to capture neologisms **hoodie, facepalm**, names **Microsoft** and it cannot capture predictable novel uses of words.

---
How does word senses make translation hard? #flashcard #FNLP #WordSenses 
	Word sense means we have to split words up (possibly in a wrong way) or words may be merged loosing required meaning.

---
What is the task of word sense disambiguation? #flashcard #FNLP #WordSenses 
	Word sense disambiguation is trying to decide which meaning a word is taking given a context. 

---
How can word sense disambiguation be taken as a classification task? #flashcard #FNLP #WordSenses 
	WSD can take in a context and classify the word into the possible meanings or with WordNet synsets the word exists in.

---
How is WSD solved with Naive Bayes? #flashcard #FNLP #WordSenses 
	We take a set of context words $\vec f$ and apply Bayes rules and make the NB assumption. We not take the maximum of the category probabilities and the probability of the words given the category.

---
What are some simple feature NB can use when performing Word Sense Disambiguation? #flashcard #FNLP #WordSenses 
	We can use directly neighboring words, or content words within a window.

---
What are some general feature NB can use for word sense disambiguation? #flashcard #FNLP #WordSenses 
	Some examples are syntactically related words, syntactic role in sense, topic in text and POS tag / surrounding POS tags.

---
What are some issues with WSD? #flashcard #FNLP #WordSenses 
	It is hard to decide the level of tags we should split between. It hard to get sense annotated corpa. All words must be trained separately and again this means synthesis techniques must be used for datasets.

---
What are semantic classes? #flashcard #FNLP #WordSenses 
	Instead of breaking words meanings down these group them together. For example Foods or animals. These can be applied to many words and used for generative rules applied to these words. These are also called **supersense**.

---
