import bpy

# challenge 1
bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0, 0))

#challenge 2
bpy.ops.mesh.primitive_cube_add(size=2, location=(3, 1, 0))

#challenge 3
for i in range(3):
    bpy.ops.mesh.primitive_cube_add(size=1, location=(i * 2, 0, 0))
