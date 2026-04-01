import FreeCAD as App
import FreeCADGui as Gui
import Part

doc = App.newDocument("TextCAD")
result = None

plate_0 = doc.addObject("Part::Box", "Plate_0")
plate_0.Length = 120.0
plate_0.Width = 90.0
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

doc.recompute()
try:
    if Gui.ActiveDocument and Gui.ActiveDocument.ActiveView:
        Gui.ActiveDocument.ActiveView.viewIsometric()
        Gui.ActiveDocument.ActiveView.fitAll()
except Exception as e:
    print(f"View scaling failed: {e}")

App.ActiveDocument.saveAs("/home/aayush/Downloads/viva-cad-ai/data/output/design_27_5fd11802.FCStd")
