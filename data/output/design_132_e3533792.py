import FreeCAD as App
import Part

doc = App.newDocument("Pro_Vertical_Tank")

# -----------------------
# TANK PARAMETERS
# -----------------------
radius = 100
height = 300
thickness = 8

# 1. Main Walls (Hollow Cylinder)
outer_cyl = Part.makeCylinder(radius, height)
inner_cyl = Part.makeCylinder(radius - thickness, height + 2) # Slightly taller
walls = outer_cyl.cut(inner_cyl)

# 2. Bottom Plate (Closing the Tank)
# Isse tank neeche se seal ho jayega
bottom = Part.makeCylinder(radius, thickness)

# 3. Top Flange (Rim for the Lid)
# Ye wo hissa hai jispar dhakkan (Lid) rakha jata hai
f_outer = Part.makeCylinder(radius + 15, 10)
f_inner = Part.makeCylinder(radius - thickness, 10)
top_flange = f_outer.cut(f_inner)
top_flange.translate(App.Vector(0, 0, height)) # Move to top

# -----------------------
# FINAL FUSION
# -----------------------
# Walls + Bottom + Top Rim = Complete Tank
vertical_tank = walls.fuse(bottom).fuse(top_flange)

Part.show(vertical_tank)
doc.recompute()