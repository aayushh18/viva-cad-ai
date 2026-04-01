import math
import FreeCAD as App
import Part

doc = App.newDocument("BoxWithFillet")

box = Part.makeBox(100, 80, 50)

fillet = box.makeFillet(2, box.Edges)

obj = doc.addObject("Part::Feature", "BoxWithFillet")
obj.Shape = fillet

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
            Part.export(objs, r'../data/output/design_56_f90fd0b5.step')
        doc.saveAs(r'../data/output/design_56_f90fd0b5.FCStd')
except Exception as e:
    print("Export Failed:", e)
