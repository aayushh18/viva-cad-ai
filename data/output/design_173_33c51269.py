import FreeCAD as App
import Part

doc = App.newDocument("PressureGauge")

# 1. Gauge Case
case = Part.makeCylinder(25, 12).cut(Part.makeCylinder(23, 12))
case.translate(App.Vector(0,0,2))

# 2. Dial Face
face = Part.makeCylinder(23, 2)
face.translate(App.Vector(0,0,2))

# 3. Needle (Thicker for visibility)
needle = Part.makeBox(15, 1.5, 1)
needle.translate(App.Vector(0, -0.75, 4))

# 4. Connection Socket (Bottom)
socket = Part.makeCylinder(5, 15)
socket.rotate(App.Vector(0,0,0), App.Vector(1,0,0), 90)
socket.translate(App.Vector(0, -23, 8))

gauge = case.fuse(face).fuse(needle).fuse(socket)

obj = doc.addObject("Part::Feature", "PressureGauge")
obj.Shape = gauge

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
