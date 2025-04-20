import bpy
import random

# challenge 1
house.scale = (random.uniform(0.8, 1.2),) * 2 + (random.uniform(1.0, 1.5),)

# challenge 2
if random.random() < 0.5:
    bpy.ops.mesh.primitive_cylinder_add(radius=0.5, depth=2, location=location)
else:
    create_house(location)

# challenge 3
if abs(x) < 2 and abs(y) < 2:
    continue  # Leave center open

# challenge 4
if abs(x) > 6 or abs(y) > 6:
    create_tree((x, y, 0))
