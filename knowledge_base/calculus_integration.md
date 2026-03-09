# Integration

Integration is the reverse of differentiation. It finds the area under a curve.

\[
\int f(x)\, dx = F(x) + C \quad \text{where } F'(x) = f(x)
\]

---

## Standard Integrals

\[
\int x^n\, dx = \frac{x^{n+1}}{n+1} + C \quad (n \neq -1)
\]

\[
\int \frac{1}{x}\, dx = \ln|x| + C
\]

\[
\int e^x\, dx = e^x + C
\]

\[
\int \sin x\, dx = -\cos x + C
\]

\[
\int \cos x\, dx = \sin x + C
\]

\[
\int \sec^2 x\, dx = \tan x + C
\]

\[
\int \frac{1}{\sqrt{1-x^2}}\, dx = \sin^{-1} x + C
\]

\[
\int \frac{1}{1+x^2}\, dx = \tan^{-1} x + C
\]

---

## Integration by Substitution

Let \(u = g(x)\), then \(du = g'(x)\,dx\).

Example:

\[
\int 2x\,e^{x^2}\,dx
\]

Let \(u = x^2\), \(du = 2x\,dx\):

\[
= \int e^u\,du = e^u + C = e^{x^2} + C
\]

---

## Integration by Parts

\[
\int u\,dv = uv - \int v\,du
\]

**ILATE Rule** — choose \(u\) in this priority order:
**I**nverse trig → **L**ogarithm → **A**lgebra → **T**rig → **E**xponential

Example:

\[
\int x e^x\,dx
\]

Let \(u = x\), \(dv = e^x\,dx\):

\[
= x e^x - \int e^x\,dx = x e^x - e^x + C = e^x(x-1) + C
\]

---

## Definite Integral

\[
\int_a^b f(x)\,dx = F(b) - F(a)
\]

Example:

\[
\int_0^2 x^2\,dx = \left[\frac{x^3}{3}\right]_0^2 = \frac{8}{3} - 0 = \frac{8}{3}
\]

---

## Key Properties of Definite Integrals

**Reversal:**

\[
\int_a^b f(x)\,dx = -\int_b^a f(x)\,dx
\]

**King's Property** (very useful in JEE):

\[
\int_0^a f(x)\,dx = \int_0^a f(a-x)\,dx
\]

Example:

\[
\int_0^{\pi} x\sin x\,dx \quad \Rightarrow \quad \text{Apply King's property to simplify}
\]

**Even function:**

\[
\int_{-a}^{a} f(x)\,dx = 2\int_0^a f(x)\,dx \quad \text{if } f(-x) = f(x)
\]

**Odd function:**

\[
\int_{-a}^{a} f(x)\,dx = 0 \quad \text{if } f(-x) = -f(x)
\]
