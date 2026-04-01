import FreeCAD as App
import Part
import Import

doc = App.newDocument("BoxWithHole")
box = Part.makeBox(20, 20, 10)
hole = Part.makeCylinder(5, 10)
hole.Placement.Base = App.Vector(10, 10, 5)
result = box.cut(hole)

obj = doc.addObject("Part::Feature", "Result")
obj.Shape = result
doc.recompute()
Import.export(doc.Objects, "../data/output/design_81_5f5094dc.step")
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
