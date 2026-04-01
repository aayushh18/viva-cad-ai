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

    current_obj = None
    try:
        print('Applying box (b1)')
        b1 = doc.addObject('Part::Box', 'b1')
        b1.Length = 120
        b1.Width = 80
        b1.Height = 10
        current_obj = b1
        doc.recompute()
    except Exception as e:
        print(f'ERROR applying box: {e}')
    try:
        if current_obj: print(f'Applying hole on {current_obj.Name}')
        if current_obj:
            h1_tool = doc.addObject('Part::Cylinder', 'h1_tool')
            h1_tool.Radius = 5
            h1_tool.Height = 10
            h1_tool.Placement = App.Placement(App.Vector(10, 10, -10/2), App.Rotation(0,0,0))
            h1 = doc.addObject('Part::Cut', 'h1')
            h1.Base = current_obj
            h1.Tool = h1_tool
            set_visible(current_obj.Name, False)
            set_visible('h1_tool', False)
            current_obj = h1
        doc.recompute()
    except Exception as e:
        print(f'ERROR applying hole: {e}')
    
    # Visualization Logic
    doc.recompute()
    try:
        import FreeCADGui as Gui
        Gui.ActiveDocument.ActiveView.viewIsometric()
        Gui.ActiveDocument.ActiveView.fitAll()
    except Exception:
        pass
    
    doc.saveAs('/home/aayush/Downloads/viva-cad-ai/data/output/design_14_c4166ada.FCStd')
    # Exporting dynamically checking visibility
    visible_objs = []
    for o in doc.Objects:
        is_vis = getattr(o, 'Visibility', True)
        if App.GuiUp and hasattr(o, 'ViewObject') and o.ViewObject:
            is_vis = getattr(o.ViewObject, 'Visibility', is_vis)
        if is_vis and hasattr(o, 'Shape'):
            visible_objs.append(o)
    
    if visible_objs:
        Part.export(visible_objs, '/home/aayush/Downloads/viva-cad-ai/data/output/design_14_c4166ada.step')
        __objs_to_export__ = []
        for i, obj in enumerate(visible_objs):
            __mesh_obj__ = doc.addObject('Mesh::Feature', f'__stl_export_{i}__')
            __mesh_obj__.Mesh = Mesh.Mesh(obj.Shape.tessellate(0.1))
            __objs_to_export__.append(__mesh_obj__)
        Mesh.export(__objs_to_export__, '/home/aayush/Downloads/viva-cad-ai/data/output/design_14_c4166ada.stl')
    
        if not App.GuiUp:
            sys.exit(0)
    
except Exception as e:
    print(f'SCRIPT_ERROR: {str(e)}')
    import traceback
    traceback.print_exc()
    if not App.GuiUp:
        sys.exit(1)