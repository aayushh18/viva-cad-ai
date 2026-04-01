import FreeCAD as App
import Part

doc = App.newDocument("Pro_Heat_Exchanger")

# 1. Main Shell (Hollow Cylinder)
shell_out = Part.makeCylinder(60, 200)
shell_in = Part.makeCylinder(55, 200)
shell = shell_out.cut(shell_in)
shell.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90) # Horizontal

# 2. End Caps (Dished Ends)
cap1 = Part.makeSphere(60)
cap1 = cap1.cut(Part.makeBox(120,120,120, App.Vector(-60,-60,0)))
cap1.rotate(App.Vector(0,0,0), App.Vector(0,1,0), -90)

cap2 = cap1.copy()
cap2.rotate(App.Vector(0,0,0), App.Vector(0,0,1), 180)
cap2.translate(App.Vector(200,0,0))

# 3. Nozzles (Top and Bottom)
nozzle = Part.makeCylinder(15, 30)
nozzle.translate(App.Vector(40, 0, 50)) # Inlet
nozzle2 = nozzle.copy()
nozzle2.translate(App.Vector(120, 0, -100)) # Outlet

hx = shell.fuse(cap1).fuse(cap2).fuse(nozzle).fuse(nozzle2)
Part.show(hx)
doc.recompute()