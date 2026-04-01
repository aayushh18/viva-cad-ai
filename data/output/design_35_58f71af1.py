import FreeCAD as App
import FreeCADGui as Gui
import Part

doc = App.newDocument("TextCAD")
result = None

box_0 = doc.addObject("Part::Box", "Box_0")
box_0.Length = 500.0
box_0.Width = 20.0
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

if 2.0*2 <= min(500.0,20.0):

    cut_cyl_1 = doc.addObject("Part::Cylinder", "CutCyl_1")
    cut_cyl_1.Radius = 2.0
    cut_cyl_1.Height = 10.0 + 10 if 10.0 else 50
    cut_cyl_1.Placement.Base = App.Vector(500.0/2, 20.0/2, -5)
    doc.recompute()

    cut_1 = doc.addObject("Part::Cut", "Cut_1")
    cut_1.Base = result
    cut_1.Tool = cut_cyl_1
    doc.recompute()
    result = cut_1

doc.recompute()
try:
    if Gui.ActiveDocument and Gui.ActiveDocument.ActiveView:
        Gui.ActiveDocument.ActiveView.viewIsometric()
        Gui.ActiveDocument.ActiveView.fitAll()
except Exception as e:
    print(f"View scaling failed: {e}")

App.ActiveDocument.saveAs("/home/aayush/Downloads/viva-cad-ai/data/output/design_35_58f71af1.FCStd")
