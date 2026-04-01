import math
import FreeCAD as App
import Part

doc = App.newDocument("Flange")

# Main Pipe (Hollow)
m_out = Part.makeCylinder(50, 10)

# Center
center = Part.makeCylinder(20, 10)
m_out = m_out.cut(center)

# Holes
for i in range(4):
    angle = math.radians(i * 90)
    x = 35 * math.cos(angle)
    y = 35 * math.sin(angle)

    hole = Part.makeCylinder(5, 10)
    hole.Placement.Base = App.Vector(x, y, 0)

    m_out = m_out.cut(hole)

obj = doc.addObject("Part::Feature", "Flange")
obj.Shape = m_out

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
