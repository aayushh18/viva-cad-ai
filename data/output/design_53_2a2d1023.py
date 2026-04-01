import FreeCAD as App
import Part
import math
import Import

if App.ActiveDocument:
    App.closeDocument(App.ActiveDocument.Name)

doc = App.newDocument("GeneratedPart")

# Plate
base = Part.makeBox(100, 50, 10)

# Slot
slot = Part.makeBox(20, 10, 10)
slot.translate(App.Vector(40, 25, 5))

# Boss
boss = Part.makeCylinder(10, 10)
boss.translate(App.Vector(60, 25, 5))

# Cut slot
result = base.cut(slot)

# Cut boss
result = result.cut(boss)

# Fillet edges
result = result.makeFillet(5, result.Edges)

# Final shape
final_shape = result

# Add to document
obj = doc.addObject("Part::Feature", "MainPart")
obj.Shape = final_shape

# Display final shape
Part.show(final_shape)

# Recompute
doc.recompute()

# Export
Import.export(doc.Objects, "../data/output/design_53_2a2d1023.step")