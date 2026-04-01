import FreeCAD as App
import FreeCADGui as Gui
import Part

doc = App.newDocument("TextCAD")
result = None

plate_0 = doc.addObject("Part::Box", "Plate_0")
plate_0.Length = 200.0
plate_0.Width = 150.0
plate_0.Height = 10.0
doc.recompute()

if result is None:
    result = plate_0
else:
    fusion_0 = doc.addObject("Part::Fuse", "Fuse_0")
    fusion_0.Base = result
    fusion_0.Tool = plate_0
    doc.recompute()
    result = fusion_0

# Slot components
sbox_1 = doc.addObject("Part::Box", "SlotBox_1")
sbox_1.Length = 20.0 - 5.0
sbox_1.Width = 5.0
sbox_1.Height = 10.0 + 10 if 10.0 else 50
if 200.0 is not None and 150.0 is not None:
    cx, cy = 200.0/2, 150.0/2
else:
    cx, cy = 0, 0

sbox_1.Placement.Base = App.Vector(cx - (20.0-5.0)/2, cy - 5.0/2, -5)

scyl1_1 = doc.addObject("Part::Cylinder", "SlotCyl1_1")
scyl1_1.Radius = 5.0/2
scyl1_1.Height = 10.0 + 10 if 10.0 else 50
scyl1_1.Placement.Base = App.Vector(cx - (20.0-5.0)/2, cy, -5)

scyl2_1 = doc.addObject("Part::Cylinder", "SlotCyl2_1")
scyl2_1.Radius = 5.0/2
scyl2_1.Height = 10.0 + 10 if 10.0 else 50
scyl2_1.Placement.Base = App.Vector(cx + (20.0-5.0)/2, cy, -5)

doc.recompute()

sfuse1_1 = doc.addObject("Part::Fuse", "SlotFuse1_1")
sfuse1_1.Base = sbox_1
sfuse1_1.Tool = scyl1_1
doc.recompute()

sfuse2_1 = doc.addObject("Part::Fuse", "SlotFuse2_1")
sfuse2_1.Base = sfuse1_1
sfuse2_1.Tool = scyl2_1
doc.recompute()

cut_1 = doc.addObject("Part::Cut", "SlotCut_1")
cut_1.Base = result
cut_1.Tool = sfuse2_1
doc.recompute()
result = cut_1

boss_2 = doc.addObject("Part::Cylinder", "Boss_2")
boss_2.Radius = 10.0
boss_2.Height = 10.0
if 200.0 is not None and 150.0 is not None:
    boss_2.Placement.Base = App.Vector(200.0/2, 150.0/2, 10.0 if 10.0 else 0)
else:
    boss_2.Placement.Base = App.Vector(0, 0, 10.0 if 10.0 else 0)
doc.recompute()

bfuse_2 = doc.addObject("Part::Fuse", "BossFuse_2")
bfuse_2.Base = result
bfuse_2.Tool = boss_2
doc.recompute()
result = bfuse_2

doc.recompute()
try:
    if Gui.ActiveDocument and Gui.ActiveDocument.ActiveView:
        Gui.ActiveDocument.ActiveView.viewIsometric()
        Gui.ActiveDocument.ActiveView.fitAll()
except Exception as e:
    print(f"View scaling failed: {e}")

App.ActiveDocument.saveAs("/home/aayush/Downloads/viva-cad-ai/data/output/design_22_4ae82bc3.FCStd")
