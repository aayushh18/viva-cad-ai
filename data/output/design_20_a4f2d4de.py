import math
import FreeCAD as App
import Part

doc = App.newDocument("CircularPlate")

# Plate parameters
radius = 50
thickness = 10

# Create plate
plate = Part.makeCylinder(radius, thickness)

# Hole parameters
hole_radius = 5
hole_distance = 2 * math.pi * radius / 6
hole_height = thickness + 2

# Create holes
holes = []
for i in range(6):
    angle = math.radians(i * 60)
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    hole = Part.makeCylinder(hole_radius, hole_height)
    hole.Placement.Base = App.Vector(x, y, -1)
    holes.append(hole)

# Cut holes from plate
for hole in holes:
    plate = plate.cut(hole)

obj = doc.addObject("Part::Feature", "CircularPlate")
obj.Shape = plate

doc.recompute()
doc.recompute()

# View Adjustment
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
            Part.export(objs, r'../data/output/design_20_a4f2d4de.step')
        doc.saveAs(r'../data/output/design_20_a4f2d4de.FCStd')
except Exception as e:
    print("Export Failed:", e)
