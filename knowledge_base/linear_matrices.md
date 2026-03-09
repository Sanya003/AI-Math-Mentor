# Matrices

A matrix is a rectangular array of numbers arranged in rows and columns.

Example:

\[
A =
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
\]

---

## Matrix Addition

Matrices can be added if they have the same dimensions.

\[
A + B =
\begin{bmatrix}
a_{11}+b_{11} & a_{12}+b_{12} \\
a_{21}+b_{21} & a_{22}+b_{22}
\end{bmatrix}
\]

---

## Matrix Multiplication

If \(A\) is \(m \times n\) and \(B\) is \(n \times p\), then \(AB\) is \(m \times p\):

\[
(AB)_{ij} = \sum_{k=1}^{n} a_{ik} \cdot b_{kj}
\]

Example:

\[
\begin{bmatrix}1 & 2\\3 & 4\end{bmatrix}
\begin{bmatrix}5 & 6\\7 & 8\end{bmatrix}
=
\begin{bmatrix}19 & 22\\43 & 50\end{bmatrix}
\]

---

## Transpose

Flip rows and columns:

\[
(A^T)_{ij} = A_{ji}
\]

\[
(AB)^T = B^T A^T
\]

---

## Types of Special Matrices

**Symmetric:** \(A = A^T\)

**Skew-symmetric:** \(A = -A^T\) (diagonal entries must be 0)

**Identity matrix:**

\[
I = \begin{bmatrix}1 & 0\\0 & 1\end{bmatrix}, \quad AI = IA = A
\]

**Orthogonal:** \(A^T A = I \implies A^{-1} = A^T\)

---

## Inverse of a 2×2 Matrix

\[
A = \begin{bmatrix}a & b\\c & d\end{bmatrix}
\implies
A^{-1} = \frac{1}{ad-bc}\begin{bmatrix}d & -b\\-c & a\end{bmatrix}
\]

Inverse exists only when \(\det(A) = ad - bc \neq 0\).

Example:

\[
A = \begin{bmatrix}2 & 1\\5 & 3\end{bmatrix},\quad \det(A) = 1
\]

\[
A^{-1} = \begin{bmatrix}3 & -1\\-5 & 2\end{bmatrix}
\]
