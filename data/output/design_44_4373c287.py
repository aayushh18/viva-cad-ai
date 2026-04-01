import FreeCAD
import Part
import math

doc = FreeCAD.newDocument()

# Flange dimensions
outer_diameter = 100  # mm
inner_diameter = 50   # mm
bore_depth = 20        # mm
bolt_diameter = 10     # mm
bolt_pitch = 20         # mm
num_bolts = 8

# Create circular plate
flange_plate = Part.makeCylinder(outer_diameter / 2, bore_depth)

# Add central bore
bore = Part.makeCylinder(inner_diameter / 2, bore_depth)
flange_plate = flange_plate.cut(bore)

# Add bolt holes in circular pattern
bolt_holes = []
for i in range(num_bolts):
    angle = 2 * math.pi * i / num_bolts
    x = outer_diameter / 2 + bolt_pitch / 2 * math.cos(angle)
    y = outer_diameter / 2 + bolt_pitch / 2 * math.sin(angle)
    bolt_holes.append(Part.makeCylinder(bolt_diameter / 2, bore_depth).translate(FreeCAD.Vector(x, y, 0)))

flange_plate = flange_plate.cut(Part.makeCompound(bolt_holes))

result = flange_plate

Part.show(result)
doc.recompute()

import Import
if len(doc.Objects) == 0:
    raise ValueError("Validation Failed: doc.Objects is empty. The design was not generated properly.")
Import.export(doc.Objects, "../data/output/design_44_4373c287.step")