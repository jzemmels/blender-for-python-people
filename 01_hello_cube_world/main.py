import bpy

# 🧹 STEP 0: Clear the scene
# Select all objects and delete them
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# 🧱 STEP 1: Add a Cube at the Origin
# Docs: https://docs.blender.org/api/current/bpy.ops.mesh.html#bpy.ops.mesh.primitive_cube_add
bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))
cube = bpy.context.active_object
cube.name = "ScriptedCube"

# 🛠️ STEP 2: Modify the Cube
# Move it up 1 unit on the Z-axis
cube.location.z += 1

# 🧭 INTERFACE EXPLORATION:
# After running this script:
# - Look at the Outliner. Do you see "ScriptedCube"?
# - Select it and open the Item tab (press `N` if needed).
# - Now change `cube.location.z += 1` to `+= 3` and rerun. What changed?

# 🧪 STEP 3: Try a Different Primitive
# Replace the cube with a UV sphere
# Docs: https://docs.blender.org/api/current/bpy.ops.mesh.html#bpy.ops.mesh.primitive_uv_sphere_add
# Comment out the cube above and try:
# bpy.ops.mesh.primitive_uv_sphere_add(location=(0, 0, 0))

# 🔗 RESOURCES
# - [primitive_cube_add](https://docs.blender.org/api/current/bpy.ops.mesh.html#bpy.ops.mesh.primitive_cube_add)
# - [primitive_uv_sphere_add](https://docs.blender.org/api/current/bpy.ops.mesh.html#bpy.ops.mesh.primitive_uv_sphere_add)
# - [Object Operators](https://docs.blender.org/api/current/bpy.ops.object.html)
# - [Intro to Scripting Workspace (YouTube)](https://www.youtube.com/watch?v=drm7Qn3EktY)

# 🌟 CHALLENGE 1:
# Add a second cube to the right (x = 2), and rotate it around Z by 45 degrees.
# Hint: new_cube.rotation_euler.z = radians(45)

# 🌟 CHALLENGE 2:
# Add a UV Sphere above the first cube (z = 3) and scale it to twice the size.
# Hint: sphere.scale = (2, 2, 2)

# 🌟 CHALLENGE 3:
# Use a loop to create a row of 5 cubes spaced along X.
# Bonus: Use `import random` to vary their heights with random.uniform(1, 3)
