# Activities and Processes
We will look at the different activities that are part of software development. Processes specify the order the activities must be taken in. The history of SE is important to understand how the processes have come about. We will go into plan driven and agile processes for software development.

## Activities
There are many activities in software development such as Requirements Capture]], [[Design]],, Construction/Implementation, Testing and Debugging, Maintenance/Evolution. 
	
#### **Requirements capture** 
Evolves knowing what the program must do (not how). This matters to the stakeholders people who have a stake in the software (users, sponsor) influence by stakeholders. Need to understand the stakeholder's requirements for the software. They may have different possible contradictory requirements. Need to resolve conflicts. Need to priorities what you need the most or first. Also need to manage evolving requirements with what stakeholders want or the world changing.

#### Design
how will we accomplish the requirements *(how instead of what)*. Higher level than code. So involves [[Modeling Language]], like [[UML]]. This is planning the solution not actually working out implementation. We need to make sure our design is **understandable** (for team members and new people). Need to be **robust to requirements change**. Need to futureproof and make it secure. Need to make an efficient solution that wont work poorly and be fast. Need to be able to divide the work effort and break it into parts that can work together **buildability** so you can be on time and budget.

#### Construction/Implementation
Need a detailed design more than just coding (more deep than design). About coding and writing it up also writing test to ensure the code works. Managing code evolution so being able to make version (version control). Then writing good documentation for developers to help with understanding. The problem here is scale the more there is the harder it gets. You will have to work in small chucks without understanding whole system.

#### Testing and Debugging
Multiple levels from will this crash a program to how do the users interact with some code. Debugging works out things that aren't working right or even not right for user requirements (what they want). Need to understand the cost of debugging since it will take a lot of budget. Depending on your plan for development this will happen at different stages. Example: test driven development you write them first then develop the code to solve them.

#### Maintenance/Evolution
Any post release change, fixing bugs, enhancing functionality, coping with changing world/market (things become obsolete not supported think Flash). Improving maintainability so that you can continue to maintain for a long time without the program becomes complicated. Software rot comes when you hack on top of hack and a well designed program becomes poorly designed and unmaintainable. Usually takes up more money than actual development. Need to design with this stage in mind. When has the rot gotten to far (replace or refactor).