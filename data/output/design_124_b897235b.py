import FreeCAD as App
import Part
import Import

doc = App.newDocument("BoxWithHole")
box = Part.makeBox(20, 20, 10)
hole = Part.makeCylinder(5, 10)
hole.Placement.Base = App.Vector(10, 10, 5)
result = box.cut(hole)

obj = doc.addObject("Part::Feature", "Result")
obj.Shape = result
doc.recompute()
Import.export(doc.Objects, "../data/output/design_124_b897235b.step")

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
