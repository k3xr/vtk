#!/usr/bin/env python

from vtk import *

reader = vtkDataSetReader()
reader.SetFileName('data/ironProt.vtk')

renderer = vtkRenderer()
renderer.SetBackground(1, 1, 1)

########################################
# To complete
# Hint: Create a 3D texture volume mapper and connect its input to the reader
# create the scalar to RGBA transfer function using a vtkColorTransferFunction
# for colors and a vtkPiecewiseFunction for the opacity. Assign the functions
# to a volume property.
# Intead of vtkActor use vtkVolume and assign to it the mapper and the property.
# volumes are added to renderers using AddVolume

####################

win = vtkRenderWindow()
win.AddRenderer(renderer)
win.SetSize(800, 800)

interactor = vtkRenderWindowInteractor()
interactor.SetRenderWindow(win)
interactor.Initialize()
interactor.Start()


