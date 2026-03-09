# Applications of Derivatives

Derivatives are used to find maxima, minima, tangents, and rates of change.

---

## Tangent and Normal to a Curve

Slope of tangent at \((x_0, y_0)\):

\[
m = f'(x_0)
\]

Equation of tangent:

\[
y - y_0 = m(x - x_0)
\]

Equation of normal (perpendicular to tangent):

\[
y - y_0 = -\frac{1}{m}(x - x_0)
\]

Example: Find tangent to \(y = x^2\) at \(x = 2\):

\[
f'(x) = 2x \implies f'(2) = 4
\]

\[
y - 4 = 4(x - 2) \implies y = 4x - 4
\]

---

## Increasing and Decreasing Functions

\[
f'(x) > 0 \implies f \text{ is increasing on that interval}
\]

\[
f'(x) < 0 \implies f \text{ is decreasing on that interval}
\]

Example: \(f(x) = x^2 - 4x\)

\[
f'(x) = 2x - 4 = 0 \implies x = 2
\]

- Decreasing on \((-\infty, 2)\), increasing on \((2, \infty)\)

---

## Maxima and Minima

**Step 1:** Set \(f'(x) = 0\) to find critical points.

**Step 2 — Second Derivative Test:**

\[
f''(c) < 0 \implies \text{local maximum at } x = c
\]

\[
f''(c) > 0 \implies \text{local minimum at } x = c
\]

Example: Find extrema of \(f(x) = x^3 - 3x^2\)

\[
f'(x) = 3x^2 - 6x = 3x(x-2) = 0 \implies x = 0,\; 2
\]

\[
f''(x) = 6x - 6
\]

\[
f''(0) = -6 < 0 \implies \text{local max at } x = 0
\]

\[
f''(2) = 6 > 0 \implies \text{local min at } x = 2
\]

---

## Rolle's Theorem

If \(f\) is continuous on \([a,b]\), differentiable on \((a,b)\), and \(f(a) = f(b)\), then:

\[
\exists\; c \in (a,b) \text{ such that } f'(c) = 0
\]

---

## Mean Value Theorem

If \(f\) is continuous on \([a,b]\) and differentiable on \((a,b)\):

\[
\exists\; c \in (a,b) \text{ such that } f'(c) = \frac{f(b) - f(a)}{b - a}
\]

Example: \(f(x) = x^2\) on \([1, 3]\):

\[
\frac{f(3)-f(1)}{3-1} = \frac{9-1}{2} = 4 \implies f'(c) = 2c = 4 \implies c = 2
\]
