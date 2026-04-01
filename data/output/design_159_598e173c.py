import FreeCAD as App
import Part

doc = App.newDocument("MountingPlate")

# Base Plate
plate = Part.makeBox(100, 100, 5)

# Corner Hole Dimensions
hole_radius = 5
hole_depth = 10

# Create and place 4 holes at corners
positions = [
    App.Vector(10, 10, -hole_depth),
    App.Vector(90, 10, -hole_depth),
    App.Vector(10, 90, -hole_depth),
    App.Vector(90, 90, -hole_depth)
]

for pos in positions:
    hole = Part.makeCylinder(hole_radius, hole_depth)
    hole.translate(pos)
    plate = plate.cut(hole)

obj = doc.addObject("Part::Feature", "MountingPlate")
obj.Shape = plate

doc.recompute()

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
