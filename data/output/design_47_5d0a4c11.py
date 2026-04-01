import FreeCAD as App
import Part
import math
import Import

if App.ActiveDocument:
    App.closeDocument(App.ActiveDocument.Name)

doc = App.newDocument("GeneratedPart")

base = Part.makeBox(10, 10, 10)
base.translate(App.Vector(0, 0, 0))

result = base

radius = 1.0
edges = result.Edges
result = result.makeFillet(radius, edges)

final_shape = result

obj = doc.addObject("Part::Feature", "MainPart")
obj.Shape = final_shape

Part.show(final_shape)

doc.recompute()

Import.export(doc.Objects, "../data/output/design_47_5d0a4c11.step")