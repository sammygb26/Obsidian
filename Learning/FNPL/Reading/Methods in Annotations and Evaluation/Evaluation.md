We may want to build some sort of *classifier*. This will give the class of different documents, for example classifying into "positive" or "negative" reviews or "span" and "not-spam". We will compare how our model performs this task with **gold labels** (which are given by human annotators). First we can construct a **confusion matrix**.

![[Pasted image 20230408111713.png]]

The two dimensions are the systems output and the gold label output. **Accuracy** is generally not used as it doesn't account for unevenly distributed classes. Instead **precision** and **recall** are used for evaluation. $$P=\frac{TP}{TP+FP}\hspace{64pt}R=\frac{TP}{TP+FN}$$But we need a way to combine these. A good way is the **F-measure** defines as $$F_\beta=\frac{(\beta^2+1)PR}{\beta^2P+R}$$We can change $\beta$ to weight $P$ and $R$ differently. With $\beta>1$ recall matters more while $\beta<1$ precision is favored more. When $\beta=1$ precision and recall are evenly balanced. This is called the $F_1$ metric. With $$F_1=\frac{2PR}{P+R}$$This is used as it is a **conservative matric** and will more heavily weight smaller values.

### Evaluating with More than two classes
We can also expand these notations to more classes with slight modification to the definitions of precision and recall. Below is a *confusion matrix* for three classes "spam", "normal" and "urgent".

![[Pasted image 20230408114532.png]]

Above is shown how to combine **precision** and **recall** for each class. We can combine these in different ways. In **macroaveraging**,  we place all values into a single matrix and compute precision and recall from that. We then average to find the overall performance. We also have **microaveraging** where we compute the performance for overall all classes by collecting into one matrix and calculating performance over that.

![[Pasted image 20230408115354.png]]

[[Methods in Annotation and Evaluation]]

