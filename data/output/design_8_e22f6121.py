import FreeCAD as App
import FreeCADGui as Gui
import Part

doc = App.newDocument("TextCAD")
result = None

cyl_0 = doc.addObject("Part::Cylinder", "Cyl_0")
cyl_0.Radius = 10.0
cyl_0.Height = 40.0
doc.recompute()

if result is None:
    result = cyl_0
else:
    fusion_0 = doc.addObject("Part::Fuse", "Fuse_0")
    fusion_0.Base = result
    fusion_0.Tool = cyl_0
    doc.recompute()
    result = fusion_0

doc.recompute()
try:
    if Gui.ActiveDocument and Gui.ActiveDocument.ActiveView:
        Gui.ActiveDocument.ActiveView.viewIsometric()
        Gui.ActiveDocument.ActiveView.fitAll()
except Exception as e:
    print(f"View scaling failed: {e}")

App.ActiveDocument.saveAs("/home/aayush/Downloads/viva-cad-ai/data/output/design_8_e22f6121.FCStd")
