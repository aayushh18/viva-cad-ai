import math
import FreeCAD as App
import Part

doc = App.newDocument("MountingPlate")

# Create a 100x100x10 mm box
plate = Part.makeBox(100, 100, 10)

# Create a 5 mm radius hole
hole = Part.makeCylinder(5, 10)

# Define the positions of the holes
positions = [
    App.Vector(15, 15, 0),
    App.Vector(85, 15, 0),
    App.Vector(15, 85, 0),
    App.Vector(85, 85, 0)
]

# Create and place the holes
for pos in positions:
    hole.Placement.Base = pos
    plate = plate.cut(hole)

obj = doc.addObject("Part::Feature", "Plate")
obj.Shape = plate

doc.recompute()
doc.recompute()

obj.purgeTouched()

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
            Part.export(objs, r'../data/output/design_4_ead6b48d.step')
        doc.saveAs(r'../data/output/design_4_ead6b48d.FCStd')
except Exception as e:
    print("Export Failed:", e)
