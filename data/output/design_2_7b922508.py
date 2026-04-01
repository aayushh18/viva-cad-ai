import math
import FreeCAD as App
import Part

doc = App.newDocument("Plate")

# Plate dimensions
plate_width = 100
plate_length = 100
plate_thickness = 10

# Hole dimensions
hole_diameter = 20
hole_depth = 10

# Create plate
plate = Part.makeBox(plate_width, plate_length, plate_thickness)

# Create and place 4 holes at corners
positions = [
    App.Vector(10, 10, -plate_thickness),
    App.Vector(plate_width - 10, 10, -plate_thickness),
    App.Vector(10, plate_length - 10, -plate_thickness),
    App.Vector(plate_width - 10, plate_length - 10, -plate_thickness)
]

for pos in positions:
    hole = Part.makeCylinder(hole_diameter / 2, hole_depth)
    hole.translate(pos)
    plate = plate.cut(hole)

obj = doc.addObject("Part::Feature", "Plate")
obj.Shape = plate

doc.recompute()
doc.recompute()

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
