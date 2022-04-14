# Design Patterns
These are solution to frequent design problems that can be solved by preset uses. We have given names to these solutions that work well. These help us take use of the knowledge of better designers. Other designers will understand these patterns also.

## Background
Patterns are used in many places. So if any common problem is seen they can be used. We see common technical problems in OO design for software engineering. We have **Pattern catalogues** that give easy references and everyone understands. 

A **pattern** will have different aspects
* A **name** publisher-subscriber.
* **Alias** which is the common name for it (*composite*, *observer*). 
* Then we have then **context** which is what circumstances lead to this kind of problem.
* The actual **problem** which the pattern aims to solve. 
* Then the **solution** the implementation of the pattern. 
* Then we have the **consequences** pros and cons.

**Cautions** -> We need to make sure we are actually needing the pattern and we are just using it to look like we have knowledge, this could have negatives effects. Another problem is that GoF solution can be considered to only solving deficiencies of OOP but there are true solutions say in FP. But we still have to use OOP as it is what people are taught.

There are different **types** of patterns.

* **Behavioral** patterns -> Identify communication patterns in our program and help ease our implementation.
* **Structural** patterns -> Ease design by allowing us to create relationships in simple ways between the different objects.

## Composite
We want to treat both collections of objects and single objects as the same object. The way we do this is we make all implement the same interface and so we can interact with all of them in the same way. In this pattern the structure of objects is like a tree where we want to treat the different permutation of this tree in the same way.

**Example** -> *Graphics Library* will implement different primitive objects like lines, text, strings etc. A user of the library want support for operation of element that are uniform across these different types. It makes sense to have different classes for these different things we can display but also some **graphic** interface that is shared by them all.
![[Pasted image 20220210215459.png]]
This is **polymorphism** where an object can have the same interface but act differently beneath. It will use the overwritten function created in the subclass. It is called **dynamic polymorphism** since it happens at runtime. We might want to group many graphics together into a *composite* **picture** element. We could *naively* use a list but this isn't enough. What we want is to treat this new object as a graphic not some other type of graphic.
![[Pasted image 20220210220116.png]]
So a **composite** pattern will have an subclass (picture) of a superclass (graphic) such that when we call a function ono one it will return the values stored in all the subclasses. a **note** is used to specify what draw does in *picture*.

#### Pros and Cons
**+** We can have trees of any depth and we don't need to write new code to do this so it is very flexible. We can also add new leaves or composites very easily by just creating the class we don't need to incorporate them into the program it is ensured to work by the interface.

**-** Maintenance issues as draw is split up between many objects we could do this top down exploring the tree and drawing objects that way. We could have a *Visitor* pattern where each operation like draw all in one class then the subclasses will all call this class.

#### Variations
We might want a function that walks all over a tree we would have to define them in graphics in this case but we would have to ensure it works well for every object.

## Observer
When we split up a system into different cooperating classes we need to make sure to maintain any dependencies between classes. So we have **subject** and **dependent** classes (that depend on the changes to the subject classes). We would also like to add and remove dependent classes without having to modify the subjects. **Observer** is used to solve this in a event driven pattern or Model View Controller pattern.

**Naïve Solution** -> We have an association between each subject with each dependent. But this leads to high *coupling*. The subject must *know* its dependents and the subjects need updating when dependents are changed.

The **solution** is the observer pattern. In this pattern we have any dependents register with a subject through an abstract observer class. The *subject* is therefore not coupled to the dependent and their implementation doesn't concern the subject. So we don't need up update how the subject notifies the dependents when their implementation changes.

![[Pasted image 20220210223641.png]]

This is done through two classes the **subject** and the **observer**. The association between subject and observer here is bidirectional. Each observer attaches itself to a subject is is dependent on. It can also be detached. A *subject* then holds a list of all attached objects. When the subject is updated it can then loop over all observers and **notify** them by calling update on each observer. This will cause **polymorphism** to take action so each observer can handle this change differently but the message sent by the observer doesn't change. This can also be done with multiple objects

![[Pasted image 20220210224203.png]]

So the subject will always be able to be attached and detached from as well as have the functionality to notify all observers. The get and set state will change with the concrete subclasses and for this the observers will keep a reference to the subject. Coupling is still increased since the actual reference from the subject to the dependent is different as it is through the observer hence it is abstracted away from the concrete observer.

![[Pasted image 20220210225126.png]]

This is how it would actually be implemented.

#### Pros and Cons
**+** This is far better than the *naïve* approach as there is less associations only between the concrete observers and their subjects or just a concert class and an abstract class. This has support for **broadcasting** where all observers can be notified of a state change on a subject.

**-** It can lead to **update** cascades where updates can cause updates and since there are many updates this can be hard to track down. It can be costly in terms of space since all the subjects need to hold a reference to the observer objects. You could use **hash maps** to associate each subject to different observers. We can also have dangling references if a subject is deleted (could be fixed by a termination notification).

#### Variations
This can work with 1 or more subject. We can also use **hash maps** to store observers of subjects to save space. We also might want multiple subjects for a given observer. We would want the update to know who sent the update for this we could send the subject as the argument to the observer. We could also have observers only attach to specific event of interest to them. Events could also be pushed to the observers where the information of note is sent with the message this would reduce coupling between observers and subject as the observers now wouldn't care about subjects but now the dependency is on the observers.

## Template
The problem is we have two different entities that have similar and shared functionality. We could **place both in different classes** and just implement the same functionality separately. However the problem here is that this would lead to code duplication and be hard to maintain as we would have to make sure to change functionality in both if we wanted to change how their shared functionality worked.

The **template** solution is we create a template abstract class and we up the functionality the entities share in this new class. So we only need to implement the shared code once. We can also implement how the common functionality function will work. Then we have abstract primitive operations that are overwritten by the concrete class. This ensures the concrete classes continue to perform the same and their functions still work the same but they can still be different.

![[Pasted image 20220215095042.png]]

This is commonly used in libraries, frameworks and helps with *auto-generated code* (instructs the code generator).

### Pros and Cons
**+** Hels remove code duplication and keep shared functions operating and acting the same. Controls what can be done by the subclasses. We can also control extensions to the main algorithm provided by subclasses. 
**-** Should minimize the number of primitive operations in order to make sure the subclasses have to do as little as possible as this can lead to poor maintainability as other people can implement too much. Its hard to tell what can be implemented or overwritten so do this could use a **prefix** as part of the operation name.

### Hook Variation
The idea here is instead of just having primitive abstract operations we have implemented operations in the **template** class these give a **default** way for the functionality to work but subclasses can override this. We can also keep empty hooks that allow subclasses to add functionality but the order is fixed to prevent errors.

![[Pasted image 20220215101322.png]]

## Singleton
The problem is we have a single instance of an object we want to create. The problem is we want a single instance of a class so a single object. We may also want to give global access to this object and we want this object to not be overwritten. A solution could be to just make a global variable but this can be overwritten and doesn't ensure multiple versions are made, so this doesn't solve the first and last problem.

In the **singleton** pattern we implement the class so it itself keeps tack of the only instance of it (like making it private). Then the class offers static functions that gives access to this object with a function called **getInstance** which is public.

![[Pasted image 20220215101343.png]]

The singleton class has a private instance variable that as soon as we try to access the class we initialize the singleton. Get instance will always just return the **instance**. We <ins>underline</ins> to show that the functionality is static and so available from the pure class. So this method needs to be called on the class overall. 

### Lazy Initialization
In this version we only initialize the instance once we have called get instance and only the first time.

### Pros and Cons
**+** This offers a controlled global access to a sole instance of a class since it is all private it is controlled by it is global since we have a getter in a static class. The object is only initialized once. Better than global variables since namespace isn't overwritten, lazy initialization isn't available also so worse for performance. It can also be easily change to allow more instances of the class by changing the get instance functionality. But still gives control so we could ensure no instances refereeing to the same thing were created.
**-** It is frequently misused when you don't need just one instance so it can add restrictions that we don't want. Introduces global state which can be unsafe. It leads to tight coupling with itself and makes coupled objects that use it. It can also be broken by multiple threads which creates multiple instances of the singleton. The class also cannot be inherited and it is hard to unit test it since it is used everywhere.

### Variations
Some will help with multiple threading and gives exceptions when class instances are created.

