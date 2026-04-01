import FreeCAD
import Part
import math

doc = FreeCAD.newDocument()

# Define dimensions
length = 100
width = 50
height = 20
fillet_radius = 5

# Create box
box = Part.makeBox(length, width, height)

# Add fillet edges
fillet_edges = []
for i in range(4):
    if i == 0:
        fillet_edges.append(Part.makeCircle(fillet_radius, FreeCAD.Vector(length / 2, width / 2, 0)))
    elif i == 1:
        fillet_edges.append(Part.makeCircle(fillet_radius, FreeCAD.Vector(length / 2, width / 2, height)))
    elif i == 2:
        fillet_edges.append(Part.makeCircle(fillet_radius, FreeCAD.Vector(0, width / 2, height / 2)))
    else:
        fillet_edges.append(Part.makeCircle(fillet_radius, FreeCAD.Vector(length, width / 2, height / 2)))

# Fuse edges
final_shape = box.fuse(fillet_edges)

# Show final shape
Part.show(final_shape)

# Export to STEP
Import.export(doc.Objects, "../data/output/design_36_de0c197d.step")

# Recompute document
doc.recompute()