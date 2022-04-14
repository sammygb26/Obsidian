# Requirements Engineering
A **software requirement** is a property that must be exhibited by something in order to solve some problem in the real world. The requirements reflect the **needs** of the different people a various levels of the organization (different expertise, contradiction, social aspect). You need to understand all the different people. **Requirements engineering** is the systematic handling of requirements.

## Types of Requirements
**Functional requirements** are also called **services** and **Input Output requirements**. Then there is **Non-functional requirements** this is how it should do it, how reliable should it be, how fast should it be, how quickly it should be developed, what standards it should conform to, ease of use. These are often called **ilities** since they are for things like efficiency, security, portability usability etc. **Non-functional** requirements are often shaped by non-functional rather than functional. Functional requirements can be worked around by non-functional always impacts the actual use of the software. Note its not always clear cut for example security may start as a non-functional requirement but if it became a feature how this was implemented it would be a functional requirement.

## Requirements vs. Design
Requirements avoid **what** is desired and now **how** what is desired should be realized. Requirements come form the problem the design is part of the solution. Requirements are much higher level than the design. This is since we need to remain flexible and only have requirements we actually need for out project.

## Stakeholders
**Requirements** are usually relevant to multiple *stakeholders*. **Stakeholders** are "any person or group who will be affected by the system, directly or indirectly". This could go form people who use the software but who it actually affects even through other people. Anyone who is affected by it. For example developers are stakeholders since the software will definitely affect them and everyone should be taken into account. Example are end users, who is paying for the software, government regulators, system architects, software developers, software testers.

## Requirements Engineering [[Activities]]
**Gathering** -> finding your requirements, **elicitation**
**Sorting out** -> Analyze them
**Writing down** -> Specification (depends on process)
**Checking** -> Validation

Many of these [[Activities]] will be done in different order and each one may take a different amount of time and may be done in different ways depending on [[Processes]]. Requirements is critical and is the **major source of project failure** according to Standish CHAOS reports. This is one motivations for agile process and its not as important for requirements engineering up front as you can go over the requirement over and over again. Then it is much cheaper to go over each agile step rather than the whole project like in a plan-driven process.

## Gathering (elicitation)
The requirements can come from many sources. **Goal** the main goal of the software the end users want, this will give a very high level requirement for the software. **Domain Knowledge** essential for understanding requirements that come from what field the software will be deployed in. **Stakeholders** vital but they can be fickly and so it is hard to get a clear idea of what they really want early in development. **Business rules** regulations for the area the the software will work in, rules the software should follow. **Operational Environment** how well it works, fast or performance. **Organizational Environment** how does software fit in the existing practices.

### Techniques 
**Interviews** -> We ask stakeholders what they actually want. Can be challenging if we don't understand the domain language being spoken and also information that seems obvious may be left out by the people we are interviewing. There may also be limited time. It is important to be **open minded** and try to get as much out of people as possible and remove yourself. **Prepare starting questions** like what the software is actually trying to change,

**Scenarios** -> There are about putting the system in a given context and seeing how it is expected to work. You can then ask **what if** and **how would you do this** questions. It works like a story so is easy for stakeholders to understand.

**Prototypes** -> Can include screen mock-ups, storyboards and early versions for the system can give stakeholders and idea of what they **do** and **don't** want. They are more really then scenarios and so you get higher quality feedback.

**Facilitated Meetings** -> Get a discussion going with multiple stakeholders in a structured manner to understand where there are conflicts and what people are willing to give up knowing other people needs and requirements. A trained facilitator is needed as some people will dominate the discussion and everyone needs to be heard.

**Observation** -> You need to understand what people are actually doing, this will give you the real detail of what people do and want. This is an immersive method where you actually watch people and it can take a lot of time and be expensive. It helps surface things that are complex and that people are omitting.

## Analysis
From elicitation we will get requirements that are in conflict. The requirements found may also be too large so we need to scale back the requirements. **Analysis** is where we whittle this list down and we want to sort and filter this list to get to a version without conflicts and has priorities and groups things together, has some structure. We want a list that **will** be realistic so has to be doable in terms of tech and budget.

## Specification
Requirement can be recorded in various ways for example with informal means, hand written cards with user stories in agile development. You could use structured English like 
![[Pasted image 20220129112745.png]]
Where each section has a high level requirement and lower level details are subsections. You can also have use case models with supporting text. Then you can also have math based language for a more formal specification, like propositional logic. This can be useful if a system is very critical the system **needs** to be accurate and not fuzzy/vague.

## Validation
**Consistency checks** need to make sure there aren't contradictions. **Completeness checks** need to make sure all take holders have been taken into account. **Realism Checks** will it be possible to implement (talk to your own company, budget). **Verifiability** is it possible to test that the requirements have been met. In this case we need to test non-functional requirements as well so we need to define them in terms of measurements we can take of the system performance for example.