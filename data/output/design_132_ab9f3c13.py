import FreeCAD as App
import Part

doc = App.newDocument("HorizontalTank")

radius = 80
length = 300
thickness = 8

# Create hollow shell
outer = Part.makeCylinder(radius, length)
inner = Part.makeCylinder(radius - thickness, length)
h_tank = outer.cut(inner)

# Rotate to horizontal
import FreeCAD
h_tank.rotate(FreeCAD.Vector(0,0,0), FreeCAD.Vector(0,1,0), 90)

Part.show(h_tank)
doc.recompute()