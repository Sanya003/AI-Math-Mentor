# Probability Basics

Probability measures the likelihood of events.

\[
0 \leq P(A) \leq 1
\]

---

## Probability Formula

\[
P(A) = \frac{\text{Favourable outcomes}}{\text{Total outcomes}}
\]

Example: Rolling a die.

\[
P(4) = \frac{1}{6}
\]

---

## Complement Rule

\[
P(A^c) = 1 - P(A)
\]

Example: Probability of **not getting 6** on a die:

\[
P(A^c) = \frac{5}{6}
\]

---

## Addition Rule

\[
P(A \cup B) = P(A) + P(B) - P(A \cap B)
\]

For **mutually exclusive** events \((P(A \cap B) = 0)\):

\[
P(A \cup B) = P(A) + P(B)
\]

Example: Drawing a king **or** a heart from a deck:

\[
P = \frac{4}{52} + \frac{13}{52} - \frac{1}{52} = \frac{16}{52} = \frac{4}{13}
\]

---

## Addition Rule for Three Events

\[
P(A \cup B \cup C) = P(A)+P(B)+P(C) - P(A\cap B) - P(B\cap C) - P(A\cap C) + P(A\cap B\cap C)
\]

---

## Independent Events

Events \(A\) and \(B\) are **independent** if:

\[
P(A \cap B) = P(A) \cdot P(B)
\]

Example: Tossing two coins. \(P(\text{HH}) = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}\)
