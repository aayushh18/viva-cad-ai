import sys
import FreeCAD as App
import Part
import Mesh
print('SCRIPT_ERROR: None') # Initializing log
try:
    import FreeCADGui as Gui
except ImportError:
    Gui = None

def set_visible(obj_name, visible):
    obj = doc.getObject(obj_name)
    if obj:
        try:
            if hasattr(obj, 'Visibility'):
                obj.Visibility = visible
        except Exception:
            pass
        if App.GuiUp and Gui:
            try:
                if hasattr(obj, 'ViewObject') and obj.ViewObject:
                    obj.ViewObject.Visibility = visible
            except Exception:
                pass

try:
    doc = App.newDocument('part')

    b1 = doc.addObject('Part::Box', 'b1')
    b1.Length = 100
    b1.Width = 100
    b1.Height = 100
    doc.recompute()
    doc.recompute()
    
    # Visualization Logic
    doc.recompute()
    try:
        import FreeCADGui as Gui
        Gui.ActiveDocument.ActiveView.viewIsometric()
        Gui.ActiveDocument.ActiveView.fitAll()
    except Exception:
        pass
    
    doc.saveAs('/home/aayush/Downloads/viva-cad-ai/data/output/design_11_e41b62ca.FCStd')
    # Exporting dynamically checking visibility
    visible_objs = []
    for o in doc.Objects:
        is_vis = getattr(o, 'Visibility', True)
        if App.GuiUp and hasattr(o, 'ViewObject') and o.ViewObject:
            is_vis = getattr(o.ViewObject, 'Visibility', is_vis)
        if is_vis and hasattr(o, 'Shape'):
            visible_objs.append(o)
    
    if visible_objs:
        Part.export(visible_objs, '/home/aayush/Downloads/viva-cad-ai/data/output/design_11_e41b62ca.step')
        __objs_to_export__ = []
        for i, obj in enumerate(visible_objs):
            __mesh_obj__ = doc.addObject('Mesh::Feature', f'__stl_export_{i}__')
            __mesh_obj__.Mesh = Mesh.Mesh(obj.Shape.tessellate(0.1))
            __objs_to_export__.append(__mesh_obj__)
        Mesh.export(__objs_to_export__, '/home/aayush/Downloads/viva-cad-ai/data/output/design_11_e41b62ca.stl')
    
        if not App.GuiUp:
            sys.exit(0)
    
except Exception as e:
    print(f'SCRIPT_ERROR: {str(e)}')
    import traceback
    traceback.print_exc()
    if not App.GuiUp:
        sys.exit(1)