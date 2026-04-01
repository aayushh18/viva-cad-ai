import math
import FreeCAD as App
import Part

doc = App.newDocument("MountingPlate")

plate = Part.makeBox(120, 120, 10)

for x, y in [(10,10), (100,10), (10,100), (100,100)]:
    leg = Part.makeCylinder(6, 80)
    leg.translate(App.Vector(x, y, -80))
    plate = plate.fuse(leg)

obj = doc.addObject("Part::Feature", "MountingPlate")
obj.Shape = plate

doc.recompute()
doc.recompute()

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
