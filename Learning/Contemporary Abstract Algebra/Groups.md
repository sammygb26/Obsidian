It will first be useful to define a **binary operation** on a set.

![[Pasted image 20221227183331.png]]

So this ensures each *ordered pair* of elements in $G$ is assigned to some other element in $G$. This condition is called **closure**. Some examples of binary operations are ordinary addition, subtraction and multiplication of integers. However division of integers is not a binary operation because an integer divided by an integer doesn't always yield an integer ($1/2=0.5$).

Another key example is the binary operations addition modulo $n$ and multiplication modulo $n$ which will take place on the set $\{0,1,2,\dots,n-1\}$, which is denoted $Z_n$.

### Group Definition

![[Pasted image 20221227183821.png]]

In words a group is a set together with an associative operation such as identity every element has an inverse, and any pair of elements can be combined without leaving the set.

A **group** is called **Albian** if for every pair of elements $a$ and $b$, $ab=ba$. Then it is **non-Albian** if for some pair of elements $a$ and $b$ $ab\neq ba$.

### Examples

##### Addition Group Examples
The set of integers $Z$, rational number $Q$ and real numbers $\mathbf R$ are all groups under ordinary addition. In each case the identity is $0$ and the inverse of $a$ is $-a$.

##### Multiplication Group Failure
The set of integers $Z$ under ordinary multiplication is not a group. Since $1$ is the identity but elements have no integer inverse. There is no integer $b$ such that $5b=1$ for example. However the real number $\mathbf R$ is a group under multiplication!

##### Complex Group Example
The subset $\{1,-1,i,-i\}$ of the complex numbers is a group under complex multiplication. Then $1$ is the identity $-1$ is the inverse of itself and $-i$ is the inverse of $i$ and visa versa.

##### Rational Group Example
The set $Q^+$ of positive rationals is a group under ordinary multiplication. The inverse of $a$ is $1/a=a^{-1}$.

##### Irrational Group Failure
The set $S$ of positive irrational numbers together with $1$ under multiplication satisfices the three properties given in the definition. However the operation is not binary one on this set as it is not closes for example $\sqrt2\cdot\sqrt2=2$.

##### Rectangular Array Example
A rectangular array of the form $\begin{bmatrix}a&b\\c&d\end{bmatrix}$ is called a $2\times2$ *matrix*. The set of all $2\times 2$ matrices with real entries is a group under component wise addition: $$\begin{bmatrix}a_1&b_2\\c_1&d_2\end{bmatrix}+\begin{bmatrix}a_2&b_2\\c_2&d_2\end{bmatrix}=\begin{bmatrix}a_1+a_2&b_1+b_2\\c_1+c_2&d_2+d_2\end{bmatrix}$$The identity is $\begin{bmatrix}0&0\\0&0\end{bmatrix}$, and the inverse of $\begin{bmatrix}a&b\\c&d\end{bmatrix}$ is $\begin{bmatrix}-a&-b\\-c&-d\end{bmatrix}$.

##### Modulo Example
The set $Z_n=\{0,1,\dots,n-1\}$ for $n\ge1$ is a group under addition modulo $n$. For any $j>0$ in $Z_n$, the inverse of $j$ is $n-j$. This group is the *group of integers modulo $n$*.

Many sets are groups under addition however for many cases multiplication prevents certain sets from being groups due to a lack of inverses for certain elements. But we can almost define groups with multiplication. To do so for real we remove the offending elements.

##### Real Number Multiplication
Multiplication of real number is not a group as $1$ is the identity but there is no real number $b$ such that $0\cdot b=1$. However the set $\mathbf R^\star$ of nonzero real numbers is a group under ordinary multiplication with t inverse of $a$ being $1/a=a^{-1}$ 

##### Matrix Multiplication Example
The **determinant** of a $2\times2$ matrix define whether it has an inverse under multiplication. For the matrix $\begin{bmatrix}a&b\\c&d\end{bmatrix}$ is $ad-bc$.  Then the set $$GL(2,\mathbf R)=\left\{\left.\begin{bmatrix}a&b\\c&d\end{bmatrix}\right||a,b,c,d\in\mathbf R,ad-bc\neq0\right\}$$is a group under matrix multiplication. This is verified by showing that any matrix in the above group multiplied to another forms a $2\times2$ matrix with a nonzero determinant. Then the inverse of a $2\times 2$ matrix $\begin{bmatrix}a&b\\c&d\end{bmatrix}$ is $$\begin{bmatrix}\frac d{ad-bc}&\frac{-b}{ad-bc}\\\frac{-c}{ad-bc}&\frac a{ad-bc}\end{bmatrix}$$
The true set of $2\times2$ matrices isn't a group under multiplication as when $\det A=0$ there is no inverse.

##### L Euler
We know that an integer $a$ has a multiplicative inverse$\mod n$ iff $a$ is less than $n$ and relatively prime to $n$. Then $U(n)$ is a group under multiplication $\mod n$. For example $U(10)=\{1,3,6,9\}$ then the Cayley table is 

![[Pasted image 20230102172005.png]]

##### Negative Modulo Example
The set $\{0,1,2,3\}$ is not a group under multiplication modulo $4$. As although $1$ and $3$ have inverse the elements $0$ and $2$ do not.

##### Complex Example
The complex numbers $\mathbf C=\{a+bi\mid a,b\in\mathbf R\, i^2=-1\}$ are a group under addition as we know the addition of any two complex numbers is a complex number. Then the inverse of $a+bi$ is $-a-bi$. The group $\mathbf C^\star$ (where the $0$ is removed) is also a group under multiplication. Here the inverse of $a+bi$ is $\frac1{a+bi}$.

##### Roots of Unity Example
The roots of unity are defined as for all integers $n\ge1$ $$\left\{\left.\cos\frac{k\cdot360\degree}n+i\frac{k\cdot360\degree}n\right||k=0,1,2,\dots,n-1\right\}$$This is a group under multiplication.  This makes sense as from DeMoivre's theorem we find that each of these elements in the set is a point on the unit complex circle. They are are squares of the complex number when $k=1$. Hence represent some angle multiple of $360\degree/n$.

##### Vector Example
The set $\mathbf R^n=\{(a_1,a_2,....,a_n)|a_1,a_2,...,a_n\in\mathbf R\}$ is a group under component wise addition.

##### Special Linear Group
The set $SF(2,Q\cup\mathbf R\cup\mathbf C\cup Z_p)$ of all $2\times2$ matrices with determinant $1$ with entries from $Q$, $\mathbf R$, $\mathbf C$ or $Z_p$ ($p$ a prime) is a non-Albian group under matrix multiplication. Here $A$ is the **special linear group** over $Q,\mathbf R, \mathbf C$ and $Z_p$. When $A=\begin{bmatrix}a&b\\c&d\end{bmatrix}$ and $\det = 1$ the inverse will be $\begin{bmatrix}a&-b\\-c&d\end{bmatrix}$. Not of course this set doesn't contain $0$ as $\det 0=0$.

We can also defined $GL(n,F)$ as the **general linear group** over $F$ then this also contains matrices with non-zero determinants.

##### Prime Modulo Example
The set $\{1,2,...,n-1\}$ is a group under multiplication iff $n$ is prime.

### Summary of Example Groups

![[Pasted image 20230102185748.png]]

Overall groups are a broad category. This allow this approach to be used in many areas however still allows interesting properties to still be deduced. This filed seeks to discover truths about algebraic systems (sets with one or more binary operations). But this should be independent of the specific operations.

### Elementary Properties of Groups
We might ask if there can be more than one identity. Note then that if we do have two identities $e$ and $e'$ then we know from the properties of some group $G$ they are identities for that. 

1. $ae=a$ for all $a$ in $G$ 
2. $e'a=a$ for all $a$ in $G$.

Then if we pick $a=e'$ for 1) and $a=e$ for 2) then we get $$e=e'e=e'$$ That is the identities are the same. There can only be one

##### Uniqueness of the Identity
![[Pasted image 20230102175004.png]]


##### Cancelation
![[Pasted image 20230102175133.png]]

This proof is simple, we know $ba=ca$. Then $a$ has an inverse $a'$. Then right multiplying by $a'$ yields $(ba)a'=(ca)a'$ then by *associativity* we get $b(aa')=c(aa')$ by the definition of the inverse we then get $be=ce$ and so $b=c$. This also implies that for some **Caley table** an element in the group only exists once in each row and column.

##### Uniqueness of Inverse
![[Pasted image 20230102175844.png]]

If there are two inverses $b$ and $b'$ then $b'a=e=ba$. But by the calculation property above this would mean $b'=b$ hence there is only one inverse.

Because of the **unique inverse** we can call *the* inverse of $g$ the name $g^{-1}$. We can also say that for any group if we have a system such that $a$ and $b$ are in $G$ then the system $ax=b$ can be solved when $x=a^{-1}b$ then $ax=a(a^{-1}b)=(aa^{-1})b=eb=b$.

Note: For groups where that addition symbol $+$ is used we would call $b$'s inverse $-b$ to be clear. Other differences of summarized below.

![[Pasted image 20230102180941.png]]

##### Socks-Shoes Property
![[Pasted image 20230102181220.png]]

We have $(ab)^{-1}(ab)=e$ but by associativity and *cancellation* we also get $b^{-1}a^{-1}(ab)=e$ hence by *cancellation* again $(ab)^-1=b^{-1}a^{-1}$.