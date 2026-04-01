import FreeCAD as App
import Part

doc = App.newDocument("TankWithProperOutlet")

# Tank Parameters
t_rad, t_ht, thick = 100, 250, 10

# Tank (Hollow)
tank = Part.makeCylinder(t_rad, t_ht).cut(Part.makeCylinder(t_rad - thick, t_ht + 5))

# Outlet Pipe Parameters
p_rad, p_len = 20, 120

# Outlet Pipe (Hollow)
p_out = Part.makeCylinder(p_rad, p_len)
p_in = Part.makeCylinder(p_rad - 3, p_len + 10) # 3mm wall thickness
h_pipe = p_out.cut(p_in)

h_pipe.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)
h_pipe.translate(App.Vector(t_rad - 5, 0, 80)) # Slightly inside tank for better fuse

# Hole in Tank Wall
hole = Part.makeCylinder(p_rad - 3, thick + 10)
hole.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)
hole.translate(App.Vector(t_rad - 5, 0, 80))

# Cut hole first, then fuse pipe
final_model = tank.cut(hole).fuse(h_pipe)

# Valve Parameters
v_rad, v_len = 15, 30

# Valve Body (Hollow)
v_body = Part.makeCylinder(v_rad, v_len).cut(Part.makeCylinder(v_rad - 3, v_len + 5))

# Valve Stem
v_stem = Part.makeCylinder(3, 20)
v_stem.translate(App.Vector(t_rad - 5, 0, 80 + v_len))

# Valve Wheel
v_wheel = Part.makeTorus(12, 2)
v_wheel.translate(App.Vector(t_rad - 5, 0, 80 + v_len + 20))

# Fuse Valve Parts
valve = v_body.fuse(v_stem).fuse(v_wheel)

# Fuse Tank and Valve
final_assembly = final_model.fuse(valve)

obj = doc.addObject("Part::Feature", "TankWithValve")
obj.Shape = final_assembly

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
