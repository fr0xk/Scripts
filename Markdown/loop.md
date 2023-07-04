
The Biot-Savart law is a mathematical equation that describes the magnetic field produced by a current-carrying conductor. It relates the magnetic field to the magnitude, direction, length, and proximity of the electric current.

According to the Biot-Savart law, a small segment of the current-carrying conductor produces a magnetic field. That segment is referred to as the element of current and is a vector quantity. The Biot-Savart law states that at any point P, the magnetic field dB due to the element dl of a current-carrying conductor is given by:

dB = (μ₀/4π) * (I * dl × r-hat) / r²

Where:
- μ₀ is the permeability of free space and is equal to 4π × 10^(-7) Tm/A.
- I is the current in the conductor.
- dl is the vector notation of the current element in the direction of the current flowing into the conductor.
- r-hat is the unit vector in the direction of the position vector r of point P from the current element.
- r is the distance of point P from the current element.

The direction of the magnetic field is always in a plane perpendicular to the line of the element and the position vector. It is given by the right-hand thumb rule, where the thumb points to the direction of conventional current, and the other fingers show the magnetic field's direction.

If a current is flowing in a circular loop, then it will produce a magnetic field according to the Biot-Savart law. The direction of the magnetic field in the circular loop is determined by using Fleming's right-hand thumb rule, which states that if you curl your right-hand fingers in the direction of the current in the circular loop, then the direction of your thumb will give you the direction of the magnetic field in the circular loop.

To derive an expression for the magnetic field on the axis of a circular loop, we can use the Biot-Savart law as follows:

- Consider a circular loop of radius a and current I.
- Let P be a point on the axis of the loop at a distance x from its center.
- Let dl be a small element of the loop subtending an angle dθ at the center.
- The position vector r of point P from the current element is given by:

r = sqrt(x² + a²)

- The angle between dl and r is π/2, so sinθ = 1.
- Applying the Biot-Savart law, we get:

dB = (μ₀/4π) * (I * dl) / r² * cosϕ

- The direction of dB is perpendicular to both dl and r, so it is along k-hat (outward) or -k-hat (inward) depending on whether I is clockwise or counterclockwise.
- To find the net magnetic field at P, we need to integrate over all elements of the loop. Note that only the component of dB along k-hat will contribute, as the other components will cancel out due to symmetry.

B = ∫ dB_k = ∫ (μ₀/4π) * (I * dl) / r² * cosϕ

Where ϕ is the angle between dB and k-hat.

- To find cosϕ, we can use geometry.

cosϕ = x / r = x / sqrt(x² + a²)

- Substituting this in the integral, we get:

B = ∫ (μ₀/4π) * (I * dl) / r² * cosϕ

B = (μ₀ *

 I * x) / [4π * (x² + a²)^(3/2)] * ∫ dl

- The integral of dl over the loop is equal to the circumference of the loop, which is 2πa.
- Therefore, we get:

B = (μ₀ * I * a²) / [2 * (x² + a²)^(3/2)]

This is the expression for the magnetic field on the axis of a circular loop due to the Biot-Savart law.￼Enter
