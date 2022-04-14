# Hash-Table
The idea behind hash tables is we would like to have a fixed array the length of the number of possible keys for a dictionary. But this space is far to large. We use a **hash function** which breaks a key into a value that varies over a much smaller range possible of our choosing. We then have a list in each of these **bins** that allows us to store multiple actual key pairs. We could just have bins with single elements which would increase speed and save space. This way we could just use an [[Array]] to store all values and just index in using a hash-function. This would lead to a hash collision when we have two keys hash to the same place however. So we use some other data structure at the end instead.
![[Pasted image 20220211151447.png]]
Another way of dealing with this problem of collisions (called **probing**) is we include in our hash function a second argument for the number of tries. Then this should have the effect of randomly choosing another entry in the dictionary to use. For this we can if we don't find a matching key at the hash just increase the number for the function. 

The problem with this is that when we remove an element we need to make sure any remaining entries that collided with it are moved back otherwise we can search the dictionary for them and not find them.

## Load
The **load** on a *hash-table* is the amount of entries. So then the **load-factor** is the number of $\frac{\textrm{\# entries}}{\# bins}$.

## Hash-functions
A good hash function will mean we have ethe least collisions so it must spread out the likely keys evenly over the dictionary. One popular way is to modulate some string by the number of bins. This ensures we wont get a key outside of our range. However this may not work well if the keys aren't evenly distributed. For example numbers ending in the same digit would be in the same bins if we hash with mod 10.

**Perfect** hashing is where our list of keys is perfectly associated with the possible spaces. So every entry goes to one space and there are no collisions. There are ways to precalculate this if we know the keys in advance.

