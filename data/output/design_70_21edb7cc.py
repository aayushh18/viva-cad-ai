import FreeCAD as App
import Part
import Import

doc = App.newDocument("Cylinder")
cyl = Part.makeCylinder(10, 50)
hole = Part.makeCylinder(5, 50)
hole.Placement.Base = App.Vector(0, 0, 25)
result = cyl.cut(hole)

obj = doc.addObject("Part::Feature", "Cylinder")
obj.Shape = result
doc.recompute()
Import.export(doc.Objects, "../data/output/design_70_21edb7cc.step")
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
