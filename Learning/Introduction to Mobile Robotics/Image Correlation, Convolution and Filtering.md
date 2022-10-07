# Image Correlation Convolution and Filtering
*Convolutions and filtering* are often used to analyze images. We will use the example of identifying "denticles" in an image to illustrate this. We may have an image (left) wish to identify the "denticles" in it which are the triangle shapes. The template $\textbf T$ can be obtained by **averaging and blurring** one or more denticles together. We can then sweep this template over possible positions $(r,c)$ and compare it to the window $\textbf W(r,c)$ at the same position.

![[Pasted image 20221006141314.png]]

A simpler situation is comparing vectors $\textbf t$ and $\textbf w$. We can take their *inner (dot) product* as a measure of their similarity. $$p(r,c)=\tau^T\omega(r,c)$$Where $\tau$ and $\omega$ are the *normalized* versions of $\textbf t$ and $\textbf w$. $$\tau=\frac{\textbf t-\textbf m_t}{||\textbf t-\textbf m_t||}\hspace{32pt}\omega=\frac{\textbf w-\textbf m_w}{||\textbf t-\textbf m_w||}$$Where $m_t$ and $m_w$ are the mean values for $\textbf t$ and $\textbf w$. This value will be the $\cos$ of the angle between the two unit vectors. Hence $$-1\le p(r,c)\le1$$The value is 1 when $\textbf W(r,c)=\alpha\textbf T+\beta$ for some $\alpha$ and $\beta$. That is $\textbf W$ is some scaled (contrast resistant) and offset (brightness resistant) versions of the template $\textbf T$ when $p(r,c)=1$. In the opposite case it will have a negative number $\alpha$.

##### Cross-correlation
When we calculate the inner product of a template and a window this is called **cross-correlation**. If we normalize first it is called **normalized cross-correlation**.

Now every $(r,c)$ yields a value $p$ so we can create another image f these values which can now be positive or negative.

The inner product without normalization for some image $I$ and template $T$ will product a new image $J$ according to:

![[Pasted image 20221006142755.png]]

Where $h$ is the height of the template. Then $I$ is at least $2h+1$ in side such that $J$ can be defined for some values of $(r,c)$.

![[Pasted image 20221006143116.png]]

![[Pasted image 20221006143044.png]]