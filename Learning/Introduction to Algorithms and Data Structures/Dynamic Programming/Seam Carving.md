## Seam Carving
We need to fit images into new dimensions for resizable layouts. Where the key objects are kept and non-key elements are removed. We do this by removing vertical and horizontal seams. A vertical seam is a connected sequence of pixels running from the top-to-bottom (left to right if horizontal). It must go down and only 1 left or 1 right. A good seam is similar to neighboring seams and we say it has low energy. The energy will be the difference between a pixel and its neighbors.

#### Specification
We are given an image $I: [m]\textrm{x}[n]$ where we have $m$ rows and $n$ columns. Each entry will have a color. 
![[Pasted image 20220124134453.png]]
*The second condition stops our seam from going to the edges*

We want a seam with low **energy** so we want to find the seam with total lowest **energy** where the sum energy is the sum of all the energies in the seam.
![[Pasted image 20220124134811.png]]

## Energy functions
We have many options for energy functions, will often use a (local) **gradient** score. There are different ways of capturing gradient in image processing. A basic L1 gradient is a sum of the horizontal and vertical change.
$$
e_1(i,j)=_{\textrm{def}}|\frac{\delta}{\delta x}I|_{ij}+|\frac{\delta}{\delta y}I|_{ij}$
$$
For example the **Sobel operators** can be used to calculate $\frac{\delta}{\delta x}$ and $\frac{\delta}{\delta x}$.
![[Pasted image 20220124152146.png]]
There can be different weights however. We would also take into account color change. But this will take $O(1)$ time to calculate.

## Finding a Seam of Minimum Energy
We will look at the vertical case. We want to find a dynamic programming solution. First we want a **recurrence** relation. We know if we have a solution in $m-1$ rows for example we can more easily calculate for $m$ rows. If a seam ends at a pixel $(m, j_m$) then we know that the second last pixel in the seam will be one of $(m-1,j_{m-1})$, $(m-1,j_{m})$, $(m-1,j_{m+1})$. We are refactoring the problem to find the best path ending in a given cell.

We are writing a function $opt(i,j)$ to find the cost of the minimum-cost vertical seam form somewhere ending in pixel $(i,j)$
![[Pasted image 20220124153144.png]]
Setting $e_I$ to $\infty$ makes sure we don't go the edges of the image.

To solve the problem we will have an $\textrm{opt}[i,j]$ array to keep track of the opt values. We will then keep another table $p[i,j]$ keeping track of the previous pixel from $(i,j)$ with the best value. Each table is bounded $[m]\textrm{x}[n]$. Since the $\textrm{opt}$ table only relied on the last row we can build it up row by row to get a solution.
![[Pasted image 20220124154023.png]]
This will be our solution in this case. To calculate each opt it will take $O(1)$ work since its just finding the min of 3. We have to do this for the whole image so it is $O(nm)$ for finding all $\textrm{opt}$ values. The last loop will take $O(n)$ time. Then the top is $O(nm)$ hence overall it is $O(mn)$ time.