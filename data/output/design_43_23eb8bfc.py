import FreeCAD
import Part

doc = FreeCAD.newDocument()

# Define dimensions
length = 10
width = 5
height = 2

# Create a box
box = Part.makeBox(length, width, height)

# Position the box at the origin
box.translate(FreeCAD.Vector(0, 0, 0))

# Store the result
result = box

# Show the result in the FreeCAD GUI
Part.show(result)

# Recompute the document
doc.recompute()

# Export the document to a STEP file
Import.export(doc.Objects, "../data/output/design_43_23eb8bfc.step")