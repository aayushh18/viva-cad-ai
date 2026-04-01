import math
import FreeCAD as App
import Part

doc = App.newDocument("MountingPlate")

# Plate dimensions
plate_length = 100
plate_width = 80
plate_thickness = 10

# Hole dimensions
hole_radius = 3
hole_depth = plate_thickness + 2

# Create plate
plate = Part.makeBox(plate_length, plate_width, plate_thickness)

# Create holes
for i in range(4):
    angle = math.radians(i * 90)
    x = 15 * math.cos(angle) + (plate_length - 30)
    y = 15 * math.sin(angle) + (plate_width - 30)

    hole = Part.makeCylinder(hole_radius, hole_depth)
    hole.Placement.Base = App.Vector(x, y, 0)

    plate = plate.cut(hole)

obj = doc.addObject("Part::Feature", "Plate")
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
            Part.export(objs, r'../data/output/design_25_1f9ed1da.step')
        doc.saveAs(r'../data/output/design_25_1f9ed1da.FCStd')
except Exception as e:
    print("Export Failed:", e)
