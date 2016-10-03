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
# to a vtkVolumeProperty.
# Intead of vtkActor use vtkVolume and assign to it the mapper and the property.
# volumes are added to renderers using AddVolume

mapper = vtkSmartVolumeMapper()
mapper.SetInputConnection(reader.GetOutputPort())

opacityTransferFunction = vtkPiecewiseFunction()
opacityTransferFunction.AddPoint(0, 0.0)
opacityTransferFunction.AddPoint(255, 0.2)

colorTransferFunction = vtkColorTransferFunction()
colorTransferFunction.AddRGBPoint(0, 1, 0, 0)
colorTransferFunction.AddRGBPoint(255, 0, 0, 1)

volumeProperty = vtkVolumeProperty()
volumeProperty.SetColor(colorTransferFunction)
volumeProperty.SetScalarOpacity(opacityTransferFunction)
volumeProperty.SetInterpolationTypeToLinear()

volume = vtkVolume()
volume.SetProperty(volumeProperty)
volume.SetMapper(mapper)

renderer.AddVolume(volume)

outline = vtkOutlineFilter()
outline.SetInputConnection(reader.GetOutputPort())

mapper = vtkPolyDataMapper()
mapper.SetInputConnection(outline.GetOutputPort())

actor = vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(0, 0, 0)
renderer.AddActor(actor)

####################

win = vtkRenderWindow()
win.AddRenderer(renderer)
win.SetSize(800, 800)

interactor = vtkRenderWindowInteractor()
interactor.SetRenderWindow(win)
interactor.Initialize()
interactor.Start()


