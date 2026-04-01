import math
import FreeCAD as App
import Part

doc = App.newDocument("Gear")

# Gear parameters
radius = 20
thickness = 5
teeth = 10
pitch_radius = radius + thickness

# Create gear
gear = Part.makeHelix(radius, pitch_radius, teeth, 360, 0, 0, 0)

# Create a solid from the gear
gear_solid = Part.makeSolid(gear)

obj = doc.addObject("Part::Feature", "Gear")
obj.Shape = gear_solid

doc.recompute()
doc.recompute()

# View Adjustment
import FreeCADGui as Gui
Gui.ActiveDocument.ActiveView.viewIsometric()
Gui.ActiveDocument.ActiveView.fitAll()

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
            Part.export(objs, r'../data/output/design_27_f19e0985.step')
        doc.saveAs(r'../data/output/design_27_f19e0985.FCStd')
except Exception as e:
    print("Export Failed:", e)
