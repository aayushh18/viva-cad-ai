import math
import FreeCAD as App
import Part

doc = App.newDocument("Rod")

cyl = Part.makeCylinder(10, 100)

obj = doc.addObject("Part::Feature", "Rod")
obj.Shape = cyl

doc.recompute()
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


try:
    import Part
    import FreeCAD as App
    doc = App.ActiveDocument
    if doc:
        objs = [obj for obj in doc.Objects if hasattr(obj, 'Shape') and obj.Shape is not None]
        if objs:
            Part.export(objs, r'../data/output/design_51_d023a1e9.step')
        doc.saveAs(r'../data/output/design_51_d023a1e9.FCStd')
except Exception as e:
    print("Export Failed:", e)
