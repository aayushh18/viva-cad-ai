import FreeCAD as App
import Part
import Import

doc = App.newDocument("Cylinder")
cyl = Part.makeCylinder(10, 50)
obj = doc.addObject("Part::Feature", "Cylinder")
obj.Shape = cyl
fillet = obj.Shape.makeFillet(2, obj.Shape.Edges)
obj.Shape = fillet
doc.recompute()
Import.export(doc.Objects, "../data/output/design_76_c14447c9.step")
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
