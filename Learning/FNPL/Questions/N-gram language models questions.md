What is useful about the idea of sentence probabilities? #flashcard #FNLP #NgramModels
	Sentence probabilities allow us to weight up different possible sentences. Due to ambiguity and variability there are always many possible sentences and meanings in natural language. We need to models how likely each is if we want to pick the best one.

---
What kind of sentences would we like to have high and low probability in a language model? #flashcard #FNLP #NgramModels 
	We want sentences with incorrect grammar or that don't make sense in context to have lower probability than those that do.

---
What is a language model? #flashcard #FNLP #NgramModels 
	A language model gives approximate probabilities for sentences in a language. There is no way to know the true probabilities hence why we need this approximation.

---
What is an error model? #flashcard #FNLP #NgramModels
	An error model may give different probabilities of mistakes being made. These can latter be combined with how likely sentences are to give spelling correction.

---
Might spelling correction be performed with a language model? #flashcard #FNLP #NgramModels 
	We would use an error model to give the different possible it takes and their probabilities. We could then weigh each one with its error probability and the probability of the sentence (from the language model) to predict how likely this was to be a mistake.

---
How might translation work with a language model? #flashcard #FNLP #NgramModels 
	We might have a **translation model** that gives possible translations and their probabilities. We then weight these by their **sentence probabilities** given by the language model to get the best option.

---
How might speech recognition work with a language model? #flashcard #FNLP #NgramModels 
	We may have an **acoustic model** that give possible interpretations of sound. We can then weight these possible sentences by their **sentence probability** form the language model to find the best one.

---
How might language models be used for prediction? #flashcard #FNLP #NgramModels 
	We can pass all the possible word we could be spelling say while texting into an LM. Then we take the top three possibilities to be our predictions as an example.

---
What is a simple way to gain word sequence probabilities? #flashcard #FNLP #NgramModels 
	We can use **training data**, a large corpus of general text (in our language). We use this large sample to **estimate** the probability of $\vec w$. For example with relative frequency estimation.

---
What is relative frequency estimation? #flashcard #FNLP #NgramModels 
	This is an intuitive way to estimate discrete probabilities. $$P_{RF}(x)=\frac{C(x)}{N}$$where $C(x)$ is the count of $x$ in a large dataset and $N=\sum_{x'}C(x')$ the total number of items in the dataset.

---
What is another name for relative frequency estimation? #flashcard #FNLP #NgramModels
	It is also called **maximum-likelihood estimation**.

---
How can MLE (Maximum Likelihood Estimation) be applied to sentences and what is the problem with this? #flashcard #FNLP #NgramModels 
	We will have to count up all occurrences of a sentence. But any sentence that neve occurs will have probability 0! Even if the sentence made sense. The general problem is anything that has no happened MLE thinks will never happen! This is generally a problem with **sparse data**.

---
How do N-gram language models how to get past the failings of MLE? #flashcard #FNLP #NgramModels 
	With N-grams we hope to build up the probability of rare large sentences from the changes of smaller shorted but more common sentences.

---
What is an N-gram model? #flashcard #FNLP #NgramModels 
	In an n-gram model we start we only use the probability of some next word given the previous $n-1$ words. We assume this is equal to the probability of that word given more than $n-1$ words. This allows us to use the probability conditional chain rule to break any sentence up into these n-gram parts.

---
What is the n-gram assumption mathematically? #flashcard #FNLP #NgramModels 
	This would be that $$P(w_1,\dots,w_n)=\prod_{i=1}^nP(w_i|w_{i-1},w_{i-1},...w_{i-N+1})$$

---
How are the probabilities in an n-gram model found? #flashcard #FNLP #NgramModels 
	We use MLE hence for a trigram model we get $$P_{MLE}(w_i|w_{i-2}w_{i-1})=\frac{C(w_i,w_{i-1},w_{i-2})}{C(w_{i-2},w_{i-1})}$$

---
How should the beginning and end of a sentence be represented when using an n-gram model? #flashcard #FNLP #NgramModels
	We should include $n-1$ start of sentence tags after every end of sentence. Then have a end of sentence tag which can be predicted in the model.

---
How are n-grams implemented on computer (what changes)? #flashcard #FNLP #NgramModels 
	Instead of using probability which can be hard as they re small number so precision can be an issue. Negative log probabilities are used instead.

---
