# Polynomials

A polynomial is an expression consisting of variables and coefficients.

General form:

\[
P(x) = a_n x^n + a_{n-1}x^{n-1} + \cdots + a_1 x + a_0
\]

---

## Degree of a Polynomial

The highest power of \(x\) determines the degree.

Example:

\[
P(x) = 3x^4 + 2x^2 + 1
\]

Degree = 4

---

## Polynomial Roots

If

\[
P(x) = 0
\]

then the solutions are called **roots**.

Example:

\[
x^2 - 5x + 6 = 0
\]

\[
(x-2)(x-3) = 0
\]

Roots:

\[
x = 2,\; 3
\]

---

## Remainder Theorem

When \(P(x)\) is divided by \((x - a)\), the remainder is \(P(a)\).

Example:

\[
P(x) = x^3 - 4x + 1, \quad \text{divided by } (x-2)
\]

\[
P(2) = 8 - 8 + 1 = 1 \quad \Rightarrow \quad \text{Remainder} = 1
\]

---

## Factor Theorem

\((x - a)\) is a factor of \(P(x)\) if and only if \(P(a) = 0\).

Example:

\[
P(x) = x^3 - 3x^2 + 2x, \quad P(0) = 0
\]

So \((x - 0) = x\) is a factor.

---

## Vieta's Formulas

For \(a_n x^n + \cdots + a_0 = 0\) with roots \(r_1, r_2, \ldots, r_n\):

\[
\sum r_i = -\frac{a_{n-1}}{a_n}
\]

\[
\prod r_i = (-1)^n \frac{a_0}{a_n}
\]

Example for cubic \(ax^3 + bx^2 + cx + d = 0\) with roots \(\alpha, \beta, \gamma\):

\[
\alpha+\beta+\gamma = -\frac{b}{a}
\]

\[
\alpha\beta+\beta\gamma+\gamma\alpha = \frac{c}{a}
\]

\[
\alpha\beta\gamma = -\frac{d}{a}
\]
