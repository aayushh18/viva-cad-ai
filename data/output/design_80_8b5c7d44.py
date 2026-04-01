import FreeCAD as App
import Part
import math
import Import

doc = App.newDocument("MultiStepShaft")
c1 = Part.makeCylinder(10, 20)
c2 = Part.makeCylinder(5, 30)
c2.Placement.Base = App.Vector(0, 0, 20)
c3 = Part.makeCylinder(3, 40)
c3.Placement.Base = App.Vector(0, 0, 40)
shaft = c1.fuse(c2).fuse(c3)

obj = doc.addObject("Part::Feature", "Shaft")
obj.Shape = shaft
doc.recompute()
Import.export(doc.Objects, "../data/output/design_80_8b5c7d44.step")
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
