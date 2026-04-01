import FreeCAD as App
import Part
import math
import Import

if App.ActiveDocument:
    App.closeDocument(App.ActiveDocument.Name)

doc = App.newDocument("GeneratedPart")

# Plate
base = Part.makeBox(50, 20, 5)

# Slot
slot = Part.makeBox(30, 20, 5)
slot.translate(App.Vector(10, 0, 0))

# Boss
boss = Part.makeCylinder(5, 5)
boss.translate(App.Vector(30, 0, 0))

# Cut slot from plate
result = base.cut(slot)

# Cut boss from result
result = result.cut(boss)

# Fillet edges
result = result.makeFillet(1, result.Edges)

# Final shape
final_shape = result

# Add to document
obj = doc.addObject("Part::Feature", "MainPart")
obj.Shape = final_shape

# Display
Part.show(final_shape)

# Recompute
doc.recompute()

# Export
Import.export(doc.Objects, "../data/output/design_48_cb90c2e8.step")