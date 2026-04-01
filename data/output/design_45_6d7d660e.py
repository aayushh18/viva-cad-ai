import FreeCAD
import Part
import math

doc = FreeCAD.newDocument()

# Flange dimensions (DN50 = 50mm diameter, 10mm thickness)
diameter = 50
thickness = 10
bolt_diameter = 10
bolt_pitch = 20
num_bolts = 8

# Create circular plate
plate = Part.makeCylinder(diameter, thickness)

# Create central bore
bore = Part.makeCylinder(diameter - 2 * bolt_diameter, thickness)
result = plate.cut(bore)

# Create bolt holes in circular pattern
angle_step = 2 * math.pi / num_bolts
for i in range(num_bolts):
    angle = i * angle_step
    bolt_x = diameter / 2 + bolt_pitch / 2 * math.cos(angle)
    bolt_y = diameter / 2 + bolt_pitch / 2 * math.sin(angle)
    bolt_z = thickness / 2
    bolt = Part.makeCylinder(bolt_diameter, bolt_diameter)
    bolt.translate(FreeCAD.Vector(bolt_x, bolt_y, bolt_z))
    result = result.cut(bolt)

# Create shaft (DN50 = 50mm diameter, 100mm length)
shaft_length = 100
shaft = Part.makeCylinder(diameter, shaft_length)

# Combine flange and shaft
result = result.fuse(shaft)

# Position flange and shaft
result.translate(FreeCAD.Vector(0, 0, shaft_length / 2))

# Show result
Part.show(result)

# Recompute document
doc.recompute()

# Export to STEP file
Import.export(doc.Objects, "../data/output/design_45_6d7d660e.step")