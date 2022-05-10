from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(exposure=10)
scene.set_floor(-0.05, (1.0, 1.0, 1.0))
scene.set_background_color((1.0, 0, 0))

# rgb(210, 209, 204)


@ti.kernel
def initialize_voxels():
    # Your code here! :-)
    scene.set_voxel(vec3(0, 0, 0), 2, vec3(0.9, 0.1, 0.1))
    # for i, j, k in ti.ndrange((10, 50), (20, 60), (20, 60)):
    #     x, y, z = float(i), float(j), float(k)
    #     if ti.sqrt((x - 30)**2 + (y - 40)**2 + (z - 40)**2) <= 20:
    #         scene.set_voxel(vec3(x, y, z), 2, vec3(1.0, 0.9, 0.1))
    n = 100
    for i, j, k in ti.ndrange((-n, n), (-n, n), (-n, n)):
        x = ivec3(i, j, k)
        if distance(x, vec3(0, 0, 0)) + 0.5 <= n:
            scene.set_voxel(vec3(i, j, k), 2, vec3(1.0, 0.9, 0.1))


initialize_voxels()

scene.finish()
