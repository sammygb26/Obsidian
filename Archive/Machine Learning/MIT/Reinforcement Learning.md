# Reinforcement Learning
Reinforcement learning is a way that humans learn.  Merging this with humans is a way to get away form the paradigm of our algorithms learning based on example rather than experiencing truly. Hence we can get away from annotation and human intervention. We have already looked at *supervised learning* where we have some data $x$ and label $y$. We want to approximate the function $x\to y$. We also have *unsupervised learning* where we have some data $x$ and we just want to observe the underlying structure and generate its own labels or labeling metrics. In **Reinforcement learning** we just get the data in terms of state-action pairs. We then attempt to maximize some reward over many timesteps.

#### Key Concepts
An **Agent** is some entity that can take actions. Our algorithm is essentially our agent as it chooses the actions and takes in percepts. We have an **environment** that the agent can take *actions* to affect. **Actions** can be taken by the agent in the environment it chooses form an *action space*. We then get observations or a **state** from the environment to update our plan. We also get a **reward** that measure our success or failure.

![[Pasted image 20220526183759.png]]

The *total reward* or **Return** is the sum of all rewards that the agent gets after some time $t$.$$R_t=\sum_{i=t}^\infty r_i=r_t+r_{t+1}+...+r_{t+n}+...$$So this is the total reward going forward form $t$. We also have a **discounted total reward**. Equal to $$R_t=\sum_{i=t}^\infty\gamma^ir_i$$This way the reward become less weighted further in the future. The *discount factor* $\gamma$ is $0<\gamma<1$ for this case.

We can define the *Q-function* as the expected total future reward an agent in state $s$ can receive with some action $a$. To better action better Q-function and worse action worse Q-function. $$Q(s_t,a_t)=\textbf E[R_t|s_t,a_t]$$We want to construct a *policy* $\pi(s)$ that takes in some state and return the best action to take. So we can given the Q-function define our best policy $\pi^*$ as$$\pi^*(s)=\underset{a}{\text{argmax }}Q(s,a)$$So our policy will take the action maximizing our total reward expected. This gives two options for reinforcement learning *value learning* where we learn $Q$ and *policy learning* where learn $\pi$.

#### Value learning
For this we will need to examine the *Q-function* more. We can take the example of breakout where we try to prevent a ball from exiting the screen like in pong. In this example the Q-function would tell us the expected reward from a response to a state. Even in this simple example which actions are good or bad isn't simple to understand even for us. We have two main options for generating Q-functions with a deep learning model.

![[Pasted image 20220526185955.png]]

We either learn the Q-function directly so we take in a state and an action giving a result or we output a number of values one for each possible action in the action space. The second is  *more efficient* as we don't need to loop through the model for every action and can just take a max of the output vector to find $\pi$.

###### Training
We can think about the ideal case for or Q-function. This would maximize return with our return. So we define our *target* as the discounted max reward we could get from any action. $$r+\gamma\cdot\underset{a'}{\text{max }}Q(s',a')\hspace{64pt}Q(s,a)$$We can define our loss as the difference squared between these two values. This makes sense as in the end we assume our Q will pick the best values.  This is called **Q-loss**. The left part is what our network is predicting while the other part is our target (best case scenario). $$\mathcal L=\textbf E\left[\left(\left(r+\gamma\cdot\underset{a'}{\text{max }}Q(s',a')\right)-Q(s,a)\right)^2\right]$$The output form our network will be our Q values we use this to pick our action giving us a new state. These are called *DQN* or *Deep Q Networks*.

![[Pasted image 20220526191423.png]]

The *downsides* of Q-learning are:
1. **Complexity** can model scenarios where the action space is discrete and small. So we cannot handle continuous action spaces.
2. **Flexibility** policy is deterministically computed from the Q function by maximizing reward so we cannot learn stochastic (random) policies.

This lead to a new class of RL training algorithms called *policy gradient methods*.

#### Policy Learning
Here we are modeling the function $\pi$ then we can just sample given our state to maximize our reward. The output isn't the reward (which we don't really need) but the probability we should choose that state.

![[Pasted image 20220526192141.png]]

We can just sample from the policy distribution we have been given. We can handle continuous action spaces by outputting a *continuous* probability distribution. In this case we output a mean $\mu$ and variance $\sigma^2$ that define a continuous distribution to do this.

![[Pasted image 20220526192331.png]]

An example of this would be a AI car outputting a distribution of steering wheel angles. What we then do is we initialize our agent into the work (with rando values). It will inevitably crash in which case we look at the action close to the reward and decrease the probability of taking those actions. The ones far from our reward we increase the probability.

![[Pasted image 20220526193438.png]]

Then when we repeat the agent learns to act better. So taking in only a reward signal the agent is able to parse out the way the world works. But how do we change the *probabilities* (in the red and green zones)?

Our agent outputs a log-likelihood for every action. This is multiplied by the discounted reward given for taking the action. Actions with high reward will be favored and ones with low reward will be punished.$$\text{loss}=-logP(a_t|s_t)R_t$$We can plug this into *gradient descent*.

#### Real Life
The main steps for this will be the same as for the car. But in the real world the state isn't exactly known the world is somewhat unobservable. For example in the real world we cannot just wait until the policy terminates. For example with real cars. We can use *high quality simulators* in hope that the results will transfer.

[[Reinforcement Learning Questions]]