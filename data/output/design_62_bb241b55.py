import FreeCAD as App
import Part
import math

doc = App.newDocument("Flange")

base = Part.makeCylinder(50, 10)

center = Part.makeCylinder(20, 10)
base = base.cut(center)

for i in range(6):
    angle = math.radians(i * 60)
    x = 35 * math.cos(angle)
    y = 35 * math.sin(angle)

    hole = Part.makeCylinder(5, 10)
    hole.Placement.Base = App.Vector(x, y, 0)

    base = base.cut(hole)

obj = doc.addObject("Part::Feature", "Flange")
obj.Shape = base

doc.recompute()