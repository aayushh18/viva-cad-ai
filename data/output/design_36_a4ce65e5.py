import math
import FreeCAD as App
import Part

doc = App.newDocument("CircPlate")

plate_radius = 50
thickness = 10
plate = Part.makeCylinder(plate_radius, thickness)

num_holes = 6
pitch_radius = 30
hole_radius = 5

for i in range(num_holes):
    angle = math.radians(i * (360 / num_holes))
    x = pitch_radius * math.cos(angle)
    y = pitch_radius * math.sin(angle)
    
    hole = Part.makeCylinder(hole_radius, thickness + 2)
    hole.Placement.Base = App.Vector(x, y, -1)
    plate = plate.cut(hole)

obj = doc.addObject("Part::Feature", "CircPlate")
obj.Shape = plate

obj.recompute() # Object level
App.ActiveDocument.recompute() # Document level
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
            Part.export(objs, r'../data/output/design_36_a4ce65e5.step')
        doc.saveAs(r'../data/output/design_36_a4ce65e5.FCStd')
except Exception as e:
    print("Export Failed:", e)
