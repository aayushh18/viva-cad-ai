import FreeCAD as App
import Part

doc = App.newDocument("TJoint")

# Main pipe
main_pipe = Part.makeCylinder(10, 60)

# Side pipe
side_pipe = Part.makeCylinder(10, 40)
side_pipe.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)
side_pipe.translate(App.Vector(30,0,20))

t_joint = main_pipe.fuse(side_pipe)

Part.show(t_joint)
doc.recompute()