To detect corners we need to look for a sharp change in gradients. The gradient is described as $$\frac{\partial\mathcal I}{\partial x}=\lim_{\partial x\to0}\frac{\mathcal I(x+\partial x,y)-\mathcal I(x,y)}{\partial x}\approx\mathcal I_{i+1,j}-\mathcal I_{i,j}$$ Then similarly we have $\partial\mathcal I/\partial y\approx \mathcal I_{i,j+1}-\mathcal I_{i,j}$. These estimates are called **finite differences**. An issue with this types of differentiation is it is sensitive to noise so we smooth the image and then perform this. It also may work to *smooth the derivative*.

However this is the same as convolving the image with some kernel since we are calculating a finite difference then smoothing that (a convolution). We think of some differentiating kernel $K$ such that$$\frac{\partial I}{\partial x}=K_{(\partial/\partial x)}**I$$ Then the smoothing function with be another kernel $S$ giving $$(K_{(\partial/\partial x)}**(S**I))=(K_{(\partial/\partial x)}**S)**I=\left(\frac{\partial S}{\partial x}\right)**I$$ Hence we only convolve with the **derivative** of the smoothing function and nothe actual smoothing function then he differentiating function.

### Edge Detection
Sharp changes in image intensity are interpreted as edges. They are made out of edge points. This cannot always be done say if an object blends into the background.  One method to detection the edges and their edge points is as follows:

![[Pasted image 20221216221038.png]]

### Orientation
A problem with the above approach is that as the brightness of the image changes the image is scaled. That is $\mathcal I$ is replaced by $s\mathcal I$ then the gradient is similarly scaled that is $||\nabla \mathcal I||$ is replaced by $s||\nabla I||$. This is a problem for our edge detectors as edge points will appear and disappear. Instead the **orientation** can be used.

### Corners
One way to find corners is to find edges. Then looking for the corner. This works poorly because edge detectors often fail at corners! This can be due to the smoothing region covering the corner. At a corner we expect to important affects. 

1. There should be large gradients.
2. In a small neighborhood the gradient orientation should swing sharply.

So we identify corners by looking for variations of orientation within a small window. The matrix:

![[Pasted image 20221216223409.png]]

give a good idea of the behavior of the orientation in a window. In a section of constant gray level both eigen values of this matrix are small because all there terms are small. In an edge window we expect large eigen value associated with gradients. The **Harris Corner detector** looks for the local maxima of $$\det(\mathcal H)-k\left(\frac{\text{trace}(\mathcal H)}{2}\right)^2$$where $k$ is some constant (like 0.5). The local maxima are tested against a threshold. This tests whether the produce of the eigenvalues ($\det(\mathcal H)$) is larger than the square of the average.

### Using Scale and Orientation to Build a Neighborhood
Whatever method we choose to build a neighborhood around a corners we want to estimate the radius of a circle for this neighborhood and this should be invariant to scaling the image.  An efficient way to to do this is to use the Laplacian of the function which in 2D is defined as $$(\nabla^2f)(x,y)=\frac{\partial^2f}{\partial x^2}+\frac{\partial^2f}{\partial y^2}$$ The Laplacian is a **linear operator** so we can use a kernel to approximate this. It is natural to smooth the image before this and so similarly to with gradients we can just convolve with the Laplacian of the smoothing function due to

![[Pasted image 20221216225009.png]]

If we apply this operator to an image at the center of the patch. The image will be $\mathcal I$, $\nabla_\sigma^2$ will be the smoothed Laplacian operator with smoothing constant $\sigma$. $\uparrow k\mathcal I$ for the image with size scaled by $k$, $(x_c,y_c)$ for the coordinates of the patch center and $(x_{kc},y_{kc})$ for the coordinates of the patch center while scaled. Then we have $$(\nabla^2_{k\sigma}\uparrow k \mathcal I)(x_c,y_c)=(\nabla^2_\sigma\mathcal I)(x_{kc},y_{kc})$$ Now choose a radius $r$ for the circular patched centered at $(x_c, y_c)$  sch that $$r(x_c,y_c)=\arg\max_\sigma\nabla^2_\sigma\mathcal I(x_c,y_c)$$If the image is scaled by $k$ then this value of $r$ will be scaled by $k$ too as is required. This corner and radius can be identified as $(x,\sigma)$ we want to detect these such that we will get the same set of them for the two images $\mathcal I$ and $\mathcal I'$ when $\mathcal I'(x)=\mathcal I(\lambda x+c)$ is a scaled translated image. Then we have $(x,\sigma)$ in the first image give $(\lambda x+c,\lambda \sigma)$ in the second. This property is called *covariance*.

