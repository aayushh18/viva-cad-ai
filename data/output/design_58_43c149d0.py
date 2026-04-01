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
    x = length / 2 + hole_radius * math.cos(angle)
    y = width / 2 + hole_radius * math.sin(angle)
    hole = Part.makeCylinder(hole_radius, thickness)
    hole.translate(App.Vector(x, y, 0))
    base = base.cut(hole)

slot_length = 60
slot_width = 12
slot = Part.makeBox(slot_length, slot_width, thickness)
slot.translate(App.Vector(length / 2 - slot_length / 2, width / 2 - slot_width / 2, 0))
base = base.cut(slot)

boss_radius = 15
boss_height = 30
boss = Part.makeCylinder(boss_radius, boss_height)
boss.translate(App.Vector(length / 2, width / 2, thickness))
base = base.cut(boss)

fillet_radius = 2
edges = base.Edges
result = base.makeFillet(fillet_radius, edges)

cylinder_radius = 10
cylinder_height = 40
cylinder = Part.makeCylinder(cylinder_radius, cylinder_height)
cylinder.translate(App.Vector(0, 0, 0))
result = result.fuse(cylinder)

final_shape = result
obj = doc.addObject("Part::Feature", "MainPart")
obj.Shape = final_shape
Part.show(final_shape)
doc.recompute()

Import.export(doc.Objects, "../data/output/design_58_43c149d0.step")