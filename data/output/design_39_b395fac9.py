import math
import FreeCAD as App
import Part

doc = App.newDocument("Cone")

cone = Part.makeCone(10, 50)

obj = doc.addObject("Part::Feature", "Cone")
obj.Shape = cone

doc.recompute()
doc.recompute()

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
            Part.export(objs, r'../data/output/design_39_b395fac9.step')
        doc.saveAs(r'../data/output/design_39_b395fac9.FCStd')
except Exception as e:
    print("Export Failed:", e)
