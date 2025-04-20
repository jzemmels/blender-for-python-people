import bpy

# challenge 1
z = height + math.sin(angle * 2) * 0.5

# challenge 2
for frame in range(1, 61):
    t = frame / 60
    x = 5 * math.sin(t * math.pi)
    camera.location = (x, 0, height)
    camera.keyframe_insert(data_path="location", frame=frame)

# challenge 3
bpy.ops.object.light_add(type='SPOT', location=(5, 0, 2))
light = bpy.context.active_object
for frame in range(1, 121):
    angle = 2 * math.pi * (frame - 1) / 120
    x = 5 * math.cos(angle)
    y = 5 * math.sin(angle)
    light.location = (x, y, 3)
    light.keyframe_insert(data_path="location", frame=frame)
