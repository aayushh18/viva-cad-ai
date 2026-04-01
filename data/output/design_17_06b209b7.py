import math
import FreeCAD as App
import Part

doc = App.newDocument("CircularPlate")

# Plate parameters
radius = 50  # mm
thickness = 10  # mm

# Hole parameters
hole_radius = 10  # mm
num_holes = 6
angle_step = 2 * math.pi / num_holes

plate = Part.makeCylinder(radius, thickness)

for i in range(num_holes):
    angle = i * angle_step
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)

    hole = Part.makeCylinder(hole_radius, thickness)
    hole.Placement.Base = App.Vector(x, y, 0)

    plate = plate.cut(hole)

obj = doc.addObject("Part::Feature", "CircularPlate")
obj.Shape = plate

doc.recompute()
doc.recompute()

obj.purgeTouched()

import FreeCADGui as Gui
Gui.ActiveDocument.ActiveView.viewIsometric()
Gui.ActiveDocument.ActiveView.fitAll()

import FreeCAD
import Part

try:
    if 'result' in locals() and result is not None:
        try:
            Part.show(result)
        except Exception:
            pass
            
    if 'doc' in locals() and doc is not None:
        doc.recompute()
        
    if FreeCAD.GuiUp:
        import FreeCADGui as Gui
        if Gui.ActiveDocument and Gui.ActiveDocument.ActiveView:
            Gui.ActiveDocument.ActiveView.viewIsometric()
            Gui.SendMsgToActiveView("ViewFit")
except Exception:
    pass


try:
    import Part
    import FreeCAD as App
    doc = App.ActiveDocument
    if doc:
        objs = [obj for obj in doc.Objects if hasattr(obj, 'Shape') and obj.Shape is not None]
        if objs:
            Part.export(objs, r'../data/output/design_17_06b209b7.step')
        doc.saveAs(r'../data/output/design_17_06b209b7.FCStd')
except Exception as e:
    print("Export Failed:", e)
