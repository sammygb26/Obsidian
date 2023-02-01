What are the drawbacks to a *belief state*? #flashcard #RA #QuantifyingUncertainty
	We have to consider every possible state no matter the likelihood of it actually happening. Our plan therefore will have to take into account all these contingencies despite their likelihood. Planning in this way may lead to failure if we don't have a plan that will for sure get us to the goal.
	
---
How does FOL fail to allow uncertainty? #flashcard #RA #QuantifyingUncertainty 
	FOL need things to have definite causes. It can allow for many possible causes but doesn't quantify how likely their are. It can also not allow for effects that only sometimes take place.

---
How does probability get around the limitations of FOL? #flashcard #RA #QuantifyingUncertainty 
	Probability allows us to quantify a relation between two variables with a number between 0 and 1 of say $a$ being true given we know $b$ is true.

---
What is a rational agent in terms of utility and probability theory? #flashcard #RA #QuantifyingUncertainty 
	A rational agent is rational iff it choses the action that yields the highest expected utility, averaged over all the possible outcomes of the action.

---
What is a sample space in probability theory? #flashcard #RA #QuantifyingUncertainty 
	The sample space in probability theory is the set of all possible worlds that could occur.

---
What is a probability model for a sample space? #flashcard #RA #QuantifyingUncertainty 
	The probability model associated each world in the sample space with a number between 0 and 1. Such that the sum over all world equals 1. This is then the probability of observing that world.

---
What is an event in probability theory? #flashcard #RA #QuantifyingUncertainty 
	This is a set of world in which some event happens. The probability of an event is therefore the sum of the probabilities for any world in which it happens.

---
What is a conditional probability? #flashcard #RA #QuantifyingUncertainty 
	The standard probability of something happening is called the unconditional prior probability. But if we want to know the probability of something happening given that something else has already happened we need the conditional or posterior probability written as $P(a|b)$

---
What is the product rule in probability? #flashcard #RA #QuantifyingUncertainty 
	$P(a|b)=\frac{P(a\land b)}{P(b)}$ is the definition of conditional probability which can be written as $$P(a\land b)=P(a|b)P(b)$$ which is the product rule.

---
What are random variables in probability theory? #flashcard #RA #QuantifyingUncertainty 
	A random variable can be defined as a function that takes every possible world in the state space to a given value (within the domain of the RV).  We can then reason about the probability of each value for the RV. The probability distribution for an RV must sum to one over all the values and defines the probability of each of the values of that RV.

---
What is a joint probability distribution? #flashcard #RA #QuantifyingUncertainty 
	A joint probability distribution defines for all combinations of values for a set of random variable the probability of that combination. Hence it defines also the conditional probabilities for all the values involved.

---
How can inference be performed with an JPD? #flashcard #RA #QuantifyingUncertainty 
	*Marginalization* can be used to find the probability for a single RV. The idea is we can marginalize out a variable by summing all the probabilities for the combinations of other variables in the JPD leaving us with the probability distribution for a single variable.
	*Conditioning* can be used to find the probability distribution for a variable given we know the value for some second variable. To do this we fix the second variable and marginalize like before we can then divide by the probability of observing the fixed variable to scale up our distribution.
	*Normalization* can also be used. If we sum up the distribution for a number of cases within our variable the result may be relatively correct in scale but doesn't sum to one. We can divide by the sum to ensure this is the case.

---
What is independence in probability theory? #flashcard #RA #QuantifyingUncertainty 
	Two RV are independent when the value on one doesn't influence our belief about the value of another. That is the conditional probability on the first given the second is the same the unconditional probability of the first. $$P(X|Y)=P(X)\hspace{8pt}P(Y|X)=P(Y)\hspace{8pt}P(X,Y)=P(X)P(Y)$$Said another way the probability of observing some combination of values for the two RVs is the same as the chance of observing the two values on their own combined, which may note be the case if one being true makes the other more likely.

---
What is bayes rule and why is it useful? #flashcard #RA #QuantifyingUncertainty
	Bayes rule is defined as follows
	$$P(a|b)=\frac{P(b|a)P(a)}{P(b)}$$This is useful as it can reverse the direction of causality from a causal one to a diagnostic one which allow useful inference.

---
Why is independence useful for real world computation? #flashcard #RA #QuantifyingUncertainty 
	Independence allows us to break a large JDP into smaller independent pats that don't effect each other. Since the size of any JDP grows $O(2^n)$ for a number of RVs $n$ this can drastically reduce the size.

---
What is a naïve bayes assumption? #flashcard #RA #QuantifyingUncertainty 
	The naïve bayes assumption is when we assume that the effects of a cause are all conditionally independent given the cause. That is $P(cause|effect_1,...effect_n)=P(cause)\prod_{i}P(effect_i|cause)$

---
