import FreeCAD as App
import Part
import math
import Import

if App.ActiveDocument:
    App.closeDocument(App.ActiveDocument.Name)

doc = App.newDocument("GeneratedPart")

length = 150
width = 100
thickness = 10

base = Part.makeBox(length, width, thickness)

hole_radius = 5
n_holes = 4

for i in range(n_holes):
    angle = 2 * math.pi * i / n_holes
    x = length / 2 + (width / 2) * math.cos(angle)
    y = width / 2 + (length / 2) * math.sin(angle)
    hole = Part.makeCylinder(hole_radius, thickness)
    hole.translate(App.Vector(x, y, 0))
    base = base.cut(hole)

slot_length = 60
slot_width = 12
slot_height = thickness
slot = Part.makeBox(slot_length, slot_width, slot_height)
slot.translate(App.Vector(length / 2 - slot_length / 2, width / 2 - slot_width / 2, 0))
base = base.cut(slot)

final_shape = base

obj = doc.addObject("Part::Feature", "MainPart")
obj.Shape = final_shape

Part.show(final_shape)

doc.recompute()

Import.export(doc.Objects, "../data/output/design_61_70dfbffb.step")