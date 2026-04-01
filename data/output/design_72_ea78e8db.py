import FreeCAD as App
import Part
import Import

doc = App.newDocument("Shaft")
c1 = Part.makeCylinder(10, 20)
c2 = Part.makeCylinder(5, 30)
c2.Placement.Base = App.Vector(0, 0, 20)
shaft = c1.fuse(c2)

obj = doc.addObject("Part::Feature", "Shaft")
obj.Shape = shaft
doc.recompute()
Import.export(doc.Objects, "../data/output/design_72_ea78e8db.step")
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
