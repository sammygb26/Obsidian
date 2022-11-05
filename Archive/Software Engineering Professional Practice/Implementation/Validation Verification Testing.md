# Validation Verification Testing
This is another activity we may take part in while maintaining and developing software. The motivation is to ensure code does what it is meant to do that is we have *high quality code*. It should also meet the requirement and expectations of stakeholders. We also want to find the cause in any failure to do so. 

This refers to all techniques for improving *product quality* by eliminating bugs. **Verifications** is whether we are building the software to meet requirements are we building it right. Then **Validations** is are we building the right software so meet expectations (more general). These may have not been capture or interpreted right in the engineering requirements phase.

**Testing** is a techniques that is used for *verification* and *validation*. Other techniques include *reviews/inspections/walkthroughs and static analysis*.

## Essence of Testing
The idea here is we pick a component and give some stimulus (inputs) then get some output. We compare to what should be achieved if there is a difference we then hunt down the *bug*. It is important to not just do testing at the class level as sometimes bugs only reveal themselves at higher levels abstraction. Classes themselves might work quite well.

We could just test as a whole. But this can make it hard to find where the bug is as we have to search a larger space. Instead we can test each subcomponent one by one. We may also have the case where multiple things are failing and then it will becomes very hard to find the combination of changes that will solve the problems all at once. Another way it to make a simulated environment around the object we are tying to test (with minimum functionality) then we test how they act. These objects are called *mock objects*. This works since the *mock objects* are very simple hence the only unknown in the tested object. This may also work for databases where we just have a simple fake database where we know the output.

## Bug?
*Bug* is an informal term but we can break it down further. We can have a *mistake* which is a human action that causes a fault (like a wrong symbol). Then we have a *fault* which is what *mistakes* cause so this is an incorrect piece of code (execution). An *error* is the discrepancy between the expected and achieved output form a class this shows the *fault* (gets out the the real world). A *failure* is when the system as a whole can't perform due to some *error*.

This means the *faults* don't always cause errors since the cases they fail with may not come up. That is the stimulus doesn't express the fault. Then *errors* may not cause *failure* if they cause errors in a non-critical way. There may be wrong values (not just wrong logic) but this may only screw up minor details like logs.

# Kinds of Tests
There are some testing approaches.

**Blackbox testing** -> Here we test the code by instead of looking at the code just running tests and comparing the output to the specification. This is also better as we don't have to change our tests when we refactor.

**White box** -> Here the internal code can be seen and tests depend on how the system is implemented and structured. We test whether it does what the developer intended.

There are some other kinds of tests however.

**Module (or unit) tests** for each class in an OO software we test the class does what it is meant to do and performs how expected. This isolates at a low lever where the errors are in a quick way.

**Integration tests** here we are arranging multiple classes together and check the classes interact in the way they are supposed to. This is a higher level way of testing that will find higher level bugs.

**System tests** here we are testing the whole system against requirements to see if it performs as desired.

**Acceptance tests** here we check *valuations* these tests are done in the use-case environment (with the customer) we want to see if they can interact with it not just if it can interact with itself. Real data is used here to check that it is working as intended.

**Stress tests** we look for how our system performs with more and more load. We want graceful degradation no catastrophic failure. 

**Performance tests** here we check other performance measures similar to stress testing.

**Regression tests** here the idea is we repeat tests every time we make a modification (or push to a repo). The idea here is that we test as we go so problems don't become buried and we will know how to solve them easier as we have been working with the code recently and we already know what change has revealed this bug.

## How to Test
We want to know how to design tests and what makes good tests. Test should be *repeatable* meaning if we repeat them we will get the same results. Hence they should succeed always for the same successful code and they should fail always for when there is an error. It shouldn't be random say if the bug shows up. Hence we need to be careful and create static environments for testing. We should also make sure to *document* our tests both what they are testing and the results (and their meaning). They need to be *precise*, *thorough* and *not vague* hence they get strait into the weeds to try and find a bug. Then should also be done on *configuration controlled* software to make sure that it is our code causing the error and we aren't getting confused and also make sure we aren't overwriting old code to solve new problems.

It can be good to write tests as we make the software or after. Another way is to make it before the benefits of this is that our development will be focused on solving the problems in the code. This also allows us to cross reference our requirements and tests hence we ensure we meet verification when the tests are met. This also ensures requirement are measurable and so testable.

### Test-First-development
The ides here is we write the code to pass the tests. The ides is that the interface and behavior of code is really all that matters. We also force our code to match requirement and make this relationship string by building around it So we *write* the tests *before* we write the code they apply to. They we *run* the tests while making the code. A benefit is we find bugs quickly as soon as they show up and so it they are easy to find. The tests can also be fine grained and local making the location again easier to find.

This can also help us make *requirement clarified* and concrete as writing these tests ensures we think through the requirements to a level that is enough for a program. This also avoids *poor ambiguity resolution* if we code first we will end up implementing in a way that just is easy to write. Hence writing the test first forces us to do it the right way for the consumer. This also ensures *tests are written* as they must be made fist and don't end up getting to a point late in development where testing is leaf behind.

### Test-Driven Development
This was developed as part of **XP**. Here we get entirely rid of requirements and just have test. This problem is if tests aren't understood communication is much harder with clients (stakeholders). This has lead to *Behavior-Driven development (BDD)* where we write English requirements in a specific way such that we can generate code from the English sentences. The problem here is it is still farther form what the stakeholders understand. We will also have to go further into design and even implementation in the requirements process.

## Evolving Tests
Here we may need to write new tests when a bug is discovered so that this bug doesn't come again in future. For example we have a series of tests yet our program still fails in some way. A good way of acting here is to *make* a test to capture this bug (so that we ensure we understand the bug). We then *check* the test fails. We then fix the bug. We then test to make sure we *pass* and really did fix the bug. We then run our other *tests* to make sure we didn't break anything else. We always *keep* our tests to ensure past problems don't arise again.

## Limitations
A major problem is the *time* it takes (even longer the writing code). The *coverage* can also be limited as the code can execute in a extremely large number of ways. We can never be sure we have caught all bugs. To get around this we can use *representative tests* which can check classes of inputs instead of fixed inputs. We may also find it hard to *emulate a live environment* for example it can be hard with threading it can be hard without running the actual program. We can also only test things that *run* like high level design requirements. So this only works for lower level things like code.

## JUnit 5 (Unit testing in Java)
This is a framework to help with automated testing in Java. There are also similar frameworks for other languages. A JUnit uses classes for testing. A class contains a test method (annotated with *@test*). This contains the code we want to be run in our test as well as *assertions* and informative messages if there is a fail.

#### Other Annotatios
We can also use *@DisplayName* to give a easier to read display name to a test
We can use *@Disable* to make a test disabled.
We can use *@Tag* to tag a test then JUnit5 for example can allow us to only run tests that are tagged.
We can also do *@Repeatedtest* this is similar to @Test but this will run a test a number of times.

We can also specify other methods in a class and annotate them with.

*@BeforeEach* execute before a test is run (prepare environment)
*@AfterEach* execute after the test to clean up the environment
*@BeforeAll* execute before all tests to for example ensure a database is being contacted.
*@AfterAll* execute after all test e.g. database is disconnected.

#### Assertions
JUnit provides a library of assert methods to use in test code for checking output of a program being tested. The most common is *assertEquals* which will pass the test only if the given values are equal. There are also many others (*assertSame* (references)). We can also add a custom error message to any of these assertions which gives a better description rather than an esoteric explination of what test failed where.

## Inline Assertions
This is a feature of Javan/ where we can have assertions spread through the code itself. We can use this to record assumptions and do sanity checks on running code. This can help us turn *faults* into *failures* so they can/have to be fixed. These can help as they can be placed in anywhere and so can catch errors as soon as possible. Assertions will cause assertion error exceptions the code execution then stops giving a failure.

Assertion checking can be switched on and off how in Java. For example on while testing but when we deploy as these error messages will be more unprofessional and confusing to customers.

## Alternatives
We can also do *overly defensive programming*. Here we return a error values when we find ourselves in a situation we can handle. This usually isn't a good idea however since it just hides faults and they always show up somewhere. It can make it hard to know where the bug came from.

We could also use regular Error Handling makes more since here we know where the error originated. But again if we are too defensive we can get a lot of duplicated codes and tests. Hence why we use testing classes instead of these options.

## Preconditions, Postconditions and Invariants
All of these can be tested for. For example a *preconditions* is a conditions that must be true when a method is called (obj$\neq$null). We can also have *postconditions* which ensure that after the method runs something is ensured to be true. We can also have a *class invariant* which is something that is always true of an object form a given class.

## Coverage
Coverage is a measure of the degree to which the source code of a program is executed by its tests. To with no tests there will be no coverage. There are different types of *coverage*.

*Statement Coverage* - The percentage of lines of code were executed by at least one test.

*Branch Coverage* - What percentage of branches of code that were executed by at least one test. That is for a condition the number of cases we test.

Coverage doesn't ensure the code if big free for example if some of the possible situations aren't simulated.

There are also *coverage tools* which show how much of your code is covered by tests. We can choose a coverage running in IntelliJ. Then when we run a test we can get if the tests were passed as well as the coverage. We can also set *tracing* which will then show branching coverage as well.

# Testing Alternatives
## Reviews walkthroughs and inspections
Here we use humans looking over code t find errors. This can help with finding bugs that are harder to find by testing for example combinations we haven't been able to thing about since .

*Reviews* are don't over an artifact and is a meeting between people. The artifact  must meet criteria before the meeting like it must run an pass tests. This is to ensure productivity. The review is there to identify problems as soon as possible. Everyone does some study beforehand to help find bugs. The developer goes away and fixes bugs on their own.

*Static Analysis* this involves inspecting code to determine properties without running it. An example of this is type checking since not all programs have types. This is an active area of research with a lot of research. It works best with *clean* languages without pointer arithmetic which makes things more complicated. Static analysis runs into trouble with more complicated properties. For example not every error can be found. This is due to complexity making infeasible to find these bugs. To help with this *annotation* can be added.

## Bug Tracking