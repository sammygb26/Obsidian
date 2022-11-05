# Refactoring
This is seen as part of maintenance. But refactoring can be seen as part of development in Agile processes as maintenance is needed throughout. *Refactoring* aims to solve the problem of code decaying over time. This is since over time tacking on new changes will make local changes. Overtime this makes changes is future harder and bugs get more frequent. *Refactoring* is when we have to re-imagine and we must restore good design in a disciplined way. Similar to design there are *refactoring patterns* that will help implementation of refactoring. There are also many tools to make this easier.

**Refactoring** is a change to the internal structure of software to make it *easier to understand, and cheaper to modify*. **Without observable changes in behavior**. We apply a series of refactoring without changing its observable behavior.

## Why Refactor
*Refactoring* makes software easier to understand and helps other people understand the code easier. *Helps* make modifications easier and quicker as the design is better. It helps find bugs as the design will be less complicated. It also helps you program faster as a refactored code is more efficient to work with.

## When to refactor?
*Refactoring* was once seen as maintenance like when old code you need to update in future. But in modern methodologies like *Extreme Programming* and Agile refactoring is done al the time continuously.

## Examples
A *refactoring* is a *small* transformation which preserves correctness. There are many examples. An example could be adding an extra parameter to a method (giving it more responsibility), this changes method behavior but *overall* the functionality remains the same. However this isn't always a good ideas a functions with many parameter are complicated and hard to work with. We can change a *Bidirectional association* to a unidirectional association. Which can decrease coupling.

### Extract Variable
Extracting a variable and giving it names can make the code easier to understand and make it easier to come back and understand what it does. Comments can also be removed which can become out of sync with the code. This *isn't performant* however but may not matter in many cases.

### Replace Conditional with Polymorphism
Instead of switching through many classes where we have different cases we can give each a different action. Instead we can put all types into one superclass which we call the functionality on this then allows us to implement on each subclass and this will simplify our calls to the subclasses. This helps as we can miss less cases when adding classes and so it is easier to add new subclasses.

## Safe Refactoring
We need to ensure our refactoring hasn't changed something. The best idea is to *test*, *refactor* and *test* again. We check before and after to see that the results are the same. It may happen that something doesn't work before and then we will avoid blaming the refactoring needlessly. We will also know if refactoring breaks code immediately. This can be done with *unit tests*. This approach increases speed of refactoring and debugging.

## IntelliJ
This is an IDE which allows many options for refactoring. You can select an item and press Ctrl + Alt + Shift + T. Refactoring can be previewed and if there are any problems or conflicts they are displayed. There is also the possibility to remove and unnecessary changes. *Safe delete* Alt + Delete remove files not referenced in source code. Copy move can move or copy an element or method to a new class F5 F6. Extracting a method makes a piece of code into a new method Ctrl + Alt + M. We can also Extract a field F, parameter P or introduce a variable V (saves expression to variable). We can rename a variable which changes its name everywhere. Inline is the opposite of extracting N. We can also change a signature Ctrl F6 for a class or function.

## Bad Smells in Code
These are sign something isn't implemented in the right way or the code is rotting. Here are some

1. *Duplicated code*
2. *Long methods*
3. *Large class* (low cohesion)
4. *Long parameter list*
5. *Lazy class* (adding more and more responsibilities to a class)
6. *Long message chains* (maybe the thing at the end of the chain should be closer)

These can all be solved through refactoring.