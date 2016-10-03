#!/usr/bin/python

from vtk import *
import struct

def read_data(filename) :
    """Reads a vector field from a file starting with the field dimensions
       in ASCII format and followed by the float data in binary format.
       Returns the vtkImageData object with the field"""
    datafile = file(filename)
    x, y, z = map(int, datafile.readline().split())

    data = vtkImageData()
    data.SetSpacing(1, 1, 1)
    data.SetDimensions(x, y, z)
    array = vtkFloatArray()
    array.SetNumberOfComponents(3)
    array.SetNumberOfTuples(x * y * z)
    for i in range(x * y * z * 3) :
        array.SetValue(i, struct.unpack('f', datafile.read(4))[0])
    data.GetPointData().SetVectors(array)

    return data

# Reading the vector field
field = read_data('data/TwoSwirls_64x64x64.vec')

def createOutline(data) :
    ########################################
    # To complete
    # Return and actor to show the outline of the dataset

    actor = vtkActor()
    return actor

########################################
# To complete
# Create a vtkPolyData or a filter that outputs vtkPolyData (e.g.
# vtkPlaneSource) to use its points as seed points.
seedsFilter = None
seedsData = None

########################################
# To complete
# Create a vtkStreamLine filter set the field as input data, configure the
# integration parameters and use SetSource to connect the vtkPolyData that
# outpus the locations of the seed points. If the vtkPolyData is generated
# by a filter call Update before connecting it.
streamLine =

########################################
# To complete
# Create a filter that converts the output of the streamline filter into
# vtkPolyData. Two options to test are vtkTubeFilter and vtkRibbonFilter.
# Assign the result to path filter.

pathFilter =

########################################

# Mapper and actor
mapper = vtkPolyDataMapper()
mapper.SetInputConnection(pathFilter.GetOutputPort())
datarange = [field.GetScalarRange()[0], field.GetScalarRange()[1]]
mapper.SetScalarRange(datarange)
transferFunction = vtkColorTransferFunction()
transferFunction.AddRGBPoint(datarange[0], 1, 0, 0)
transferFunction.AddRGBPoint(datarange[1], 0, 0, 1)
mapper.SetLookupTable(transferFunction)

actor = vtkActor()
actor.SetMapper(mapper)

# Creating the renderer and the render window
renderer = vtkRenderer()
renderer.AddActor(actor)
renderer.AddActor(createOutline(field))
renderer.SetBackground(0.2, 0.3, 0.4)

window = vtkRenderWindow()
window.AddRenderer(renderer)
window.SetSize(800, 800)

# Creating the interactor that handles the window events and provides
# the main rendering loop
interactor =vtkRenderWindowInteractor()
interactor.SetRenderWindow(window)
interactorStyle = vtkInteractorStyleSwitch()
interactor.SetInteractorStyle(interactorStyle)
interactorStyle.SetCurrentStyleToTrackballCamera()

########################################
# To complete (part2)
# Assign the interactor to the widget and hook the observer callbacks to
# the events StartInteractionEvent and EndInteractionEvent. The end
# interaction event has to refresh the vtkPolyData for the seeds and
# trigger rendering

########################################

interactor.Initialize()
interactor.Start()




