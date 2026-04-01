import FreeCAD as App
import Part

doc = App.newDocument("MultiStepShaft")

# Step 1: Base Shaft
c1 = Part.makeCylinder(10, 20)
c1.Name = "BaseShaft"

# Step 2: Middle Shaft
c2 = Part.makeCylinder(5, 30)
c2.Name = "MiddleShaft"
c2.Placement.Base = App.Vector(0, 0, 20)

# Step 3: Top Shaft
c3 = Part.makeCylinder(3, 40)
c3.Name = "TopShaft"
c3.Placement.Base = App.Vector(0, 0, 50)

# Fuse all shafts together
shaft = c1.fuse(c2).fuse(c3)

# Add the shaft to the document
obj = doc.addObject("Part::Feature", "MultiStepShaft")
obj.Shape = shaft

# Recompute the document
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
