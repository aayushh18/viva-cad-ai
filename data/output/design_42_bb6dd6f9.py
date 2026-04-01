import FreeCAD
import Part
import math

doc = FreeCAD.newDocument()

# Define dimensions
length = 10
width = 5
height = 2
fillet_radius = 0.5

# Create box
box = Part.makeBox(length, width, height)

# Create fillet shape
fillet_shape = Part.makeFillet(box, fillet_radius)

# Create result shape
result = fillet_shape

# Show result
Part.show(result)

# Recompute document
doc.recompute()

# Export to STEP file
import Import
if len(doc.Objects) == 0:
    raise ValueError("Validation Failed: doc.Objects is empty. The design was not generated properly.")
Import.export(doc.Objects, "../data/output/design_42_bb6dd6f9.step")