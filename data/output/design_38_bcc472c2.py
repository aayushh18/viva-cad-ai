import FreeCAD
import Part
import math

doc = FreeCAD.newDocument()

# Create cylinder
cylinder = Part.makeCylinder(10, 40)
cylinder.translate(FreeCAD.Vector(0, 0, 20))

# Show the cylinder
cylinder.Shape.show()

# Export the document to a STEP file
Import = FreeCAD.importModule("Import")
Import.export(doc.Objects, "../data/output/design_38_bcc472c2.step")

# Recompute the document
doc.recompute()