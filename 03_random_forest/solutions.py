import bpy

# challenge 1
foliage.scale = (random.uniform(0.8, 1.2),) * 3

# challenge 2
trunk.rotation_euler.z = random.uniform(0, 3.14)

# challenge 3
for i in range(20):
    angle = i * (2 * math.pi / 20)
    x = 6 * math.cos(angle)
    y = 6 * math.sin(angle)
    create_tree((x, y, 0))
