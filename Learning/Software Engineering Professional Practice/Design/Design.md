# Design
If [[Requirements Engineering]] is about the what, then design is about the how. Requirements engineers try to leave things flexible so the designer should be in charge of that. This usually doesn't evolve coding however. This is a creative process. There are guidelines however.

**Models** are used to describe design, like [[UML]] or [[Simlink]] these are often graphical but can allow simulation as well which can give us performance ideas. **Written documents** are also used to explain design to yourself and new team members.

**Design** needs to meet the functional and non-functional requirements that need to be followed. It should be easy to explain to those who have to implement it. It should also make use of already existing technology as we don't want to reinvent anything. Design should be adapted to the developers as the design is only as good as its implementation.

There are different levels of design. These go from [[Architectural Design]], to [[Detailed Design, Software Design Principles]].

## Software Design Principles
These will help give a good design for a wide variety of projects. We will give some key ones. We have to make sure that a class that is **inheriting** from a class is actual similar to that class. We want to keep a class pure to what it is for example it doesn't make sense to extend a linked list for something that isn't purely a linked list like an address book (what if you want to change to a HashMap?).

**Cohesion** -> The strength of a relationship between pieces of functionality within a component, **high** cohesion is desirable. We keep what is conceptually the same within the same class and don't add things that are too different (a class should be tight nit).

**Coupling** -> How interconnected are different components. We want low coupling and make different classes not so connected so that they can be independent and work in the best way for their situation.

**Abstraction** -> Creating a view of some entity that focuses on the information that is relevant to a particular purpose, ignores any implementation or extra data. Inside it can be complex but outside it should be a simple minimal interface. Instead of using bare classes and numbers we create classes so hide this.

**Encapsulation** -> Grouping internal details of an abstraction inaccessible. So this hides everything behind an interface while abstraction just creates the interface. This makes sure only the functionality required is given and so we prevent errors from occurring by limiting control.

**Separation** -> This is the separation of interface and implementation. We create an interface that is known to a client and we take this away from how it is realized.

**Decomposition (modularization)** -> This is splitting a large system into smaller components with distinct responsibilities and well-defined interfaces. Allows reuse and makes components more understandable.

## Agile vs Plan-driven
There are different ways to do **plan-driven** and agile we will look at two extreme cases. In plan driven all the different activities are separate and not woven together. We keep a lot of heavy weight design documentation along with modeling notation . Then we implement according to the plan. Agile we focus on design and implementation. **Agile** still does high level design so this is often done at the start. We go over design and implementation on each cycle. Only informal documentation is kept to save time and not make anything that isn't used. The design doesn't output specifications but instead helps with code implementation. **Models** are still used in Agile but there is far less used, they are used for communication and understanding rather than being an exact design to follow.

### Reality
Companies in reality use a mix of the different design types. Neither types such as **waterfall** or **XP** are not preferred by most problems. They can be used for extreme cases that fit them but in actual use cases many people thing a mix of the two is the best option. Some examples are **Just Enough** up front design and **Adaptable** design.

### Waterfall
**Waterfalls** is a popular process used and it **plan-driven**. Here the design is completed and perfected before implementation so called **Big Design Up Front** (maxim). A lot of documentation is made in all these steps. This is good is requirements aren't changing and or you can predict the changes. You never go down the wrong path. Saves work if nothing is changed therefore. Makes design understandable since there is so much documentation and effort goes into understanding. Since everything is done up front this can also make the cost **predictable**.

A problem is if we can't predict changes and we don't know what the requirements will be. It can be very costly to change when we use a so much planning. It will only be discovered after all the planning so design will need to be redone. **Can't change the plan** so doesn't help with extra features. We can also add too many features in design that aren't needed, as we **may** need them later but in reality this is a waste.

### Extreme Programming
This is an **agile** approach and is the most influential approach. The design maxim is **YAGNI** or You Aren't Gonna Need It. So there is no engineering is the opposite of the extra features in **waterfall** nothing is overengineered. We only focus on what is need in a cycle. Another maxim is **DTSTTCPW** or Do The Simples Thing That Can Possible Work, we just sprint to the finish line and create an working product as fast as possible. These maxims make up the idea of simple design in XP. Another thing that comes out of this is **emergent design**, here no design is done up front a design is grown as the problem is explored we only react to the feedback as the product changes. We only work in parts giving time for it to form on its own and make something new. We only work on what is needed in the current design.

#### + and - of maxims
**+** The maxims are less wasteful than those in waterfall. There can be little loses but the amortized overall cost will be very low as we are working in small iterations. It is a safer long term bet. The maxims make design easier to understand since less complexity as simples thing is done all the time (but this is controversial as it goes against the wisdom of Plan-Driven approach). The maxims also target need directly so you will get a product that actually solve the problem purely. **Gold plating** isn't needed.

**-** Not building flexible components that can adapt to the future as **YAGNI** but later this can come back to bite you. This contradicts **refactoring** where we adapt code to make it more useful later, but this contradicts **YAGNI** so its benefits like having code be more expandable later can be removed.

#### + and - Emergent Design
Take advantage of learning as they emerge so we can always change and expand design. Encourages collaboration as everyone can have input into the design and we aren't just following someone's design blindly everyone can have an input. Any uncertainty about how useful the design will be is removed as we know it is solving a problem we have otherwise we don't create it. Time is also saves as we aren't doing so much in depth documentation.

A problem can be that since we add little part of design this can lead to overall bad design as the big picture is missed, so can get a poor design. Adding little bits at a time can lead to design rot (hence why we need refactoring). It can also be difficult to predict the cost of something as we just keep adding and adding until we get an acceptable product there is no roadmap and we don't know how many iterations are needed.

# Detailed Design
This is what happens inside a **subsystem** or **component**. We only work with the external interfaces to our component and we have to build the classes and their behavior do fit these interfaces. Even if you are doing a large project this breaks it down into chucks. Your interfaces must be understandable and not too artificial so it is important to think about this in the [[Architectural Design]] phase.

[[Design Questions]]
