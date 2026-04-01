import FreeCAD as App
import Part

doc = App.newDocument("TankWithProperOutlet")

# -----------------------
# TANK PARAMETERS
# -----------------------
tank_radius = 100
tank_height = 250
thickness = 10

# Outer tank
tank_outer = Part.makeCylinder(tank_radius, tank_height)

# Inner hollow
tank_inner = Part.makeCylinder(tank_radius - thickness, tank_height)

# Hollow tank
tank = tank_outer.cut(tank_inner)

# -----------------------
# OUTLET PIPE PARAMETERS
# -----------------------
pipe_radius = 20
pipe_length = 120

# Pipe (horizontal)
pipe = Part.makeCylinder(pipe_radius, pipe_length)

# Rotate pipe to horizontal
pipe.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)

# Position pipe (side of tank)
pipe.translate(App.Vector(tank_radius, 0, 80))

# -----------------------
# HOLE IN TANK (IMPORTANT)
# -----------------------
hole = Part.makeCylinder(pipe_radius, thickness + 5)

# Rotate hole same as pipe
hole.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)

# Position hole same place
hole.translate(App.Vector(tank_radius, 0, 80))

# Cut hole from tank
tank_with_hole = tank.cut(hole)

# -----------------------
# FINAL FUSION
# -----------------------
final_model = tank_with_hole.fuse(pipe)

# Show result
Part.show(final_model)
doc.recompute()