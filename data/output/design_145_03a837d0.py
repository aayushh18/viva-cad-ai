import FreeCAD as App
import Part

doc = App.newDocument("Cylinder")

radius = 10
height = 40

outer = Part.makeCylinder(radius, height)
inner = Part.makeCylinder(radius - 1, height + 2) # Slightly taller
cylinder = outer.cut(inner)

obj = doc.addObject("Part::Feature", "Cylinder")
obj.Shape = cylinder

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
