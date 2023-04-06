What is an embedding for a word? #flashcard #FNLP #NeuralEmbeddings
	An embedding of a word is a vector representation of that word. An embedding defines a matrix the height of our vocabulary and with of our embedding space.

---
What are some different ways to get word embeddings? #flashcard #FNLP #NeuralEmbeddings 
	One-Hot, Latent Semantic Analysis, Prediction based

---
How are words embedded in a one-hot embedding? #flashcard #FNLP #NeuralEmbeddings 
	In a one-hot embedding we have a $V$ dimensional vector. Each word is given a element in this vector. The embedding of said word just has that value equal to 1 and all other values 0.

---
What are some issues with one-hot encoding of words? #flashcard #FNLP #NeuralEmbeddings 
	1) The vectors must be very long for a space for every word. 2) They also don't capture any similarity between words.

---
How are latent vectors generated in latent semantic analysis? #flashcard #FNLP #NeuralEmbeddings 
	In latent semantic analysis we build a vector for each word which describes the common context of a word. Then we get a truncated SVD such that word are only limited by some $d$ dimensions as are contexts.

---
What is the idea that allows the neural approach to generate embeddings?  #flashcard #FNLP #NeuralEmbeddings 
	The idea is to take prediction based model. We then train the representations of our words as context or word representations to maximize our prediction of our training data.

---
What is Mikolov's Skipgram?  #flashcard #FNLP #NeuralEmbeddings 
	We are trying to predict a word from its context. For example $$p(w_{t-2}\mid w_t)p(w_{t-1}\mid w_t)p(w_{t+1}\mid w_t)p(w_{t+2}\mid w_t)$$

---
How are the probabilities for Mikolov's Skipgram found yielding a neural embedding?  #flashcard #FNLP #NeuralEmbeddings 
	We have a list of **central** word vectors (for $o$) and **context** word vector vectors for $c$. We calculate $$p(o\mid c)=\frac{\exp(u_o^Tv_c)}{\sum_{w\in V}\exp(u_w^Tv_c)}$$That is we take the **SoftMax** of the dot predict between the two vectors for context and actual.

---
What loss is optimized to gain context vector from a Mikolov's Skipgram model? #flashcard #FNLP #NeuralEmbeddings 
	We optimize for each word and each character in there window the $-\log$ probability of the context word given the center vector (from the center word). That is: $$J(\theta)=-\frac1T\log L(\theta)=-\frac1T\sum_{t=1}^T\sum_\underset{j\neq0}{-m\le j\le m}\log p(w_{t+j}\mid w_t,\theta)$$

---
What is the context between LSA and training context and center vector by optimizing a Mikolov's Skipgram model?  #flashcard #FNLP #NeuralEmbeddings 
	The connection is that training MS for context and center word corresponds to factorizing the PMI matrix just as in LSA (at least approximately).

---
How does logistic regression pick a class based on the class and object vectors?   #flashcard #FNLP #NeuralEmbeddings 
	LR takes the the dot product of each context vector with the class vector. A SoftMax is then taken of the whole thing to get the final probability distribution over the classes.

---
How does a NN classifier work within a Neural Network?  #flashcard #FNLP #NeuralEmbeddings 
	The key idea is we are training to generate feature vector to pass into a trained Logistic Regression model.

---
How can class detection be performed with a NN?   #flashcard #FNLP #NeuralEmbeddings 
	We need to get an embedding of a document we can compare to our class vectors. One way is to sum all documents word vectors together from Word2Vec GloVe etc.

---
