import FreeCAD as App
import Part

doc = App.newDocument("Pro_Assembly")

# 1. Base Plate
plate = Part.makeBox(120, 120, 10)

# 2. Add 4 Legs
for x, y in [(10,10), (100,10), (10,100), (100,100)]:
    leg = Part.makeCylinder(6, 80)
    leg.translate(App.Vector(x, y, -80))
    plate = plate.fuse(leg)

# 3. Add a Big Tank on top
tank_out = Part.makeCylinder(50, 100)
tank_in = Part.makeCylinder(47, 105) # Hollow tank
tank = tank_out.cut(tank_in)
tank.translate(App.Vector(60, 60, 10)) # Center it on plate

final_assembly = plate.fuse(tank)
Part.show(final_assembly)
doc.recompute()