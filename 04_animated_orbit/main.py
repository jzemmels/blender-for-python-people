import bpy
import math

# 🧹 STEP 0: Clear the scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# 🧱 STEP 1: Create a central object to orbit
bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0, 1))
center_obj = bpy.context.active_object
center_obj.name = "CentralSphere"

# 📷 STEP 2: Add a camera
bpy.ops.object.camera_add(location=(5, 0, 2))
camera = bpy.context.active_object
camera.name = "OrbitCamera"
camera.data.lens = 35  # Optional: set lens

# Point the camera at the sphere using a Track To constraint
track_to = camera.constraints.new(type='TRACK_TO')
track_to.target = center_obj
track_to.track_axis = 'TRACK_NEGATIVE_Z'
track_to.up_axis = 'UP_Y'

# 🧭 INTERFACE EXPLORATION:
# Select the camera and go to the Constraints tab (chain icon) — can you see the Track To?
# Try changing `TRACK_NEGATIVE_Z` to `TRACK_NEGATIVE_Y` in the script and see how the camera's orientation changes.

# 🎞️ STEP 3: Animate the camera in a circular orbit
scene = bpy.context.scene
scene.frame_start = 1
scene.frame_end = 120

radius = 5
height = 2

for frame in range(scene.frame_start, scene.frame_end + 1):
    angle = 2 * math.pi * (frame - 1) / scene.frame_end
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    z = height

    camera.location = (x, y, z)
    camera.keyframe_insert(data_path="location", frame=frame)

# 🧭 INTERFACE CHECK:
# Switch to the "Animation" workspace and press spacebar to play.
# In the Timeline, you should see 120 frames of animation.
# Go to the Graph Editor and observe the curve for the camera’s location.

# 🔗 RESOURCES
# - [object.camera_add](https://docs.blender.org/api/current/bpy.ops.object.html#bpy.ops.object.camera_add)
# - [Track To constraint](https://docs.blender.org/api/current/bpy.types.Constraint.html)
# - [keyframe_insert](https://docs.blender.org/api/current/bpy.types.ID.html#bpy.types.ID.keyframe_insert)
# - [Blender Animation Basics (video)](https://www.youtube.com/watch?v=LLV7h-WLIxw)

# 🌟 CHALLENGE 1:
# Animate the camera's height (`z`) to slowly rise and fall during the orbit — like a drone flying in a circle.
# Hint: try `z = height + math.sin(angle) * 0.5`

# 🌟 CHALLENGE 2:
# Instead of a full orbit, animate a back-and-forth movement between two points with easing.
# Use the Graph Editor to inspect and edit interpolation curves.

# 🌟 CHALLENGE 3:
# Replace the orbiting object with a **light** instead of a camera, and light your scene from different angles!
# Try using a `SUN` or `SPOT` light and animate its rotation and position.
