import FreeCAD as App
import Part
import Import

doc = App.newDocument("Box")
box = Part.makeBox(20, 20, 20)
fillet = box.makeFillet(2, box.Edges)

obj = doc.addObject("Part::Feature", "Box")
obj.Shape = fillet
doc.recompute()
Import.export(doc.Objects, "../data/output/design_118_985dd911.step")

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
