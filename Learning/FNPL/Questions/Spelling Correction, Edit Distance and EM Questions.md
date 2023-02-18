What noisy channel insight makes spelling correction easier? #flashcard #FNLP #SpellingEditDistEM
	We want to find the most likely intended language $y$ given the received language $x$. But this can be changes to the produce of the likelihood of the original language and the probability of the mistake with some constant factor removed. $$\underset{y}{\arg\max}P(y\mid x)=\underset{y}{\arg\max}P(x\mid y)P(y)$$

---
How might a spelling correction algorithm work? #flashcard #FNLP #SpellingEditDistEM 
	We may have a large dictionary of real words. We split or merge words in the input string and consider correction that differ by some number of mistakes. How likely each series of mistakes is can give us $P(x\mid y)$ then this can be combined with a language model giving $P(y)$.

---
How might a simple spelling correction noise model be made? #flashcard #FNLP #SpellingEditDistEM 
	A simple spelling correction noise model could be made by considering all the different possible changes to match the observed text with some other text. This gives the **edit distance algorithm**. With the special case that edits are takes to cost not just 1 depending on the edit. We **assume** the edits are independent and each as likely to occur given the text.

---
How can the probabilities for probabilistic edit distance be found? #flashcard #FNLP #SpellingEditDistEM 
	With our corpus of labeled examples of indented and observed text we can match corrected to observed words. Edits between the two then also describes the errors made. We can thereby count the number of errors of each type with relation to the number of non errors. This allows us to perform MLE to get probabilities.

---
How can the edits between two text be found? #flashcard #FNLP #SpellingEditDistEM 
	We can use edit distance to do this which gives each edit a cost (in probability or some other form). The minimum cost can then be picked and this gives the most probable sequence of edits.

---
How is edit distance found between two strings? #flashcard #FNLP #SpellingEditDistEM 
	The trick is to break the problem into finding the minimum edit from substring to each other a combination of how smaller strings are edited along with a cost for each action that could combine them. The minimum of this gives the edit distance to get to that substring pair. Then adjacent substring can be build up from this. This continues until the edit distance for the whole sequence is reached.

---
What problem would our model have calculating edit probabilities without labeled answers? #flashcard #FNLP #SpellingEditDistEM 
	We can find the edit probabilities if we have paired edits and true texts. Then we can find edits from error text to intended text if we have edit costs (or likelihoods). There is a catch-22 here however as we need one for the other. To get around this **expectation maximization** can be used.

---
How is expectation maximization used to find edit probabilities given only intended and edited texts? #flashcard #FNLP #SpellingEditDistEM 
	We can perform the **expectation step** and find the edits given some initial guess of probabilities. This can then be used in the **maximization step** to find the probabilities of edits that make these edits most likely. The E and M step are then iteratively performed to get better approximation for each. 

---
If we are performing EM to find edit probabilities what is theta? #flashcard #FNLP #SpellingEditDistEM 
	There are the model parameters. We are maximizing the probability of our edits given these parameters. The edits probability is assumed to be the probability of each error given the intended sentence.

---
