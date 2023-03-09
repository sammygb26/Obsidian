What is the aim in POS tagging? #flashcard #FNLP #MorphologyParsing
	Here we want to break a sentence down into its tokens along with their POS tags which describe the grammatical role they are playing.

---
Why is POS tagging useful? #flashcard #FNLP #MorphologyParsing 
	They is useful when performing syntactic analysis on the sentence. POS tags can also be used as features in classifiers.

---
How is name entity recognition a POS tagging task? #flashcard #FNLP #MorphologyParsing 
	In **name entity recognition** we are aiming to find for different words in a text what the label they belong to. For example a person, organization or location.

---
Why is POS tagging unnatural for name entity recognition? #flashcard #FNLP #MorphologyParsing 
	Names are often hierarchical (e.g. "Scottish Football Fans") but but NER only recognizes a single layer.

---
How is information field segmentation a POS tagging task? #flashcard #FNLP #MorphologyParsing 
	In **information field segmentation** we label a text with different fields which could say fill out a information form.

---
What is sequence labeling what do labels depend on? #flashcard #FNLP #MorphologyParsing 
	In sequence labeling the label we give a word depends on 1) The word itself and 2) labels of surrounding words

---
How does sequence labeling lend itself to Hidden Markov Model Parsing? #flashcard #FNLP #MorphologyParsing 
	If we assume 1) The label of a word only depend on some $n$ previous  words and 2) The word is independent of everything given the label we can use a HMM to perform sequence modeling. These assumptions aren't perfect but work well given the dependencies in sequence modeling.

---
What are open class words? #flashcard #FNLP #MorphologyParsing 
	These are words that describe content in general they change and are added often into a language.

---
What are closed class words? #flashcard #FNLP #MorphologyParsing 
	These are also called **function words** and they describe how open words relate to each other. Generally these change slowly in a language.

---
How might the number of POS tags change? #flashcard #FNLP #MorphologyParsing 
	The POS tags we require change based on the task. We may choose if we should distinguish say between proper nouns (names) and common nouns. Singular and plural nouns. Past and present verbs, auxiliary and main verbs. This will depend on the **task**.

---
In general how many POS tags are used for English? #flashcard #FNLP #MorphologyParsing
	In general around 40-100 tags are used.

---
Why is POS tagging hard in other languages? #flashcard #FNLP #MorphologyParsing 
	POS tagging relies on the simple morphology of English. But other languages have much richer morphology like in agglutinative languages. To have meaningful pos tags here would require thousands of tags.

---
Generally why is POS tagging hard? #flashcard #FNLP #MorphologyParsing 
	In general POS tagging is hard due to ambiguity in which tag should apply to what word. There is **sparse data** as there are many possible pos tag pairs that many not appear in training. Then many techniques in English don't work well for other languages which have richer morphology or less corpa available.

---
What do we assume applies (what is important) when we perform POS tagging? #flashcard #FNLP #MorphologyParsing
	We assume as in **sequential modeling** that only the word itself, and the surrounding tags apply.

---
What problem can a sequential modeling assumption leading to in POS tagging? #flashcard #FNLP #MorphologyParsing 
	Sequential modeling requires clear rules that are applied sequentially but in messy colloquial language rules are often disobeyed and so these rules can get confused.

---
If we apply a HMM to POS tagging what do we assume about the generation of the text? #flashcard #FNLP #MorphologyParsing 
	We assume a tag can be chosen based on previous tags so we use $P(t_i|t_{i-1})$ then we assume a word is just based on its tag $P(w_i|t_i)$. These are bad for generation but good for parsing.

---
How can POS tagging with a HMM assumption be seen as a FSM? #flashcard #FNLP #MorphologyParsing 
	The FSM has many different states for the different tags. Since the next state is just based of this previous state we can the probabilities of moving down any edge are given as a probability. Then each state also has an emission probability for each word.

---
With a HMM pos tag model how can we calculate the joint probability of a sentence and its tags? #flashcard #FNLP #MorphologyParsing 
	We can find the probability of the tag sequence by multiplying probabilities for each tag change and then each word being emitted in each state. This comes from the independence assumption given by taking a HMM model.

---
How can tagging be perfumed with a HMM model? #flashcard #FNLP #MorphologyParsing 
	In tagging we want the most likely sequence of states (POS tags) given the emissions (words). With a HMM model we can use the Viterbi algorithm to get this.

---
For a HMM model of POS tagging what are the parts? #flashcard #FNLP #MorphologyParsing 
	The **emissions** are words. The **states** are POS-tags. The **Transition probabilities** are $P(t_i|t_[I-1])$. The emission probabilities are $P(w_i|t_I)$. Then the **initial state** is just the start tag.

---
