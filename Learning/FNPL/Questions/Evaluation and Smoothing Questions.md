What are the two kinds of evaluation? #flashcard #FNLP #MethodsInAnnotationAndEvaluation
	There is **Extrinsic** where we measure performance on a downstream application and **Intrinsic** where we design a measure that is inherent to the current task.

---
What are the benefits and shortcomings of extrinsic and intrinsic evaluation? #flashcard #FNLP #MethodsInAnnotationAndEvaluation
	Extrinsic evaluation is better as it gives us measurements that are useful and informative to our context. However it is hard to do as models bust be compatible with the same downstream tasks to be comparable.

---
What is entropy mathematically? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	Entropy is a measure of the randomness of a variable. It is defined as $$H(X)=\sum_x-P(x)\log_2 P(x)$$

---
Given that entropy is measured in bits what does this say about how the state of the system may be found out? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	It will take on average the entropy number of Y/N questions to find the outcome for the random variable.

---
How does the average number of bits needed to encode a message change with entropy? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	The average number of bits needed to encode some message is always greater than the entropy of that message.

---
What is the entropy in English and how is this found? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	On average to guess well humans only need 1.3  y/n questions to find the next word in a sequence.

---
What is cross entropy for evaluating LMs and what is the problem with this? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	Cross entropy can be used to measure if a probability measure is stacking up to some other probability measure. This will be $$H(P,\hat P)=\sum_x-P(x)\log_2\hat P(x)$$this is always greater than regular entropy on our variable. 

---
What is the problem with using cross entropy to evaluate LMs? #flashcard #FNLP #MethodsInAnnotationAndEvaluation  
	**We don't know $P(x)$** but we want to find $H(P,\hat P)=\sum_x-P(x)\log_2\hat P(x)$. To get around this we may instead use $$H_M(w_1,...w_n)=-\frac1n\log_2P_M(w_1,...w_n)$$which assumes all words are equally likely in the original data. With an n-gam this is the average negative log probability while predicting a sentence.

---
How can the entropy of an n-gram model be approximated? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	To approximate the entropy of an n-gram model for a sentence. We can take an average of the negative log probabilities for each word predicted.

---
What is perplexity? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	This is analogous to cross entropy and can be through of as the branching factor for each choice (with n-grams word prediction) it is $$2^{\text{cross-entropy}}$$

---
What problem comes when we test for entropy on some corpus? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	Since the corpus and the model change we cannot compare the scores of one model vs another. Low entropy means the model is good or the corpus is easy.

---
What is the problem with evaluating using cross entropy when we have sparse data? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	Sparse data means $0$ probability for some things. This means the cross entropy becomes infinite and our model is infinitely wrong. Say if a word is never seen before our model can't be right.

---
What is smoothing? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	IN smoothing the plan is to change the distribution we are using so that the values given are less extreme. this help deal with sparse data.

---
How does laplace smoothing work? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	In laplace smoothing we simple add 1 to every count for different possibilities. We then also have to add the number of possibilities to the denominator.

---
What is the problem with laplace smoothing? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	Since we make the denominator so large while not increasing the high scoring values by the much in terms of count, their original probabilities get drowned out.

---
What is Lidstone smoothing? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	In Lidstone smoothing we have some small $\alpha$ to all the counts. Then we have $\alpha N$ to the denominator. This reduces the problem of probabilities getting washed out but may still not give optimal results.

---
How does good Turing smoothing work? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	The idea is we move the counts down. So any item with 0 count gets the probability mass that was in the 1 count values. They get their mass from the two counts and so on. With some magic to get the top counts and smoothing to get good values.

---
How does good Turing work mathematically? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	In good Turing we want $\frac c N$ for out probability to be replaced by $\frac{c^\star}N$. We have $$c*=(c+1)\frac{N_{c+1}}{N_c}\hspace{16pt}P_{* c}=\frac{c*}{N}=\frac{(c+1)\frac{N_{c+1}}{N_c}}N$$

---
What is a good interpretation of cross entropy? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	We can imagine cross entropy $H(x,y)=-\sum p(x)\log p(y)$ from the point of view of $x$ being true. Then this measures the average amount someone believing $y$ (distribution) sees the information  increase after the event.

---
What is the difference between laplace and Lidstone smoothing? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	Laplace is a form of Lidstone smoothing. The idea is basically to add $\gamma$ to every count even the unseen count. This way nothing has probability 0.

---
