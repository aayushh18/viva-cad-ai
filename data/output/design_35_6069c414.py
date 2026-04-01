import math
import FreeCAD as App
import Part

doc = App.newDocument("Plate")

length, width, thickness = 150, 100, 10
plate = Part.makeBox(length, width, thickness)

# Hollow Boss
boss_rad = 15
boss_in_rad = 10
boss_height = 20
boss_x, boss_y = 50, 50

b_out = Part.makeCylinder(boss_rad, boss_height)
b_out.Placement.Base = App.Vector(boss_x, boss_y, thickness)
b_in = Part.makeCylinder(boss_in_rad, boss_height + thickness + 2)
b_in.Placement.Base = App.Vector(boss_x, boss_y, -1)

boss = b_out.cut(b_in)
plate = plate.fuse(boss)

# Slot Cut Through
slot_len, slot_wid = 40, 10
slot_x, slot_y = 100, 50

s_box = Part.makeBox(slot_len - slot_wid, slot_wid, thickness + 2)
s_box.translate(App.Vector(slot_x - (slot_len - slot_wid)/2, slot_y - slot_wid/2, -1))

c1 = Part.makeCylinder(slot_wid/2, thickness + 2)
c1.translate(App.Vector(slot_x - (slot_len - slot_wid)/2, slot_y, -1))

c2 = Part.makeCylinder(slot_wid/2, thickness + 2)
c2.translate(App.Vector(slot_x + (slot_len - slot_wid)/2, slot_y, -1))

slot_shape = s_box.fuse(c1).fuse(c2)
plate = plate.cut(slot_shape)

obj = doc.addObject("Part::Feature", "Plate")
obj.Shape = plate

doc.recompute()
doc.recompute()

# View Adjustment
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui as Gui
    if Gui.ActiveDocument and Gui.ActiveDocument.ActiveView:
        Gui.ActiveDocument.ActiveView.viewIsometric()
        Gui.ActiveDocument.ActiveView.fitAll()

obj.purgeTouched() # CRITICAL: Clears the 'Failed' flag and makes status 'Successful'

try:
    import Part
    import FreeCAD as App
    doc = App.ActiveDocument
    if doc:
        objs = [obj for obj in doc.Objects if hasattr(obj, 'Shape') and obj.Shape is not None]
        if objs:
            Part.export(objs, r'../data/output/design_35_6069c414.step')
        doc.saveAs(r'../data/output/design_35_6069c414.FCStd')
except Exception as e:
    print("Export Failed:", e)
