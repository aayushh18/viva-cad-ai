import FreeCAD as App
import Part
import math
import Import

doc = App.newDocument("FilletBox")
box = Part.makeBox(20, 20, 20)
fillet = box.makeFillet(2, box.Edges)

obj = doc.addObject("Part::Feature", "FilletBox")
obj.Shape = fillet
doc.recompute()
Import.export(doc.Objects, "../data/output/design_104_8f46f654.step")
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
