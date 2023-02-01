# Probabilistic Reasoning over Time
To do inference with time in a non-deterministic environment before we had to keep track of a belief state. We then used a transition model to predict future states and a sensor model to update our beliefs. Here we will extend the same idea using *Bayesian Networks* to handle uncertain transition and sensor models.

## Time and Uncertainty
If the world is static we can use any percepts forever with the same amount of weight. For this we make a *static assumption* that things don't change without us (clearly false in the real world). Without this we need to sum up percepts over time to give our beliefs about the world.

We will view the world as a series of snapshots **time slices** each of which contains a set of random variables some of which we can observe. For now we will have the same subset of variables observed each step. $X_t$ will be the RV $X$'s state at time $t$ and $E_t$ is the observed evidence. So at time $t$ we have $E_t=e_t$ (evidence). The state starts at $t=0$ and we get evidence from $t=1$.

---
An example is where we are trying to determine the value of the weather form if we see our boss being an umbrella in. We will have $U_t$ (umbrella) the observation variable and $R_t$ (raining) the unobserved variable.

---

## Transition and sensor models
After we have gotten our state and evidence variables we need to describe how they change with time. For this we need our *transition model* and our *sensor/emissions models*. Our transition model gives the probability distribution of our latest state variables given our current ones. That is $P(X_t|X_{0:t-1})$. But $X_{0:t-1}$ is unbounded as $t$ increases, to deal with this we make a *Markov assumption* that the current state only depends on a finite number of previous states, seen bellow.

![[Pasted image 20220412091054.png]]

Once we have made this assumption we have a *Markov process* or *Markov chain*. A *first-order Markov process* only depends on the previous state (a). We have

![[Pasted image 20220412091318.png]]

With the *Markov Assumption* our $P(X_t|X_{0:t-1})$ is just a finite CPT. We also make a *Sensor Markov Assumption* that any evidence variable only depends on the current state. With this we get

![[Pasted image 20220412091542.png]]

Therefore $P(E_t|X_t)$ is our sensor model or observation model. For the umbrella world both are given.

![[Pasted image 20220412091656.png]]

We also need a prior probability for our starting variable $P(X_0)$ that allows us to state everything. With this we can give a formula for the JPD entries.

![[Pasted image 20220412091946.png]]


If something in our world affects our future states systematically and is affected by previous actions then our transition model will violate the Markov assumption. We get get around this be incorporating the state of this thing into our model but we then need to specify a transition model of it aswell.

## Inference in Temporal Models
There are many inference tasks we will want to do with these *Dynamic Bayesian Networks*.

1. *Filtering* -> where we estimate the posterior distribution over the most recent state given all evidence to data. This is also called *state estimation*
2. *Prediction* -> where we estimate the posterior distribution of *future* states.
3. *Smoothing (Hindsight)* -> where we compute the posterior distribution over *past* state given evidence to date.
4. *Most likely explination* -> where we give a sequence of observations that has the greatest probability of generating our current state.
5. *Learning* -> where we learn the transition and sensor models from observations (this requires smoothing)

## Filtering and prediction
A useful filtering algorithm needs to maintain a current state estimate and update it to make our computation not go up with time as the world moves on. We want to estimate the result for $t+1$ form $t$ and this is called *recursive estimation*. We then have two parts first we updates our estimate for $X_{t+1}$ then we updates this with new evidence $e_{t+1}$. We get the following derivation

![[Pasted image 20220412094323.png]]

There are two parts $P(X_{t+1}|e_{1:t})$ will be our updated distribution. While $P(e_{t+1}|X_{t+1})$ is our sensor model where we get the one step prediction we want. We use $\alpha$ as a normalizing constant to make sure the axioms of probability as satisfied while making the calculations more easy.  If we loop over every possible value for $X_t$ and weight it by its likelihood given the emissions we get

![[Pasted image 20220412095028.png]]

Which gives our desired formulation based on our prediction for the previous state. Within variable elimination we can think about updating $f_{1:t}$ to becomes $f_{1:t+1}$ 

![[Pasted image 20220412095337.png]]

*Prediction* extends filtering to work with no evidence variables into the future and in fact we have already incorporated one step of prediction into our model for the first timestep into the future. We instead want

![[Pasted image 20220412095754.png]]

This can be don't only with the transition  model and note the sensor model.

We can also estimate *likelihood* of our current evidence sequence. This is given as a similar reclusive formulation

![[Pasted image 20220412100504.png]]

The likelihood calculation as it goes on multiplies many numbers smaller than 1 leading to floating-point arithmetic problems.

## Smoothing
We want to compute the distribution over prior states given our evidence sequence. The way we do this is in two parts. A message forward from evidence leading up to the state we care about and evidence back which we have since collected updating our belief. Hence we break it down as follows

![[Pasted image 20220412100748.png]]

$f$ and $b$ are the forwards and backwards messages defined appropriately. The forward message is given simply from the *filtering* formula. The backwards formula is $P(e_{k+1:t}|X_k)$ and can be expanded as

![[Pasted image 20220412101057.png]]

The first and third factor come from our emissions and transition model respectively while the second one is a recursive call. This give our formulation as

![[Pasted image 20220412101416.png]]

If we keep recuring with backwards we reach $P(e_{t+1:t}|X_t)=P(|X_t)$ since $e_{t+1:t}$ is empty hence always true in this setting. An application of this that smooths over the whole sequence is called the forward-backward algorithm. It takes constant time when the DBN can be expressed as a *polytree*.

![[Pasted image 20220412102546.png]]

## Most likely Sequence
To find the most likely sequence we can apply the *Veterbi Algorithm* which is a Dynamic programming algorithm that allows us to calculate the solution in time proportional to the length of the sequence. The way this works is we keep track of the maximum likelihood for any value at any sequence length. The maximum likelihood for the next values will be a max of the two likelihoods for the previous values. We can track back at the end to get our sequence.

![[Pasted image 20220412103052.png]]

## Hidden Markov Models
In a *Hidden Markov Model* or *HMM* we are a dynamic Bayesian network but we have just one state variable and just one emissions variable. Any other dynamic Bayesian network can be converted into a *HMM* however this may take a lot of computation as there will be many more states *HMM*s allow for simplified matrix algorithms that improve on the previously mentioned ones.

## Simplified matrix algorithms
If our *HMM* has $S$ possible states then we can describe the transition model with a $S\times S$ matrix. This basically gives a simplified form for representing the summation over all states. As all states and their transitions to other states is captures in each entry of the matrix. We define the matrix $T$ to be the transition matrix such that

![[Pasted image 20220412103821.png]]

We can also put the sensor model into matrix form. Since we know the value of the evidence variable the matrix changes hence we have $O_t$ for the emissions matrix at time $t$. We can define the forward equation as the following.

![[Pasted image 20220412104431.png]]

And the backward equations similarly as the following

![[Pasted image 20220412104443.png]]

This will take time $O(S^2t)$ as each time we multiply $S\times S$ elements. This can be sped up by GPU hardware however. The messages are given as column vectors hence the flow through the matrices. If we keep track of the messages we can with constant space requirements compute all the smoothing for a sequence. The requirements on this are that the transition matrix is invertible and every step has an observation.

The matrix formulation can also improve online smoothing with a fixed lag $d$ where we want the smoothed estimate for a state $d$ in the past. We have from our previous time step 

![[Pasted image 20220412105323.png]]

And we want to calculate

![[Pasted image 20220412105407.png]]

We can calculate the forward portion using a filtering process form above. We can instead of updating the backwards message only update a combined matrix that rolls together all the backward message steps up to $d$ that is

![[Pasted image 20220412105931.png]]

Looking at the equation for the timestep in the future

![[Pasted image 20220412105957.png]]

We achieve a simple update procedure

![[Pasted image 20220412110016.png]]

## Dynamic Bayesian Networks
A *DBN* is a probability model where we have some state variables and some dependency on previous time steps. We can convert a *DBN* into a *HMM* and all *HMMs* are *DBNs* but we will save a lot of space not doing this if our *DBN* is spares as the size of the *HMM* transition matrix grows exponentially with the number of variables incorporated into the composite state variable of the HMM. We have just as before state variables $X_0$ and observed variables $E_0$ for brevity the same sets are kept in every timestep.

## Constructing DBNs
We need three pieces of information to construct a DBN. The *prior distribution* of the state variables $P(X_0)$; the *transition model* $P(X_{t+1}|X_t)$; and the *sensor model* $P(E_t|X_t)$. Then we also need the topology of the connections between the state variables. Some examples are given bellow.

![[Pasted image 20220412112343.png]]

The first is the umbrella example and the second could be a battery powered robot moving on the XY plane. It has a speed $\dot X$ and position $X$. We see the speed and position affect the position in the future. We also have the Battery and a meter reading its value.

Our sensors give values describing the state of true variable We can give then a *Gaussian error model* meaning their values drop of in likelihood in a gaussian way. Small errors are not really a problem but failure is. How do we deal with a sensor that dies without giving us any warning that its values are will become useless, how do we stop their incorporation into our model of the world.

A *transient failure* is the simples kind of failure. Every now and again our sensor sends nonsense. For example our BMeter might randomly sent some 0s every now and again despite a full battery. If we have no error described in our model a small number of 0s may cause our robot to believe its battery is completely empty even if this is very unlikely given our transition model. If we add some probability to the sensor giving this error reading it can take care not to reduce the posterior distribution on our battery level to an erroneous one. We would add more error than a gaussian error model but it would still be an unlikely outcome. The problem is this doesn't deal with *persistent failure*. We have a *transient failure model* but not a *persistent failure model*.

![[Pasted image 20220412113951.png]]

This is seen in the two graphs showing the expected battery reading. We see that without a *transient failure model* a small blip will give erroneous expected battery level. With an error model this can be take care of and our expected level doesn't decrease that much. If we have consistent failure we eventually decide it must be 0 rather than it failing.

To take care of this we add a new variable that affects if the BMeter reading that is if its broken.

![[Pasted image 20220412114345.png]]

We see in this the Broken transition model means we can break but we never unbreak. This gives the following behavior where with persistent failure we become certain our meter has broken. Our confidence in all battery values decays after that to a stationary level.

## Exact Inference in DBNs
Dynamic Bayesian networks are Bayesian networks therefore we can use *unrolling* and make every slice of the DBN art of a BN and use the same techniques as in [[Probabilistic Reasoning]]. This doesn't work well for filtering or smoothing however. Our unrolled network's size and complexity grows as time goes on. If we use *variable elimination* however we can maintain a factor which describes our belief in the previous state. This can then be used in our constant state and we can update in time proportional to the size of the DBN. We keep *summing out* old slices of the DBN so keeping at most two slices at any time. The problem is this is still exponential in the size of the network. Hence we must fall back on approximate methods for this. We do however use this to update a slice at a time instead of the whole network improving the number of samples needed. The problem is that over time our system can loose track of what is going on since we always sample without taking into account the downstream observations. This means we need an exponential number of particles to maintain accuracy.

To get around this we can use either throw always samples with low likelihood and duplicate ones with high or we can use a technique called *particle filtering*. Here we keep a population of particles we propagate them through the network to get for each a new state. We then weight them based on how likely they were an resample generating a new population in each state based on the likelihood.

![[Pasted image 20220412121157.png]]

![[Pasted image 20220412121227.png]]

This algorithm is in fact *consistent* and keeps good probabilities as $N\to\infty$

[[Probabilistic Reasoning Over Time Questions]]