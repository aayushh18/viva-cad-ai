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
    hole = Part.makeCylinder(5, 5)
    hole.Placement.Base = App.Vector(x, y, 2.5)
    plate = plate.cut(hole)

obj = doc.addObject("Part::Feature", "Plate")
obj.Shape = plate
doc.recompute()
Import.export(doc.Objects, "../data/output/design_65_ab1f415f.step")
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
