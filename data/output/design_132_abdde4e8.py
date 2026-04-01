import FreeCAD as App
import Part

doc = App.newDocument("Pro_HX_Fixed")

# 1. Main Shell (Hollow)
shell = Part.makeCylinder(50, 180).cut(Part.makeCylinder(46, 180))
shell.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)

# 2. End Caps (Dished Ends)
def make_cap(pos_x, rot_angle):
    cap = Part.makeSphere(50)
    # Cut half sphere to make a cap
    cap = cap.cut(Part.makeBox(100,100,100, App.Vector(-50,-50,-100)))
    cap.rotate(App.Vector(0,0,0), App.Vector(0,1,0), rot_angle)
    cap.translate(App.Vector(pos_x, 0, 0))
    return cap

cap_left = make_cap(0, -90)
cap_right = make_cap(180, 90)

# 3. In/Out Nozzles
n1 = Part.makeCylinder(12, 25)
n1.translate(App.Vector(40, 0, 45))
n2 = n1.copy()
n2.translate(App.Vector(100, 0, -115)) # Opposite side

hx = shell.fuse(cap_left).fuse(cap_right).fuse(n1).fuse(n2)
Part.show(hx)
doc.recompute()