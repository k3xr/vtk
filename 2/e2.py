#!/usr/bin/env python

from vtk import *

def addWireframeBoundingBox(reader, renderer) :
    outline = vtkOutlineFilter()
    outline.SetInputConnection(reader.GetOutputPort())

    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(outline.GetOutputPort())

    actor = vtkActor()
    actor.SetMapper(mapper)
    renderer.AddActor(actor)


def addBoundaryWithColorMap(reader, renderer) :
    mapper = vtkDataSetMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    reader.Update()
    range = [reader.GetOutput().GetScalarRange()[0],
             reader.GetOutput().GetScalarRange()[1]]
    mapper.SetScalarRange(range)

    transferFunction = vtkColorTransferFunction()
    transferFunction.AddRGBPoint(range[0], 1, 0, 0)
    transferFunction.AddRGBPoint(range[1], 0, 0, 1)
    mapper.SetLookupTable(transferFunction)

    actor = vtkActor()
    actor.SetMapper(mapper)
    renderer.AddActor(actor)

def addIsosurfacesAndCutPlane(reader, renderer) :
  
    contour = vtkContourFilter()
    contour.SetInputConnection(reader.GetOutputPort())
    contour.SetNumberOfContours(3)
    contour.SetValue(0, 1.5)
    contour.SetValue(1, 3.0)
    contour.SetValue(2, 4.5)

    mapper = vtkDataSetMapper()
    mapper.SetInputConnection(contour.GetOutputPort())

    reader.Update()
    range = [reader.GetOutput().GetScalarRange()[0],
             reader.GetOutput().GetScalarRange()[1]]
    mapper.SetScalarRange(range)

    actor = vtkActor()
    actor.SetMapper(mapper)
    renderer.AddActor(actor)

    cutter = vtkCutter()
    plane = vtkPlane()
    plane.SetNormal(1, 1, 1)
    plane.SetOrigin(0, 0, 0)
    cutter.SetCutFunction(plane)
    cutter.SetInputConnection(reader.GetOutputPort())

    cutter.Update()
    print cutter.GetOutput().GetInformation()

    mapper = vtkDataSetMapper()
    mapper.SetInputConnection(cutter.GetOutputPort())
    mapper.SetScalarRange(range)
    actor = vtkActor()
    actor.SetMapper(mapper)
    renderer.AddActor(actor)

reader = vtkDataSetReader()
reader.SetFileName('data/noise.vtk')

renderer = vtkRenderer()
renderer.SetBackground(0.2, 0.3, 0.4)

addWireframeBoundingBox(reader, renderer)
#addBoundaryWithColorMap(reader, renderer)
#addIsosurfacesAndCutPlane(reader, renderer)

win = vtkRenderWindow()
win.AddRenderer(renderer)
win.SetSize(800, 800)

interactor = vtkRenderWindowInteractor()
interactor.SetRenderWindow(win)
interactor.Initialize()
interactor.Start()
