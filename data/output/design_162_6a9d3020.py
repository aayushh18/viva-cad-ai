import FreeCAD as App
import Part
import math

doc = App.newDocument("Pattern")

plate = Part.makeBox(50, 50, 10)

for i in range(4):
    angle = math.radians(i * 90)
    x = 15 * math.cos(angle) + 25
    y = 15 * math.sin(angle) + 25

    hole = Part.makeCylinder(3, 10)
    hole.Placement.Base = App.Vector(x, y, 0)
    plate = plate.cut(hole)

obj = doc.addObject("Part::Feature", "Plate")
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
