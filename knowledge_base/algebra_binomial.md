# Binomial Theorem

The Binomial Theorem expands powers of a binomial expression.

\[
(a + b)^n = \sum_{r=0}^{n} \binom{n}{r} a^{n-r} b^r
\]

where \(\binom{n}{r} = \dfrac{n!}{r!(n-r)!}\)

---

## General Term

The \((r+1)\)-th term in the expansion of \((a+b)^n\):

\[
T_{r+1} = \binom{n}{r} a^{n-r} b^r
\]

Example: Find \(T_4\) in \((x + 2)^7\):

\[
T_4 = \binom{7}{3} x^4 (2)^3 = 35 \cdot x^4 \cdot 8 = 280x^4
\]

---

## Middle Term

- If \(n\) is **even**: one middle term at \(T_{\frac{n}{2}+1}\)
- If \(n\) is **odd**: two middle terms at \(T_{\frac{n+1}{2}}\) and \(T_{\frac{n+3}{2}}\)

Example: Middle term in \((x + 1)^8\):

\[
T_5 = \binom{8}{4} x^4 = 70x^4
\]

---

## Term Independent of x

Set the power of \(x\) in \(T_{r+1}\) equal to zero and solve for \(r\).

Example: Find term independent of \(x\) in \(\left(x + \dfrac{1}{x}\right)^6\):

\[
T_{r+1} = \binom{6}{r} x^{6-r} \cdot x^{-r} = \binom{6}{r} x^{6-2r}
\]

Set \(6 - 2r = 0 \implies r = 3\):

\[
T_4 = \binom{6}{3} = 20
\]

---

## Coefficient Properties

\[
\binom{n}{0} + \binom{n}{1} + \cdots + \binom{n}{n} = 2^n
\]

\[
\binom{n}{0} - \binom{n}{1} + \binom{n}{2} - \cdots = 0
\]

\[
\binom{n}{r} = \binom{n}{n-r} \quad \text{(symmetry)}
\]

Pascal's identity:

\[
\binom{n}{r-1} + \binom{n}{r} = \binom{n+1}{r}
\]
