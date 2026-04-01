import FreeCAD as App
import Part

doc = App.newDocument("TankWithOutlet")

# Tank
tank_outer = Part.makeCylinder(100, 250)
tank_inner = Part.makeCylinder(90, 250)
tank = tank_outer.cut(tank_inner)

# Pipe
pipe = Part.makeCylinder(20, 100)

# Move pipe to bottom side
pipe.translate(App.Vector(100, 0, 50))

# Fuse
result = tank.fuse(pipe)

Part.show(result)
doc.recompute()