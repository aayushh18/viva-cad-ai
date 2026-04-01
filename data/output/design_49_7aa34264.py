import math
import FreeCAD as App
import Part

doc = App.newDocument("TJoint")

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
doc.recompute()

try:
    import Part
    import FreeCAD as App
    doc = App.ActiveDocument
    if doc:
        objs = [obj for obj in doc.Objects if hasattr(obj, 'Shape') and obj.Shape is not None]
        if objs:
            Part.export(objs, r'../data/output/design_49_7aa34264.step')
        doc.saveAs(r'../data/output/design_49_7aa34264.FCStd')
except Exception as e:
    print("Export Failed:", e)
