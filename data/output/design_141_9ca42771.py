import FreeCAD as App
import Part

doc = App.newDocument("Gate_Valve")

# Gate Valve Body
body_out = Part.makeSphere(30)
body_in = Part.makeSphere(25)
body = body_out.cut(body_in)

# End Flanges
f1_out = Part.makeCylinder(45, 10)
f1_in = Part.makeCylinder(40, 10)
f1 = f1_out.cut(f1_in)
f1.translate(App.Vector(-30, 0, 0))

f2_out = f1_out.copy()
f2_in = f1_in.copy()
f2 = f2_out.cut(f2_in)
f2.translate(App.Vector(30, 0, 0))

# Hand Wheel
wheel_out = Part.makeCylinder(30, 30)
wheel_in = Part.makeCylinder(25, 30)
wheel = wheel_out.cut(wheel_in)
wheel.translate(App.Vector(0, 0, 50))

# Final Assembly
valve = body.fuse(f1).fuse(f2).fuse(wheel)

# Add to Document
obj = doc.addObject("Part::Feature", "Gate_Valve")
obj.Shape = valve

# Recompute
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
