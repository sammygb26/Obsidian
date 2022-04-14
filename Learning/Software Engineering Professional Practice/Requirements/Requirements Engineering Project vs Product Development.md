# Requirements Engineering Project vs Product Development

## Projects
In **projects** the requirements are given by a contract the system is made for one paying customer, like business systems that will work for a long time. **Plan-driven** in the best choice since what is required wont change as it is in the contract. Pure agile will not work in this case since agile isn't build to follow a contract and instead tries to communicate with the customers, agile will also not follow a deadline very well.

## Products
In **products** the developing team decides what the features are. These are usually generic and work for many customers. There is no main customer you need to make a product that is attractive to the customer and is better than the coopetition. You need to deliver to market quickly and react to changes. You can talk with potential customers and continue to talk to them and listen to keep them. This all means it works best with **agile** as you need to talk to customers and understand their needs.

#### Features
We can identify **features** rather than requirements since its not required by a paying customer is it something that entices potential customers. We can stick to requirements as a convention since these might as well be required for successful software.

#### Elicitation
Interview, surveys and meetings are expensive so small companies may do more informal techniques instead. Companies may also be hostile to new change since the decision to change software might hurt employees for example automating jobs.

#### Personas
these are imagined users that give a type of use for our product. These should be cross checked against actual user data. Personas in general need, personalization (name, personal circumstances, stock photo) to make it more relatable, job-related, education (background, level of skill and experience) and relevance (motivation for using the product what they may want).
![[Pasted image 20220130120821.png]]
We personalize with a name and a story, we talk about her job and her needs, we talk about education, her level of technical skills out system should aim to help her and we are talking about the motivation for us the relevance.

This is all about eh priorities of the users and what they want and it helps the team relate to the users and have a shared vision of the software keeping people working together. It also motivates developers since they have to empathies with the personas. Should be careful not to have too many as there will be a lot of overlap in terms of needs and priorities (stick to about **5**).

#### Scenarios
There are narratives explaining what a user wants to do and how they might accomplish them. These are from the perspective of users and what they want. They can come from user interviews but also you can use **personas** in the scenarios. We want scenarios per role what the role will do. Instead of as in use cases we would use more high level scenarios with less detail and with more narrative and context.

We need a brief statement of the overall objects, we want references to the persona involved, we want what is involved in doing the activity, we may also need what cannot be done by the current system and we want one way the identified problem may be addressed.
![[Pasted image 20220130121648.png]]

A way to make **scenarios** can be to start from the personas and imagine problem they might have that our product could solve. We can get different people to work on different scenarios and everyone can come together to refine and discuss them.

**Advantages** -> Way of brainstorming with the team what the system should do
						The help reach a shared view of what the system should do
						Facilitate communication and stimulate design creativity
						Easy to write and understand so users can get involved

**Disadvantages** -> Not specifications so may be incomplete and lack detail
								Might also overlap.
								Recommended using 3-4 per persona so things don overlap

#### User Stories
There are more detailed stories given in a concrete way he things that a user wants from a system. They originate in agile development. They are more rigid in their layout.
![[Pasted image 20220130122517.png]]
This gives us simple what they want. Here are some examples
![[Pasted image 20220130123210.png]]

**Advantages** -> Helps with getting idea for what the system should do
						Like personas help reach a shared vision
						Help communication and get better design
						Can be used for planning iteration cycle if detailed enough

**Disadvantages** -> Not specific, may be complete or lack detail

Scenarios are more natural and easier for users to understand they can provide context for actions and ways our system might be used.

#### Obtaining Requirements
Requirements need to be independent, make sense and actually help users. There are many trade-offs.
								Simplicity <-> Functionality
								Familiarity <-> Novelty
								Automation <-> Control

We want to avoid **feature creep** where we get more and more requirements making it impossible to develop. We need to examine scenarios and look for **active verbs** (like use, send, update, open). We want to especially look what is done. We need to think about what supports these actions on the system and then we think about implementation of this. User stories can immediately suggest requirements.

We need to represent in a simple way and add detail later as not to slow us down.

**Input/Action/Output** -> We have some input then some action we want to do with the input and what output we want form that.
**Description/Constraints/Comments** -> We can give this as a narrative, a series of statements using the notation {action} the {result} {by/for/of/to} {object}, or a set of user stories. This list should be agreed upon by the team.

The requirements should be shared and discussed and agreed with the team.

All these tequniques look at user needs so can lead to a product that is accepted by users, they do lock in how we work now by only showing how users do things now. So we make useful software but not innovative software. For this we can add additional requirements that are innovative.

ddeclare