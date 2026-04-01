import FreeCAD as App
import Part

doc = App.newDocument("MultiStepShaft")

# Step 1: Base Shaft
c1 = Part.makeCylinder(10, 20)
c1_label = "Base Shaft"

# Step 2: Middle Shaft
c2 = Part.makeCylinder(5, 30)
c2.Placement.Base = App.Vector(0, 0, 20)
c2_label = "Middle Shaft"

# Step 3: Top Shaft
c3 = Part.makeCylinder(2, 10)
c3.Placement.Base = App.Vector(0, 0, 50)
c3_label = "Top Shaft"

# Fuse all shafts together
shaft = c1.fuse(c2).fuse(c3)

# Add shaft to document
obj = doc.addObject("Part::Feature", "MultiStepShaft")
obj.Shape = shaft

# Recompute document
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
