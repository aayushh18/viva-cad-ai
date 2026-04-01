import math
import FreeCAD as App
import Part

doc = App.newDocument("WaterTank")

# Tank Parameters
radius = 80
height = 300
thickness = 8

# Create hollow shell
outer_cyl = Part.makeCylinder(radius, height)
inner_cyl = Part.makeCylinder(radius - thickness, height + 2) 
walls = outer_cyl.cut(inner_cyl)

# Bottom Plate (Closing the Tank)
bottom = Part.makeCylinder(radius, thickness)

# Top Flange (Rim for the Lid)
f_outer = Part.makeCylinder(radius + 15, 10)
f_inner = Part.makeCylinder(radius - thickness, 10)
top_flange = f_outer.cut(f_inner)
top_flange.translate(App.Vector(0, 0, height)) 

# Outlet Pipe Parameters
p_radius = 20
p_length = 120

# Create outlet pipe
p_out = Part.makeCylinder(p_radius, p_length)
p_in = Part.makeCylinder(p_radius - 3, p_length + 10) 
h_pipe = p_out.cut(p_in)

h_pipe.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)
h_pipe.translate(App.Vector(radius - 5, 0, 80)) 

# Hole in tank wall
hole = Part.makeCylinder(p_radius - 3, thickness + 10)
hole.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)
hole.translate(App.Vector(radius - 5, 0, 80))

# Final tank model
final_model = walls.cut(hole).fuse(h_pipe).fuse(bottom).fuse(top_flange)

obj = doc.addObject("Part::Feature", "WaterTank")
obj.Shape = final_model

doc.recompute()
doc.recompute()

import FreeCAD
import Part

try:
    if 'result' in locals() and result is not None:
        try:
            Part.show(result)
        except Exception:
            pass
            
    if 'doc' in locals() and doc is not None:
        doc.recompute()
        
    if FreeCAD.GuiUp:
        import FreeCADGui as Gui
        if Gui.ActiveDocument and Gui.ActiveDocument.ActiveView:
            Gui.ActiveDocument.ActiveView.viewIsometric()
            Gui.SendMsgToActiveView("ViewFit")
except Exception:
    pass


try:
    import Part
    import FreeCAD as App
    doc = App.ActiveDocument
    if doc:
        objs = [obj for obj in doc.Objects if hasattr(obj, 'Shape') and obj.Shape is not None]
        if objs:
            Part.export(objs, r'../data/output/design_42_77df41c3.step')
        doc.saveAs(r'../data/output/design_42_77df41c3.FCStd')
except Exception as e:
    print("Export Failed:", e)
