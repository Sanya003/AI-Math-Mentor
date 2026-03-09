# Vectors

A vector has both **magnitude** and **direction**.

\[
\vec{a} = a_1\hat{i} + a_2\hat{j} + a_3\hat{k}
\]

---

## Magnitude

\[
|\vec{a}| = \sqrt{a_1^2 + a_2^2 + a_3^2}
\]

---

## Unit Vector

\[
\hat{a} = \frac{\vec{a}}{|\vec{a}|}
\]

---

## Dot Product (Scalar Product)

\[
\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos\theta = a_1 b_1 + a_2 b_2 + a_3 b_3
\]

Two vectors are **perpendicular** if:

\[
\vec{a} \cdot \vec{b} = 0
\]

Projection of \(\vec{a}\) onto \(\vec{b}\):

\[
\text{proj} = \frac{\vec{a} \cdot \vec{b}}{|\vec{b}|}
\]

---

## Cross Product (Vector Product)

\[
\vec{a} \times \vec{b} =
\begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
a_1 & a_2 & a_3 \\
b_1 & b_2 & b_3
\end{vmatrix}
\]

\[
|\vec{a} \times \vec{b}| = |\vec{a}||\vec{b}|\sin\theta
\]

This equals the **area of the parallelogram** formed by \(\vec{a}\) and \(\vec{b}\).

Two vectors are **parallel** if \(\vec{a} \times \vec{b} = \vec{0}\).

---

## Scalar Triple Product

\[
[\vec{a}\;\vec{b}\;\vec{c}] = \vec{a} \cdot (\vec{b} \times \vec{c}) = \det\begin{bmatrix}a_1&a_2&a_3\\b_1&b_2&b_3\\c_1&c_2&c_3\end{bmatrix}
\]

Vectors are **coplanar** if and only if:

\[
[\vec{a}\;\vec{b}\;\vec{c}] = 0
\]

\(|[\vec{a}\;\vec{b}\;\vec{c}]|\) gives the **volume of the parallelepiped**.

---

## Angle Between Two Vectors

\[
\cos\theta = \frac{\vec{a} \cdot \vec{b}}{|\vec{a}||\vec{b}|}
\]

Example: \(\vec{a} = (1,0,0)\), \(\vec{b} = (1,1,0)\):

\[
\cos\theta = \frac{1}{\sqrt{2}} \implies \theta = 45°
\]
