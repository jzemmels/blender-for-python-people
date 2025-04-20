import bpy
import random

# 🧹 STEP 0: Clear the scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# 🧱 STEP 1: Create a ground plane
bpy.ops.mesh.primitive_plane_add(size=20, location=(0, 0, 0))
ground = bpy.context.active_object
ground.name = "VillageGround"

# 🏠 STEP 2: Create a single house
def create_house(location):
    # Base cube (house body)
    bpy.ops.mesh.primitive_cube_add(size=1, location=location)
    house = bpy.context.active_object
    house.scale = (1, 1, 1)
    house.location.z = 0.5  # Raise it above the ground
    house.name = "HouseBase"

    # Roof (cone)
    bpy.ops.mesh.primitive_cone_add(radius1=1.2, depth=1, location=location)
    roof = bpy.context.active_object
    roof.location.z = 1.5
    roof.name = "HouseRoof"

# Create one house at (0, 0)
create_house((0, 0, 0))

# 🧭 INTERFACE EXPLORATION:
# Look at the Outliner — you should see “HouseBase” and “HouseRoof”
# Select each object and inspect its dimensions and transforms.

# 🏘️ STEP 3: Procedurally generate a grid of houses
for x in range(-4, 5, 2):
    for y in range(-4, 5, 2):
        if random.random() < 0.8:  # Leave some plots empty
            size = random.uniform(0.8, 1.2)
            loc = (x + random.uniform(-0.2, 0.2), y + random.uniform(-0.2, 0.2), 0)
            create_house(loc)

# 🧭 VISUAL CHECK:
# Switch to the Layout or Rendered view. Does your village look varied?
# Rerun the script a few times — how does the layout change?

# 🔗 RESOURCES
# - [Object creation](https://docs.blender.org/api/current/bpy.ops.mesh.html)
# - [Transformations](https://docs.blender.org/api/current/bpy.types.Object.html)
# - [Random module](https://docs.python.org/3/library/random.html)
# - [Procedural modeling with Python](https://www.youtube.com/watch?v=q3Z4EemR8gY)

# 🌟 CHALLENGE 1:
# Add variation in building height and width.
# Try changing `house.scale.z` or adding taller roof cones.

# 🌟 CHALLENGE 2:
# Create different building "types" — maybe tall towers, or round huts using cylinders.
# Use `random.choice` to select a building type per plot.

# 🌟 CHALLENGE 3:
# Add a central square (clear space in the middle), and maybe a big statue!
# Bonus: use a different primitive or a built-in mesh for the statue.

# 🌟 BONUS CHALLENGE:
# Add trees (from Lesson 3) around the perimeter of the village.
# Try scripting them to only appear outside a radius from the center.
