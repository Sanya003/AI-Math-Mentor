# Derivatives

The derivative measures the **rate of change** of a function.

\[
f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
\]

---

## Power Rule

\[
\frac{d}{dx}(x^n) = nx^{n-1}
\]

Example:

\[
\frac{d}{dx}(x^4) = 4x^3
\]

---

## Derivative of Constants

\[
\frac{d}{dx}(c) = 0
\]

Example:

\[
\frac{d}{dx}(5) = 0
\]

---

## Sum Rule

\[
\frac{d}{dx}(f(x)+g(x)) = f'(x)+g'(x)
\]

Example:

\[
\frac{d}{dx}(x^2+3x) = 2x+3
\]

---

## Product Rule

\[
\frac{d}{dx}(u \cdot v) = u'v + uv'
\]

Example:

\[
\frac{d}{dx}(x^2 \sin x) = 2x \sin x + x^2 \cos x
\]

---

## Quotient Rule

\[
\frac{d}{dx}\left(\frac{u}{v}\right) = \frac{u'v - uv'}{v^2}
\]

Example:

\[
\frac{d}{dx}\left(\frac{x^2}{\cos x}\right) = \frac{2x \cos x + x^2 \sin x}{\cos^2 x}
\]

---

## Chain Rule

\[
\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)
\]

Example:

\[
\frac{d}{dx}(\sin(x^2)) = \cos(x^2) \cdot 2x
\]

---

## Standard Derivatives Table

\[
\frac{d}{dx}(e^x) = e^x
\]

\[
\frac{d}{dx}(\ln x) = \frac{1}{x}
\]

\[
\frac{d}{dx}(\sin x) = \cos x
\]

\[
\frac{d}{dx}(\cos x) = -\sin x
\]

\[
\frac{d}{dx}(\tan x) = \sec^2 x
\]

\[
\frac{d}{dx}(\sin^{-1} x) = \frac{1}{\sqrt{1-x^2}}
\]

\[
\frac{d}{dx}(\tan^{-1} x) = \frac{1}{1+x^2}
\]

---

## Implicit Differentiation

Differentiate both sides with respect to \(x\), treating \(y\) as \(f(x)\).

Example: Find \(\frac{dy}{dx}\) for \(x^2 + y^2 = 25\)

\[
2x + 2y\frac{dy}{dx} = 0 \implies \frac{dy}{dx} = -\frac{x}{y}
\]
