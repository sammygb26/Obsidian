# Use Cases
It is important when writing a description of a systems behaviors from the viewpoint of the users. This is since they are the ones using the system. We can break this description down into units each triggered (with interaction) by some user. **Use cases** describe these chucks of behavior of a system. Use cases describe **functional** requirements but can include **non-functional** elements.

**Use case** -> *A test or coherent unit of functionality which the system is required to support*

Use cases have **actors** which are roles that interact with the system either job roles like a cashier or system roles like a bank card system. There are two types of actors **primary** and **secondary**. **Primary Actors** have a goal and initiate interaction with the system, while **Secondary Actors** do not though they do still interact with the system.

A use case is described by a main sequence of steps (path) necessary to achieve the use case's goal (although there can be backups if not everything goes to plan). Each of these possible paths is a **use case instance** or a **scenario**.

**Example**
![[Pasted image 20220129143026.png]]
The order isn't fixed and some of the steps are very high level but we want to keep this flexible to not constrain development. It isn't written formally to increase flexibility and make it easy to communicate. Extensions can also be used to make the path more flexible.
![[Pasted image 20220129144110.png]]
You can also use a template to fill out to make a use case
![[Pasted image 20220129144409.png]]

## Connection and Scope
A use case can have different levels of detail depending on where we are in development process. It may refer to other use cases for more information of particular steps. It may also describe different scopes like a system of system a single system or a component of a system.

## Diagrams
[[UML]], Unified Modeling Language can be used to set out use cases and give an understand of the system overall. This is done with [[Use Case Diagrams]].

## Requirement Engineering Organized by Use Cases
You can use use cases to structure how you go about requirements engineering. They can help identify what you system needs to do and who will interact with it. You can then use this information for elicitation and understanding use cases the actors will have. Use cases then set a baseline that must be reached by the system we can build requirement that allow us to perform the use cases. It can also give non-functional requirements such as security.

## Advantages and Disadvantages
This can help with **design validation**, where we can walk through designs with our use cases to check if the classes provide the needed functionality and that the interaction are as expected. They can help with testing to help us find good system tests from what the system needs to do.

You can go too far with describing steps witch can hinder the designer. You can also identify supporting actors too much when they are not needed. You don't want to make design decisions that will limit what you can do later you want to keep it flexible. They can also loose site of what is actually needed in implementation and so make a system that will be hard to develop. Also use cases miss automatic functionality since there is no primary actor to use the system.