import math
import FreeCAD as App
import Part

doc = App.newDocument("Shaft")

# Step 1
c1 = Part.makeCylinder(10, 20)

# Step 2
c2 = Part.makeCylinder(5, 30)
c2.Placement.Base = App.Vector(0, 0, 20)

# Step 3
c3 = Part.makeCylinder(3, 40)
c3.Placement.Base = App.Vector(0, 0, 50)

shaft = c1.fuse(c2).fuse(c3)

obj = doc.addObject("Part::Feature", "Shaft")
obj.Shape = shaft

# Elbow Pipe
R = 50 # Bend radius
r_out = 15 # Outer pipe radius
r_in = 12 # Inner pipe radius

outer = Part.makeTorus(R, r_out, App.Vector(50, 0, 0), App.Vector(0,0,1), 0, 360, 90)
inner = Part.makeTorus(R, r_in, App.Vector(50, 0, 0), App.Vector(0,0,1), 0, 360, 90)
elbow = outer.cut(inner)

elbow.translate(App.Vector(60, 0, 0))

final_model = shaft.fuse(elbow)

obj = doc.addObject("Part::Feature", "Final Model")
obj.Shape = final_model

doc.recompute()
doc.recompute()

obj.purgeTouched()

# View Adjustment
import FreeCADGui as Gui
Gui.ActiveDocument.ActiveView.viewIsometric()
Gui.ActiveDocument.ActiveView.fitAll()

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
            Part.export(objs, r'../data/output/design_5_0f72cba2.step')
        doc.saveAs(r'../data/output/design_5_0f72cba2.FCStd')
except Exception as e:
    print("Export Failed:", e)
