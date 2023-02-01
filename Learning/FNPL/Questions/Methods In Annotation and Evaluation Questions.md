What are different factors that an affect that annotation of some data? #flashcard #FNLP #MethodsInAnnotationAndEvaluation
	1. Source of the data
	2. Annotation scheme
	3. Annotators
	4. Annotation software
	5. Quality Control

---
What do we want to consider when think about the source of our data when annotating? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	We want a good diverse dataset, money may also be of concern and we want the correct size of dataset.

---
How does our annotation scheme affect the annotations we get in the end? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	The annotation scheme defines what we are annotating. So we must pick one that relates to the information we want about any sentence.

---
How might different annotators affect our annotations? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	Annotators may be trained or untrained or may be biased in the way they annotate.

---
What is an annotation scheme? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	An annotation scheme defines what we ware annotating. It may be clear cut or ambiguous what annotations should be.

---
How can annotation guidelines help while annotating? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	Annotation guidelines give lots of examples of how data should and shouldn't be annotated. The idea is that human annotators can read these instructions and give more expected definite results. These guidelines can be very extensive and long however.

---
What are some causes of annotation error? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	We may have simple errors like hitting the wrong button. Or context errors like not reading the full context. Not noticing **pre-annotation errors**. Forgetting guideline details. Or cases not anticipated by the guidelines.

---
What do the failures of annotation lead to when it comes to gold labels? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	In truth because the annotation is not perfect so too are the gold labels. This limits how much a system can meaningfully learn.

---
What is Inter-annotator agreement (IAA)? #flashcard #FNLP #MethodsInAnnotationAndEvaluation
	We measure this to see how much different annotators agree or don't. This is used to give a guide to the quality of our annotations. **Raw agreement** take into account only the pure rate at which annotators agree for different sentences.

---
What other errors may be revealed if we look past raw agreement with IAA? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	Moving on we may see that there is structure to the mistakes. For example a group of annotators all changing the same word means there may be a possible missed interpretation.

---
How can crowd sourcing be used for annotation (and problems)? #flashcard #FNLP #MethodsInAnnotationAndEvaluation
	This is a cheaper way to get annotators. We get large groups of people on the internet to do a certain task. The problem is people are trying to make money here (at least with Amazon Mechanical Turk) and may also not be trained.

---
What is gold standard evaluation? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	Here we evaluate a model against some annotated truth we assume to be correct. These can be used for both training and testing data. With testing not done on training data.

---
What is model tuning and what problem can it lead to? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	To tune a model we train it and then use some test set to evaluate. We train different examples  then adjust the parameters get the best result. A problem could be overfitting the training data. For this reason it is performed don a dev set rather than the true test set.

---
What is cross-validation? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	This is a way of evaluating a model if a dataset is small. We take $k$ segments of our data. Then we train the model on each keeping a different $k$th of the data behind.  In the end we can combine all data to get a better model.

---
What is the simplest way to measure a models performance? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	We can use accuracy the proportion correct of the total size of the test set.

---
How is precision defined as a performance metric? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	Precision can be through of as the percentage of shots out model made that were on target. This is $$\frac{\text{TP}}{\text{TP + FP}}$$

---
How is recall defined as a performance metric? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	Recall can be through of as the percentage of targets you hit. This is $$\frac{\text{TP}}{\text{TP+FN}}$$

---
How is F1 score defined? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	This is the harmonic mean of $P$ (precision) and $R$ (recall) and so is $$F_1=\frac{2\cdot P\cdot R}{P+R}$$

---
If we have a performance metric how can we put it into context with actual performance? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	We can compare it to a simpler "dumber" model and see how it compares and we can compare it to human performance.

---
What is important when comparing model performance especially when there are only small differences? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	We should consider **significance** which measure the probability that our measurements are randomly in our range.

---
What are the two kinds of significance tests? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	There are **parametric** when we know the underlying distribution type to be normal/gaussian. Then **non-parametric** when we combine many distributions and bootstrap the significance.

---
What is error analysis? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	This is where we investigate the kinds of errors a system is making to understand its failings or why it is failing.

---
What is a confusion matrix? #flashcard #FNLP #MethodsInAnnotationAndEvaluation 
	A confusion matrix describes for many categories how errors were made. This can be done when the categories are discrete. The diagonals will then be the correct cases.

---
