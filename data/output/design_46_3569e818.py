import FreeCAD
import Part
import math

doc = FreeCAD.newDocument()

# Define gear parameters
pitch_diameter = 50  # mm
number_of_teeth = 20
tooth_width = 5  # mm
hole_diameter = 5  # mm
hole_pitch = 10  # mm

# Create gear body
gear_body = Part.makeCylinder(pitch_diameter / 2, pitch_diameter, 100)

# Create central bore
bore = Part.makeCylinder(pitch_diameter / 2, pitch_diameter / 2, 100)
gear_body = gear_body.cut(bore)

# Create bolt holes
bolt_holes = []
for i in range(number_of_teeth):
    angle = 2 * math.pi * i / number_of_teeth
    x = pitch_diameter / 2 + hole_pitch * math.cos(angle)
    y = pitch_diameter / 2 + hole_pitch * math.sin(angle)
    bolt_holes.append(Part.makeCylinder(hole_diameter / 2, hole_diameter, 100).translate(FreeCAD.Vector(x, y, 0)))

gear_body = gear_body.fuse(bolt_holes)

# Create shaft
shaft = Part.makeCylinder(pitch_diameter / 2, pitch_diameter, 200)

# Add gear to document
result = gear_body

# Show result
Part.show(result)

# Export to STEP
Import.export(doc.Objects, "../data/output/design_46_3569e818.step")

# Recompute document
doc.recompute()