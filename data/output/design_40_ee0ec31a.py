import FreeCAD
import Part
import math

doc = FreeCAD.newDocument()

# Plate dimensions
plate_diameter = 100.0  # mm
plate_thickness = 10.0  # mm
slot_width = 20.0  # mm
slot_depth = 10.0  # mm
boss_diameter = 20.0  # mm
boss_height = 10.0  # mm

# Plate
plate = Part.makeCylinder(plate_diameter / 2, plate_thickness)

# Slot
slot_radius = plate_diameter / 2 - slot_width / 2
slot = Part.makeCylinder(slot_radius, slot_depth)
slot.translate(FreeCAD.Vector(0, 0, plate_thickness / 2 - slot_depth / 2))

# Boss
boss = Part.makeCylinder(boss_diameter / 2, boss_height)
boss.translate(FreeCAD.Vector(0, 0, plate_thickness / 2 - boss_height / 2))

# Cut slot and boss from plate
result = plate.cut(slot).cut(boss)

# Show result
Part.show(result)

# Export to STEP
Import.export(doc.Objects, "../data/output/design_40_ee0ec31a.step")

# Recompute document
doc.recompute()