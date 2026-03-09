# Quadratic Equations

A quadratic equation has the standard form:

\[
ax^2 + bx + c = 0, \quad a \neq 0
\]

---

## Quadratic Formula

\[
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\]

Example: Solve \(2x^2 - 4x - 6 = 0\)

\[
x = \frac{4 \pm \sqrt{16 + 48}}{4} = \frac{4 \pm 8}{4}
\]

\[
x = 3 \quad \text{or} \quad x = -1
\]

---

## Discriminant

\[
D = b^2 - 4ac
\]

| Condition | Nature of Roots |
|-----------|----------------|
| \(D > 0\) | Two distinct real roots |
| \(D = 0\) | Two equal real roots |
| \(D < 0\) | Two complex conjugate roots |

---

## Sum and Product of Roots

If \(\alpha\) and \(\beta\) are roots of \(ax^2 + bx + c = 0\):

\[
\alpha + \beta = -\frac{b}{a}
\]

\[
\alpha \beta = \frac{c}{a}
\]

Example: For \(x^2 - 5x + 6 = 0\):

\[
\alpha + \beta = 5, \quad \alpha\beta = 6 \implies \alpha = 2,\; \beta = 3
\]

---

## Forming Equation from Roots

\[
x^2 - (\alpha + \beta)x + \alpha\beta = 0
\]

Example: Roots are \(3\) and \(-2\):

\[
x^2 - (3 + (-2))x + (3)(-2) = 0
\]

\[
x^2 - x - 6 = 0
\]

---

## Useful Identities

\[
\alpha^2 + \beta^2 = (\alpha+\beta)^2 - 2\alpha\beta
\]

\[
\alpha^3 + \beta^3 = (\alpha+\beta)^3 - 3\alpha\beta(\alpha+\beta)
\]

\[
|\alpha - \beta| = \frac{\sqrt{D}}{|a|}
\]

---

## Sign of Quadratic Expression

For \(f(x) = ax^2 + bx + c\) with roots \(\alpha < \beta\):

- If \(a > 0\): \(f(x) < 0\) for \(x \in (\alpha, \beta)\)
- If \(a < 0\): \(f(x) > 0\) for \(x \in (\alpha, \beta)\)
- If \(D < 0\) and \(a > 0\): \(f(x) > 0\) for all \(x \in \mathbb{R}\)
