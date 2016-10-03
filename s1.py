#!/usr/bin/env python

from vtk import *

sphere = vtkSphereSource()
sphere.SetCenter(0, 0, 0)
sphere.SetRadius(1)
# Changing the tessellation resolution
sphere.SetThetaResolution(16)
sphere.SetPhiResolution(16)

# Mapper object that will convert the sphere source into polygonal mesh
mapper = vtkPolyDataMapper()
mapper.SetInputConnection(sphere.GetOutputPort())

# Creating the actor that will place the polygonal mesh into the
# scene and manage it's render attributes. */
actor = vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(1, 0, 0)

# Creating the renderer and the render window
renderer = vtkRenderer()
renderer.AddActor(actor)
renderer.SetBackground(0.2, 0.3, 0.4)

########################################
# To complete
# Adding a cone actor

cone = vtkConeSource()
cone.SetCenter(0, 0, 0)
cone.SetHeight(2)
cone.SetRadius(1)
cone.SetResolution(64)

mapper = vtkPolyDataMapper()
mapper.SetInputConnection(cone.GetOutputPort())

actor = vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(1, 0.5, 0)
actor.SetPosition(2.25, 0, 0)

renderer.AddActor(actor)

########################################
# To complete
# Adding a cube with the polygonal data set defined by hand

# Creating the point array
points = vtkPoints()
coords = [[i % 2 * 2, (i >> 1) % 2 * 2, (i >> 2) * 2] for i in range(8)]
for c in coords :
    points.InsertNextPoint(c)

# Creating the cell array
quads = [[0, 1, 3, 2], [4, 5, 7, 6],
         [0, 2, 6, 4], [1, 3, 7, 5],
         [0, 1, 5, 4], [2, 3, 7, 6]]

cells = vtkCellArray()
for indices in quads :
    face = vtkIdList()
    for index in indices:
        face.InsertNextId(index)
    cells.InsertNextCell(face)
    # cells.InsertNextCell(4, indices) # Only for VTK 6.2
polyData = vtkPolyData()
polyData.SetPoints(points)
polyData.SetPolys(cells)

mapper = vtkPolyDataMapper()
mapper.SetInputData(polyData)

actor = vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(1, 1, 0)
actor.SetPosition(3.5, -1, -1)

renderer.AddActor(actor)

#########################################
## To complete
## Adding a polygonal model loaded from a .ply file
reader = vtkPLYReader()
reader.SetFileName("data/bunny.ply")

normalFilter = vtkPolyDataNormals()
normalFilter.ComputePointNormalsOn()
normalFilter.ComputeCellNormalsOff()
normalFilter.SetInputConnection(reader.GetOutputPort())

mapper = vtkPolyDataMapper()
mapper.SetInputConnection(normalFilter.GetOutputPort())

actor = vtkActor()
actor.SetMapper(mapper)
actor.SetPosition(6.75, -1, 0)
actor.SetScale(10, 10, 10)
actor.GetProperty().SetColor(1, 1, 0.5)

renderer.AddActor(actor)

# Creating the window and assinging the renderer to it

win = vtkRenderWindow()
win.AddRenderer(renderer)
win.SetSize(800, 800)

# Creating the interactor that handles the window events and provides
# the main rendering loop
interactor = vtkRenderWindowInteractor()
interactor.SetRenderWindow(win)

interactor.Initialize()
interactor.Start()
