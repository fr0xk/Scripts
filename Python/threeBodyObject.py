import math
import os
import time

G = 6.6743e-11  # Gravitational constant

# Masses (in kg)
M_sun = 1.989e30
M_earth = 5.972e24
M_asteroid = 2.8e12  # Approximate mass of a small asteroid

# Initial positions (in meters) and velocities (in meters per second)
# Simplified 2D model
bodies = {
    'sun': {'mass': M_sun, 'pos': [0, 0], 'vel': [0, 0]},
    'earth': {'mass': M_earth, 'pos': [1.496e11, 0], 'vel': [0, 2.978e4]},  # 1 AU from Sun, average orbital speed
    'asteroid': {'mass': M_asteroid, 'pos': [3.14e11, 0], 'vel': [0, 1.4e4]}  # Rough orbit and speed for the asteroid
}

def gravitational_force(m1, m2, r1, r2):
    r = [r2[0] - r1[0], r2[1] - r1[1]]
    distance = math.sqrt(r[0]**2 + r[1]**2)
    force_magnitude = G * m1 * m2 / distance**2
    return [force_magnitude * (r[0] / distance), force_magnitude * (r[1] / distance)]

def update_motion(dt, body1, body2):
    force = gravitational_force(body1['mass'], body2['mass'], body1['pos'], body2['pos'])
    acc = [force[0] / body2['mass'], force[1] / body2['mass']]
    body2['vel'] = [body2['vel'][0] + acc[0] * dt, body2['vel'][1] + acc[1] * dt]
    body2['pos'] = [body2['pos'][0] + body2['vel'][0] * dt, body2['pos'][1] + body2['vel'][1] * dt]

dt = 86400  # Time step of one day in seconds
output_count = 0

for step in range(1000):
    update_motion(dt, bodies['sun'], bodies['asteroid'])
    update_motion(dt, bodies['earth'], bodies['asteroid'])
    
    if output_count % 30 == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
    
    output_count += 1
    
    print(f"Step {step + 1}")
    print(f"{'Body':<10}{'Position (m)':<30}{'Velocity (m/s)':<30}")
    print(f"{'-'*70}")
    for name, body in bodies.items():
        pos = f"[{body['pos'][0]:.2e}, {body['pos'][1]:.2e}]"
        vel = f"[{body['vel'][0]:.2e}, {body['vel'][1]:.2e}]"
        print(f"{name:<10}{pos:<30}{vel:<30}")
    
    time.sleep(43200)  # For real-time effect
