What is a Corpa? #flashcard #FNLP #Corpa
	A Corpa is a collection of language / body of utterances. It can be used to train an NLP system. 

---
What should we are about ensuring when creating a corpus? #flashcard #FNLP #Corpa
	We should ensure it reflects natural language and isn't biased.  We should also ensure it represents the type of language we want it to either be used to train for or verify a system to work with.

---
What is metadata is a corpus? #flashcard #FNLP #Corpa
	This is extra information either generated from context or annotated by humans.

---
What are gold labels? #flashcard #FNLP #Corpa
	These are used when performing supervised learning and are the standard we compare our system to as we try to make it perform the same as this.

---
How might we build a simple sentiment detector? #flashcard #FNLP #FNLPIntroduction 
	We could introduce a weight - or + to each word. Then we break the text we are analyzing into words and sum up the scores to get our final score. This may be called a **bucket-of-words** models as we don't care about structure at all.

---
What are some problems with a bucket-of-words sentiment detector model? #flashcard #FNLP #FNLPIntroduction 
	A bucket of words model may fair to understand ambiguous sentences and pick up on sarcasm irony or insertion of other's opinions.

---
