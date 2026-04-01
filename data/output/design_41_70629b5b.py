import FreeCAD
import Part
import math

doc = FreeCAD.newDocument()

# Extract dimensions from user input
radius = 10
height = 40

# Create cylinder
cylinder = Part.makeCylinder(radius, height)

# Position cylinder at origin
cylinder.translate(FreeCAD.Vector(0, 0, 0))

# Store result in variable named: result
result = cylinder

# Show result in FreeCAD GUI
Part.show(result)

# Recompute document
doc.recompute()

# Export result to STEP file
import Import
if len(doc.Objects) == 0:
    raise ValueError("Validation Failed: doc.Objects is empty. The design was not generated properly.")
Import.export(doc.Objects, "../data/output/design_41_70629b5b.step")