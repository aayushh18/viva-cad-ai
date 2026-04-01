import FreeCAD as App
import Part
import Import

doc = App.newDocument("Pro_Elbow_Fix")

R = 50 # Bend radius
r_out = 15 # Outer pipe radius
r_in = 12 # Inner pipe radius

outer = Part.makeTorus(R, r_out, App.Vector(0,0,0), App.Vector(0,0,1), 0, 360, 90)
inner = Part.makeTorus(R, r_in, App.Vector(0,0,0), App.Vector(0,0,1), 0, 360, 90)
elbow = outer.cut(inner)

obj = doc.addObject("Part::Feature", "Elbow")
obj.Shape = elbow
doc.recompute()
Import.export(doc.Objects, "../data/output/design_132_2bbb5b31.step")

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
            Gui.ActiveDocument.ActiveView.fitAll()
except Exception:
    pass
