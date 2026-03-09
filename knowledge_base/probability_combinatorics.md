# Permutations and Combinations

Counting techniques used to compute sample spaces and events.

---

## Fundamental Counting Principle

If task 1 can be done in \(m\) ways and task 2 in \(n\) ways:

\[
\text{Total ways} = m \times n
\]

---

## Permutations

Ordered arrangements of \(r\) objects from \(n\):

\[
^nP_r = \frac{n!}{(n-r)!}
\]

Example: Arrange 3 letters from \(\{A, B, C, D\}\):

\[
^4P_3 = \frac{4!}{1!} = 24
\]

---

## Combinations

Unordered selections of \(r\) objects from \(n\):

\[
^nC_r = \binom{n}{r} = \frac{n!}{r!(n-r)!}
\]

Example: Choose 3 students from 5:

\[
\binom{5}{3} = \frac{5!}{3! \cdot 2!} = 10
\]

---

## Key Properties

\[
\binom{n}{r} = \binom{n}{n-r}
\]

\[
\binom{n}{0} = \binom{n}{n} = 1
\]

\[
\binom{n}{r} + \binom{n}{r+1} = \binom{n+1}{r+1} \quad \text{(Pascal's identity)}
\]

---

## Circular Arrangements

Arranging \(n\) distinct objects in a circle:

\[
(n-1)!
\]

Example: 5 people around a table:

\[
(5-1)! = 4! = 24
\]

---

## Arrangements with Repetition

\(n\) objects where \(p\) are of type 1, \(q\) of type 2, \(r\) of type 3:

\[
\frac{n!}{p!\; q!\; r!}
\]

Example: Arrangements of MATHEMATICS (11 letters: M×2, A×2, T×2):

\[
\frac{11!}{2!\cdot 2!\cdot 2!} = \frac{39916800}{8} = 4989600
\]
