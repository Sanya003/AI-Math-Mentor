# Systems of Linear Equations

A system of linear equations can be written in matrix form:

\[
AX = B
\]

where \(A\) is the coefficient matrix, \(X\) is the column of unknowns, and \(B\) is the constants column.

---

## Cramer's Rule

For a system with \(\det(A) \neq 0\):

\[
x_i = \frac{\det(A_i)}{\det(A)}
\]

where \(A_i\) is matrix \(A\) with the \(i\)-th column replaced by \(B\).

Example: Solve \(2x + y = 5\) and \(5x + 3y = 13\):

\[
A = \begin{bmatrix}2&1\\5&3\end{bmatrix}, \quad \det(A) = 1
\]

\[
\det(A_1) = \begin{vmatrix}5&1\\13&3\end{vmatrix} = 2, \quad
\det(A_2) = \begin{vmatrix}2&5\\5&13\end{vmatrix} = 1
\]

\[
x = \frac{2}{1} = 2, \quad y = \frac{1}{1} = 1
\]

---

## Matrix Inverse Method

\[
X = A^{-1}B \quad \text{(only when } \det(A) \neq 0\text{)}
\]

---

## Consistency (Rouché–Capelli Theorem)

Let \(\rho(A)\) denote the rank of matrix \(A\).

| Condition | Solution |
|-----------|----------|
| \(\rho(A) = \rho([A\|B]) = n\) | Unique solution |
| \(\rho(A) = \rho([A\|B]) < n\) | Infinitely many solutions |
| \(\rho(A) \neq \rho([A\|B])\) | No solution (inconsistent) |

---

## Homogeneous System

\[
AX = 0
\]

Always has the trivial solution \(X = 0\).

Non-trivial solutions exist when:

\[
\det(A) = 0
\]

---

## Row Reduction (Gaussian Elimination)

Write the augmented matrix \([A \mid B]\) and reduce to row echelon form.

Example: Solve \(x + y = 3\), \(2x - y = 0\):

\[
\begin{bmatrix}1&1&3\\2&-1&0\end{bmatrix}
\xrightarrow{R_2 - 2R_1}
\begin{bmatrix}1&1&3\\0&-3&-6\end{bmatrix}
\]

\[
y = 2, \quad x = 1
\]
