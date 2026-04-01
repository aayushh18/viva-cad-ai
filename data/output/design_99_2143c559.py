import FreeCAD as App
import Part
import Import

doc = App.newDocument("Cylinder")
cyl = Part.makeCylinder(10, 40)
obj = doc.addObject("Part::Feature", "Cylinder")
obj.Shape = cyl
doc.recompute()
Import.export(doc.Objects, "../data/output/design_99_2143c559.step")
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
