import FreeCAD as App
import Part

doc = App.newDocument("TankWithProperOutlet")

# --- TANK (Hollow) ---
t_rad, t_ht, thick = 100, 250, 10
tank = Part.makeCylinder(t_rad, t_ht).cut(Part.makeCylinder(t_rad - thick, t_ht + 5))

# --- OUTLET PIPE (Hollow) ---
p_rad, p_len = 20, 120
p_out = Part.makeCylinder(p_rad, p_len)
p_in = Part.makeCylinder(p_rad - 3, p_len + 10) # 3mm wall thickness
h_pipe = p_out.cut(p_in)

h_pipe.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)
h_pipe.translate(App.Vector(t_rad - 5, 0, 80)) # Slightly inside tank for better fuse

# --- HOLE IN TANK WALL ---
hole = Part.makeCylinder(p_rad - 3, thick + 10)
hole.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)
hole.translate(App.Vector(t_rad - 5, 0, 80))

# Cut hole first, then fuse pipe
final_model = tank.cut(hole).fuse(h_pipe)

Part.show(final_model)
doc.recompute()