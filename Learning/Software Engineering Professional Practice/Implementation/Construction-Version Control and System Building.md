# Construction Version Control and System Building
Version control is a means by which we keep track of different and passed versions in order to not loose any information that would other wise be overwritten. It allows us to keep track of all the different work done on a project and go back in time if anything changes that we don't want.

## Problem of Systems Changing
As the program changes over time to fix bugs and keep up with new software and hardware. We may also have to maintain multiple version at any point in time (stable, release, alpha etc.). It is easy to loose track of which changes realized in which version and what parts you want to keep and loose. Hel is needed in managing the different versions.

**Software Configuration Management** is what is used to overcome these difficulties. This is used with *version control* where we track multiple versions and ensure changes don't interfere. We also use *system building* where we don't want to have to rebuild a project every time a small change is made. System building helps us work with the code in a more real time manor where we can check what changes were actually made faster. A hierarchy is created through linking then only the parts required to recompile recompile when a file is changed.

## Version Control
A system will *evolve over time*. As a program evolves there is a main path called a *trunk* which is the main version of the program. New things are tried in *branches*, these are separate version that are made that don't make changes to the trunk version which is working properly. When something work we can merge into the main branch to add the new functionality. We can also have *discontinuous development branch* which we don't incorporate into the final version and are left. We can also have *tagged versions* which we can release and we give them a name so we can easily find them in our version control system.

A *version control system* is a configuration manager that keep track of the above features. A copies of every version (every edit) of file sin maintained. Change logs are also maintained which says who made a change and when. The *system* also allows multiple people to work on the same file as the same time. It can show the *diffs* between versions. This would be a problem as usually two files may be made then when both are committed, one after the other, the first will be overwritten however causing a loss of work.

## Lock-Modify-Unlock Model
This is a type of *version-control* implementation. Here an editor checks-out a file from a repository stating whether it is read only or read-write. If its read write then the file gets locked this means no-one else can write to it. We can then edit it and the check it back in as which point the lock expires and people can use it again. This ensures only one person is changing a file at a time therefore a file can't be overwritten. This is better than before as files aren't lost but this isn't efficient as only one person can work at a file at a time. Then people can also forget to check it back in so this becomes a block to doing work. *RCS* is an old version control system that works with this. It can also only work on small files and not directory branches. But it can keep multiple versions and save deltas between versions.

## Copy-Modify-Merge Model
*CVS* and *SVN* are newer systems base don *RCS*. These can handle directory hierarchies for projects. There is a single master repository. They use *copy-modify-merge* model. In this we checkout the whole project we modify it then we try to check back in with the whole project. But we can get denies when there has been an update in the mean time. In this scenario we need to do an update where we compare the updated version to our edit. There will be *non-contradictory* parts that we can merge automatically. But if there are *contradictory* (overlapping) parts we need to manually resolve the conflict then we can check in. The *central-repository* can be anywhere local or in the cloud.

**Three-way-merge** is a way of accomplishing a merge between two different versions of a file. We will explain it in 8 steps.

1. We have an original file for example "Alpha, Bravo, Charlie" this is the *common ancestor*
2. Tester 1 edits the files to becomes "Alpha, Foxtrot, Charlie".
3. Tester 2 edits "Delta, Alpha, Echo, Charlie"
4. Tester 2 commits changes (no-worries)
5. Tester 1 Commit fails (as update is needed as there were changes)
6. Tester 1 updates and merge reports conflicts "Delta, Alpha, << .mine Foxtrot == , Echo >> .r4 Charlie" The contradictions only happen where there is an edit overlap
7. Tester 1 then fixes  so there is no contradictory
8. Tester 1 then commits

We might worry about non-overlapping edits and edits even though they don't overlap can contradict in terms of logic. so we should *compile and test* after a merger.

## Distributed Version Control
There are many tools that use this type of system. Like *Git*, *Mercurial*, *Bazaar*. Previous versions discussed have a single central repository. These ones all have many repositories of the same software this is called *Distributed version control system* or **dVCS**. The disadvantage of the pervious model means you need to be connected to that central repository at all times in order to check in and out. In these systems we can have local repositories so we can do work even when disconnected. Hence we have less of a dependencies. We can also work while disconnected. We can also use it faster as we only have to update our local repository. The problem is it is more complicated and harder to understand and versions can get out of sync.

![[Pasted image 20220306130452.png]]

This is the version used by *git*. The way this works is we push and pull form the central repository but this makes a local repository where we can commit and update. This allows us to work on files when disconnected.


![[Pasted image 20220306130625.png]]

You can also have more complicated versions where local reps communicate between each other and so this can becomes far more complicated. So protocols are required to make sure inconsistencies don't happen and we stay on track.

## Branches
In simple *VCSs* we just have a single linear sequences of versions of software. But we may need multiple versions of the same item of code base. Hence we will have 2 branches out the same ancestor. So we can have a version we release to customers but slowly update with bug fixes while we have another unreleased version we are adding new features to. *Branching* is used to support this. A three way is done before as there is the common ancestor and the two edited versions. 

## Build Tools
The idea here is that there is a compilation hierarchy and when we build the project we build the minimum number of files to reconstruct the overall file.

## Gradle
This is the official Android build tool. It is based on Groovy which is built on the Java JVM and it is easier to understand than XML-based tools and concise and less verbose. It is also highly configurable and quite performant compared to Maven. this is due to its use of incremental builds so it only runs when necessary, it cache builds and the Gradle daemon keeps build information in memory. It also provide a web based interface for debugging and optimizing.