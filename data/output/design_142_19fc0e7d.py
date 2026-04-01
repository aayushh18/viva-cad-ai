import FreeCAD as App
import Part

doc = App.newDocument("SupportStand")

# Top Plate
plate = Part.makeBox(200, 200, 15)

# Leg dimensions
r_leg = 10
h_leg = 120

# Create and place 4 legs at corners
positions = [
    App.Vector(10, 10, -h_leg),
    App.Vector(190, 10, -h_leg),
    App.Vector(10, 190, -h_leg),
    App.Vector(190, 190, -h_leg)
]

stand = plate
for pos in positions:
    leg = Part.makeCylinder(r_leg, h_leg)
    leg.translate(pos)
    stand = stand.fuse(leg)

obj = doc.addObject("Part::Feature", "SupportStand")
obj.Shape = stand

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
            Gui.ActiveDocument.ActiveView.fitAll()
except Exception:
    pass
