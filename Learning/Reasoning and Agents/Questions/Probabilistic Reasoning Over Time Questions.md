What is a *static assumption* a world? #flashcard #RA #ProbabilisticReasoningOverTime
	The static assumption means we assume the world doesn't change unless we take an action. This allows us to represent the world in discrete slices corresponding to choices we make or time ticks passing.

---
How are temporal Bayesian network set up? #flashcard #RA #ProbabilisticReasoningOverTime 
	Temporal Bayesian networks are set up by making the static assumption. This allows us to break reasoning about RVs through time into splices for individual time slices. If we also make the Markov assumption (that the current state only depends on a limited number of previous states) we can describes how the previous states affect the current state with a *transition model*.

---
What is the transition and sensor model in a dynamic Bayesian network? #flashcard #RA #ProbabilisticReasoningOverTime 
	The transition model describes how previous states affect the current state. So the possible values and their distribution in previous states conditionally influence current states. The sensor model describes how the hidden random variables affect the variables we can sense. Hence allows us to refine our belief of the hidden variables state.

---
What are the five types of inferences in a dynamic Bayesian network and what do they predict? #flashcard #RA #ProbabilisticReasoningOverTime 
	*Filtering* -> is where we estimate the posterior distribution for the most recent state given evidence to data.
	*Prediction* -> where we estimate the posterior distribution of future states.
	*Smoothing* -> where we compute the posterior distribution of past states given all evidence to data.
	*Most likely explination* -> where we give a most likely sequence of past states given what we have sensed.
	*Learning* -> where we infer the transition and sensor model from our observations

---
How is filtering and prediction performed in a dynamic Bayesian network? #flashcard #RA #ProbabilisticReasoningOverTime 
	We want $P(X_{t+1}|e_{1:t+1})$, to find this we can apply Bayes' rule to get $\alpha P(e_{t+1}|X_{t+1})P(X_{t+1}|e_{1:t})$ that is we update the probability for the previous prediction with the change of seeing our evidence.
	For $P(X_{t+1}|e_{1:t})$ we can expand by marginalizing over $X_{t}$ (the previous time step). That is for we find the chance for every $X$ values given how likely it was for each previous state scaled by how likely they were. Finally giving $$\alpha P(e_{t+1}|X_{t+1})\sum_{X_t}P(X_{t+1}|X_t)P(X_t|e_{1:t})$$We can note that the final probability that is the probability distribution for the previous state given the percept sequence not including the latest percept is also a filtering problem. Hence we have recursion. The part after the sum in the prediction state and it updated by filtering each time step which incorporates the newest percept.

---
Describe how filtering and prediction works without going into the math. #flashcard #RA #ProbabilisticReasoningOverTime 
	The task for prediction is what is the chance for each value in the hidden state given the percept sequence for previous time slices. This can be found by asking for every possible current state what is the chance for every next state. This is given by the transition model. While the change of the previous state is given by filtering the prediction given the current percept.
	Filtering is performed using emissions model. We can get the change of each current state given previous perceptions (prediction) and so we can scale each of these by how likely they are with the current percept.
	Prediction and filtering cycle backwards recursively hence bottom our to the initial distribution in our model.
	
---
How is smoothing performed in a Dynamic Bayesian network? #flashcard #RA #ProbabilisticReasoningOverTime 
	Smoothing is to predict the probability of past states given the percept sequence up to date. We can calculate the probability of the past state given the percept up to it using the same technique as filtering giving us $P(X_k|e_{1:k})$. We we also need to update given future predictions. That is for every possible state at $k$ what is its chance it will give the next perceptions in the sequence. $P(e_{k+1:t}|X_k)$. This is expanded by marginalizing over the next $X$ in the sequence. So for every possible next state after the one we are examining we want to know how likely it is to give the state as $k$ and how likely it is itself aswell as how likely it is to give the next perception. These three parts are $P(e_{k+1}|x_{k+1})$ the likelihood for the next percept for some given next state (provided by the emissions model). $P(e_{k+2:t}|x_{k+1})$ the probability of the actual possible next state given the remaining percept sequence (which is just recursion) and $P(x_{k+1}|X_k)$ which is the probability of the next $k$ given the current $k$ (transition model). This is the backwards message part. Both the change of $X_k$ given the past percepts and future percepts can be multiplied together to give the overall probability.

---
Describe how smoothing without math. #flashcard #RA #ProbabilisticReasoningOverTime 
	We want the probability distribution of a value in the past given the percept sequence up to it and past it. So we need the probability given the past percepts before it and the probability given the future percepts. The past part is just filtering. The future part can be expanded for by looking at the distribution of the next state given the state we are looking at and the next percepts. Due to conditional independence we can now ignore the state we are looking at except to weight distribution of the past state we are looking at given the next state (from the transition model). The probability of the next percepts given the next state can be expanded as the probability of the next percept given the next state and the probability of the next state given the next percepts after the one already stated. The first part comes from the emissions model and the second part is recursive. It will bottom out when we reach the current state and there are no more percepts. The probability given the previous and next states can then be multiplied point wise to give the overall probability.

---
How can we find the most likely sequence? #flashcard #RA #ProbabilisticReasoningOverTime 
	The most likely sequence can be found using the Viterbi algorithm. They way this works is for each slice in time we keep track of which previous state would have been most likely to cause each possible state in the future. This works since no matter what the most likely future state must have come from one of the possible last states and it couldn't have been not the most likely one as otherwise the overall path wouldn't be the most likely. We keep track of the likelihood of the most likely path leading to each state until the end at which point we can choose said end point and trace back the path that would make it most likely giving our most likely sequence of states.

---
What is a hidden Markov model? #flashcard #RA #ProbabilisticReasoningOverTime 
	A hidden Markov model is a type of dynamic Bayesian network where there is just one hidden random variable and just one emission. It is also the case that the emission only depends on the currents state and the currents state only depends on the previous state. Any dynamic Bayesian network can be convert to a HMM by converting all the state variable to a single variable which is a combination of the other where the values are the possible combinations of the others.

---
How can the filtering and backwards messages be simplified in a hidden Markov model? #flashcard #RA #ProbabilisticReasoningOverTime 
	Every time we perform a filtering step we need to do two things. We find a prediction for how probably the next states values are given the new state and we weight that based on our next percept. Both these procedures are weighting hence linear transformations. So we can in code them into matrices. 
	The transition matric $T$ is a $S\times S$ matric (when we have $S$ states in the state) that for some cell $i,j$ gives the change of some $i$ state becoming the $j$ state. Hence a vector distribution can be taken in an weighted to give a new distribution. We can use the transpose of the matrix to update a message from the future. When we update with some perceptions taken into account we need to reweight the vector based on how likely the output is. We can use a diagonal matrix for each time splice to do this. It will take in some vector in $R_S$ and multiply each value by some number that is the likelihood of the perceptions given the state. This allows us to represent the filtering message as $f_{1:t+1}=\alpha O_{t+1}T^Tf_{1:t}$ and the backwards message as $b_{k+1:t}=TO_{k+1}b_{k+2:t}$

---
What are th parts of a Dynamic Bayesian network? #flashcard #RA #ProbabilisticReasoningOverTime 
	The parts are a collection of state Random variable. The interaction from one time slice to the next is captures by the transition model. There are also random variables we can perceive who values are conditional on the state variables. This connection is described in the emissions model or sensor model. We also describe an initial distribution for the state variables in the first time slice.

---
What is a transient and persistent failure in a sensor? #flashcard #RA #ProbabilisticReasoningOverTime 
	A transient failure is when a sensor gives inaccurate readings for a small amount of time. In this case the sensor may break for a couple of seconds but regain functionality thereafter. A persistent failure is when our sensor break for good. That is it never regains functionality and stays broken.

---

How can we quantify different error models purely with an emissions model? #flashcard #RA #ProbabilisticReasoningOverTime 
	The emissions describes how a perceived random variables depends on a hidden one. Or how a perception depends on the true state of the world. We can assume it is a true reflection of the world. That is its states gives an accurate reading of the real world. We can also give a *Gaussian error model* this accounts for small inaccuracies the likelihood of which can be describes by the variance of the gaussian curve. We can also distribute the error model however we like for example giving a small chance for a 0 reading despite the actual value being 5.

---
How can we model small errors in our sensors? #flashcard #RA #ProbabilisticReasoningOverTime 
	We can use a Gaussian error model that gives for each true state some likelihood to readings that don't reflect the true value.

---

How can we model a transient failure in our emissions model? #flashcard #RA #ProbabilisticReasoningOverTime 
	Our emissions model can describe how likely each perception is given some true state. Therefore we can account for transient failures by giving adding a small chance for completely wrong readings. We may already use a Gaussian error model but this adds chance for failure.

---
What is the problem with transient and persistent errors when we don't account for them in our error model? #flashcard #RA #ProbabilisticReasoningOverTime 
	This can lead to our agents perception of the world shifting drastically depending a simple short failure in the sensor. This is as the agent trusts the sensor completely or assume it is at least close to the answer. If we also have a persistent error our agent will quickly trust a failed sensor more than what is reasonably expected given the transition model.

---
What is the problem with persistent errors even when we add probability mass for transient errors in our model? #flashcard #RA #ProbabilisticReasoningOverTime 
	Our agent may not trust a sensor that shifts completely out of the blue but if the sensor stays broken it may trust it over time as it isn't shifting. The agent cannot understand that the sudden shift in sensor reading may suggest erroneous results as this isn't modeled.

---
How can we model for persistent failure with a sensor? #flashcard #RA #ProbabilisticReasoningOverTime 
	We can add a new state variable which the sensor also depends on that describes a brokens sensor. If there is no chance of the sensor unbreaking itself. Then the agent will come to not trust the sensor readings. This leads to its belief in any state deteriorating over time.

---
What is the simples way to perform inference in a DBN? #flashcard #RA #ProbabilisticReasoningOverTime 
	A DBN is just a Bayesian Network so we can unroll it over time and use any inference methods for a regular bayes network.

---
What are the problems with just unrolling a bayes network? #flashcard #RA #ProbabilisticReasoningOverTime 
	Just unrolling a Bayes' network means its size and complexity grows with time. This means any agent using this method will either get more inaccurate or slower over time.

---
What is a better method than unrolling for Dynamic Bayesian Networks? #flashcard #RA #ProbabilisticReasoningOverTime  
	We can keep track of our previous belief state or belief distribution over previous possible states. This can be describes as a factored representation that can be passed through variable elimination.

---
What is the problem with using standard approximate inference in a Dynamic Bayesian network? #flashcard #RA #ProbabilisticReasoningOverTime 
	If we use approximate inference our future samples will depend on our previous samples. This way over time inaccuracy will grow and we will no longer be able to trust our inference. This is solved by particle filtering.

---
How does particle filtering work for inference in DBNs? #flashcard #RA #ProbabilisticReasoningOverTime 
	This idea takes care of growing inaccuracy in approximate sample interference. The idea is instead of just keeping a number of samples flowing through our network we weight and resample based on how likely previous samples were. This allows our system to pay more attention to the parts of the DBN which are most likely to represent the true world state. Hence more accurate results are achieved.

---
