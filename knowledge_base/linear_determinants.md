# Determinants

The determinant is a scalar value computed from a square matrix.

---

## 2×2 Determinant

\[
\det\begin{pmatrix}a & b\\c & d\end{pmatrix} = ad - bc
\]

Example:

\[
\det\begin{pmatrix}3 & 2\\1 & 4\end{pmatrix} = 12 - 2 = 10
\]

---

## 3×3 Determinant (Cofactor Expansion)

Expand along the first row:

\[
\det(A) = a_{11}(a_{22}a_{33} - a_{23}a_{32}) - a_{12}(a_{21}a_{33} - a_{23}a_{31}) + a_{13}(a_{21}a_{32} - a_{22}a_{31})
\]

---

## Key Properties

Swapping two rows **negates** the determinant:

\[
\det(A') = -\det(A)
\]

If two rows are identical:

\[
\det(A) = 0
\]

Scalar multiplication:

\[
\det(kA) = k^n \det(A) \quad \text{for } n \times n \text{ matrix}
\]

Product rule:

\[
\det(AB) = \det(A) \cdot \det(B)
\]

Transpose:

\[
\det(A^T) = \det(A)
\]

---

## Singular Matrix

A matrix is **singular** (no inverse) when:

\[
\det(A) = 0
\]

---

## Adjoint and Inverse

Cofactor \(C_{ij} = (-1)^{i+j} M_{ij}\) where \(M_{ij}\) is the minor.

\[
\text{adj}(A) = \text{transpose of cofactor matrix}
\]

\[
A^{-1} = \frac{\text{adj}(A)}{\det(A)}
\]

Key identity:

\[
A \cdot \text{adj}(A) = \det(A) \cdot I
\]
