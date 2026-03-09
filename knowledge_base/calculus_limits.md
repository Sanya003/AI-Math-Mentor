# Limits

A limit describes the value a function approaches as the input approaches a point.

\[
\lim_{x \to a} f(x) = L
\]

---

## Standard Limits (Must Memorise)

\[
\lim_{x \to 0} \frac{\sin x}{x} = 1
\]

\[
\lim_{x \to 0} \frac{\tan x}{x} = 1
\]

\[
\lim_{x \to 0} \frac{e^x - 1}{x} = 1
\]

\[
\lim_{x \to 0} \frac{\ln(1+x)}{x} = 1
\]

\[
\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x = e
\]

\[
\lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{1}{2}
\]

\[
\lim_{x \to a} \frac{x^n - a^n}{x - a} = n \cdot a^{n-1}
\]

---

## L'Hôpital's Rule

Used for indeterminate forms \(\frac{0}{0}\) or \(\frac{\infty}{\infty}\).

\[
\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}
\]

Example:

\[
\lim_{x \to 0} \frac{\sin x}{x} \quad \Rightarrow \quad \lim_{x \to 0} \frac{\cos x}{1} = 1
\]

---

## Limit at Infinity

Divide numerator and denominator by the highest power of \(x\).

Example:

\[
\lim_{x \to \infty} \frac{3x^2 + 1}{5x^2 - 2} = \frac{3}{5}
\]

---

## One-Sided Limits

Left-hand limit:

\[
\lim_{x \to a^-} f(x)
\]

Right-hand limit:

\[
\lim_{x \to a^+} f(x)
\]

A limit exists only if:

\[
\lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x)
\]

---

## Indeterminate Forms

| Form | Method |
|------|--------|
| \(0/0\) | Factorise or L'Hôpital |
| \(\infty/\infty\) | Divide by highest power or L'Hôpital |
| \(1^\infty\) | Use \(e^{\lim (f-1) \cdot g}\) |
| \(0 \times \infty\) | Rewrite as \(0/0\) or \(\infty/\infty\) |

Example for \(1^\infty\):

\[
\lim_{x \to 0}(1 + \sin x)^{\cot x} = e^{\lim_{x \to 0} \sin x \cdot \cot x} = e^1 = e
\]
