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

# Create fillet shape
fillet_shape = Part.makeFillet(box, fillet_radius)

# Store result
result = fillet_shape

# Show result
Part.show(result)

# Export to STEP file
Import.export(doc.Objects, "../data/output/design_39_b3453232.step")

# Recompute document
doc.recompute()