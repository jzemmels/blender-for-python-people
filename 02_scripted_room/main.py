import bpy

# Clear the scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Add a floor
bpy.ops.mesh.primitive_plane_add(size=10, location=(0, 0, 0))

# Add a light
bpy.ops.object.light_add(type='SUN', location=(5, 5, 5))

# Add a camera
bpy.ops.object.camera_add(location=(7, -7, 5))
bpy.context.object.rotation_euler = (1.1, 0, 0.78)
