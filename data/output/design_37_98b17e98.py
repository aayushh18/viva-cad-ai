import FreeCAD as App
import FreeCADGui as Gui
import Part

doc = App.newDocument("TextCAD")
result = None

box_0 = doc.addObject("Part::Box", "Box_0")
box_0.Length = 150.0
box_0.Width = 100.0
box_0.Height = 10.0
doc.recompute()

if result is None:
    result = box_0
else:
    fusion_0 = doc.addObject("Part::Fuse", "Fuse_0")
    fusion_0.Base = result
    fusion_0.Tool = box_0
    doc.recompute()
    result = fusion_0

if 5.0*2 <= min(150.0,100.0):

    offset = 10
    positions = [
        (offset, offset),
        (150.0-offset, offset),
        (offset, 100.0-offset),
        (150.0-offset, 100.0-offset)
    ]

    for j, pos in enumerate(positions):
        cut_cyl_1_j = doc.addObject("Part::Cylinder", f"CutCyl1_{j}")
        cut_cyl_1_j.Radius = 5.0
        cut_cyl_1_j.Height = 10.0 + 10 if 10.0 else 50
        cut_cyl_1_j.Placement.Base = App.Vector(pos[0], pos[1], -5)
        doc.recompute()

        cut_1_j = doc.addObject("Part::Cut", f"Cut1_{j}")
        cut_1_j.Base = result
        cut_1_j.Tool = cut_cyl_1_j
        doc.recompute()
        result = cut_1_j

# Slot components
sbox_2 = doc.addObject("Part::Box", "SlotBox_2")
sbox_2.Length = 60.0 - 12.0
sbox_2.Width = 12.0
sbox_2.Height = 10.0 + 10 if 10.0 else 50
if 150.0 is not None and 100.0 is not None:
    cx, cy = 150.0/2, 100.0/2
else:
    cx, cy = 0, 0

sbox_2.Placement.Base = App.Vector(cx - (60.0-12.0)/2, cy - 12.0/2, -5)

scyl1_2 = doc.addObject("Part::Cylinder", "SlotCyl1_2")
scyl1_2.Radius = 12.0/2
scyl1_2.Height = 10.0 + 10 if 10.0 else 50
scyl1_2.Placement.Base = App.Vector(cx - (60.0-12.0)/2, cy, -5)

scyl2_2 = doc.addObject("Part::Cylinder", "SlotCyl2_2")
scyl2_2.Radius = 12.0/2
scyl2_2.Height = 10.0 + 10 if 10.0 else 50
scyl2_2.Placement.Base = App.Vector(cx + (60.0-12.0)/2, cy, -5)

doc.recompute()

sfuse1_2 = doc.addObject("Part::Fuse", "SlotFuse1_2")
sfuse1_2.Base = sbox_2
sfuse1_2.Tool = scyl1_2
doc.recompute()

sfuse2_2 = doc.addObject("Part::Fuse", "SlotFuse2_2")
sfuse2_2.Base = sfuse1_2
sfuse2_2.Tool = scyl2_2
doc.recompute()

cut_2 = doc.addObject("Part::Cut", "SlotCut_2")
cut_2.Base = result
cut_2.Tool = sfuse2_2
doc.recompute()
result = cut_2

boss_3 = doc.addObject("Part::Cylinder", "Boss_3")
boss_3.Radius = 15.0
boss_3.Height = 30.0
if 150.0 is not None and 100.0 is not None:
    boss_3.Placement.Base = App.Vector(150.0/2, 100.0/2, 10.0 if 10.0 else 0)
else:
    boss_3.Placement.Base = App.Vector(0, 0, 10.0 if 10.0 else 0)
doc.recompute()

bfuse_3 = doc.addObject("Part::Fuse", "BossFuse_3")
bfuse_3.Base = result
bfuse_3.Tool = boss_3
doc.recompute()
result = bfuse_3

try:
    shape = result.Shape
    fillet_shape = shape.makeFillet(2.0, shape.Edges)
    fillet_obj = doc.addObject("Part::Feature", "Fillet_4")
    fillet_obj.Shape = fillet_shape
    result = fillet_obj
    doc.recompute()
except Exception as e:
    print(f"Fillet failed: {e}")

doc.recompute()
try:
    if Gui.ActiveDocument and Gui.ActiveDocument.ActiveView:
        Gui.ActiveDocument.ActiveView.viewIsometric()
        Gui.ActiveDocument.ActiveView.fitAll()
except Exception as e:
    print(f"View scaling failed: {e}")

App.ActiveDocument.saveAs("/home/aayush/Downloads/viva-cad-ai/data/output/design_37_98b17e98.FCStd")
