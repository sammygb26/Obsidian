# Architectural design
An **architecture** is the organization through the components of a program and how they relate to the environment. It is very hard to change as it effect so many features. It can therefore be described as what isn't changed as our project evolves.

A **component** is a named software unit that implements coherent set of functionality or features or a collection of one or more services that may be used by some other components. A **service** is a coherent unit of functionality. A **model** is a named set of components which have something in common like providing a related service.

Architecture is important since is has a fundamental influence on non-functional requirement. Like our speed relying on our system and how things work together. It also affects the complexity of the software and can make our project less maintainable. There are many tradeoffs to be made here and it depends on the system we are developing. A lot of non-functional requirements will counteract each other and so it is hard to develop.

## Process
Architectural design involves creating a description of the architecture showing components and their relationship. We need to pay attention to many things such as:
-> Non-functional requirements
-> Product lifetime: long lived should be able to evolve.
-> Software reuse: saves time, constrains architectural choices.
-> Number of users: if very variable, architecture should allow quickly scaling up and down
-> Software compatibility: constrains architectural choices.
-> Planned schedule, team capabilities, budget etc.

## Trade-offs
Maintainability vs Performance -> having fine grained components will increase maintainability but will reduce performance as there will be much more communications overhead etc.
Security vs Usability -> Layers of components can help with security however these layers make the program hard to use.
Availability vs time to market and cost -> availability is how much your site is always available at all times. Redundant components help with availability, but at increased cost, complexity error proneness.

## Main questions 
1. How should the system be decomposed into a set of components,
2. How should the components be distributed and communicate.
3. What technologies should be used in developing the system.

## Steps

**1) Decomposing the system into architectural components** -> We start with high scale components and break them down into smaller components.
We want to localize relationships to make sure there aren't to many connections making our project horribly complex.

**-- Reducing Complexity --**
**Separation of Concern** We want to reduce shared dependencies so components work on their own. We want to make sure components have but one job since this will make the design more understandable.
**Stable Interfaces** hiding important implementation details behind some interface can be useful since it allows us to change those implementation details later without changing the project.
**Implement Once** We want to make sure we only implement something once.

**Layered Structure**
A basic way to apply the guidelines is with a **generic layered architecture** all components are organized into layers. Each layer then holds more low level details going down. For example the bottom layer will be database management with the top layer being the user level interface. Each layer only interacts with other layers through API interfaces so that the implementation is of no concern. The low level layers provide more general functionality so that the high level layers abstract away and we get more expressive functionality.

**2) Distribution and communication** This is used to define how servers will be distributed and how components will be distributed to them. An example of this is the client server architecture.

**Client Server Architecture** The idea here is that you have one server and many clients. The servers provide a service the clients request the service and information is sent to the clients for them to make use of. The servers have to process the information and send it to the client.
![[Pasted image 20220204100533.png]]
**Client Server Architecture for web-based and mobile software products** The idea here is we have many clients and the all request responses from Servers. We have a load balancer that balances the loads coming in to each server.

**Multi-tier client server architecture** Here there are multiple layers of servers. There is a client server architecture where the servers share a database.
![[Pasted image 20220204101735.png]]
This can woke well for structured data where you want all servers to be updated at once or if you have many local servers. This is also a *monolithic* architecture with large components.

**The Service-oriented architecture** Client-server system with lots of servers (not monolithic). Services are stateless so can be relocated, distributed, migrated between servers. This is a good choice if components need to change often, if there is a need for scalability and resilience to failure.
![[Pasted image 20220204102329.png]]
Here we have a web server and then a web-service gateway which is in charge of picking the right service for the client.

**Peer to Peer** in this architecture you have a lot of clients (called peers). There is not central server all the peers interact with the others directly. An example of this would be blockchains. The peers all put up some of their resources to help the network.
![[Pasted image 20220204102651.png]]

**Message bus architecture** this looks similar to a client server architecture but it isn't the same. All the clients but messages on the bus and the clients wait for messages and respond to them. The difference is the bus doesn't do computation on the bus is simply stores messages.
![[Pasted image 20220204102917.png]]

**3) Technological Considerations** Technologies need to be picked as they will affect the possibility of different architecture designs (just expensive / difficult)
* **Database** -> Relational or NoSQL. Relational is better if non structured or needs to be updated (also big data), NoSQL if data is simply stored and retrieved.
* **Delivery Platform** -> browser or mobile, changes power available so client or how expensive development is.
* **Server** -> using cloud and if so what cloud provider.
* **Use of Open Source Software** makes development cheaper but limits possibilities.
* **Development technologies** mobile development toolkits, web application frameworks, advantages (gives you a leg up, not starting from scratch)/disadvantages(constrains architecture to what was already imagined).