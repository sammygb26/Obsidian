# Environment States
States are what our [[Agents]] can be in. An agent's job is to navigate states to the **goal state**. 

## Representation of States
There are three ways to represent stating in general **atomic representation**, **factored representation** and **structured representation**.
* **Atomic Representation** -> In this each state is indivisible a state has no relation to another state. Each one is wholly different. This allows the different states to be graphed our with the edges being actions. This graph structure allows [[Reasoning and Agents/Search/Search]] to work well for this type.
* **Factored Representation** -> Environment is also described by variables and attributes in states. In this case two states can have these variables and attribute in common.
* **Structured Representation** -> In this the state is described not just by numbers and attributes but also by objects and so defined explicitly.

Going down this list we start of with very unexpressive representation and reach a very expressive one.

[[Environment States Questions]]