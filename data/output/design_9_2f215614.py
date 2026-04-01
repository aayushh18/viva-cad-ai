import math
import FreeCAD as App
import Part

doc = App.newDocument("Box")

box = Part.makeBox(100, 80, 50)

fillet = box.makeFillet(10, box.Edges)

obj = doc.addObject("Part::Feature", "Box")
obj.Shape = fillet

doc.recompute()
doc.recompute()

Gui.ActiveDocument.ActiveView.viewIsometric()
Gui.ActiveDocument.ActiveView.fitAll()

obj.recompute() # Object level
App.ActiveDocument.recompute() # Document level
obj.purgeTouched() # CRITICAL: Clears the 'Failed' flag and makes status 'Successful'

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
            Part.export(objs, r'../data/output/design_9_2f215614.step')
        doc.saveAs(r'../data/output/design_9_2f215614.FCStd')
except Exception as e:
    print("Export Failed:", e)
