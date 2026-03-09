# Conditional Probability

Conditional probability is the probability of event \(A\) **given** that \(B\) has occurred.

\[
P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) \neq 0
\]

---

## Multiplication Rule

\[
P(A \cap B) = P(A \mid B) \cdot P(B) = P(B \mid A) \cdot P(A)
\]

For three events:

\[
P(A \cap B \cap C) = P(A) \cdot P(B \mid A) \cdot P(C \mid A \cap B)
\]

---

## Independence via Conditional Probability

\(A\) and \(B\) are independent if and only if:

\[
P(A \mid B) = P(A)
\]

---

## Total Probability Theorem

If \(B_1, B_2, \ldots, B_n\) are mutually exclusive and exhaustive events:

\[
P(A) = \sum_{i=1}^{n} P(A \mid B_i) \cdot P(B_i)
\]

Example: Two boxes. Box 1 has 3 red, 2 blue. Box 2 has 1 red, 4 blue. A box is chosen at random, then a ball drawn. Find \(P(\text{red})\):

\[
P(R) = P(R \mid B_1) \cdot P(B_1) + P(R \mid B_2) \cdot P(B_2)
\]

\[
= \frac{3}{5} \cdot \frac{1}{2} + \frac{1}{5} \cdot \frac{1}{2} = \frac{3}{10} + \frac{1}{10} = \frac{2}{5}
\]

---

## Bayes' Theorem

Updates probability after observing evidence.

\[
P(B_k \mid A) = \frac{P(A \mid B_k) \cdot P(B_k)}{\displaystyle\sum_{i=1}^{n} P(A \mid B_i) \cdot P(B_i)}
\]

Example: Using the boxes above, given red ball drawn, find \(P(\text{Box 1})\):

\[
P(B_1 \mid R) = \frac{\frac{3}{5} \cdot \frac{1}{2}}{\frac{2}{5}} = \frac{\frac{3}{10}}{\frac{4}{10}} = \frac{3}{4}
\]
