import bpy
import random
import math

# 🧹 STEP 0: Clear the scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# 🌳 STEP 1: Create a Single Tree
# Use a cylinder for the trunk
bpy.ops.mesh.primitive_cylinder_add(radius=0.1, depth=1, location=(0, 0, 0.5))
trunk = bpy.context.active_object
trunk.name = "Trunk"

# Use a cone for the foliage (top)
bpy.ops.mesh.primitive_cone_add(radius1=0.4, depth=1, location=(0, 0, 1.5))
foliage = bpy.context.active_object
foliage.name = "Foliage"

# 🧭 INTERFACE EXPLORATION:
# In the Outliner, look at "Trunk" and "Foliage"
# Select the cone and try changing the radius1 and depth in the script. What happens?

# 🔁 STEP 2: Create Multiple Trees Randomly
for i in range(20):
    x = random.uniform(-5, 5)
    y = random.uniform(-5, 5)
    trunk_height = random.uniform(0.8, 1.2)
    foliage_height = trunk_height + 1.0

    # Trunk
    bpy.ops.mesh.primitive_cylinder_add(
        radius=0.1, 
        depth=trunk_height, 
        location=(x, y, trunk_height / 2)
    )
    trunk = bpy.context.active_object
    trunk.name = f"Trunk_{i}"

    # Foliage
    bpy.ops.mesh.primitive_cone_add(
        radius1=0.4, 
        depth=1.2, 
        location=(x, y, trunk_height + 0.6)
    )
    foliage = bpy.context.active_object
    foliage.name = f"Foliage_{i}"

# 🧭 EXPLORATION:
# Run the script multiple times. Do the trees look different each time?
# Try changing the range of random values to make the forest denser or sparser.

# 🔗 RESOURCES
# - [primitive_cylinder_add](https://docs.blender.org/api/current/bpy.ops.mesh.html#bpy.ops.mesh.primitive_cylinder_add)
# - [primitive_cone_add](https://docs.blender.org/api/current/bpy.ops.mesh.html#bpy.ops.mesh.primitive_cone_add)
# - [Python random module](https://docs.python.org/3/library/random.html)
# - [mathutils for 3D vectors (Blender)](https://docs.blender.org/api/current/mathutils.html)

# 🌟 CHALLENGE 1:
# Add scale variation to the foliage: try `foliage.scale = (s, s, s)` using random.uniform.

# 🌟 CHALLENGE 2:
# Add rotation to each tree so they aren't all perfectly aligned.
# Hint: use radians + `obj.rotation_euler.z = random_angle`

# 🌟 CHALLENGE 3:
# Create a circular forest by placing trees around the edge of a circle instead of randomly.
# Hint: use math.cos(angle) and math.sin(angle) to place trunks in a ring.
