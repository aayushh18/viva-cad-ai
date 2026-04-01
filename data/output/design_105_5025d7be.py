import FreeCAD as App
import Part
import math
import Import

doc = App.newDocument("BoxWithFillet")
box = Part.makeBox(20, 20, 20)
fillet = box.makeFillet(2, box.Edges)

obj = doc.addObject("Part::Feature", "BoxWithFillet")
obj.Shape = fillet
doc.recompute()
Import.export(doc.Objects, "../data/output/design_105_5025d7be.step")
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
