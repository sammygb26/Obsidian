### Symmetries of a Square
We will consider an abstract square object. Say we remove it from some plane. How might we be able to move it or rotate it and then place it back into its place again? We might consider all the ways of doing this. Although we note there are many actions that have the same outcome for example a $90\degree$ rotation is the same as a $450\degree$ rotation and so they shall be considered equivalent. The motion of the square is constrained by it needing to fit back in however we might label the corners to understand the effect of some transformation and indeed how combinations might be equivalent. Here are all such transformation on a labeled square.

![[Pasted image 20221223182209.png]]

This set encompasses all possible transformation on the square. This can be seen from the facts that the position of all colors is defined by a single corner's **location** and **orientation** (face up or face down). Any particular corner has 4 possible positions and 2 orientation. Hence there are 8 possible states all given as outcomes above. If we apply two motions after each other we gain one of these states.

![[Pasted image 20221223182537.png]]

We see that the final output gives the same square as $D$ on its own hence these two motions are equivalent to $D$. This suggests we can **compose** two function and this makes sense when we consider each motion a function with from the set of square regions to itself. Hence we can write $HR_{90}=D$. In particular the combination of the eight motions $R_0,R_{90},R_{180},R_{270},H,V,D$ and $D'$ with the composition operation for the *dihedral group of order 8* (order being the number of elements), this is denoted $D_4$.

To show the relation behind this set we ca write an **operation table** or **Caley table**. This show for every composition of motions where the horizontal label is applied first then the vertical label.

![[Pasted image 20221223183332.png]]

This table fills in without requiring new motions showing again that our set of motions makes up all possible motions. Algebraically this says that if $A$ and $B$ are in $D_4$ then so is $AB$. This property is called **closure** this is one of the requirements for a mathematical system to be a group. Also note that if $A$ is an element of $D_4$ then $AR_0=R_0A=A$. Thus combining any motion with $R_0$ gives the motion back. This is called the **identity** (another requirement for a group). We also see that for every element $A$ in $D_4$ there is some element $B$ such that $AB=R_0$. Here $B$ is the **inverse** of $A$ and visa versa, this is another requirement for a group. We also see each row and column only has a motion once, again all groups must have this.

- We also see that in $D_4$ we have that $HD\neq DH$ this can be said as the group is **non-commutative** or **non-Abelian**. In fact when for some group $ab=ba$ this will be **commutative** or **Abelian**.

Combining the above properties with **associativity** gives the properties for groups. Associativity simply is the condition that $(ab)c=a(bc)$ for all $a,b,c$ in the set.

##### Properties Required for Groups
1) Closure
2) Existence of an Identity
3) Existence of Inverses
4) Associativity

### The Dihedral Groups
The above analysis can be done for an equilateral triangle or some regular polygon or any regular $n$-gon ($n\ge3$). The corresponding group is denoted by $D_n$ and is called the *dihedral group of order 2n*. These groups have many applications. A molecule of *ammonia* can be seen to have $D_3$ symmetry.

![[Pasted image 20221223185747.png]]

Then x-ray crystallography can be used to reveal the inner structure of a crystals molecules by examining the symmetries in the projection of the molecule.

![[Pasted image 20221223185857.png]]

The *dihedral group of order 2n is often called the group of symmetries of a regular n-gon*. A **plane symmetry** on a figure $F$ in a plane is a function from the plane to itself that carries $F$ onto $F$ and preserves distances. This means for any points $p$ and $q$ in the plane, the distance from the image of $p$ to the image of $q$ is the same as the distance between $p$ and $q$. The **symmetry group** of a plane figure is the set of all symmetries of the figure.

This definition is analogous to the definition of symmetries is 3D space.

##### Motions Definition
A **rotation** of a plane about a point in the plane is a symmetry on that plane that maintains said point in the same place. A **reflection** about a line can be seen as a transformation taking every point on the line to the same position then every other line is in a different position such that the line is a perpendicular bisector from $q$ (untransformed) to $q'$ (transformed). If the transformation is still symmetric we will flip about the line. This is the same as a $180\degree$ rotation in 3D space about the same line we are reflecting.

* So $H,V,D,D'$ are reflections in 2D on a plane while they are rotations about the same axis in 3D.

Then similarly just as a reflection about a line cannot be achieved by physical motion in 2D a reflection across a plane in 3D cannot be achieved by physical motion in 3D. Many objects and figures have rotational but not reflective symmetry. A symmetry group consisting of the rotation symmetries of $0\degree,360\degree/n,2(360\degree)/n,\dots,(n-1)360\degree$ is called a **cyclic rotation group of order n** and is denoted by $\langle R_{360/n}\rangle$. Examples bellow:

![[Pasted image 20221224190652.png]]

[[Introduction to Groups Questions]]
