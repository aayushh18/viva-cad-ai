import FreeCAD as App
import Part

doc = App.newDocument("Gate_Valve")

# 1. Body (Hollow Sphere)
body_out = Part.makeSphere(30)
body_in = Part.makeSphere(25)
body = body_out.cut(body_in)

# 2. End Flanges (Hollow Discs)
def make_flange(radius):
    flange_out = Part.makeCylinder(radius, 10)
    flange_in = Part.makeCylinder(radius - 5, 10)
    return flange_out.cut(flange_in)

flange_left = make_flange(45)
flange_right = flange_left.copy()
flange_right.translate(App.Vector(60, 0, 0))

# 3. Handwheel (Torus)
wheel_out = Part.makeTorus(30, 5)
wheel_in = Part.makeTorus(25, 5)
wheel = wheel_out.cut(wheel_in)
wheel.translate(App.Vector(0, 0, 50))

# 4. Final Assembly
gate_valve = body.fuse(flange_left).fuse(flange_right).fuse(wheel)

# Add to document
obj = doc.addObject("Part::Feature", "Gate_Valve")
obj.Shape = gate_valve

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
