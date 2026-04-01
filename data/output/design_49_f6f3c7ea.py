import FreeCAD as App
import Part
import math
import Import

if App.ActiveDocument:
    App.closeDocument(App.ActiveDocument.Name)

doc = App.newDocument("MountingPlate")

# Base plate
base = Part.makeBox(100, 100, 5)

# Corner holes
hole_radius = 5
hole_distance = 90
hole_count = 4

for i in range(hole_count):
    angle = 2 * math.pi * i / hole_count
    x = hole_distance * math.cos(angle)
    y = hole_distance * math.sin(angle)
    hole = Part.makeCylinder(5, 5)
    hole.translate(App.Vector(x, y, 2.5))
    base = base.cut(hole)

# Final shape
final_shape = base

# Add to document
obj = doc.addObject("Part::Feature", "MountingPlate")
obj.Shape = final_shape

# Display
Part.show(final_shape)

# Recompute
doc.recompute()

# Export
Import.export(doc.Objects, "../data/output/design_49_f6f3c7ea.step")