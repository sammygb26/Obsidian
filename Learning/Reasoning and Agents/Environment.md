# Environments
[[Agents]] exist in environments and it is their ability to change these environments that allows them to peruse goals and it is the nature of these environments that affects the way they will make those choices.

## Task Environments
These are essentially the problems to which [[Agents]] are the solution. They are defined by **PEAS** or Performance, Environment, Actuators, Sensors. [[Agents]] themselves are defined by their Performance measure, Environment, Actuators, Sensors as well as their behavior.

##### Performance measure
This is the measure of how well the the goal is completed and defines the goal of our agent.
##### Environment
This is the world the agent will interact with and perceive.
##### Actuators
This is what the agent will use to interact with the world. Essentials the tools it has to complete its goal.
##### Sensors
This is what the agent will use to perceive its environment and what it can use to help it decide what actions to take through the actuators.

## Properties of Task Environments
We can categorize our environment so we know what to make assumptions about and what not do to focus our development of our decision making process.

#### Observability
This is whether we have a complete or incomplete view of what is going on in the environment. So in chess the environment is **fully** observable since we can see all pieces but in say for a human the world is **partially** observable since we aren't omniscient. Or it could be if there is noise in our sensors so we can't trust them completely.

#### Deterministic 
This is whether we know the outcome of our action that we take. It is either **deterministic** we know what will happen or **stochastic** we don't know for sure what will happen. If we don't know what will happen only because we don't know the environment fully it is perceived as stochastic. So a deterministic game would be connect 4 where you know where your pieces will go a stochastic game would be Plinko where you pieces bounce around and you don't know where they will end up.

#### Sequential
This is whether the past actions affect the future ones. An environment is **episodic** if the previous doesn't affect the next ones. Think the mail sorting robot its previous actions don't affect the following ones.  An environment is **sequential** if the following states depend on the previous ones for example a cross word where the decisions made will affect what decisions you can make in the future or the affect of those decisions. In this type of environment planning may be required.

#### Static
This is whether the environment is constantly evolving and changing as the agent exists. It is **static** then it only changes when the agent makes an action. In a **dynamic**  environment the agent is continuously asked what it wants to do and the environment continues to change with or without the agent choosing an action.

#### Discrete
This is whether the environment changes in discrete chucks or if time flow continuously. An environment is **discrete** if percepts, actions and episodes all happen in discrete intervals like moves in chess. An environment is **continuous** if action happen continuously and flow with time.

#### Number of [[Agents]]
This is just the number of agents so either **single** there is just the agent we are modeling. Then there is **multiple** agents where we may model the other agents to predict their actions. They can also act in a **competitive** or **cooperative** manor.

This all gives two properties **benign** where the environment if fully observable deterministic, episodic, static, discrete and single agent. But a **chaotic** environment is partially observable, stochastic, sequential, dynamic, continuous and multi agent.

-- Reading *Artificial Intelligence with Modern Applications (3rd edition)* Chapter 2

[[Environments Questions]]