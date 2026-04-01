import math
import FreeCAD as App
import Part

doc = App.newDocument("RectBlock")

length, width, height = 100, 80, 50

plate = Part.makeBox(length, width, height)

obj = doc.addObject("Part::Feature", "RectBlock")
obj.Shape = plate

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
            Part.export(objs, r'../data/output/design_47_6e14bb4c.step')
        doc.saveAs(r'../data/output/design_47_6e14bb4c.FCStd')
except Exception as e:
    print("Export Failed:", e)
