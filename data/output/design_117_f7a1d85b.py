import FreeCAD as App
import Part
import math
import Import

doc = App.newDocument("UserInput")

# Get user input
radius = float(input("Enter the radius of the base: "))
height = float(input("Enter the height of the base: "))
num_holes = int(input("Enter the number of holes: "))
hole_radius = float(input("Enter the radius of the holes: "))
hole_distance = float(input("Enter the distance between holes: "))

# Create the base
base = Part.makeCylinder(radius, height)

# Create the holes
for i in range(num_holes):
    angle = math.radians(i * 360 / num_holes)
    x = radius + hole_distance * math.cos(angle)
    y = radius + hole_distance * math.sin(angle)
    hole = Part.makeCylinder(hole_radius, height)
    hole.Placement.Base = App.Vector(x, y, 0)
    base = base.cut(hole)

obj = doc.addObject("Part::Feature", "UserInput")
obj.Shape = base
doc.recompute()
Import.export(doc.Objects, "../data/output/design_117_f7a1d85b.step")

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
            Gui.ActiveDocument.ActiveView.fitAll()
except Exception:
    pass
