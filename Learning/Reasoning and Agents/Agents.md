# Agents
The main idea behind an agent is that they have agency. They interact within [[Environment]] and have goals and use these to make decisions; taking in the sensations through the sensors they decide what actions to take to change the environment to affect what is happening and so accomplish their goals.
![[Pasted image 20220118141952.png]]
Sensing is done through sensors either virtual like files or messages or physical like a camera or a microphone. An agents **percept** refers to the perceptual inputs into that agent. Then its **percept sequence** is the complete history of everything the agent has perceived. Acting is done through actuators either virtual or physical like legs or hands and so on. An agent is described by the environment it acts in the goals it peruses, the percepts it reads from and the actions it can take to change the environment.

*Example* : **mail sorting** the goal is to sort a stream of letters on a belt. The sensors may be camera that reads the address the actuators may be an arm that can push the letters on to the correct belt.

*Example* : **smart home** the goal may depend on the user and what they want keeping it a certain temperature at certain times be more efficient etc. The sensors could be energy meters, thermometers, cameras etc. The actuators could be heaters, lights etc.

*Example*: **autonomous car** the environment would be a road, the sensors would be cameras,  speedometers, fuel indicator, radar etc. Then 

An agent function takes in an agents **percept sequence** and returns the actions the agent will then perform. An **agent program** implements this function. 

## Types of Agent
#### Simple Reflex Agents
In this type of agent the actions only depend on the immediate percepts. For example a smart home of this type could just sense cold so turn on heaters. These have rule to tell them what to do and a fixed goal. This type of agent could be easily implemented as a simple lookup table however this type of agent is limited at it is impossible for more complicated [[Environment]]s to do this. It will be $n^t$ where $a$ is the number of possible states and $t$ is the number of previous timesteps. So for reflex agents $t=1$ so this becomes possible.
![[Pasted image 20220118171739.png]]
*Simple agent program*
![[Pasted image 20220118171912.png]]
Often reflex agents can get stuck in loops to overcome this you can use **randomized** actions.

#### Model-Based Reflex Agents
In this type actions may depend on the history or unperceived aspects of the world. They have some sort of model of the world. An internal world model in maintained within the agent. So the agent holds itself some idea of how the world evolves given its state and the actions the agent takes this is called a **model**. An example would be a smart hoover mapping out a flat. They need to learn the environment without it being hard coded in. These have  a model to tell them what to do, but again simple conditional logic tells us how to act.
![[Pasted image 20220118172752.png]]

#### Goal-Based Agents
Agents so far have fixed implicit goals in this case the goal can change for the agent. An example would be a cleaning made robot whose goal can change based on what the user wants. Or a driving robot where it goes at the same turn depends on its destination goal. The process the agent used can be sometimes simple however it can also be complicated the agent may have reason about how to accomplish a goal, the previous agents don't have goals they are just designed to fulfill them. This is done through [[Reasoning and Agents/Search/Search]] and planning.
![[Pasted image 20220118143648.png]]

#### Utility-Based Agents
Agents so have have a single goad at once. But agents of this type have to juggle goals. The **utility** is a measure of how 
well an agent is acting. An example of this is the autonomous car. It has to do many things get you to where you are going, stay safe, be quick, obey the law.
![[Pasted image 20220118173701.png]]

#### Learning Agents
The idea is that every agent so far has a given action plan what it does given a situation given a past and a goal will always be the same (based on rules, goals and model a utility and so on). But with a learning agent this can change as the agent experiences. So it could try to find poor strategies and find new ones for itself.
![[Pasted image 20220118173802.png]]
There are two parts split here the **learning elements** and the **performance** element. The first is responsible for making improvements on the performance element and second is responsible for making actual actions in the world. The **critic** provides information on how well the agent is acting this is needed as the percepts alone don't tell us about our success. The **problem generator** suggests actions that will lead to new and informatic experiences.

## Types of behavior
We can define how well an agent in performing by a **performance measure** which keeps track of the how well the agent is completing its goal. A **rational agent** is one that always does the action that it expects to maximize this performance measure.

Formally we would say *For each possible percept sequence, a rational agent should select an action that is expected to maximize its performance measure, given the evidence provided by the percept sequence and whatever built-in knowledge the agent has.*

Note we must say "expects" since it would not make sense to treat acting rationally as always making the best action since it is impossible to actually doing this without having omniscient. This could lead to agents that are truly more rational being seen choosing the wrong choice compared to a less rational agent since neither know the full picture.  An omniscient agent knows the actual outcome of its actions and can act accordingly; but omniscience is impossible in reality.

#### Information Gathering
In our definition of rationality we say an agent must act to maximize expected performance measure given its percept sequence. So take an agent crossing the road if it doesn't look both ways it has no reason to expect a car so it will cross but it could then be hit by a car. The idea here is that it isn't rational to cross the road if we haven't checked. To perform the most rational choices an agent must therefore gather information through **exploration**.

#### Learning
Since a rational agent must maximize expected outcomes to its goal it should also learn from performing actions that don't work out to its favor. This is so that in the future it wont do those action again even though it know they very may well not work out.

#### Autonomy
Autonomy of an agent is the level to which it relies on prior knowledge. It is **autonomous** if it doesn't rely on inbuilt knowledge an **non autonomous** if it does.

-- Reading *Artificial Intelligence with Modern Applications (3rd edition)* Chapter 2

[[Agents Questions]]