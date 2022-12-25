For 2D matrices we have a simple formula

![[Pasted image 20221218142313.png]]

For a more complicated 3D matrix we can make a formula by trying to reduce the matrix to an identity matrix through. This yields

![[Pasted image 20221218142511.png]]

This suggests an inductive method for defining the determinant of any square matrix in terms of the determinants of smaller matrices. So for a $4\times4$ matrix we use $3\times3$ matrix determinants and so on. To describe this we give the definition of **cofactors** as

![[Pasted image 20221218142834.png]]

The sign of the cofactor $(-1)^{i+j}$ gives a checkerboard patter for the whole matrix meaning depending on where the cofactor is taken it will be inverted or not.

![[Pasted image 20221218143006.png]]

Then we can define the  cofactor expansion of a matrix as

![[Pasted image 20221218143105.png]]

This asserts that $\det A$ can be computer by entries of row $1$ multiplied by their corresponding cofactors. But this can actually be done for any row or column.

![[Pasted image 20221218143242.png]]

This allows us to determine the determinant of any square matrix.