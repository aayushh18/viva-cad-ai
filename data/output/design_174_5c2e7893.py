import FreeCAD as App
import Part

doc = App.newDocument("Flange")

# Base Plate
outer = Part.makeCylinder(50, 10)
inner = Part.makeCylinder(40, 10)
plate = outer.cut(inner)

# Bolt Circle
bolt_circle = Part.makeCylinder(35, 10)
bolt_circle.translate(App.Vector(0, 0, 5))

# Holes
holes = []
for i in range(6):
    angle = i * math.pi * 2 / 6
    x = 35 * math.cos(angle)
    y = 35 * math.sin(angle)
    hole = Part.makeCylinder(4, 10)
    hole.translate(App.Vector(x, y, 0))
    holes.append(hole)

# Fuse holes with bolt circle
bolt_circle = bolt_circle.fuse(Part.makeCompound(holes))

# Fuse bolt circle with plate
flange = plate.fuse(bolt_circle)

obj = doc.addObject("Part::Feature", "Flange")
obj.Shape = flange

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
