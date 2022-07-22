# Binary Classification	
This is a very simple task in machine learning basically we take some input and classify it to into a true class or false class. This could be in say an image contains cats or not. In a simple network we must first unroll our network into a vector. An image is a WxH 2D array of pixel values. If we have multiple values for different color channels we will also have say 3 channels for each image. Therefore the size of this *feature vector* will be $n_x=WHC=64\cdot64\cdot3=1288$. Where C is the number of color channels. If we have $m_{train}$ training examples of the form for *supervised learning* $$\{(x^{(1)},y^{(1)}),(x^{(1)},y^{(1)}),...,(x^{(m)},y^{(m)})\}$$ We can also define a matrix $X=[x^{(1)},x^{(2)},...,x^{(m)}]$ made by stacking all the $x$s in columns. It will have $m$ columns and be $n_x$ high. We can also a matrix $Y=[y^{(1)},y^{(2)},...,y^{(m)}]$ which is a $1\times m$ matrix of the labels. We would say $X.shape=(n_x,m)$ and $Y.shape=(1,m)$ with the first number being the number of rows and the second being the number of columns.

# Logistic Regression
When we are predicting a binary class we may use a model taking in our feature factor $x^{(i)}$ weighting each feature by some weight vector $w$ and adding on a bias $b$. Our prediction becomes $\hat y=w^Tx^{(i)}+b$. But we want a binary class and this will simply output. We want to know if  $\hat y$ belongs to our true or false class. But this model will output a linear function where the values can be very negative or very positive or anywhere between. Instead we can use a **sigmoid** function. This take very large numbers and makes them close to 1 and very small numbers close to 0. It is defined as $$\sigma(x)=\frac{1}{1+e^{-x}}$$ Very small negative numbers becomes $1/1+e^{\text{very large number}}$ hence approach 0 and very large numbers becomes $1/1+e^{\text{very negative number}}$ hence approach 1. The graph of this function is.

![[Pasted image 20220708140649.png]]

So we can instead use the model $\hat y=\sigma(w^tx^{(i)}+b)$. Now we need a **loss function** which we can use to learn $w$ and $b$. One option is the squared difference between the true label $y$ and the predicted label $\hat y$. That is $\mathcal L(\hat y,y)=\frac12(\hat y-y)^2$ but this has a *nonconvex* geometry when we try to optimize it and gradient descent based methods will get stuck in local minima.  Instead we can use $$\mathcal L(\hat y, y)=-(y\hspace{3pt}log(\hat y)+(1-y)\hspace{3pt}log(1-\hat y))$$
We can examine how this looks by seeing what happens when $y=1$ and $y=0$ (our true label). If $y=1$ then this reduces to $-log(\hat y)$ hence the closer $\hat y$ is to 0 (the wrong answer) the loss is massive. Then the opposite when $y=0$ it reduces to $-log(1-\hat y)$ hence is very large when $\hat y\to1$.

The *loss function* is defined on just a single example but the **cost function** is defined over the whole training examples. It will be $$J(w,b)=\frac1m\sum_{i=1}^m\mathcal L(\hat y^{(i)},y^{(i)})=-\frac1m\left[y^{(i)}log(\hat y^{(i)})+(1-y^{(i)})log(1-\hat y^{(i)})\right]$$
Now in training we want to find the parameters $w$ and $b$ that minimize $J$.

### Gradient Descent
To find $w$ and $b$ we will use the gradient descent algorithm. The basic way this works it we take the high dimensional derivative of $J(w,d)$ with respect to all the different dimensions of $w$ and the value $b$. This gives us the direction we should shift $w$ and $b$ to maximize $J$ and we take this away to minimize $J$.  We then take of a small fraction of this direction $\alpha$ the **learning rate** repeatedly until we converge on some value.$$w:=w-\alpha\frac{\delta J(w,b)}{\delta w}$$ Then we updates $b$ as $$b:=b-\alpha\frac{\delta J(w,b)}{\delta b}$$

### Computation Graph
This describes some computation we might execute. We can take some example $J(a,b,c)=3(a+bc)$. There are actually three computations to do this. $u=bc$, $v=a+u$ and finally $J=3v$. This will give the following *computational graph*

![[Pasted image 20220708145501.png]]

This kind of graph helps us optimize $J$ just as we want when $J$ is the *cost function*. To compute the output we go from left to right and to compute *derivatives* to optimize our model we go from right to left.

### Derivatives with a Computation Graph
We have the following computation graph for $J$ and we want to optimize $J$.

![[Pasted image 20220708145535.png]]

So we first want to understand how a change in $v$ affects $J$.  We can find since $J=3v$ that $\frac{dJ}{dv}=3$. The increase in $J$ is three times the increase in $v$. Now we might want to know how $a$ affects $J$. We can say that $\frac{dJ}{dv}=3$ and since $\frac{dv}{da}=1$ then $\frac{dJ}{da}=3$ as $a$ changes $J$ through $v$ $\frac{dJ}{da}=\frac{dJ}{dv}\frac{dv}{da}$. To having calculates a derivative closer to $J$ we can calculate the derivative for a values closer to the raw values. Hence the idea of back propagation. As a convention $dvar$ often refers to the change in the output value with respect to $var$.

### Logistic Regression Gradient Descent
In *logistic regression* our variables are set up as follows:

![[Pasted image 20220708151527.png]]

This can be written as a computation graph we will assume there are only two dimensions so two features $x_1$ and $x_2$. This will give the following *computation graph*

![[Pasted image 20220708151757.png]]

We want to modify $w_1$, $w_2$ ($w$) and $b$ to minimize $\mathcal L(a,y)$, We first want to calculate the change in the loss with respect to $a$ which becomes $da=\frac ya+\frac{1-y}{1-a}$  through calculus. Now that we know $da$ we can find $dz=\frac{\mathcal L}{dz}=\frac{d\mathcal L(a,y)}{dz}=a-y$. Then we can find $dw_1=x_1dz$ and $dw_2=x_2dz$ and $d_b=d_z$. Then we can take all these gradients of our values. But this is just for a single example so we need to compute the same for $J$ instead of $\mathcal L$.

The *cost function* is the average *loss* over all examples. We have found $dw_1^{(i)}$, $dw_1^{(i)}$ and $db^{(i)}$ and it can be found that the derivative of the average of these is just the average of their derivatives. That is $$\frac{\delta}{\delta w_1}J(w,b)=\frac1m\sum_{i=1}^m\frac{\delta}{\delta w_i}\mathcal L\left(a^{(i)},y^{(i)}\right)$$So we just need to average the gradients over all the samples to get the gradient change to implement *gradient descent*.

[[Binary Classification and Logistic Regression Questions]]