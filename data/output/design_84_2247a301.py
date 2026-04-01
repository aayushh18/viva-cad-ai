import FreeCAD as App
import Part
import math
import Import

doc = App.newDocument("Plate")
plate = Part.makeBox(50, 50, 10)

# Create slot
slot_width = 10
slot_depth = 5
slot_length = 30
slot = Part.makeBox(slot_width, 10, slot_depth)
slot.Placement.Base = App.Vector(25, 25, 0)
plate = plate.cut(slot)

# Create boss
boss_radius = 10
boss_height = 5
boss = Part.makeCylinder(boss_radius, boss_height)
boss.Placement.Base = App.Vector(25, 25, 5)
plate = plate.cut(boss)

obj = doc.addObject("Part::Feature", "Plate")
obj.Shape = plate
doc.recompute()
Import.export(doc.Objects, "../data/output/design_84_2247a301.step")
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
