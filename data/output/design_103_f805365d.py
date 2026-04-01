import FreeCAD as App
import Part
import Import

doc = App.newDocument("BoxFillet")
box = Part.makeBox(20, 20, 20)
fillet = box.makeFillet(2, box.Edges)

obj = doc.addObject("Part::Feature", "BoxFillet")
obj.Shape = fillet
doc.recompute()
Import.export(doc.Objects, "../data/output/design_103_f805365d.step")
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
