What is the aim in classification? #flashcard #FNLP #NaiveBayesClassification
	The aim in naive bayes is given some document we want to predict which class is belongs to. The documents are also called features and the class a label.

---
What are some examples of classification? #flashcard #FNLP #NaiveBayesClassification 
	Some examples f classification are spam detection, sentiment analysis, disease diagnosis, topic detection, language detection, gender detection etc.

---
How could N-gram model be applied to classification? #flashcard #FNLP #NaiveBayesClassification 
	N-gram models give probabilities these could be used for classification if we can use the probability of a sentence to discriminate between the labels.

---
How might a naive bayes classifier work? #flashcard #FNLP #NaiveBayesClassification 
	A naive bayes classifier works based on two parts. We use **bayes rule** to note the $P(c\mid d)$ can be expressed as $P(d\mid c)P(c)$ taking out a constant factor. Then we assume $d$ is made of features $f$. Then the **naive** assumption is that all features as independent given the class. Hence $$P(f_1,f_2,\dots,f_n\mid c)=P(f_1\mid c)\dots P(f_n\mid c)$$

---
Why is naive bayes sometimes called a bag of words classifier? #flashcard #FNLP #NaiveBayesClassification 
	Naive bayes is sometimes called a BOW classifier as the independence assumption means feature order and structure doesn't matter, their relation is words so it is as though we threw all the features is a bag and shook them.

---
How can a naive bayes classifier be trained? #flashcard #FNLP #NaiveBayesClassification
	We want to find two things the **prior probability** $P(c)$ and the **likelihoods** $P(w_i\mid c)$. For both we use MLE. $P(c)$ is the proportion of examples that are in class $c$. Then $P(w_i\mid c)$ is the proportion words in text of class $c$ that is $w_i$.

---
What problem can arise when MLE is used for naive Bayes? #flashcard #FNLP #NaiveBayesClassification 
	A major problem is zero counts. If some words doesn't appear in a class then it will make the class completely unlikely. But **smoothing** can be used to overcome this.

---
Why is naive bayes called a linear classifier? #flashcard #FNLP #NaiveBayesClassification 
	Since $\log$ is monotonic the argmax will not be changed if we take a log of the contents. This makes the overall a sum of the log of each prior and the feature probabilities given the class. This is simple of the form $w^Tx+b$ with log prior $b$ and feature existence $x_i$ with log probability $w_i$.

---
What are some optimization that can be made to naive bayes sentiment analysis? #flashcard #FNLP #NaiveBayesClassification 
	1 counts can be used where the number of times a word is used in a document is reduced to there or not. Negation can also be taken into account by appending $NOT$ to the beginning of negated words.

---
How can sentiment lexicons be used with naive bayes? #flashcard #FNLP #NaiveBayesClassification 
	There are pretrained lists of positive and negative words. They can be used to augment the training data and get a model that is more robust to unseen words.

---
How can ignoring stop words help naive bayes? #flashcard #FNLP #NaiveBayesClassification
	Stop words don't give much meaning on their won and simply connect words. Naive bayes ignores this information hence stop words can be safely removed to improve model performance.

---
When is semi-supervision useful? #flashcard #FNLP #NaiveBayesClassification 
	This is useful when we have some labeled data but a large amount of unlabeled data. We can train a model on the labeled data and then use this to label the unlabeled data and gain insight into features only present in the unlabeled data. 

---
What is a problem is basic semi-supervision? #flashcard #FNLP #NaiveBayesClassification 
	A problem with basic semi-supervision where we directly train on labeled data as if their labeles were as good as gold labels is mistakes. Especially when the mistakes are due to a lack of certainty as to which class an example belongs to.

---
How can we get bast the certainty problem in semi-supervision? #flashcard #FNLP #NaiveBayesClassification 
	One way to get past this is by using confidence values or probabilities of + or - labels instead of straight 0s or 1s. Then the weights pleased on these examples is tempered.

---
How can EM be used with semi-supervised learning? #flashcard #FNLP #NaiveBayesClassification 
	We train or model initially on known labeles. This can then be used to predict the labeles in an **E** step for the unlabeled data. We can then use this to get a better approximation of classes in an **M** step. We repeat this to converge onto a good estimation of what predicts a class.

---
What are the advantages of Naive bayes? #flashcard #FNLP #NaiveBayesClassification 
	It is **easy to implement**. It is **fast** to train and classify. It **doesn't** require as much training data as other methods. It also **usually works reasonably well**. This all means it works well as a basic algorithm.

---
What are some disadvantages of naive bayes? #flashcard #FNLP #NaiveBayesClassification 
	The naive bayes assumption is destructive and remove a lot of modeling capability. It uses all features but they may not all be relevant.

---
What is the harmonic mean? #flashcard #FNLP #NaiveBayesClassification 
	The harmonic mean is the inverse of the average sum of inverses. This gives the a mean which more heavily weights small values.

---
What is the F_1 score? #flashcard #FNLP #NaiveBayesClassification 
	For P and R this is $$\frac{2PR}{P+R}$$ and is the harmonic mean of $P$ and $R$.

---
How can the performance on more than two class be evaluated? #flashcard #FNLP #NaiveBayesClassification 
	We can look at a confusion matrix to see how each class if mixed up with others.

---
What are the two options for evaluating performance on multiple classes? #flashcard #FNLP #NaiveBayesClassification
	There is macro averaging where we look at the performance in a form all together (like a confusion matrix of all classes). Or **micro averaging** where we look at small confusion matrices for each class.

---
What is the problem with the usual test/dev/train dataset split? #flashcard #FNLP #NaiveBayesClassification 
	The problem with this is it can use up a lot of our data in tests that don't add to performance.

---
What is a way to get around the data limitation it splitting up data into test/dev/train segments? #flashcard #FNLP #NaiveBayesClassification 
	One way is the use $k$-fold cross validation. The data is split into $k$ segments. Then we train $k$ model leaving out one of the $k$ segments for each to train. This mean any changes are tested against the whole dataset and to our dev set isn't biased. The problem is this is computationally expensive.

---
Why is statistical significance testing needed in model evaluation? #flashcard #FNLP #NaiveBayesClassification 
	We need a way to know how much a model is better than some other and if it truly is or if it more by chance it seems better. With statistical significance testing we test the distribution of a hypothesis and give a p-value which is the random chance some instance of our model false performs in a way to comply with this null hypothesis.

---
How can p-values be found? #flashcard #FNLP #NaiveBayesClassification 
	This can either be done **parametrically** where we know the type of distribution of our models performance. Or it can be done non-parametrically with bootstrapping.

---
How is a statistical hypothesis test carried out? #flashcard #FNLP #NaiveBayesClassification 
	We give hypothesis. The null-hypothesis (we hope to disprove). Then our p values is the probability of our data given our null hypothesis. Hence if this is low the null hypothesis is likely not true.

---
How is a bootstrap p-value obtained? #flashcard #FNLP #NaiveBayesClassification 
	We require a sample of our data. Then we take random samples of this set with replacement. We calculate the proportion of times give this sample our null hypothesis is true or not. The proportion is our p-value.

---
