import FreeCAD as App
import Part
import math
import Import

if App.ActiveDocument:
    App.closeDocument(App.ActiveDocument.Name)

doc = App.newDocument("GeneratedPart")

base = Part.makeBox(100, 20, 10)

slot_width = 10
slot_height = 10
slot_depth = 5
slot_pos_x = 50
slot_pos_y = 5

slot = Part.makeBox(slot_width, slot_depth, slot_height)
slot.translate(App.Vector(slot_pos_x, slot_pos_y, 0))
result = base.cut(slot)

boss_radius = 5
boss_height = 10
boss_pos_x = 70
boss_pos_y = 5

boss = Part.makeCylinder(boss_radius, boss_height)
boss.translate(App.Vector(boss_pos_x, boss_pos_y, 0))
result = result.cut(boss)

final_shape = result

obj = doc.addObject("Part::Feature", "MainPart")
obj.Shape = final_shape

Part.show(final_shape)

doc.recompute()

Import.export(doc.Objects, "../data/output/design_57_fe9c98d4.step")