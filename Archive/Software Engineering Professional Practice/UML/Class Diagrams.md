# Class Diagrams
These are used to describe how classes work and the interaction between them. This is part of **modeling**, where a **model** is a precise representation of some information needed to solve a problem. **UML** class diagrams can be converted to XML so can be imported and converted to structures. 

## Representation
A class is represented as a rectangle with a name inside. A class as a design entity is an example of a **model element** but this rectangle is a **presentation** element meaning it can contain more classes that aren't mentioned.
![[Pasted image 20220208133458.png]]
**Compartments** are made within the rectangle for *attributes* and *operations* to add to the basic class. **Methods** -> **Operations**. We have the convention **name : type** for argument, variables and functions. A class or type is always **capitalized**.
![[Pasted image 20220208133510.png]]
We can also have **visibility** we use **+** for public **-** for private and protected with **#** (but this is optional) and language dependent.
![[Pasted image 20220208133826.png]]
We can also have relationships between classes. An **association** is a most simple relationship (just a solid line). We can also have a optional name on the association with an arrow showing the direction of the association.
![[Pasted image 20220208133946.png]]
When we have an **association** between classes this means there is a link between objects of those classes. A **link** is an instance of an association while a **object** is an instance of a class. Classes are sets of objects and association are sets of links. We can also have role names at each end of the association.
![[Pasted image 20220208134233.png]]
We can also have **visibility** with this (+,-) to show that the PT object has references to the tutees. We can also have optional **multiplicities** where to show how many of a given type is associated with another class.
![[Pasted image 20220208134451.png]]
For example here a Student has 1 PT and a PT has between 1 and 30 students (**..** means a range). We can also have * meaning an unknow number. So a student can have at least one course. Then a course can have any number of students.

We can also show **Navigability** where we add an arrow. So if we have an arrow to an class form another. This means a object from the source of a arrow can access the object at the end of the arrow. In practice bellow this means a course has access to the students taking the course.
![[Pasted image 20220208134748.png]]
In this case it is actually undefined the other way around we need a $\times$ if that isn't the case.

## Attributes vs Associations
![[Pasted image 20220208134928.png]]
The second is more concrete and less abstract. It gives more detail and shows the actual implementation. We can't use **both** as this is redundant. We would prefer to use **attributes** for simple classes we don't need to reference these types. But we could have this another way around with classes we make as we want to show their relations

## Generalization
This is the same as **inheritance** that is we have a **is a** relationship. The below example says every LibraryMember *is a* MemberOfStaff. The notation we have here is an **empty** unfilled triangle showing the arrow. It points to the superclass not the subclass.
![[Pasted image 20220208135229.png]]

## Interfaces
An interface in **UML** is a representation of operations that can be realized by an actual class. To show c class is implementing an interface (we say **realizing**) we use a dotted line with an empty arrow head. This points from the class to the **interface**.
![[Pasted image 20220208135512.png]]
This means the class needs to implement all the methods of the interface. We also have the bellow alternative notation for **realization** done with a lollypop. This is done when there are a lot of associations to clean up.
![[Pasted image 20220208135600.png]]

## Making Class Diagrams
We can first underline all the noun phrases. We remove all the redundancies, synonyms, anything outside scope, operations of events, attributes, anything too deep
![[Pasted image 20220208135828.png]]
