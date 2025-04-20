import bpy
import random

class OBJECT_OT_add_random_primitive(bpy.types.Operator):
    bl_idname = "object.add_random_primitive"
    bl_label = "Add Random Primitive"
    
    def execute(self, context):
        types = ['Cube', 'UV_Sphere', 'Cylinder']
        choice = random.choice(types)
        x, y = random.uniform(-3, 3), random.uniform(-3, 3)
        
        if choice == 'Cube':
            bpy.ops.mesh.primitive_cube_add(location=(x, y, 1))
        elif choice == 'UV_Sphere':
            bpy.ops.mesh.primitive_uv_sphere_add(location=(x, y, 1))
        elif choice == 'Cylinder':
            bpy.ops.mesh.primitive_cylinder_add(location=(x, y, 1))
        
        return {'FINISHED'}

class VIEW3D_PT_random_primitive(bpy.types.Panel):
    bl_label = "Random Primitive Panel"
    bl_idname = "VIEW3D_PT_random_primitive"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tools'
    
    def draw(self, context):
        layout = self.layout
        layout.operator("object.add_random_primitive")

def register():
    bpy.utils.register_class(OBJECT_OT_add_random_primitive)
    bpy.utils.register_class(VIEW3D_PT_random_primitive)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_add_random_primitive)
    bpy.utils.unregister_class(VIEW3D_PT_random_primitive)

if __name__ == "__main__":
    register()
