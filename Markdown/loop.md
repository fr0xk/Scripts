
Biot-Savart law is a mathematical equation that describes the magnetic field produced by a current carrying conductor. It relates the magnetic field to the magnitude, direction, length, and proximity of the electric current.

According to Biot-Savart law, a small segment of the current carrying conductor produces a magnetic field. That segment is referred to as the element of current and is a vector quantity. The Biot-Savart law states that at any point P due to the magnetic field dB due to element dl of a current-carrying is given by:

```latex
$$dB = \frac{\mu_0}{4\pi} \frac{Idl \times \hat{r}}{r^2}$$
```

Where,

- $\mu_0$ is the permeability of free space and is equal to $4\pi \times 10^{-7}$ Tm/A.
- $I$ is the current in the conductor.
- $dl$ is the vector notation of current element in the direction of current flowing into the conductor.
- $\hat{r}$ is the unit vector in the direction of position vector $r$ of point P from the current element.
- $r$ is the distance of point P from the current element.

The direction of the magnetic field is always in a plane perpendicular to the line of element and position vector. It is given by the right-hand thumb rule where the thumb points to the direction of conventional current and the other fingers show the magnetic field’s direction.

If a current is flowing in a circular loop, then there will be a magnetic field produced by it according to Biot-Savart law. The direction of the magnetic field in circular loop is decided by using Fleming’s right hand thumb rule and it states that “curl your finger of right hand in the direction of current in circular loop, then the direction of thumb will gives you the direction of the magnetic field in a circular loop”.

To derive an expression for the magnetic field on the axis of a circular loop, we can use Biot-Savart law as follows:

- Consider a circular loop of radius $a$ and current $I$ as shown in the figure below.

![circular loop](https://school.careers360.com/sites/default/files/2021-08/Biot%20Savart%20Law%20Topic%20PGE%20Image%201.png)

- Let $P$ be a point on the axis of the loop at a distance $x$ from its center.
- Let $dl$ be a small element of the loop subtending an angle $d\theta$ at the center.
- The position vector $r$ of point P from the current element is given by:

```latex
$$r = \sqrt{x^2 + a^2}$$
```

- The angle between $dl$ and $r$ is $\frac{\pi}{2}$, so $\sin\theta = 1$.
- Applying Biot-Savart law, we get:

```latex
$$dB = \frac{\mu_0}{4\pi} \frac{Idl \times \hat{r}}{r^2}$$
```

- The direction of $dB$ is perpendicular to both $dl$ and $r$, so it is along $\hat{k}$ (outward) or $-\hat{k}$ (inward) depending on whether $I$ is clockwise or anticlockwise.
- To find the net magnetic field at P, we need to integrate over all elements of the loop. Note that only the component of $dB$ along $\hat{k}$ will contribute, as the other components will cancel out due to symmetry.

```latex
$$B = \int dB_k = \int \frac{\mu_0}{4\pi} \frac{Idl}{r^2} \cos\phi$$
```

Where $\phi$ is the angle between $dB$ and $\hat{k}$.

- To find $\cos\phi$, we can use geometry as shown in the figure below.

![geometry](https://school.careers360.com/sites/default/files/2021-08/Biot%20Savart%20Law%20Topic%20PGE%20Image%202.png)

We have:

```latex
$$\cos\phi = \frac{x}{r} = \frac{x}{\sqrt{x^2 + a^2}}$$
```

- Substituting this in the integral, we get:

```latex
$$B = \int \frac{\mu_0}{4\pi} \frac{Idl}{r^2} \cos\phi$$
```

```latex
$$B = \frac{\mu_0 I x}{4\pi (x^2 + a^2)^{3/2}} \int dl$$
```

- The integral of $dl$ over the loop is equal to the circumference of the loop, which is $2\pi a$.
- Therefore, we get:

```latex
$$B = \frac{\mu_0 I x}{4\pi (x^2 + a^2)^{3/2}} 2\pi a$$
```

```latex
$$B = \frac{\mu_0 I a^2}{2 (x^2 + a^2)^{3/2}}$$
```

This is the expression for the magnetic field on the axis of a circular loop due to Biot-Savart law.
