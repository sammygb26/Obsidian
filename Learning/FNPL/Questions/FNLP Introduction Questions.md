What are some applications of NLP? #flashcard #FNLP #FNLPIntroduction
	Machine translation, Information retrieval, QA, Dialogue Systems, Information Extraction, Summarization, Sentiment Analysis

---
What are some core technologies of NLP? #flashcard #FNLP #FNLPIntroduction 
	Language modeling, Parts-of-speech tagging, Syntactic parsing, Name-entry recognition, coreference resolution, word sense disambiguation, semantic role labeling.

---
What are the different layers of language? #flashcard #FNLP #FNLPIntroduction 
	**Syntax** (how words relate to each other), **parts of speech** (labeling for types of words), **words** (the actual words), **morphology** (type of word), **semantics** (meaning of word), **discourse** (relation to other words).

---
What are two things that make NLP hard? #flashcard #FNLP #FNLPIntroduction 
	**Variability** (the same thing can be said many ways) and **ambiguity** (the same things can be taken to mean different things).

---
What is the problem with syntactic ambiguity? #flashcard #FNLP #FNLPIntroduction 
	It is never quite clear how the syntax of a sentence should be parsed. But there is a combinatorial large number of interpretations and so it is infeasible to disambiguate with large and complex sentences.

---
What is an aspect of word distribution that makes NLP hard? #flashcard #FNLP #FNLPIntroduction 
	The relationship between word frequency and ranking is a logarithmic one. Words used less are exponentially less likely to show up in text. This means there will be many words we may see in practice that are only see once or never in training. 

---
What is Zipf's law? #flashcard #FNLP #FNLPIntroduction 
	his says that the frequency of a word times the rank of a word is approximately constant. So words lower in rank are proportionally lower in frequency. This means low ranking words are almost never seen.

---
What is robustness and how can it be challenging for NLP systems? #flashcard #FNLP #FNLPIntroduction 
	NLP systems bay be trained on some corpus but used on some differently distributed dataset for example articles vs texts on the internet. Or it may be expected to work on incorrect grammar.

---
Why is context hard in NLP? #flashcard #FNLP #FNLPIntroduction 
	Many sentences require information about the world to make sense. To allow NLP system to make sense of these meaning they must  have knowledge of the world embedded and be able to apply it which is hard without having intelligent NLP systems.

---
Why is language diversity a problem for NLP systems? #flashcard #FNLP #FNLPIntroduction 
	There are many languages around the world and not all of them have the same structure as English. So to get NLP systems correct they must be able to parse all these kinds of languages and not be restricted to simpler languages. Techniques that work for one language may not work for others.

---
Why is probabilistic modeling use for NLP? #flashcard #FNLP #FNLPIntroduction 
	There are many sources of uncertainty like **ambiguity, variability, need for robustness and lack of knowledge**. Probability can be used to model this and so get a more realistic system. This probabilistic system give **best explination** rather than all **possible explanations**.

---
What is statistical NLP? #flashcard #FNLP #FNLPIntroduction 
	Statistical NLP uses Corpa of data to learn statistical patters allowing data to be parsed statistically.

---
What is a noun? #flashcard #FNLP #FNLPIntroduction 
	A noun is the name of a person, place, thing or idea (man,  box,  Aberdeen, Grand Falls).

---
What is a pronoun? #flashcard #FNLP #FNLPIntroduction 
	A pronoun is a word used in the place of noun. It is like a pointer to some noun (she, we, they, it)

---
What is a verb? #flashcard #FNLP #FNLPIntroduction 
	A verb expresses an action or being (jump, is, write, become)

---
What is an adjective? #flashcard #FNLP #FNLPIntroduction 
	An adjective modifies or describes a noun or pronoun. (jump is write become)

---
What is an adverb? #flashcard #FNLP #FNLPIntroduction 
	An adverb describes or modifies a verb or adjective. (very, gently, carefully, well)

---
What is a preposition? #flashcard #FNLP #FNLPIntroduction 
	A preposition is a word placed before a noun pronoun to form a phrase modifying another word in the sentence, so it gives structure (by, with, about, until).

---
What is a conjunction? #flashcard #FNLP #FNLPIntroduction 
	A conjunction joins, words, phrases or clauses (and, but, or, while, because)

---
What is an interjection? #flashcard #FNLP #FNLPIntroduction 
	An interjection is a word used to express emotion (oh, wow, oops)

---
