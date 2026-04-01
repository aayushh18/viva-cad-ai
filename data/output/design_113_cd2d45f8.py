import FreeCAD as App
import Part
import math
import Import

doc = App.newDocument("Mug")

body = Part.makeCylinder(50, 100)
base = Part.makeCylinder(20, 10)
base.Placement.Base = App.Vector(0, 0, 100)
body = body.cut(base)

handle = Part.makeCylinder(5, 50)
handle.Placement.Base = App.Vector(0, 0, 0)
body = body.cut(handle)

obj = doc.addObject("Part::Feature", "Mug")
obj.Shape = body
doc.recompute()
Import.export(doc.Objects, "../data/output/design_113_cd2d45f8.step")
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
