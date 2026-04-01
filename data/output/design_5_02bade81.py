import FreeCAD as App
import Part

doc = App.newDocument("Valve")

# 1. Main Hollow Body (Sphere)
body_out = Part.makeSphere(22)
body_in = Part.makeSphere(19)
valve_body = body_out.cut(body_in)

# 2. Side Connectors (Hollow pipes with Flanges)
for x_pos in [-25, 25]:
    # Pipe
    p_out = Part.makeCylinder(12, 15)
    p_in = Part.makeCylinder(10, 20)
    pipe = p_out.cut(p_in)
    pipe.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)
    pipe.translate(App.Vector(x_pos if x_pos < 0 else 10, 0, 0))
    
    # Flange (The round plate at the end)
    flange = Part.makeCylinder(20, 4)
    flange.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)
    flange.translate(App.Vector(x_pos if x_pos < 0 else 21, 0, 0))
    
    valve_body = valve_body.fuse(pipe).fuse(flange)

# 3. Stem and Handwheel
stem = Part.makeCylinder(4, 30)
stem.translate(App.Vector(0,0,15))
wheel = Part.makeTorus(18, 3)
wheel.translate(App.Vector(0,0,45))

final_valve = valve_body.fuse(stem).fuse(wheel)
obj = doc.addObject("Part::Feature", "Valve")
obj.Shape = final_valve

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
