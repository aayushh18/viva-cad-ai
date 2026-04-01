import FreeCAD as App
import Part

doc = App.newDocument("Pro_TJoint")

# Main Pipe (Hollow)
m_out = Part.makeCylinder(15, 80)
m_in = Part.makeCylinder(12, 80)
main_pipe = m_out.cut(m_in)
main_pipe.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)

# Side Pipe (Hollow)
s_out = Part.makeCylinder(15, 40)
s_in = Part.makeCylinder(12, 45) # Thoda lamba taaki andar tak saaf kate
side_pipe = s_out.cut(s_in)
side_pipe.translate(App.Vector(40, 0, 0))

t_joint = main_pipe.fuse(side_pipe)
Part.show(t_joint)
doc.recompute()