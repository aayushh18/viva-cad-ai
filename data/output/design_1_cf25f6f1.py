import math
import FreeCAD as App
import Part

doc = App.newDocument("MountingPlate")

# Base Plate
plate = Part.makeBox(100, 100, 10)

# Corner Hole dimensions
r_hole = 6
h_hole = 20

# Create and place 4 holes at corners
positions = [
    App.Vector(10, 10, -h_hole),
    App.Vector(90, 10, -h_hole),
    App.Vector(10, 90, -h_hole),
    App.Vector(90, 90, -h_hole)
]

for pos in positions:
    hole = Part.makeCylinder(r_hole, h_hole)
    hole.translate(pos)
    plate = plate.cut(hole)

obj = doc.addObject("Part::Feature", "MountingPlate")
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
