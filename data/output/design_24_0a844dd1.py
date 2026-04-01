import math
import FreeCAD as App
import Part

doc = App.newDocument("MountingPlate")

plate = Part.makeBox(100, 100, 10)

for i in range(4):
    angle = math.radians(i * 90)
    x = 15 * math.cos(angle) + 25
    y = 15 * math.sin(angle) + 25

    hole = Part.makeCylinder(3, 10)
    hole.Placement.Base = App.Vector(x, y, 0)

    plate = plate.cut(hole)

obj = doc.addObject("Part::Feature", "Plate")
obj.Shape = plate

hole_cylinder_height = 10 + 2  # Plate thickness + 2mm
hole_placement = App.Vector(0, 0, -1)  # Ensures the tool object protrudes through both top and bottom faces

for i in range(4):
    angle = math.radians(i * 90)
    x = 15 * math.cos(angle) + 25
    y = 15 * math.sin(angle) + 25

    hole = Part.makeCylinder(3, hole_cylinder_height)
    hole.Placement.Base = App.Vector(x, y, hole_placement.X)

    obj = doc.addObject("Part::Feature", f"Hole_{i}")
    obj.Shape = hole

doc.recompute()
obj.purgeTouched()
obj.recompute()

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
            Part.export(objs, r'../data/output/design_24_0a844dd1.step')
        doc.saveAs(r'../data/output/design_24_0a844dd1.FCStd')
except Exception as e:
    print("Export Failed:", e)
