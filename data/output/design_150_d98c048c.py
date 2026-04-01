import FreeCAD as App
import Part

doc = App.newDocument("MultiStepShaft")

# Step 1: Base Shaft
base_shaft_out = Part.makeCylinder(20, 100)
base_shaft_in = Part.makeCylinder(18, 100)
base_shaft = base_shaft_out.cut(base_shaft_in)

# Step 2: Middle Shaft
middle_shaft_out = Part.makeCylinder(15, 80)
middle_shaft_in = Part.makeCylinder(13, 80)
middle_shaft = middle_shaft_out.cut(middle_shaft_in)
middle_shaft.translate(App.Vector(0, 0, 20))

# Step 3: Top Shaft
top_shaft_out = Part.makeCylinder(10, 60)
top_shaft_in = Part.makeCylinder(8, 60)
top_shaft = top_shaft_out.cut(top_shaft_in)
top_shaft.translate(App.Vector(0, 0, 40))

# Final Assembly
final_shaft = base_shaft.fuse(middle_shaft).fuse(top_shaft)

# Add to document
obj = doc.addObject("Part::Feature", "MultiStepShaft")
obj.Shape = final_shaft

# Recompute
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
            Gui.ActiveDocument.ActiveView.fitAll()
except Exception:
    pass
