import FreeCAD as App
import Part
import FreeCADGui as Gui

doc = App.newDocument("Pro_Flow_Meter_Assembly")

# 1. PARAMETERS
length = 300
pipe_r = 20
thick = 3
flange_r = 40
flange_thick = 8

# 2. HOLLOW PIPE
outer = Part.makeCylinder(pipe_r, length)
inner = Part.makeCylinder(pipe_r - thick, length + 2)
inner.translate(App.Vector(0, 0, -1))
pipe = outer.cut(inner)

# 3. TWO END FLANGES (Top and Bottom)
def make_flange(z_pos):
    f_out = Part.makeCylinder(flange_r, flange_thick)
    f_in = Part.makeCylinder(pipe_r - thick, flange_thick + 2)
    f_in.translate(App.Vector(0, 0, -1))
    f = f_out.cut(f_in)
    f.translate(App.Vector(0, 0, z_pos))
    return f

flange_bottom = make_flange(0)
flange_top = make_flange(length - flange_thick)

# 4. DIGITAL FLOW METER (Exactly in the middle)
# Ek box jo flow sensor/transmitter ka kaam karega
meter_box = Part.makeBox(40, 40, 30)
meter_box.translate(App.Vector(-20, -20, (length/2) - 15)) # Centered at L/2

# 5. FINAL ASSEMBLY
final_shape = pipe.fuse(flange_bottom).fuse(flange_top).fuse(meter_box)

# 6. OBJECT & STATUS FIX
obj = doc.addObject("Part::Feature", "FlowSystem")
obj.Shape = final_shape

# Mandatory Status Cleanup
obj.recompute()
App.ActiveDocument.recompute()
obj.purgeTouched() # Green status ensure karega

# 7. VIEW ADJUSTMENT
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
            Part.export(objs, r'../data/output/design_8_b4d9b0a0.step')
        doc.saveAs(r'../data/output/design_8_b4d9b0a0.FCStd')
except Exception as e:
    print("Export Failed:", e)
