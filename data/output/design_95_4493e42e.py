import FreeCAD as App
import Part
import math
import Import

doc = App.newDocument("Plate")
plate = Part.makeBox(100, 50, 10)

# Slot
slot_width = 20
slot_depth = 10
slot_height = 40
slot_x = 25
slot_y = 0
slot = Part.makeBox(slot_width, slot_depth, slot_height)
slot.Placement.Base = App.Vector(slot_x, slot_y, 0)
plate = plate.cut(slot)

# Boss
boss_radius = 20
boss_height = 10
boss_x = 75
boss_y = 0
boss = Part.makeCylinder(boss_radius, boss_height)
boss.Placement.Base = App.Vector(boss_x, boss_y, 0)
plate = plate.cut(boss)

obj = doc.addObject("Part::Feature", "Plate")
obj.Shape = plate
doc.recompute()
Import.export(doc.Objects, "../data/output/design_95_4493e42e.step")
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
