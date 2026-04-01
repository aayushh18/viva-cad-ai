import FreeCAD
import Part
import math

doc = FreeCAD.newDocument()

# Plate dimensions
plate_thickness = 10  # mm
plate_diameter = 100  # mm
bolt_diameter = 10  # mm
bolt_pitch = 20  # mm

# Create plate
plate = Part.makeCylinder(plate_diameter / 2, plate_thickness)
plate.translate(FreeCAD.Vector(0, 0, plate_thickness / 2))

# Add central bore
bore = Part.makeCylinder(plate_diameter / 2, plate_thickness)
bore.translate(FreeCAD.Vector(0, 0, plate_thickness / 2))
plate = Part.cut(plate, bore)

# Add bolt holes
num_bolts = 4
bolt_radius = plate_diameter / 2 / 2
for i in range(num_bolts):
    angle = 2 * math.pi * i / num_bolts
    bolt_x = plate_diameter / 2 + bolt_pitch * math.cos(angle)
    bolt_y = plate_diameter / 2 + bolt_pitch * math.sin(angle)
    bolt = Part.makeCylinder(bolt_diameter / 2, plate_thickness)
    bolt.translate(FreeCAD.Vector(bolt_x, bolt_y, plate_thickness / 2))
    plate = Part.cut(plate, bolt)

# Add mounting plate to document
doc.addObject("Part::Feature", "MountingPlate").Shape = plate

# Show final shape
Part.show(plate)
doc.recompute()

# Export to STEP file
Import.export(doc.Objects, "../data/output/design_37_f075daa2.step")