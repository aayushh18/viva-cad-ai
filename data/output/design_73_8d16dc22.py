import FreeCAD as App
import Part
import Import

doc = App.newDocument("SteppedShaft")
c1 = Part.makeCylinder(10, 20)
c2 = Part.makeCylinder(5, 30)
c2.Placement.Base = App.Vector(0, 0, 20)
shaft = c1.fuse(c2)

obj = doc.addObject("Part::Feature", "SteppedShaft")
obj.Shape = shaft
doc.recompute()
Import.export(doc.Objects, "../data/output/design_73_8d16dc22.step")
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
