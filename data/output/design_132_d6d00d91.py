import Part

doc = App.newDocument("Pro_Lid")

# 1. Main Cover Plate
plate = Part.makeCylinder(55, 5)

# 2. Rim (The part that goes inside the tank)
rim_out = Part.makeCylinder(50, 10)
rim_in = Part.makeCylinder(47, 10)
rim = rim_out.cut(rim_in)
rim.translate(App.Vector(0,0,-5)) # Moves it below the plate

# 3. Handle (U-shape approximate)
h1 = Part.makeCylinder(4, 20)
h1.translate(App.Vector(-15, 0, 5))
h2 = Part.makeCylinder(4, 20)
h2.translate(App.Vector(15, 0, 5))
cross = Part.makeBox(34, 6, 4)
cross.translate(App.Vector(-17, -3, 25))

final_lid = plate.fuse(rim).fuse(h1).fuse(h2).fuse(cross)
Part.show(final_lid)
doc.recompute()