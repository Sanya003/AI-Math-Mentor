# Probability Distributions

A probability distribution describes how probabilities are spread over outcomes.

---

## Binomial Distribution

Used when there are exactly \(n\) independent trials, each with success probability \(p\).

\[
X \sim B(n, p)
\]

\[
P(X = r) = \binom{n}{r} p^r (1-p)^{n-r}, \quad r = 0, 1, \ldots, n
\]

Mean:

\[
E[X] = np
\]

Variance:

\[
\text{Var}(X) = np(1-p)
\]

Example: A die is rolled 5 times. Find \(P(\text{exactly 2 sixes})\):

\[
p = \frac{1}{6},\quad n = 5,\quad r = 2
\]

\[
P(X=2) = \binom{5}{2}\left(\frac{1}{6}\right)^2\left(\frac{5}{6}\right)^3 = 10 \cdot \frac{1}{36} \cdot \frac{125}{216} = \frac{1250}{7776}
\]

---

## Useful Result

\[
P(X \geq 1) = 1 - P(X = 0) = 1 - (1-p)^n
\]

Example: Probability of **at least one** six in 3 rolls:

\[
P(X \geq 1) = 1 - \left(\frac{5}{6}\right)^3 = 1 - \frac{125}{216} = \frac{91}{216}
\]

---

## Geometric Distribution

Number of trials until the **first** success.

\[
P(X = k) = (1-p)^{k-1} \cdot p, \quad k = 1, 2, 3, \ldots
\]

Mean:

\[
E[X] = \frac{1}{p}
\]

Example: Keep rolling until 6 appears. Expected number of rolls:

\[
E[X] = \frac{1}{1/6} = 6
\]
