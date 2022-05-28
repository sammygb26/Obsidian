What are the key concepts needed to understand reinforcement learning? #flashcard #MachineLeanringMIT #ReinforcementLearning
	Reinforcement learning is make to be similar to the way humans. Learn we have some agent (our network) and it acts in the environment (chooses actions) then senses and gets rewards.

---
What is the total reward, what is it called for some timestep t in a reinforcement learning setting and what are the variations on it? #flashcard #MachineLeanringMIT #ReinforcementLearning 
	This is called the Return and is equal to the sum of rewards past some timestep $t$. We can also have a discounted total reward which is equal to a weighted sum where the further in the future we go the more we discount the rewards. Each further timestep is a higher power of the discount factor $\gamma$.

---
What is the Q function in reinforcement learning? #flashcard #MachineLeanringMIT #ReinforcementLearning 
	The Q-function can be thought of as some function that takes in a current state and an action and predicts the expected reward that will be achieved in the future. The is the expected total reward.

---
What is the policy of an agent in reinforcement learning? #flashcard #MachineLeanringMIT #ReinforcementLearning 
	The policy of an agent in reinforcement learning can be through of as a function taking in some state our agent is in ang giving the best action to take that will maximize the total reward after this point.

---
What are the two ways for a reinforcement learning agent to learn? #flashcard #MachineLeanringMIT #ReinforcementLearning 
	The two ways are policy learning and value learning. In value learning we attempt to learn/model the Q function. While in value iteration we attempt to learn the policy function.

---
What are the two forms of value learning networks? #flashcard #MachineLeanringMIT #ReinforcementLearning 
	We can have a network that learns the function directly therefore taking in an action and a state. Or we can have a model that takes in just a state and outputs all the expected return for each action at once. The second is preferred as it is more efficient as it doesn't have to be run for all possible values.

---
How can we train a reinforcement learning value based model? #flashcard #MachineLeanringMIT #ReinforcementLearning 
	We use a Q-loss. This takes in our best case reward which is current reward plus the max Q value possible moving on. Then we take the difference between this and our predicted Q value. Networks using this are called DQNs or Deep Q Networks.

---
What are the downsides of Q-learning? #flashcard #MachineLeanringMIT #ReinforcementLearning 
	The *complexity* grows with the number of possible actions therefore we cannot handle continuous action spaces. We also cannot learn *stochastic* random policies since our Q function maximization requires on know action state rules.

---
How do policy learning based learning models work? #flashcard #MachineLeanringMIT #ReinforcementLearning 
	Policy based learning models work by estimating the probability of taking each action given a state instead of just how much each state will reward. We then sample from this distribution to give some action.

---
How can policy learning methods work with both discrete and continuous probability distribution? #flashcard #MachineLeanringMIT #ReinforcementLearning 
	We can output instead of just a series of probabilities a number of variables defining a continuous probability distribution like a normal distribution.

---
How can a policy learning based model be trained? #flashcard #MachineLeanringMIT #ReinforcementLearning 
	We run our agent in the environment. When it stops running we can take the negative log likelihood for each action take multiplied by the total reward. This way small probabilities for bad actions are rewarded, large probabilities for large rewards are also rewarded as well as the respective inverses.

---
What problems does reinforcement learning come into when we take in into the real world/ #flashcard #MachineLeanringMIT #ReinforcementLearning 
	The real-world is stochastic aswell as being not entirely observable. Our agents will have to deal with this randomness. We also cannot always fail in the same way as in a simulation.

---
