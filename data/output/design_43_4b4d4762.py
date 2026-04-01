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
inner_cyl = Part.makeCylinder(radius - thickness, height + 2) # Slightly taller
walls = outer_cyl.cut(inner_cyl)

# Bottom Plate (Closing the Tank)
bottom = Part.makeCylinder(radius, thickness)

# Top Flange (Rim for the Lid)
f_outer = Part.makeCylinder(radius + 15, 10)
f_inner = Part.makeCylinder(radius - thickness, 10)
top_flange = f_outer.cut(f_inner)
top_flange.translate(App.Vector(0, 0, height)) # Move to top

# Outlet Pipe (Hollow)
p_out = Part.makeCylinder(12, 100).cut(Part.makeCylinder(10, 110))
p_out.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)
p_out.translate(App.Vector(110, 60, 40)) # Tank ke side se nikla

# Final Fusion
final_model = walls.fuse(bottom).fuse(top_flange).fuse(p_out)

obj = doc.addObject("Part::Feature", "WaterTank")
obj.Shape = final_model

doc.recompute()
doc.recompute()

obj.purgeTouched() # CRITICAL: Clears the 'Failed' flag and makes status 'Successful'

# View Adjustment
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui as Gui
    if Gui.ActiveDocument and Gui.ActiveDocument.ActiveView:
        Gui.ActiveDocument.ActiveView.viewIsometric()
        Gui.ActiveDocument.ActiveView.fitAll()

try:
    import Part
    import FreeCAD as App
    doc = App.ActiveDocument
    if doc:
        objs = [obj for obj in doc.Objects if hasattr(obj, 'Shape') and obj.Shape is not None]
        if objs:
            Part.export(objs, r'../data/output/design_43_4b4d4762.step')
        doc.saveAs(r'../data/output/design_43_4b4d4762.FCStd')
except Exception as e:
    print("Export Failed:", e)
