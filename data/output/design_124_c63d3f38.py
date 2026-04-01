import FreeCAD as App
import Part
import math
import Import

doc = App.newDocument("MultiStepShaft")
c1 = Part.makeCylinder(10, 20)
c2 = Part.makeCylinder(5, 30)
c2.Placement.Base = App.Vector(0, 0, 20)
c3 = Part.makeCylinder(3, 40)
c3.Placement.Base = App.Vector(0, 0, 40)
c4 = Part.makeCylinder(2, 50)
c4.Placement.Base = App.Vector(0, 0, 50)

shaft = c1.fuse(c2)
shaft = shaft.fuse(c3)
shaft = shaft.fuse(c4)

obj = doc.addObject("Part::Feature", "MultiStepShaft")
obj.Shape = shaft
doc.recompute()
Import.export(doc.Objects, "../data/output/design_124_c63d3f38.step")

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
