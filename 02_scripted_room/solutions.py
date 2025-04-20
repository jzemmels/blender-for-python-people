import bpy
import math

# challenge 1
bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))
cube = bpy.context.active_object
cube.rotation_euler = (0, 0, math.radians(45))

# challenge 2
bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))
cube = bpy.context.active_object
cube.scale = (2, 0.5, 1)

# challenge 3
bpy.ops.mesh.primitive_cube_add()
cube = bpy.context.active_object

mat = bpy.data.materials.new(name="RedMaterial")
mat.diffuse_color = (1, 0, 0, 1)
cube.data.materials.append(mat)