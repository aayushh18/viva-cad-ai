import FreeCAD as App
import Part
import math
import Import

doc = App.newDocument("Plate")

plate = Part.makeBox(100, 100, 10)

slot = Part.makeBox(20, 10, 10)
slot.Placement.Base = App.Vector(50, 50, 0)
plate = plate.cut(slot)

boss = Part.makeCylinder(10, 10)
boss.Placement.Base = App.Vector(70, 70, 0)
plate = plate.cut(boss)

obj = doc.addObject("Part::Feature", "Plate")
obj.Shape = plate
doc.recompute()
Import.export(doc.Objects, "../data/output/design_83_3aca2247.step")
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
