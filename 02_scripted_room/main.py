import bpy

# 🧹 STEP 0: Clear the scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# 🧱 STEP 1: Create a Room (Floor + 4 Walls)
# Add a plane to act as the floor
bpy.ops.mesh.primitive_plane_add(size=6, location=(0, 0, 0))
floor = bpy.context.active_object
floor.name = "Floor"

# Create one wall using a cube
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, -3, 1.5))
wall = bpy.context.active_object
wall.scale = (3, 0.1, 1.5)
wall.name = "BackWall"

# 🧭 INTERFACE EXPLORATION:
# - In the Outliner, look at "BackWall"
# - With it selected, press `N` and inspect the scale: why is it (3, 0.1, 1.5)?
# - What happens if you change the Z scale to 3 in the script?

# 🧱 STEP 2: Duplicate and rotate the wall to form the room
# Add left wall
bpy.ops.mesh.primitive_cube_add(size=1, location=(-3, 0, 1.5))
left_wall = bpy.context.active_object
left_wall.scale = (0.1, 3, 1.5)
left_wall.name = "LeftWall"

# Add right wall
bpy.ops.mesh.primitive_cube_add(size=1, location=(3, 0, 1.5))
right_wall = bpy.context.active_object
right_wall.scale = (0.1, 3, 1.5)
right_wall.name = "RightWall"

# Add front wall
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 3, 1.5))
front_wall = bpy.context.active_object
front_wall.scale = (3, 0.1, 1.5)
front_wall.name = "FrontWall"

# 🧭 INTERFACE CHECK:
# Go to the Layout tab → 3D Viewport
# Rotate the view and look at the room — does it look square?
# Try changing the wall height (Z-scale) to 2 and rerun the script.

# 🔗 RESOURCES
# - [primitive_plane_add](https://docs.blender.org/api/current/bpy.ops.mesh.html#bpy.ops.mesh.primitive_plane_add)
# - [primitive_cube_add](https://docs.blender.org/api/current/bpy.ops.mesh.html#bpy.ops.mesh.primitive_cube_add)
# - [Transforming Objects](https://docs.blender.org/api/current/bpy.types.Object.html#bpy.types.Object.scale)

# 🌟 CHALLENGE 1:
# Add a ceiling using a second plane at z = 3, rotated to be horizontal.
# Hint: use rotation_euler and set the Z rotation to 0, X to radians(180)

# 🌟 CHALLENGE 2:
# Add a cylinder to the center of the room as a pillar.
# Make it tall (z = 1.5) and scaled small on X and Y (e.g., 0.3).
# Docs: https://docs.blender.org/api/current/bpy.ops.mesh.html#bpy.ops.mesh.primitive_cylinder_add

# 🌟 CHALLENGE 3:
# Create a grid of 3x3 columns spaced out evenly across the floor.
# Use nested for-loops and translate each cylinder into position.
