import FreeCAD as App
import Part

doc = App.newDocument("MultiStepShaft")

# Base Shaft
base_shaft_radius = 20
base_shaft_height = 100
base_shaft = Part.makeCylinder(base_shaft_radius, base_shaft_height)

# Step 1
step1_radius = 25
step1_height = 50
step1 = Part.makeCylinder(step1_radius, step1_height)
step1.translate(App.Vector(0, 0, base_shaft_height))

# Step 2
step2_radius = 30
step2_height = 75
step2 = Part.makeCylinder(step2_radius, step2_height)
step2.translate(App.Vector(0, 0, base_shaft_height + step1_height))

# Final Shaft
final_shaft = base_shaft.cut(step1).cut(step2)

obj = doc.addObject("Part::Feature", "MultiStepShaft")
obj.Shape = final_shaft
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
