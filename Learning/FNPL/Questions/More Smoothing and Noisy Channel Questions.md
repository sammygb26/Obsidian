What problem does smoothing solve? #flashcard #FNLP #SmoothingNoisyChannel
	Smoothing helps solve the problem of zero counts in our data leading to 0 probabilities from relative frequency estimation.

---
What is the hole problem with Good Turing? #flashcard #FNLP #SmoothingNoisyChannel 
	Good Turing doesn't work when there are hole in our input distribution. That is it must be true that $N_i>0\implies N_{i-1}>0$. This can be solved by using linear regression to estimate the true distribution.

---
How can we deal with unknown words in a distribution and what is the problem? #flashcard #FNLP #SmoothingNoisyChannel 
	A problem is there is an uncountable number of unknown words and we will never catch them all. If we include them we will either wash out the probabilities for the words we do know of end up with the same problem of very small probabilities for 0 counts. To get around this we can replace all unknown words with the keyword $UNK$ for unknown.

---
What probability can come from assigning the same unknown probability to all unknown n-grams (and solutions)? #flashcard #FNLP #SmoothingNoisyChannel 
	The problem is not all unseen n-grams should be treated the same. "Scottish beer drinkers" vs "Scottish beer eaters". Of course one is more likely. There are two ways to deal with this **interpolation** and **backoff**.

---
How does interpolation work for unseen n-grams? #flashcard #FNLP #SmoothingNoisyChannel 
	In interpolation higher and lower order n-grams are combined to give the final value. We use a weighted average of the three probabilities to estimate the higher order probability more accurately. For example $$P(three\mid I, spent) = \lambda_1 P_1(three) + \lambda_2 P_2(I\mid spent) +\lambda_3P_3(three\mid I, spent)$$

---
Why in interpolation must all the weighting coefficient sum to 1? #flashcard #FNLP #SmoothingNoisyChannel 
	Each of our probabilities when marginalized should be equal to 1. Similarly our final output should have this property too, so that is is a probability. The coefficients summing to one ensures this.

---
How are the interpolation weights generally found? #flashcard #FNLP #SmoothingNoisyChannel 
	Interpolation weights are generally found by testing on the dev set.

---
What is the idea behind Katz Back-off? #flashcard #FNLP #SmoothingNoisyChannel 
	The idea behind Katz back off is to scale back the probabilities from our higher order model. This gives "leftover probability mass" which can be used for unseen values. This is done by using lower order n-grams for these unknown values.

---
How would Katz-back-off work for a trigram model? #flashcard #FNLP #SmoothingNoisyChannel 
	For known values we return a scaled back probability. Then for unknown values we use a bigram probability scaled down to fit into the probability space left after the higher order downscaling. This can be done recursively with a unigram aswell.

---
What do we define mathematically to make Katz-back off work? #flashcard #FNLP #SmoothingNoisyChannel 
	We start with some n-gram measure $P$ then we define $P^*$ to be this n-gram scaled down by some factor. Then the back off probability $P_{BO}$ is define so that for unknown values we use a $\alpha$ scaled back back of of a lower order n-gram.

---
What is the multi-word problem with n-grams? #flashcard #FNLP #SmoothingNoisyChannel 
	The multiword problem is that some multi-word phrases are often used together and can often be used as filler in sentences. This heightens the likelihood our model will predict these sequences. This causes the model to repeat these phrases when generating text. An example would be "you-see".

---
Does smoothing help with multi-word expressions? #flashcard #FNLP #SmoothingNoisyChannel 
	No, usually smoothing doesn't really help with multiword expressions. However **Kneser-Ney Smoothing** is meant to.

---
What is the idea behind Kneser-Ney Smoothing? #flashcard #FNLP #SmoothingNoisyChannel 
	The idea behind Kneser-Ney smoothing is to use the number of ways a word can be used as its "count" instead of the count. This should help with multi-word expressions as they are only used ones.

---
How does Kneser-Ney smoothing work? #flashcard #FNLP #SmoothingNoisyChannel 
	In KN smoothing we defined a new count $N_{1+}$ which is equal to $$N_{+1}(\bullet w_i)=|\{w_{i-1}:c(w_{i-1},w_i)>0\}|$$ MLE can then be performed on this.

---
How is word similarity applied to smoothing? #flashcard #FNLP #SmoothingNoisyChannel 
	Word similarity can be used to allow uncommon words to be have their probabilities heightened if a similar word has counts in some probability. For example **salmon** and **swordfish** may be used in the same way. But salmon is much more likely to appear in the corpus. And so it's counts should be shared with swordfish to give better approximations.

---
What is a class-based model in smoothing? #flashcard #FNLP #SmoothingNoisyChannel 
	Here we define for differen't words a hidden state $c_i$ that is the class of the word. We can then use $$P_{CL}(w_i\mid w_{i-1})=P(c_i \mid c_{i-1})P(w_i\mid c_i)$$This basically has the structure of a **hidden Markov model**.

---
What is a distributed word representation? #flashcard #FNLP #SmoothingNoisyChannel 
	In a distributed word-representation a word is represented as a vector of values. These encode the word in a space where similar words should be close and the structure of the space can be used to understand words.

---
How are distributed word representations used to give word similarity? #flashcard #FNLP #SmoothingNoisyChannel 
	Distributional word representations give words as vectors. Their distance can be taken as a measure of their similarity.

---
What is a distributional embedding of a word? #flashcard #FNLP #SmoothingNoisyChannel 
	In a distributional embedding a word is converted into a vector. Embedded in a vector space. Similar words should be related in this space.

---
Where does the name distributional representation come from? #flashcard #FNLP #SmoothingNoisyChannel 
	The idea is the instead of the word being a single values. It's meaning is distributed through many values making up its vector.

---
What is a problem when it comes to training distributional representations? #flashcard #FNLP #SmoothingNoisyChannel 
	Training distributional representations used a lot of resources.

---
What is a benefit of using distributional representations? #flashcard #FNLP #SmoothingNoisyChannel 
	Words are complex their syntax and semantics are often intertwined. Distributional representations allow both of these properties to be captured in one representation

---
What is the noise channel model? #flashcard #FNLP #SmoothingNoisyChannel 
	This is a model where we are trying to find some hidden distributions after some noise has been applied to it.

---
What are the parts of a noisy channel model? #flashcard #FNLP #SmoothingNoisyChannel 
	We have $P(Y)$ the hidden distribution, $P(X|Y)$ the noisy encoding and $P(X)$ the output sequence we get.

---
What are the parts of the noisy channel model when it comes to spelling correction? #flashcard #FNLP #SmoothingNoisyChannel 
	$P(Y)$ will be the intended language of the writer. $P(X|Y)$ models the mistakes made in writing. $P(X)$ will be the output error filled text we get.

---
Mathematically how can we estimate the hidden value in a noisy channel mode? #flashcard #FNLP #SmoothingNoisyChannel 
	We are given $P(X)$ we want to know $P(Y)$. Hence we want $P(Y|X)$. We will get $$y=\underset{y}{\arg\max} P(y|x)=\underset{y}{\arg\max}P(x|y)P(y)$$where we would divide the LHS by $P(X)$ but we can remove this as it doesn't change with $y$.

---
Why is it useful to split P(Y|X) up int P(Y) and P(X|Y) for inference? #flashcard #FNLP #SmoothingNoisyChannel 
	It complicates this as we need to find more probability distributions. However $P(Y|X)$ is task specific. $P(X|Y)$ is a noise model which is also task specific but may not require as many examples and take a more generative path. The key thing is that $P(Y)$ can come form a language model which can be trained on vast amount more data. This makes the overall method work fat better.

---
