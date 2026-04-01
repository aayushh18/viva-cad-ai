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
hole_radius = 5
slot_length = 60
slot_width = 12
boss_radius = 15
boss_height = 30
fillet_radius = 2

base = Part.makeBox(length, width, thickness)

# FLANGE
R = (length - 2 * hole_radius) / 2
n = 4
flange = Part.makeCylinder(R, thickness)
flange = flange.cut(Part.makeCylinder(R - hole_radius, thickness))
for i in range(n):
    angle = 2 * math.pi * i / n
    x = R * math.cos(angle)
    y = R * math.sin(angle)
    hole = Part.makeCylinder(hole_radius, thickness)
    hole.translate(App.Vector(x, y, thickness / 2))
    flange = flange.cut(hole)

# PLATE WITH HOLES
plate = base.cut(flange)

# SLOT
slot = Part.makeBox(slot_length, slot_width, thickness)
slot.translate(App.Vector((length - slot_length) / 2, (width - slot_width) / 2, 0))
plate = plate.cut(slot)

# BOSS
boss = Part.makeCylinder(boss_radius, boss_height)
boss.translate(App.Vector((length - boss_radius * 2) / 2, (width - boss_radius * 2) / 2, thickness))
plate = plate.cut(boss)

# FILLET
plate = plate.makeFillet(fillet_radius, plate.Edges)

final_shape = plate

obj = doc.addObject("Part::Feature", "MainPart")
obj.Shape = final_shape

Part.show(final_shape)

doc.recompute()

Import.export(doc.Objects, "../data/output/design_60_f7b9dad5.step")