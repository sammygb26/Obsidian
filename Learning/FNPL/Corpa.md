Natural langue parse is very challenging due to **ambiguity**. Languages are also **unbounded** due to recursion. This makes it hard to nail down in every instance what is meant. Most NLP these days uses Corpa to train systems but even if you don't do that you need Corpa to test different systems.

##### Corpora in NLP
A **corpus** can be defines in different ways but in linguistics it is: a body of utterances, as words or sentences, *assumed* to be representative of and used for lexical, grammatical or other linguistic analysis.

The corpus is never complete and is instead just representative (we hope). The problem is really for things not in the corpus set. We test on a holdout set from the Corpus. We assume our training Corpus is distributed the same as our test / holdout. 

The data in a corpus should be, **naturally-occurring** and this should create a more **natural** language system. Metadata is also added on to the information added this can be through of as annotation. This can the be used for supervised learning. But this can also generally include metadata.

A particular interest for **core NLP** and the course are **linguistic annotations** where humans have read the text and marked categories or structures describing their system and / or meaning.

##### LDC
This is the **linguistic data consortium** they have annotated many different corpa. For example :

* **Brown** which have 500 text labeled with the sense in which the word is assumed to be used (by a marker).
* **WSJ** 6 years of Wall Street Journal; was labeled with syntax trees. (very hard work)
* **ECI**: European Corpus Initiative, multilingual
* **BNC**: 100M words, balanced selection of written and spoken genres
* **Redwoods**: Treebank aligned to wide-coverage grammar; several genres
* **Giga word**: 1B words of news text.
* **AMI**: Multimedia (video, audio, synchronized transcripts) 
* **Google Books N-gams**: 5M books 500B words (361B English)
* **Flickr 8K**: image with NL captions
* **English Visual Genome**: Images, bounding boxes => NL descriptions

##### Markup
There are several common markup formats for structuring linguistic data, these include XML, JSON, CoNLL-style (one token per line, annotation in tab-seperated columns). Some datasets, such are WordNet and PropBank, use custom file formats. NLTK provides friendly Python APIs for reading many corpora so you don't need to worry about this.

### Sentiment Analysis
Here we try to look at a review the sentiment and then we can look at the true scores

![[Pasted image 20230121133623.png]]

We can look at different word and their structure to give our analysis. In **bag-of-words** we can just count out positive and negative words. But we have **negation** that can reverse the meaning of word. The negation has scope but this can depend on sarcasm. Or a word like awful can be said as **awfully good** or just **awful**.

##### How would we build a sentiment analyzer
We need to know :
1. What is the input for each prediction? (sentence? or a full text? test + metadata?)
2. What ae the possible outputs? (+ or - / stars)
3. How will it decide?
4. How will you measure its effectiveness?

The last one would require data to test. Before we build a system, we need to choose a dataset for evaluation. This is important as

1. Good science requires controlled experimentation
2. Good engineering required benchmarks
3. You intuition about typical input are probably wrong

We need to have multiple datasets one **training**, one **development** (if we're training hyperparameters) as you hack your system and one reserved for **testing** (we never show our network until the very end).

### Where can you get a corpus?
Many copra are prepared specifically for linguistic/NLP research with text from context providers (e.g. newspapers). In fact, there is an entire subfield devoted to developing new **language resources**. We may want to make our own by scraping websites to get data (like chat GPT).

### Annotations
To evaluate and compare sentiment analyzers, we need review with **gold labels** (+ or -) attached. But these are always noisy somewhat are no annotation is perfect. These could be
1. Derived automatically from the original data artifact (**metadata** such as star rating) or
2. Added by a human  annotator who reads the text
	- Issue to consider / measure : How consistent are human annotators? If they often have trouble deciding or agreeing, how can this be addressed?

### Evaluation Metric
We also want to compare against the **gold** labels, we can give the text of each review as input to out system and measure how often its output matches the gold label for example. $$\text{accuracy}=\frac{\text{\#corect}}{\text{\#total}}$$

### A simple sentiment classification algorithm
Use a **sentiment lexicon** to count positive and negative:

![[Pasted image 20230121135654.png]]

There are some problems with simple counting:
1. Sense ambiguity
2. Sarcasm / irony
3. text could mention expectations or opposing viewpoint, in contrast to authors actual opinion.
Opinion words may be describing (e.g.) a character's attitude rather than an evaluation of the film. Some words act as semantic modifiers of other opinion-bearing words/phrases so interpreting the full meaning requires sophistication

![[Pasted image 20230121140023.png]]

With **more data** it may still be hard to know whether words that seem positive or negative tend to actually be used that way. A data-driven method: we could use **frequency counts** to ascertain which words tend to be positive or negative.

# NLTK
This is a tool kit for python 2.7 and stands for the **Natural Language Toolkit**. It open source and community-built. It was designed for teaching NLP so has simple to access datasets.

![[Pasted image 20230121140403.png]]

##### Word Frequencies
![[Pasted image 20230121140933.png]]

![[Pasted image 20230121140950.png]]

##### Bag-of-words frequencies

![[Pasted image 20230121141052.png]]

Notice movie comes first as there are possible more negative that positive reviews so without balancing we may get an unrepresentative relative frequency.

### Tokenization
If we look are some corpus we can joint the together the progenerated tokens. The task in tokenizing is to take a messy text and apply logical rules to break up different possible words into the tokens.

![[Pasted image 20230121141909.png]]

[[Corpa Questions]]