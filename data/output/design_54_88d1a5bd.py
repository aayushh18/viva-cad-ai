import FreeCAD as App
import Part
import math
import Import

if App.ActiveDocument:
    App.closeDocument(App.ActiveDocument.Name)

doc = App.newDocument("GeneratedPart")

R = 50
n = 10
h = 10
r = 10

base = Part.makeCylinder(R, h)
tool = Part.makeCylinder(R - r, h)

base = base.cut(tool)

for i in range(n):
    angle = 2 * math.pi * i / n
    x = R * math.cos(angle)
    y = R * math.sin(angle)
    hole = Part.makeCylinder(r, h)
    hole.translate(App.Vector(x, y, 0))
    base = base.cut(hole)

final_shape = base

obj = doc.addObject("Part::Feature", "MainPart")
obj.Shape = final_shape

Part.show(final_shape)

doc.recompute()

Import.export(doc.Objects, "../data/output/design_54_88d1a5bd.step")