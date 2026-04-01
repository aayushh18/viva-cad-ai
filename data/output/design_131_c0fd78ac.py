import FreeCAD as App
import Part

doc = App.newDocument("Tank")

radius = 100
height = 300
thickness = 10

outer = Part.makeCylinder(radius, height)
inner = Part.makeCylinder(radius - thickness, height)

tank = outer.cut(inner)

Part.show(tank)
doc.recompute()