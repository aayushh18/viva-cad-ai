import FreeCAD as App
import Part
import math
import Import

doc = App.newDocument("MountingPlate")

plate = Part.makeBox(100, 100, 5)

for i in range(4):
    angle = math.radians(i * 90)
    x = 45 * math.cos(angle) + 50
    y = 45 * math.sin(angle) + 50
    hole = Part.makeCylinder(5, 10)
    hole.Placement.Base = App.Vector(x, y, 0)
    plate = plate.cut(hole)

obj = doc.addObject("Part::Feature", "MountingPlate")
obj.Shape = plate
doc.recompute()
Import.export(doc.Objects, "../data/output/design_93_6f077814.step")
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
