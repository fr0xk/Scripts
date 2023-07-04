The Biot-Savart law is a mathematical equation that describes the magnetic field produced by a current-carrying conductor. It relates the magnetic field to the magnitude, direction, length, and proximity of the electric current.

According to the Biot-Savart law, a small segment of the current-carrying conductor produces a magnetic field. That segment is referred to as the element of current and is a vector quantity. The Biot-Savart law states that at any point P, the magnetic field \(\mathbf{dB}\) due to the element \(\mathbf{dl}\) of a current-carrying conductor is given by:

\[
\mathbf{dB} = \frac{\mu_0}{4\pi} \frac{I\,d\mathbf{l} \times \mathbf{\hat{r}}}{r^2}
\]

Where:
- \(\mu_0\) is the permeability of free space and is equal to \(4\pi \times 10^{-7}\) Tm/A.
- \(I\) is the current in the conductor.
- \(d\mathbf{l}\) is the vector notation of the current element in the direction of the current flowing into the conductor.
- \(\mathbf{\hat{r}}\) is the unit vector in the direction of the position vector \(\mathbf{r}\) of point P from the current element.
- \(r\) is the distance of point P from the current element.

The direction of the magnetic field is always in a plane perpendicular to the line of the element and the position vector. It is given by the right-hand thumb rule, where the thumb points to the direction of conventional current, and the other fingers show the magnetic field's direction.

If a current is flowing in a circular loop, then it will produce a magnetic field according to the Biot-Savart law. The direction of the magnetic field in the circular loop is determined by using Fleming's right-hand thumb rule, which states that if you curl your right-hand fingers in the direction of the current in the circular loop, then the direction of your thumb will give you the direction of the magnetic field in the circular loop.

To derive an expression for the magnetic field on the axis of a circular loop, we can use the Biot-Savart law as follows:

- Consider a circular loop of radius \(a\) and current \(I\) as shown in the figure below.

![circular loop](https://school.careers360.com/sites/default/files/2021-08/Biot%20Savart%20Law%20Topic%20PGE%20Image%201.png)

- Let \(P\) be a point on the axis of the loop at a distance \(x\) from its center.
- Let \(d\mathbf{l}\) be a small element of the loop subtending an angle \(d\theta\) at the center.
- The position vector \(\mathbf{r}\) of point P from the current element is given by:

\[
\mathbf{r} = \sqrt{x^2 + a^2}
\]

- The angle between \(d\mathbf{l}\) and \(\mathbf{r}\) is \(\frac{\pi}{2}\), so \(\sin\theta = 1\).
- Applying the Biot-Savart law, we get:

\[
\mathbf{dB} = \frac{\mu_0}{4\pi} \frac{I\,d\mathbf{l}}{r^2} \cos\phi
\]

- The direction of \(\mathbf{dB}\) is perpendicular to both \(d\

mathbf{l}\) and \(\mathbf{r}\), so it is along \(\mathbf{\hat{k}}\) (outward) or \(-\mathbf{\hat{k}}\) (inward) depending on whether \(I\) is clockwise or counterclockwise.
- To find the net magnetic field at \(P\), we need to integrate over all elements of the loop. Note that only the component of \(\mathbf{dB}\) along \(\mathbf{\hat{k}}\) will contribute, as the other components will cancel out due to symmetry.

\[
\mathbf{B} = \int \mathbf{dB}_k = \int \frac{\mu_0}{4\pi} \frac{I\,d\mathbf{l}}{r^2} \cos\phi
\]

Where \(\phi\) is the angle between \(\mathbf{dB}\) and \(\mathbf{\hat{k}}\).

- To find \(\cos\phi\), we can use geometry as shown in the figure below.

![geometry](https://school.careers360.com/sites/default/files/2021-08/Biot%20Savart%20Law%20Topic%20PGE%20Image%202.png)

We have:

\[
\cos\phi = \frac{x}{r} = \frac{x}{\sqrt{x^2 + a^2}}
\]

- Substituting this in the integral, we get:

\[
\mathbf{B} = \int \frac{\mu_0}{4\pi} \frac{I\,d\mathbf{l}}{r^2} \cos\phi
\]

\[
\mathbf{B} = \frac{\mu_0 I x}{4\pi (x^2 + a^2)^{3/2}} \int d\mathbf{l}
\]

- The integral of \(d\mathbf{l}\) over the loop is equal to the circumference of the loop, which is \(2\pi a\).
- Therefore, we get:

\[
\mathbf{B} = \frac{\mu_0 I a^2}{2 (x^2 + a^2)^{3/2}}
\]

This is the expression for the magnetic field on the axis of a circular loop due to the Biot-Savart law.
