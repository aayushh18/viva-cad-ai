import FreeCAD as App
import Part

doc = App.newDocument("HorizontalTank")

radius = 80
length = 300

cylinder = Part.makeCylinder(radius, length)

# Rotate to horizontal
import FreeCAD
cylinder.rotate(FreeCAD.Vector(0,0,0), FreeCAD.Vector(0,1,0), 90)

Part.show(cylinder)
App.ActiveDocument.recompute()