There are two kinds of spelling errors we might correct **non-word errors** where the misspelled word isn't in the dictionary. While **real word spelling errors** are for misspellings that do exist but  are still the wrong word.

## The Noisy Channel Model
![[Pasted image 20230415143849.png]]

Here we treat the misspelled word as if it were passed through a *distorted* noisy communication channel. We want to recognize the *true* word that is hidden. We are predicting a word $\hat w$ out of our vocabulary $V$ given some noisy version $x$. We want the most likely one given our observed $x$ $$\hat w=\underset{w\in V}{\arg\max}P(w\mid x)$$Now $P(w\mid x)$ may be hard to estimate and we can break it up using **Bayes rule** and then simplifying. This gives us $$\hat w=\underset{w\in V}{\arg\max}P(x\mid w)P(w)$$The **likelihood** or **channel model** of the nosy channel producing an observation $x$ is given by $P(x\mid w)$. The **prior probability** is $P(w)$.

If we want to perform **error-word correction** we can use *Damerau-Levenshtein* edit distance which also includes *transpositions* aswell as deletions and replacements. We can also restrict this to edit distance one words for simplicity. From this point we can find all edit distance one real words from a dictionary.

![[Pasted image 20230415150657.png]]

For each possibility we can calculate $P(x\mid w)$ from a parameter matrix for each type of error. These tell us the frequency of mistakes made with a letter. We then divide this by the count observed of the observed letter sequence. In the end we calculate $P(x\mid w)$ as

![[Pasted image 20230415151109.png]]

We can now combine this with our language model to give us  probabilities for each word.

![[Pasted image 20230415151146.png]]

The choice of $P(w)$ in this case is form a unigram model. But we may want to take the context of surrounding words into account.

## Real-word spelling errors
These are errors that end as real words. They can come from homophones or just close words or even grammatical errors.