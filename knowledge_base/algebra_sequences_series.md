# Sequences and Series

A sequence is an ordered list of numbers. A series is the sum of a sequence.

---

## Arithmetic Progression (AP)

An AP has a constant difference \(d\) between consecutive terms.

General term:

\[
a_n = a + (n-1)d
\]

Sum of \(n\) terms:

\[
S_n = \frac{n}{2}[2a + (n-1)d] = \frac{n}{2}(a + l)
\]

where \(l\) is the last term.

Example: AP is \(2, 5, 8, \ldots\), find \(S_{10}\):

\[
a = 2,\; d = 3,\; S_{10} = \frac{10}{2}[4 + 9(3)] = 5 \times 31 = 155
\]

---

## Geometric Progression (GP)

A GP has a constant ratio \(r\) between consecutive terms.

General term:

\[
a_n = a \cdot r^{n-1}
\]

Sum of \(n\) terms \((r \neq 1)\):

\[
S_n = \frac{a(r^n - 1)}{r - 1}
\]

Sum to infinity \((|r| < 1)\):

\[
S_\infty = \frac{a}{1 - r}
\]

Example: GP \(3, 6, 12, \ldots\), find \(S_5\):

\[
r = 2,\; S_5 = \frac{3(2^5 - 1)}{2 - 1} = 3 \times 31 = 93
\]

---

## Harmonic Progression (HP)

\(a, b, c\) are in HP if \(\frac{1}{a}, \frac{1}{b}, \frac{1}{c}\) are in AP.

Harmonic Mean:

\[
H = \frac{2ab}{a+b}
\]

---

## AM–GM–HM Inequality

For positive numbers:

\[
AM \geq GM \geq HM
\]

\[
\frac{a+b}{2} \geq \sqrt{ab} \geq \frac{2ab}{a+b}
\]

Equality holds when \(a = b\).

---

## Standard Summation Formulas

\[
\sum_{k=1}^{n} k = \frac{n(n+1)}{2}
\]

\[
\sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}
\]

\[
\sum_{k=1}^{n} k^3 = \left[\frac{n(n+1)}{2}\right]^2
\]
