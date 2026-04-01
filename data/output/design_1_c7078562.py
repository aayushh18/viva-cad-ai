import math
import FreeCAD as App
import Part

doc = App.newDocument("MountingPlate")

length, width, thickness = 120, 80, 10
offset = 10
hole_radius = 5

plate = Part.makeBox(length, width, thickness)

centers = [
    (offset, offset),
    (length - offset, offset),
    (offset, width - offset),
    (length - offset, width - offset)
]

for x, y in centers:
    hole = Part.makeCylinder(hole_radius, thickness + 2)
    hole.Placement.Base = App.Vector(x, y, -1)
    plate = plate.cut(hole)

obj = doc.addObject("Part::Feature", "MountingPlate")
obj.Shape = plate

doc.recompute()
doc.recompute()

obj.purgeTouched()

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
            Part.export(objs, r'../data/output/design_1_c7078562.step')
        doc.saveAs(r'../data/output/design_1_c7078562.FCStd')
except Exception as e:
    print("Export Failed:", e)
