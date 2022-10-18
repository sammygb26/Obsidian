How can two vectors similarity be compared? #flashcard #MOB #ImageCorrConvFilter
	Two vectors can be compared by taking their inner product with where we also normalize the vectors. $$p(r,c)=\tau^T\omega(r,c)$$ where $$\tau=\frac{\textbf t-\textbf m_t}{||\textbf t-\textbf m_t||}\hspace{32pt}\omega=\frac{\textbf w-\textbf m_w}{||\textbf t-\textbf m_w||}$$

---
How can comparing vectors be scaled up to matrices? #flashcard #MOB #ImageCorrConvFilter 
	We can use the same trick taking the say an $n\times n$ matrix to be and $n^2$-dimensional vector. Then taking the dot product of the two normalized vectors.

---
When we have a matrix and a template and their similarity is 1 what relation holds between them? #flashcard #MOB #ImageCorrConvFilter 
	At this point we know that one is just a scaled and shifted version of the other as they are the same when normalized. That is $$\textbf W=\alpha\textbf T+\beta$$

---
What calculation takes place in cross-correlation and normalized cross-correlation? #flashcard #MOB #ImageCorrConvFilter 
	Here we perform an inner product between the vector conversions of our two matrices. If it is normalized then we also normalize these vectors before taking the product.

---
How does cross-correlation between a filter and an image lead to a new image? #flashcard #MOB #ImageCorrConvFilter 
	Each cross-correlation we perform takes place between two matrices one of which is defined by a 2D index into the image. So we can make a new image where each value is given by the correlation passing in its indices. $$I(r, c)=\textbf T^T\textbf W(r,c)$$

---
