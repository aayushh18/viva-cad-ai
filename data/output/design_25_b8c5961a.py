import math
import FreeCAD as App
import Part

doc = App.newDocument("Flange")

# 1. Main Pipe (Hollow)
m_out = Part.makeCylinder(50, 80)
m_in = Part.makeCylinder(45, 80)
main_pipe = m_out.cut(m_in)
main_pipe.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)

# 2. Center Pipe (Hollow)
center = Part.makeCylinder(20, 80)
center.Placement.Base = App.Vector(0, 0, 40)
main_pipe = main_pipe.cut(center)

# 3. Add 6 Holes
for i in range(6):
    angle = math.radians(i * 60)
    x = 35 * math.cos(angle)
    y = 35 * math.sin(angle)

    hole = Part.makeCylinder(5, 10)
    hole.Placement.Base = App.Vector(x, y, 0)

    main_pipe = main_pipe.cut(hole)

obj = doc.addObject("Part::Feature", "Flange")
obj.Shape = main_pipe

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
