# High Quality Code
This is very important especially for large projects. Failure to have high quality ode can hurt a lot with these larger projects. We will also look at **Javadoc** which is a way to keep track of code while implementing it. Our code needs to meet requirements but should be able to deal with changes in the future. This come from maintainability. We want to make sure we can reuse parts of our code when this change happens. The larger projects get the more important this is a high quality code can be better understood by more people and so changed by more people. So *high quality code is easier to use for a team and transfers well between people and yourself in the future*. Code reviews are used to check code against multiple people so allowing bug checking and quality assurance.

## Bracketing
Bracketing can change how readable code is. You should be consistent with with the bracketing used this allows the code base as a whole to be easier to read. If you don't stay consistent people have to switch the way the read the code and this makes it more of a headache to read. **Standards** are used to standardize these types of things across a company but they need to be *followed*.

## Indentation
This is how white space is used to within a file. It makes code easier to read and it is important to use indentation to make code easier to read. So languages in fact make this part of the syntax to ensure correct indentation is used. Again **standards** are given on this. Indentation makes namespaces easier to understand and generally helps the idea of the code get into our brains. One problem is different **IDE**s use a different number of spaces for a tab. Again a *convention* must be reached in **standards**.

## Naming
Names should be descriptive and clear therefore small names that don't give understanding of the code. Comments can also becomes useless and not help with this making code very hard to understand. Some common variables used like $i$ and $j$ are find as their meaning is understood within a list.

We should also make sure not to use **magic numbers** in formulae. Instead we can use constants. This makes the code easier to read and understand as well as more maintainable as the values can be more switches out easier.

Spaces between operators should be standardized as well. Keeping this the same can make the code easier to read. You can use grouping to show presidency in an operation but if you aren't careful this can get more confusing.

## Commenting
Comments should only exist to explain things the code doesn't already explain so no unneeded comments. If you have too many comments it can make the whole code harder to understand. When writing code clearly comments will not be needed. Some problem might be that comments aren't updated with the code and so the comment become a hindrance making it more difficult for the code to understand. The best scenario is the minimize the number of comments by making the code clear.

## How To
Make sure the maintains the same *standards* throughout the codebase. Then we need to make sure to use *meaningful* names and make sure to keep them *updated*. We need to make sure to avoid *cryptic comments* firstly by avoiding the use of comments and then making them very simple when you do have to write them. We want to keep *local variables' scope restricted* for example it doesn't make sense to add all variables at the top only when they are needed so we don't have to look around so much (curly brackets can be used for this).

We should order if else statements with more frequent cases first. Hence we read the fewest lines to understand what the program does overall. We should make sure to use the right kinds of loops again making the code easier to understand. Along we this we should *avoid deep nesting* which makes it hard to understand what is going on. We can split into method to add names to make sections more understandable. We should try to avoid *long methods* as it is hard to understand what these do it make the logic of the code unclear. We should use *defensive programming* where we check that things we have assumed are true. For example we check arguments are in the correct ranges or not *null*. This way we can catch if the wrong values are being given (error message). This can also help avoid crashes. We should make sure to use the patterns and OO design we have already covered.

We should get the best of using functions and repeating code. So its better to call a function multiple times rather than write the same piece of code multiple times. We should avoid separating methods if this makes the code overall more complicated however. We should *clean code* to make sure there is no confusion about what is or isn't used later. *Don't be too cleaver* by this we want to make sure we don't make code so smart and complicated it becomes impossible to understand.

# Javadoc
We need to ensure every document has documentation that is aimed at the users of the code. If we separate code and documentation is means they can get out of sync and make it harder to maintain. *Javadoc* allows you to write comments into Java code which are automatically converted into documentation for your project. We have to follow *Javadoc* syntax. There are similar things for other languages.

We start with /** and end with * /. We can use HTML like notation within the comment. We can use @ to specify parameters (@param), returns (@return) and @see to link to documentation of other classes.

# Relationship Construction-Design
We may often have an *interface* being implemented by one *class*. The idea here is to allow the implementation to change behind the use of the object. We could use control modifiers instead of using an interface (like *private*). The difference is the implementation and the interface are together. This is considered to be more ugly. We should focus on design to make the most of OO and so increasing cohesion and decreasing coupling. We should use *inheritance* to reduce how much we have to change and do. Then of course we should use *interfaces* to decouple users from implementations.

## Packages
These are units of encapsulation and allow us to limit what is accessed to only the interfaces. They can also be used to control the namespace and so make code more simple and ordered.