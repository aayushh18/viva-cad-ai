import FreeCAD as App
import Part

doc = App.newDocument("MountingPlate")

# Base Plate
plate = Part.makeBox(100, 100, 5)

# Corner Holes
hole_radius = 5
hole_depth = 10

for i in range(4):
    angle = i * 90
    x = 50 * math.cos(math.radians(angle)) + 50
    y = 50 * math.sin(math.radians(angle)) + 50
    
    hole = Part.makeCylinder(hole_radius, hole_depth)
    hole.translate(App.Vector(x, y, 0))
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
