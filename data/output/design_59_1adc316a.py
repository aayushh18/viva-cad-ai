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
outer_cylinder = Part.makeCylinder(boss_radius, boss_height)
inner_cylinder = Part.makeCylinder(boss_radius - 5, boss_height)
outer_cylinder = outer_cylinder.cut(inner_cylinder)

hole_pattern = []
for i in range(4):
    angle = 2 * math.pi * i / 4
    x = boss_radius * math.cos(angle)
    y = boss_radius * math.sin(angle)
    hole_pattern.append(Part.makeCylinder(hole_radius, boss_height).translate(App.Vector(x, y, 0)))

outer_cylinder = outer_cylinder.cut(hole_pattern[0])
for hole in hole_pattern[1:]:
    outer_cylinder = outer_cylinder.cut(hole)

# PLATE WITH HOLES
plate = base
plate = plate.cut(Part.makeBox(length - 20, width - 20, thickness).translate(App.Vector(10, 10, 0)))
plate = plate.cut(Part.makeBox(20, 20, thickness).translate(App.Vector(length - 10, width - 10, 0)))
plate = plate.cut(Part.makeBox(20, 20, thickness).translate(App.Vector(10, width - 10, 0)))
plate = plate.cut(Part.makeBox(20, 20, thickness).translate(App.Vector(length - 10, 10, 0)))

# SHAFT
shaft = Part.makeCylinder(boss_radius, boss_height)
shaft = shaft.translate(App.Vector(length / 2, width / 2, 0))

# FINAL SHAPE
final_shape = plate.fuse(outer_cylinder).fuse(shaft)

# FEATURES
final_shape = final_shape.makeFillet(fillet_radius, final_shape.Edges)

# FINAL OUTPUT
obj = doc.addObject("Part::Feature", "MainPart")
obj.Shape = final_shape

Part.show(final_shape)

doc.recompute()

Import.export(doc.Objects, "../data/output/design_59_1adc316a.step")