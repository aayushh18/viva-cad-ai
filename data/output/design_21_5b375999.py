import math
import FreeCAD as App
import Part

doc = App.newDocument("Flange")

# Main Pipe (Hollow)
m_out = Part.makeCylinder(50, 80)
m_in = Part.makeCylinder(20, 80)
main_pipe = m_out.cut(m_in)

# Side Pipe (Hollow)
s_out = Part.makeCylinder(50, 40)
s_in = Part.makeCylinder(20, 45) # Thoda lamba taaki andar tak saaf kate
side_pipe = s_out.cut(s_in)
side_pipe.translate(App.Vector(40, 0, 0))

flange = main_pipe.fuse(side_pipe)

# Holes
for i in range(6):
    angle = math.radians(i * 60)
    x = 35 * math.cos(angle)
    y = 35 * math.sin(angle)

    hole = Part.makeCylinder(5, 10)
    hole.Placement.Base = App.Vector(x, y, 0)

    flange = flange.cut(hole)

obj = doc.addObject("Part::Feature", "Flange")
obj.Shape = flange

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
