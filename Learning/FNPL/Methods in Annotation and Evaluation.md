**David Hume** was an early empiricist. The idea that we learn through experience and experiments. This idea is learned in *statistical learning* and it is assumed we can learn in this way.

## Annotation
There are different factors that can affect how we do annotation.
1. **Source of the data** - We want a good diverse dataset, money may also be of concern and we want to ensure it is of correct size.
2. **Annotation scheme** - Here we need to decide on a way to annotate. It must relate to what information we want to be sorted.
3. **Annotators** - We need annotators to perform this annotation. But they may vary in quality.
4. **Annotation software** - We can use different annotation software and this may give different results and change how the annotators function.
5. **Quality control procedures** - We may need to perform this as the end.

##### Annotation Scheme
With a well trained annotator, many annotations are straightforward. Like word types or sentiment. But other example may be harder, text may be ambiguous and there be a gray area between categories specified in the scheme.


![[Pasted image 20230124122101.png]]

Annotation is not as easy as you might thing. Any annotation scheme will have some difficult cases where there is a gray area. The language needs this to be **flexible** and it changes over time. This can get even harder with **semantics**.

*Annotation guidelines* are useful to ensure good quality for our annotations. Documenting conventions in an annotation manual is important to give a **consistent result**. These can be very complicated and hard to use

![[Pasted image 20230124122410.png]]

Even comparatively simple schemes take many pages to disambiguate.

##### Annotation Quality
Even with extensive guidelines, human annotations won't be perfect. 
- **Simple errors** (hitting wrong button)
- **Not reading the full context**
- **Not noticing an erroneous pre-annotation** (pre-annotations are simple computer system that can perform basic annotation)
- **Forgetting a detail from guidelines** (also can change over time)
- **Cases not anticipated or not fully specified guidelines** (leads to inconsistency)

##### Inter-annotator agreement (IAA)
This is a way to estimate reliability of annotations. We have multiple people annotation a common sample  and measure **inter annotator**/ coder / rate **agreement**.

**Raw agreement rate** proportion of labels in agreement. If the annotation task is perfectly well-defined and annotator well trained they will agree 100%. With low rate we may want to redo guidelines. This can be thought of as the **human ceiling** and limits how well a machine can learn.

Some measures take knowledge about the annotation scheme into account. There can also be the case that annotators agree **on accident**. But this may be a common error. This can be somewhat corrected for when we assume the mistakes are uncorrelated.

##### Crowdsourcing
QC is more important when eliciting annotation from "the crowd". For example **amazon mechanical Turk** allows you to pay small amount of money for small amount of work from anonymous web uses. We need to take measure to ensure annotators are qualified and taking the task seriously. They may also lie about their competency (for example with a certain language). We can use **redundancy** to combat noise and reject annotators who fall bellow a given mark.

## Evaluation
Scientific method rests on making a testing hypothesis. We can than reject failed hypothesis and gain knowledge that way. Evaluation is not just for public review but allows us to manage internal development. It is also used to allow systems to improve themselves.

##### Hypotheses
We may ask questions about how well our model is performing or how it performs better than some other model. We can also ask questions about our data. Or about our annotators (IAA).

##### Gold Standard Evaluation
In many cases we have a record of "the truth". For example what is the best human judgement as to what the correct segmentation / tag / parse / reading is. **Gold standards** are used for training and evaluation. But we **must test on unseen data** as our model will overfit and we will get erroneously high results. We can also overfit to the training set so we must use a **development set** which we run many times (unlike the test set).

##### Cross-Validation
If our dataset is  **too small** to have a nice train / test / dev split. We could use $k$-fold-cross-validation. We partition the data into $k$ pieces with different held-out set, using the rest of the data for training. After $k$ folds every data point will have a held our prediction. After we have tunes the system. We can train on all datapoints.

![[Pasted image 20230124124258.png]]

We pick $k$ based on performance and how much data we have.


##### Measuring Model's Performance
To measure accuracy we divide the number of correct prediction over the side of the test set.

![[Pasted image 20230124124412.png]]

But when our data isn't balanced in terms of classes we can get erroneously high results or low ones. So we can also use other measurements. For example Precision, Recall and F-Score. For isolating performance on a particular label in multi-label tasks.

![[Pasted image 20230124124554.png]]

![[Pasted image 20230124124613.png]]

$F_1$ is a good way to combines both $P$ and $R$.

##### Upper Bounds, Lower Bounds?
How can we compare to other models or how humans work. There are many different **baselines models** we can compare accuracy to. For example we can use a model that always picks the most common output (dumb). We can compare to humans and if we work at the same level as humans we may want to stop.

##### Significance
When we are comparing measurements we are comparing estimates. We may ask if the differences are **significant** or we randomly get a higher or lower result. To know this we want to estimate the distribution of possible results.

There are two kinds of significance tests.

**Parametric** - when the underlying distribution is normal / Gaussian
**Non-parametric** - otherwise, these are more expensive to compute but only work with large datasets. But these are commonly used in NLP since often we don't get Gaussian distributions.

##### Error Analysis
Summary scores are important but don't always tell the full picture. **Error analysis** is key as it allows for failure to be understood so we can learn from them. This may also lead to finding bugs. A **confusion matrix** is a common way to do this

![[Pasted image 20230124125539.png]]

It shows (off-diagonal) how different tags are getting mixed up. Is there a pattern in the data?

##### How do we select a test set?
We want to select a test set usually by randomly splitting our data. This ensures they are distributed similarly. But we almost always use the networks differently in practice (on data not the same as what we have collected). This is **covariance shift**.

[[Methods In Annotation and Evaluation Questions]]