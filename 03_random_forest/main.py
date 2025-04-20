import bpy
import random

# Clear existing objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Create a base plane
bpy.ops.mesh.primitive_plane_add(size=10, location=(0, 0, 0))

# Add random trees
for i in range(20):
    x, y = random.uniform(-5, 5), random.uniform(-5, 5)
    bpy.ops.mesh.primitive_cylinder_add(radius=0.1, depth=1, location=(x, y, 0.5))
    bpy.ops.mesh.primitive_cone_add(radius1=0.5, depth=1, location=(x, y, 1.5))
