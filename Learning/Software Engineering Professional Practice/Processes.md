# Processes
The job of processes is to specify the order of out activities. What we want from our activities and how does this feed into later activities. How do we organize to perform activities (people). Then how arrange people and resource to perform activities. We need to plan our properly to make sure we complete our goals. Need to reduce risk as development goes on so our project doesn't fail. Also takes in monitoring where we keep track of our development to make sure things aren't going wrong. The process interrogates itself to find out what's going wrong and so can adapt to overcome difficulties. [[Process Models]] are designs for processes but are ideals and will be adapted, mixed and matched.

## Plan-driven
In plan driven processes all activities are planned out in advance and progress is measured against this plan. We try to stick to the plan as we go on. This does make it hard to react to change however.

##### Characteristics and Applicability
-Make a plan and stick to it
-Thorough documentation as project goes on (helps new team members or people moving around project space)
-Use of modeling ([[UML]]) as we go on (helps with communication)
-System is specified in detail before development begins
-Cannot react to change since plan is so absolute (costly to fix)
-Most appropriate for long lifetime, critical and embedded systems (security concerns must be tested for so hard to hack it together)

## Agile
Laid out in *agile manifesto*. **Individuals and interactions** over processes and tools (we car more about the users interaction rather than how the system works). **Working software** over comprehensive documentation (its better it works than it doesn't but is documented). **Customer collaboration** over contract negotiation (its more important everyone gets what they want rather than what was specified). **Responding to change** over following a plan (going with the flow more). The workflow is shown below.
![[Pasted image 20220124121055.png]]
We look at what we need to do. We find from the unfinished features the most important features. We then plan to implement this along with the engineers to make an honest plan. There is **daily communication** between customers and between team. There is constant inter team communication so that everyone's expertise are used. There is team autonomy in this system. In the end there is **working software** finished that has solved the problem. You can then get feedback on this and repeated.

##### Principles
1. Customer satisfaction by rapid delivery of software the customer wants
2. Welcome changing requirement even late in development (prepared for change)
3. Working software is developed frequently (weeks rather than months)
4. Working software is the measure of progress (rather than progress in the plan)
5. Sustained development able to maintain a pace rather than sprint for the finish (not overworking people)
6. Close co-operation between business people and developers (people over documentation, minimize wasted time rather than scrutinizing design documentation)
7. Face-to-face conversation is best communication (teams are co-located so they can communicate effectively)
8. Projects build around motivated individuals who can get a job done (developers are trusted not managed)
9. Continuous attention to technical excellence and good design
10. Simplicity (maximize what is not done) don't overcomplicate it and leave the bloat out
11. Best requirement and designs from self-organizing teams
12. Regular reflection on process and tuning behavior (making sure you are doing good work and make sure the process it working)

##### Applicability
Best used for low criticality systems since the system wont work to a exact specification (security). Better for senior developers since required to make decisions while in plan based junior developers can follow a plan but do not make decisions like in agile. Works well when change is often (unlike plan based where change is hard), change is embraced in agile. Plan driven works well for large numbers of developers, having a plan can keep everyone working together and uses the people effectively. However agile require communication between people so it can be harder to scale. Agile demands a culture of change since change is required but a hierarchical culture works better in plan based since need to have top down orginization.