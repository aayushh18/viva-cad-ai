import FreeCAD as App
import Part
import math
import Import

doc = App.newDocument("Plate")
plate = Part.makeBox(100, 50, 10)

hole = Part.makeCylinder(15, 10)
hole.Placement.Base = App.Vector(75, 25, 0)
plate = plate.cut(hole)

obj = doc.addObject("Part::Feature", "Plate")
obj.Shape = plate
doc.recompute()
Import.export(doc.Objects, "../data/output/design_89_d51dfbbe.step")
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
