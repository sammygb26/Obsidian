# Structuring Machine Learning Projects
We will have many idea of how to improve our models performance. But there are strategies that allow us to choose better options.

### Orthogonalization
There are many things to try and many things to change when designing a network. It is important to know what to turn to achieve some effects. This is called **orthogonalization**. When designing intuitive systems some hyperparameter or control must have an intuitive impact. With the example of a TV where each nob only move the image a certain way. The opposite of this is each control has some combination of effects. Hence it is important to use hyperparameters that done have conflicting effects if we want to tune the effects to what we want. When the controls are *orthogonal* and aligned with what we want to tune it is far easier to get the results we want.

In machine learning the results we want to turn may be the accuracy in *training*, *development* and *testing*. We therefor want hyperparameters that can be used to train each one of these individually.

## Setting Up Your Goal
When trying out different options it can be important to have a **single number evaluation metric** that allows you to tell if you are performing better or worse on the problem. If we have multiple metric then a new network and perform better on one and worse on another hence we do not know if it is better. It is more effecting to quickly pick one network as the best and iterate further on it. Hence we make a combined score which we follow instead.

However we cannot always combine metrics like for example *accuracy* and *running time*. We want to combine these two into an overall evaluation metric. But it may be artificial to combine some weighted sum. We can also say we want to *maximize* accuracy and the running times must be *less than* some value. In this case accuracy is an **optimizing metric** and running time is a **satisfying metric**. This allows us to have to individually metrics and still pick the best.

We also need to carefully set up our training/development and test sets to maximize efficiency. Where *dev* set is also called **hold-out cross validation**. We want to make sure we are taking the test and dev set form the same distribution. Our dev set is like setting up a target we are trying to hit. Then our test set is how we evaluate the model which will be a different target. There are many rules to choose train and dev and test sets form some set of data. However all we really want is the sets to be accurate with the most going to *training*. Hence with very large datasets we can use a very small fraction and still get an accurate result. We may want very accurate evaluation in the test set hence we would want more examples.

We may also want to change our dev/test set and metrics. That is we are changing the target we are aiming for.  We may find our matric doesn't rank order our algorithms correctly in this case we need to change the metric. This may also change when our algorithm is deployed and we get far lower quality data for example. Here our metric isn't reflecting how well our algorithms perform hence we need to change the matric.

## Comparing to Human-level Performance
The key idea is that since we can now perform at the level of humans it is natural to compare. This gives a good metric for many problems and a level to aim to which we know is possible. The growth after this point becomes far harder as we approach the theoretical maximum. This limit is called the *bayes optimal error* gives by the best function from $X\to Y$ which can never be surpassed. One reason why we get less better after surpassing humans is that there are less tools available before we surpass them. For example we can get labeled data from humans we can get insight by looking at why the human dis better and we can better analyze bias and variance.

#### Avoidable Bias#
We want an algorithm to perform well but not too well. If humans have near perfect accuracy at 1%. In this case if we get 8 and 10% for train and dev we know we should try to improve training hence we have bias for sure. If humans had 7.5% error instead we may see that training is doing just fine and instead we should try to reduce dev error so the *variance*. Therefor its good to know bayes error and hence how far we can go to improve. Therefore decide to work on bias or variance. The idea is that *human performance* is a good approximation of *bayes error*. Therefore we tread the difference between our performance and human/bayes performance and the **avoidable bias** which we can work on.

### Understand Human-Level Performance
We need to get an actual measure of what human level performance is help give a performance of bayes error. For example with medical imaging. A regular human makes 3% error, a regular doctor 1%, an experienced doctor 0.7%, a team of experienced doctors 0.5% error. So which error is **human level error**? If we think of human error as a proximate for *bayes error* we can look at the best performance as bayes error must be less that the best human effort. Often however a *typical doctor* may be a good result and give a desirable result. 

Once we know the *avoidable bias* given by our chosen human level error we can compare it to the *variance*. The difference between the different measures of human bias only becomes the most meaningful when we are looking at a similar size for the two values. The key idea is that 0% error isn't possible to achieve in many cases.

### Surpassing Human Level Performance
As we surpass human level performance we cannot know if we are overfitting or if we are still below bayes error. We might think that if we are better than even a team it can be really hard to know how to do better. It can be hard to make progress at this point. Many tasks with **structured data** have been surpassed whereas *natural perception tasks* are harder to beat. These systems also use huge amounts of data to surpass human level performance whereas a human may find it hard.

## Improving Model Performance
To perform supervised learning we must assume we can make *avoidable bias low* and this will generalize well to the dev/test sets. Hence we chance hyperparameters to optimize *avoidable bias* and then try to improve dev/test performance that is the *variance*. The techniques we use are **orthogonalized** if the change we make only affect one of these values. 

To lower **avoidable bias** we can
	Train a bigger network
	Train longer/better optimization algorithm
	NN architecture/hyperparameter search (size etc.)

To lower **variance** we can
	Get more data (allowing better generalization)
	Regularize (l2, dropout, data augmentation)
	Can also change NN arcetecture/hyperparameter search (etc.)

## Error Analysis
If you model isn't performing at the level of human performance and that is what we want. Manually examining the results can give insight into what to try next. We can look at the distribution of  of how our network is mislabeling to see where the problem is. So if one set makes up 5% of errors improving that set will only improve the error to 95% of its original. This process of analyzing solving what problems will solve what issue will give you insight into what is the most ideal problem to work on. This is called **error analysis**. A good way to do this is create a table with columns for possible things we can try. We then count up the dev set error each solution would remove.

![[Pasted image 20220813143613.png]]

This doesn't tell us what to choose but tells us the best we could possible do by solving each problem. 

#### Cleaning Up data
We may find that some data is mislabeled (by humans/ wrong label) in out *training set*. We need to asses if we should correct these. The algorithms are fairly robust to errors in the training set if these errors are *random*. Hence these can be ignored. **Systematic Errors** for example will cause this bias to be ingrained into the network. We may also have some number of training examples that are wrong. We can include a column for this in our *error analysis table*. We can then count up the percentage of errors due to mislabeled examples. We may only want to change this if it makes a significant different to the use of the dev set that is the relative difference between the labeling error rate and true errors. We would want to apply any processing to the dev set also to train train set. We also need to check if things we labeled correctly (model) were truly labeled wrong. It can be ok to leave the train set however as the network can be robust to this.

#### Building First System Quickly and Iterating
There can be many direction we can go in with our network and choices we could make. To overcome this we can *set up quickly and iterate*. Hence we make a dev/test se and a metric. Then we build an initial system quickly to start to understand the challenges and problem better. We can then use **error analysis** to tell us what direction and techniques we should employ to improve our performance.

## Mismatched Training and Dev/Test Set
Our networks have a thirst for data so many times data is just added in without balancing the dev/test and training sets. For example we may want to incorporate field data after our model is launched to supplement training data. But we really care about our performance on the true field data. Hence just shuffling them in would make our dev/test set inaccurate and get the new images into the training data. Hence we are aiming for the wrong target. Instead we can take dev/test from our field data and add in the remaining examine not needed to the training data. This good things here is our target for performance in correct and this will get better performance even if we have worse training data.

#### Bias and Variance with Mismatched Data Distributions
When we estimate bias and variance we can use it to guide network development. With a *human level performance* of ~0% and then with training 1% and dev 10% we would usually say there is high bias. However what if the training and dev sets are from different distributions how do we know which is performing worse. We changed two things at the same time the *distribution* and the data *not being seen*. Hence we do not know which each causes how much of the problem. We can add a new distribution called the *training-dev set* which has the same training as the test data however isn't used to describe the performance of the network. We then look at the training error, training-dev error and dev error. The difference between training-dev and dev is caused by the difference in distributions while the difference between train and train-dev is cuased by **variance**. With a high train-dev to dev difference this instead a **mismatch problem**.

![[Pasted image 20220813164129.png]]

The numbers don't always get higher and in fact the dev and test sets can be easier and give better results. To get a more general result we can split human level for each set. We can at this point make a table for each data distribution.

![[Pasted image 20220813164552.png]]

All of this gives the new problem of **data mismatch**.

#### Addressing Data Mismatch
A good first step is to manually look at errors in the dev set this may tell you categories of errors which is causing the mismatch (noise, different set up etc.). Then we look to make the training data more similar like simulating noise and so on.

We can use *artificial data synthesis* to make training data more similar to test data. For example adding car noises to speech recognition to be used in cars.

![[Pasted image 20220813165013.png]]

One problem may be that if we have say 10,00 hours of original audio and only say 1 hour of noise we may overfit to the training set. The problem is as humans we cannot see this. Another example is using rendered cars which will look different enough to us but may only represent a small subset of possible cars. The problem is we are **synthesizing to a small subset**.

## Transfer Learning
This is where we train a network on one task then retrain on a new one. So we for example learn to recognize an object they retrain on some new data set like diagnosing x-rays. A way to do this is remove the final layer and re-initialize a new set of random weights for the final layer. We then use a new training set to retrain the network. With a small set we may just train the final layer where as with more data we may retrain the whole network. The first task is called *pretraining* and the final step is called *fine tuning*. So for example we may train on a *speech recognition system* and then *fine tune* to some trigger word dataset. The key use of this is when we only have a **small dataset** hence the larger one can our network by it not having to learn how to identify small scale features. This technique only makes sense when transferring from some A $\to$ B if 1) A and B have the same input $x$, 2) You have a lot more data in task A than B and 3) Low level features form A could be helpful for learning B.

## Multitask Learning
Here instead of training one task then another we train all task simultaneously and hope that tasks help the learning of the other tasks. We may be trying to identify 4 elements in an image for car driving. We would therefore have 4 labels for each example and our network would output 4 $y$ values into a (4,1) $\hat y$. The overall loss would therefore be $$loss:\hat y^=\frac1m\sum_{i=1}^m\sum_{j=1}\mathcal L\left(\hat y_j^{(i)},y^{(i)}_j\right)$$This cost function is an example of multitask learning. The idea is training 4 network at once gives better results than just one at a time. And we can still do this even when some labels are unknown or the network is only trained for each example at a time.

This makes sense 1) when our task shar low level features 2) when the amount of data is similar (this isn't always true) and also there are many tasks giving a boost to each other 3) when we can train a big enough network to be good at all tasks otherwise we may use transfer learning.

## End-to-end Deep Learning
The idea is that instead of taking multiple steps in some process we instead replace this with one large network taking in all the data. this *end to end approach* works best with very large datasets where as the hand build method may work better for smaller amount of data. But it can be in many cases that breaking a problem down can improve performance rather than taking an end-to-end approach,

Some reasons this is through to work are:
	1) **Lets the data speak** so the most appropriate function will be the one the network tends to rather than the human element giving bias
	2) It also means we need **less hand designed components** which can be hard and costly to develop

Some reasons it doesn't work sometimes are:
	1) **Needs a lot of data** for some x $\to$  y mapping to train the systems.
	2) Excludes potential hand designed components which is a useful  way to inject domain knowledge.