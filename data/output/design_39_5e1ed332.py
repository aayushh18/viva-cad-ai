import FreeCAD as App
import FreeCADGui as Gui
import Part

doc = App.newDocument("TextCAD")
result = None

box_0 = doc.addObject("Part::Box", "Box_0")
box_0.Length = 200.0
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

if 2.0*2 <= min(200.0,20.0):

    offset = 200.0 / (3 + 1)
    positions = [(offset * (j + 1), 20.0/2) for j in range(3)]
    
    for j, pos in enumerate(positions):
        cut_cyl_1_j = doc.addObject("Part::Cylinder", f"CutCyl1_{j}")
        cut_cyl_1_j.Radius = 2.0
        cut_cyl_1_j.Height = 10.0 + 10 if 10.0 else 50
        cut_cyl_1_j.Placement.Base = App.Vector(pos[0], pos[1], -5)
        doc.recompute()

        cut_1_j = doc.addObject("Part::Cut", f"Cut1_{j}")
        cut_1_j.Base = result
        cut_1_j.Tool = cut_cyl_1_j
        doc.recompute()
        result = cut_1_j

doc.recompute()
try:
    if Gui.ActiveDocument and Gui.ActiveDocument.ActiveView:
        Gui.ActiveDocument.ActiveView.viewIsometric()
        Gui.ActiveDocument.ActiveView.fitAll()
except Exception as e:
    print(f"View scaling failed: {e}")

App.ActiveDocument.saveAs("/home/aayush/Downloads/viva-cad-ai/data/output/design_39_5e1ed332.FCStd")
