What is a classic example of where distributional semantics is useful? #flashcard #FNLP #DistributionalSemantic
	Distributional semantics is well suited to the  problem of **gradation** and **similarity**. For example take the questions "What is a good way to remove wine stains?" and the answer "Salt is a great way to eliminate wine stains." We need a good way to compare worse like good and great or remove and eliminate.

---
What is the problem wit using a thesaurus to get around the problem of similarity and gradation? #flashcard #FNLP #DistributionalSemantic 
	The problem is the limited number of examples we have to work with. We can never cover all words and so an automatic approach is needed.

---
What is the idea behind meaning from context? #flashcard #FNLP #DistributionalSemantic 
	The idea behind meaning from context is that the use and meaning of words can be found purely from their placement and use in language. Purely by the use of a word or placement in a sentence we can gleam the meaning from the context.

---
What is the distributional hypothesis? #flashcard #FNLP #DistributionalSemantic 
	This can be boiled down to: "We can infer meaning just by looking at the contexts a word occurs in" or meaning is the context. This way **similar contexts imply similar meanings**.

---
Where does the name distributional semantics come from? #flashcard #FNLP #DistributionalSemantic 
	In linguistics distribution - means the set of context that a particular item occurs in.

---
What is another name for distributional semantic models?  #flashcard #FNLP #DistributionalSemantic 
	Vector-space models.

---
In a basic way how can a word be represented in a distributional way?  #flashcard #FNLP #DistributionalSemantic
	A word can be represented as a vector of its contexts for example words is co-occurs with and otherwise 0.

---
What is First-order and Second-order cooccurrence in distributional semantics?  #flashcard #FNLP #DistributionalSemantic
	**First-order co-occurrence** (syntagmatic association) is typically relates words which are nearby each other.
	**Second order co-occurrence** (paradigmatic association) relates words which have similar neighbors.

---
What are some common ways to get a good context for a word?  #flashcard #FNLP #DistributionalSemantic 
	Generally **stopwords** are ignored (uninformative). Different sizes from 5 -100 (best for whole document meaning) words can be used. Relations other than cooccurrence like relation through syntax. Lower than 5 word contexts are only best for *syntactic similarity* and only for frequent words

---
What is the problem with binary indicators in distributional semantics?  #flashcard #FNLP #DistributionalSemantic 
	The problem with these binary indicators is they aren't very informative and frequency of co-occurrence isn't used. is there convey no sense of words.

---
What is one way to work out if a collocation has occurred? #flashcard #FNLP #DistributionalSemantic 
	One way is to use **pointwise mutual information** where we compare the actual probability to the who words predicted probability.

---
What is the formula for pointwise mutual information? #flashcard #FNLP #DistributionalSemantic 
	The formula is $$PMI(x,y)=\log_2\frac{p(x,y)}{p(x)p(y)}$$

---
What is a problem with using PMI to compute collocations? #flashcard #FNLP #DistributionalSemantic 
	A problem is the marginal pdfs will be very low when both word probabilities are low. This way the  PMI for co-occurring infrequent words will be massive.

---
What are some other ways to find collocations? #flashcard #FNLP #DistributionalSemantic 
	Other ways of measuring statistical (in)dependence. Like student -t-test, $\chi^2$, dice coefficient, likelihood ratio test, Lin association test etc

---
What improvements can be made to PMI to find collocations? #flashcard #FNLP #DistributionalSemantic 
	We can use smoothing, weighting, discarding and negative elements.

---
With PMI what do our word representations become? #flashcard #FNLP #DistributionalSemantic 
	Our word representations become vectors of PMI (or PPMI). This makes each word a point in a high dimensional vector space.

---
What is a problem with using Euclidian distance as a similarity measure? #flashcard #FNLP #DistributionalSemantic 
	If even one dimension is large the distance will be large and so mostly similar vectors can be mistaken.

---
What is the problem with using the dot product as a similarity measure? #flashcard #FNLP #DistributionalSemantic 
	This isn't invariant to vector length and so more common words are more similar than non-common ones.

---
What are the benefits of using the normalized dot product as a similarity measure? #flashcard #FNLP #DistributionalSemantic 
	This comes down to all words being weighted the same overall and so instead we end up calculating the cosine of the angle between.

---
What are some other measures of vector similarity? #flashcard #FNLP #DistributionalSemantic 
	Some other examples are the Jaccard measure, dice measure, Jenson-Shannon divergence etc.

---
What are different ways to evaluate a distributional semantics system? #flashcard #FNLP #DistributionalSemantic 
	We can perform extrinsic evaluation in tasks like IR or QA, automatic essay marking. Then intrinsic is often a comparison to psycholinguistic data like *relatedness judgements* and *word associations*.

---
How are relatedness judgements found? #flashcard #FNLP #DistributionalSemantic 
	Here participants are given two words and asked to rank 1-10 how related they are. The final score is taken as an average of these.

---
What is a problem with asking relatedness judgements? #flashcard #FNLP #DistributionalSemantic 
	The **context** can affect the results a lot and casts double on their validity.

---
How are word associations measured? #flashcard #FNLP #DistributionalSemantic 
	participants see/hear a word and must say the first word that comes to mind. A probability is given to each word based on this.

---
How are word associations compared to machine associations? #flashcard #FNLP #DistributionalSemantic 
	The associations can form a ranked list we can then compare this to the machine similarity numbers and see which match the most.

---
Why does it make sense to learn a more compact space in distributional semantics? #flashcard #FNLP #DistributionalSemantic 
	We can represent words with a much smaller space than the size of the vocabulary.

---
What is the latent semantic analysis method for reducing the dimensionality? #flashcard #FNLP #DistributionalSemantic 
	The idea is to use a **truncated SVD**. Then the V vector will be a set of word vector these can be combined with content vector representing context. To get a word similarity to another we compare their word vector, and content vectors through a lower dimensional diagonal matrix.
	
---
What is the NN approach to reducing embedding dimensionality? #flashcard #FNLP #DistributionalSemantic 
	In this approach we train a NN to reduce the dimensionality of these words to a lower space. This can be done by using the words to predict context words then using some hidden layers and the embedding or methods similar to LSA.

---
What is compositionality?  #flashcard #FNLP #DistributionalSemantic 
	Compositionality is the idea that we can make up some whole as a composition of parts. In language this is often the case like *red barn* just being a barn that is read. But it can also not be the case *bar raising* is not raising a barn. The *white house* isn't just a house that is white.

---
What are different ways to apply compositionality in a vector space?  #flashcard #FNLP #DistributionalSemantic 
	We can use different computations. We want something that works in the form $$\text{meaning}(w_1w_2)=\text{meaning}(w_1)\space\oplus\space\text{meaning}(w_2)$$we can use **vector addition** (not very well), **tensor product** and **nonlinear operations learned by NNs** (current).

---
