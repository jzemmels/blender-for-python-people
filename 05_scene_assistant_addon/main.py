import bpy

class OBJECT_OT_setup_scene(bpy.types.Operator):
    bl_idname = "object.setup_simple_scene"
    bl_label = "Setup Simple Scene"
    
    def execute(self, context):
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)
        
        # Add lighting
        bpy.ops.object.light_add(type='SUN', location=(5, 5, 5))
        
        # Add camera
        bpy.ops.object.camera_add(location=(7, -7, 5))
        cam = bpy.context.active_object
        cam.rotation_euler = (1.1, 0, 0.78)
        
        # Add floor
        bpy.ops.mesh.primitive_plane_add(size=10, location=(0, 0, 0))
        return {'FINISHED'}

class VIEW3D_PT_scene_assistant(bpy.types.Panel):
    bl_label = "Scene Assistant"
    bl_idname = "VIEW3D_PT_scene_assistant"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tools'
    
    def draw(self, context):
        layout = self.layout
        layout.operator("object.setup_simple_scene")

def register():
    bpy.utils.register_class(OBJECT_OT_setup_scene)
    bpy.utils.register_class(VIEW3D_PT_scene_assistant)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_setup_scene)
    bpy.utils.unregister_class(VIEW3D_PT_scene_assistant)

if __name__ == "__main__":
    register()
