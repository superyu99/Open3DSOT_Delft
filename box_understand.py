from datasets.data_classes import PointCloud, Box
from pyquaternion import Quaternion


box_center_velo = [0,0,0]
# size = [anno["width"], anno["length"], anno["height"]]
size = [1, 2, 1]
orientation = Quaternion(
    axis=[0, 0, -1], radians=0.2) #* Quaternion(axis=[0, 0, -1], degrees=90)
bb = Box(box_center_velo, size, orientation)


import numpy as np
import open3d as o3d



vertices = bb.corners().T

# Create a PointCloud object from the vertices
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(vertices)

# Compute the convex hull of the point cloud
hull, _ = pcd.compute_convex_hull()

# Create a TriangleMesh from the convex hull
mesh = o3d.geometry.TriangleMesh(vertices=hull.vertices, triangles=hull.triangles)

origin = o3d.geometry.TriangleMesh.create_coordinate_frame(size=2)

# Display the mesh
o3d.visualization.draw_geometries([mesh,origin])