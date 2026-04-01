import FreeCAD as App
import Part
import math
import Import

if App.ActiveDocument:
    App.closeDocument(App.ActiveDocument.Name)

doc = App.newDocument("GeneratedPart")

base = Part.makeBox(10, 10, 10)
result = base

radius = 1
edges = result.Edges
result = result.makeFillet(radius, edges)

final_shape = result
obj = doc.addObject("Part::Feature", "MainPart")
obj.Shape = final_shape

Part.show(final_shape)

doc.recompute()

Import.export(doc.Objects, "../data/output/design_62_025de01a.step")