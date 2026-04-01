import FreeCAD as App
import Part
import Import

doc = App.newDocument("Plate")
plate = Part.makeBox(50, 50, 10)
hole = Part.makeCylinder(5, 10)
hole.Placement.Base = App.Vector(25, 25, 0)
plate = plate.cut(hole)

obj = doc.addObject("Part::Feature", "Plate")
obj.Shape = plate
doc.recompute()
Import.export(doc.Objects, "../data/output/design_69_9552a747.step")
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
