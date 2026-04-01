import FreeCAD as App
import FreeCADGui as Gui
import Part

doc = App.newDocument("TextCAD")
result = None

plate_0 = doc.addObject("Part::Box", "Plate_0")
plate_0.Length = 165.0
plate_0.Width = 165.0
plate_0.Height = 18.0
doc.recompute()

if result is None:
    result = plate_0
else:
    fusion_0 = doc.addObject("Part::Fuse", "Fuse_0")
    fusion_0.Base = result
    fusion_0.Tool = plate_0
    doc.recompute()
    result = fusion_0

boss_1 = doc.addObject("Part::Cylinder", "Boss_1")
boss_1.Radius = 51.0
boss_1.Height = 45.0
if 165.0 is not None and 165.0 is not None:
    boss_1.Placement.Base = App.Vector(165.0/2, 165.0/2, 18.0 if 18.0 else 0)
else:
    boss_1.Placement.Base = App.Vector(0, 0, 18.0 if 18.0 else 0)
doc.recompute()

bfuse_1 = doc.addObject("Part::Fuse", "BossFuse_1")
bfuse_1.Base = result
bfuse_1.Tool = boss_1
doc.recompute()
result = bfuse_1

if 9.0*2 <= min(165.0,165.0):

    cut_cyl_2 = doc.addObject("Part::Cylinder", "CutCyl_2")
    cut_cyl_2.Radius = 9.0
    cut_cyl_2.Height = 18.0 + 10 if 18.0 else 50
    cut_cyl_2.Placement.Base = App.Vector(165.0/2 + 62.5, 165.0/2 + 0.0, -5)
    doc.recompute()

    cut_2 = doc.addObject("Part::Cut", "Cut_2")
    cut_2.Base = result
    cut_2.Tool = cut_cyl_2
    doc.recompute()
    result = cut_2

if 9.0*2 <= min(165.0,165.0):

    cut_cyl_3 = doc.addObject("Part::Cylinder", "CutCyl_3")
    cut_cyl_3.Radius = 9.0
    cut_cyl_3.Height = 18.0 + 10 if 18.0 else 50
    cut_cyl_3.Placement.Base = App.Vector(165.0/2 + 0.0, 165.0/2 + 62.5, -5)
    doc.recompute()

    cut_3 = doc.addObject("Part::Cut", "Cut_3")
    cut_3.Base = result
    cut_3.Tool = cut_cyl_3
    doc.recompute()
    result = cut_3

if 9.0*2 <= min(165.0,165.0):

    cut_cyl_4 = doc.addObject("Part::Cylinder", "CutCyl_4")
    cut_cyl_4.Radius = 9.0
    cut_cyl_4.Height = 18.0 + 10 if 18.0 else 50
    cut_cyl_4.Placement.Base = App.Vector(165.0/2 + -62.5, 165.0/2 + 0.0, -5)
    doc.recompute()

    cut_4 = doc.addObject("Part::Cut", "Cut_4")
    cut_4.Base = result
    cut_4.Tool = cut_cyl_4
    doc.recompute()
    result = cut_4

if 9.0*2 <= min(165.0,165.0):

    cut_cyl_5 = doc.addObject("Part::Cylinder", "CutCyl_5")
    cut_cyl_5.Radius = 9.0
    cut_cyl_5.Height = 18.0 + 10 if 18.0 else 50
    cut_cyl_5.Placement.Base = App.Vector(165.0/2 + 0.0, 165.0/2 + -62.5, -5)
    doc.recompute()

    cut_5 = doc.addObject("Part::Cut", "Cut_5")
    cut_5.Base = result
    cut_5.Tool = cut_cyl_5
    doc.recompute()
    result = cut_5

doc.recompute()
try:
    if Gui.ActiveDocument and Gui.ActiveDocument.ActiveView:
        Gui.ActiveDocument.ActiveView.viewIsometric()
        Gui.ActiveDocument.ActiveView.fitAll()
except Exception as e:
    print(f"View scaling failed: {e}")

App.ActiveDocument.saveAs("/home/aayush/Downloads/viva-cad-ai/data/output/design_34_38d4f54e.FCStd")
