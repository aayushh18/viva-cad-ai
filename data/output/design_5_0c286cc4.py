import math
import FreeCAD as App
import Part

doc = App.newDocument("RectBlock")

length, width, thickness = 100, 80, 10
extrusion_depth = 500

block = Part.makeBox(length, width, extrusion_depth)

obj = doc.addObject("Part::Feature", "RectBlock")
obj.Shape = block

doc.recompute()
doc.recompute()

obj.purgeTouched() # CRITICAL: Clears the 'Failed' flag and makes status 'Successful'

# View Adjustment
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui as Gui
    if Gui.ActiveDocument and Gui.ActiveDocument.ActiveView:
        Gui.ActiveDocument.ActiveView.viewIsometric()
        Gui.ActiveDocument.ActiveView.fitAll()

try:
    import Part
    import FreeCAD as App
    doc = App.ActiveDocument
    if doc:
        objs = [obj for obj in doc.Objects if hasattr(obj, 'Shape') and obj.Shape is not None]
        if objs:
            Part.export(objs, r'../data/output/design_5_0c286cc4.step')
        doc.saveAs(r'../data/output/design_5_0c286cc4.FCStd')
except Exception as e:
    print("Export Failed:", e)
