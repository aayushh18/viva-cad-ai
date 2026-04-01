import FreeCAD as App
import Part

doc = App.newDocument("Valve_Fixed")

# Valve Body (Central Sphere or Box)
body = Part.makeSphere(20)

# Connectors (Left and Right)
c1 = Part.makeCylinder(12, 30)
c1.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)
c1.translate(App.Vector(-30, 0, 0))

c2 = c1.copy()
c2.translate(App.Vector(60, 0, 0))

# Stem and Wheel (Top part)
stem = Part.makeCylinder(5, 25)
stem.translate(App.Vector(0,0,15))

wheel = Part.makeTorus(15, 3)
wheel.translate(App.Vector(0,0,40))

# Fuse all
valve = body.fuse(c1).fuse(c2).fuse(stem).fuse(wheel)

obj = doc.addObject("Part::Feature", "Valve")
obj.Shape = valve

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
