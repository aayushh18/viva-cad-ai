import os

def build_model(commands_list: list) -> dict:
    model = {
        "length": None,
        "width": None,
        "height": None,
        "operations": []
    }

    for raw_cmd in commands_list:
        if not raw_cmd:
            continue

        # Split multiple commands on the same line if needed
        text = raw_cmd.replace(" create ", "\ncreate ").replace(" add ", "\nadd ")
        cmds = [c.strip() for c in text.splitlines() if c.strip()]

        for cmd in cmds:
            # ---------------- BOX ----------------
            if cmd.startswith("create box"):
                print("Creating box...")
                if len(model["operations"]) > 0:
                    print("Fusing objects...")
                try:
                    tokens = cmd.split()
                    L = float(tokens[tokens.index("length") + 1])
                    W = float(tokens[tokens.index("width") + 1])
                    H = float(tokens[tokens.index("height") + 1])

                    if L <= 0 or W <= 0 or H <= 0:
                        raise ValueError("Dimensions must be positive")

                    model["operations"].append({
                        "type": "create_box", "length": L, "width": W, "height": H
                    })
                    if model["length"] is None:
                        model["length"], model["width"], model["height"] = L, W, H

                except Exception as e:
                    raise ValueError("Invalid box command") from e

            # ---------------- PLATE ----------------
            elif cmd.startswith("create plate"):
                print("Creating plate...")
                if len(model["operations"]) > 0:
                    print("Fusing objects...")
                try:
                    tokens = cmd.split()
                    L = float(tokens[tokens.index("length") + 1])
                    W = float(tokens[tokens.index("width") + 1])
                    T = float(tokens[tokens.index("thickness") + 1])

                    if L <= 0 or W <= 0 or T <= 0:
                        raise ValueError("Dimensions must be positive")

                    model["operations"].append({
                        "type": "create_plate", "length": L, "width": W, "thickness": T
                    })
                    if model["length"] is None:
                        model["length"], model["width"], model["height"] = L, W, T

                except Exception as e:
                    raise ValueError("Invalid plate command") from e

            # ---------------- CYLINDER ----------------
            elif cmd.startswith("create cylinder"):
                print("Creating cylinder...")
                if len(model["operations"]) > 0:
                    print("Fusing objects...")
                try:
                    tokens = cmd.split()
                    rad = float(tokens[tokens.index("radius") + 1])
                    h = float(tokens[tokens.index("height") + 1])

                    if rad <= 0 or h <= 0:
                        raise ValueError("Dimensions must be positive")

                    model["operations"].append({
                        "type": "create_cylinder", "radius": rad, "height": h
                    })
                    if model["length"] is None:
                        model["length"], model["width"], model["height"] = rad*2, rad*2, h

                except Exception as e:
                    raise ValueError("Invalid cylinder command") from e

            # ---------------- SLOT ----------------
            elif cmd.startswith("add slot"):
                print("Adding slot...")
                try:
                    tokens = cmd.split()
                    sl = float(tokens[tokens.index("length") + 1])
                    sw = float(tokens[tokens.index("width") + 1])

                    if sl <= 0 or sw <= 0:
                        raise ValueError("Dimensions must be positive")

                    model["operations"].append({
                        "type": "slot", "length": sl, "width": sw
                    })
                except Exception as e:
                    raise ValueError("Invalid slot command") from e

            # ---------------- BOSS ----------------
            elif cmd.startswith("add boss"):
                print("Adding boss...")
                try:
                    tokens = cmd.split()
                    r = float(tokens[tokens.index("radius") + 1])
                    h = float(tokens[tokens.index("height") + 1])

                    if r <= 0 or h <= 0:
                        raise ValueError("Dimensions must be positive")

                    model["operations"].append({
                        "type": "boss", "radius": r, "height": h
                    })
                except Exception as e:
                    raise ValueError("Invalid boss command") from e

            # ---------------- HOLES ----------------
            elif cmd.startswith("add") and "hole" in cmd:
                try:
                    tokens = cmd.split()

                    count = 1
                    pattern = "single"

                    if tokens[1].isdigit():
                        count = int(tokens[1])

                    radius = float(tokens[tokens.index("radius") + 1])
                    if radius <= 0:
                        raise ValueError("Radius must be positive")

                    if "corner" in cmd:
                        pattern = "corner"
                        print("Applying pattern...")
                    elif "linear" in cmd:
                        pattern = "linear"
                        print("Applying pattern...")
                    elif "at" in tokens:
                        pattern = "custom"
                        idx = tokens.index("at")
                        x = float(tokens[idx + 1])
                        y = float(tokens[idx + 2])
                        model["operations"].append({
                            "type": "hole",
                            "radius": radius,
                            "count": count,
                            "pattern": pattern,
                            "x": x,
                            "y": y
                        })
                        continue
                    else:
                        print("Adding holes...")

                    model["operations"].append({
                        "type": "hole",
                        "radius": radius,
                        "count": count,
                        "pattern": pattern
                    })

                except Exception as e:
                    raise ValueError("Invalid hole command") from e

            # ---------------- FILLET ----------------
            elif cmd.startswith("add fillet"):
                print("Applying fillet...")
                try:
                    r = float(cmd.split()[-1])
                    if r <= 0:
                        raise ValueError("Fillet radius must be positive")

                    model["operations"].append({
                        "type": "fillet",
                        "radius": r
                    })

                except Exception as e:
                    raise ValueError("Invalid fillet command") from e

            # ---------------- CHAMFER ----------------
            elif cmd.startswith("add chamfer"):
                print("Applying chamfer...")
                try:
                    r = float(cmd.split()[-1])
                    if r <= 0:
                        raise ValueError("Chamfer radius must be positive")

                    model["operations"].append({
                        "type": "chamfer",
                        "radius": r
                    })

                except Exception as e:
                    raise ValueError("Invalid chamfer command") from e

            # ---------------- SPHERE ----------------
            elif cmd.startswith("create sphere"):
                print("Creating sphere...")
                if len(model["operations"]) > 0:
                    print("Fusing objects...")
                try:
                    tokens = cmd.split()
                    rad = float(tokens[tokens.index("radius") + 1])
                    if rad <= 0:
                        raise ValueError("Radius must be positive")
                    model["operations"].append({
                        "type": "create_sphere", "radius": rad
                    })
                    if model["length"] is None:
                        model["length"], model["width"], model["height"] = rad*2, rad*2, rad*2
                except Exception as e:
                    raise ValueError("Invalid sphere command") from e

            # ---------------- CONE ----------------
            elif cmd.startswith("create cone"):
                print("Creating cone...")
                if len(model["operations"]) > 0:
                    print("Fusing objects...")
                try:
                    tokens = cmd.split()
                    rad1 = float(tokens[tokens.index("radius1") + 1])
                    rad2 = float(tokens[tokens.index("radius2") + 1])
                    h = float(tokens[tokens.index("height") + 1])
                    if rad1 < 0 or rad2 < 0 or h <= 0 or (rad1 == 0 and rad2 == 0):
                        raise ValueError("Invalid dimensions")
                    model["operations"].append({
                        "type": "create_cone", "radius1": rad1, "radius2": rad2, "height": h
                    })
                    if model["length"] is None:
                        max_r = max(rad1, rad2)
                        model["length"], model["width"], model["height"] = max_r*2, max_r*2, h
                except Exception as e:
                    raise ValueError("Invalid cone command") from e

            # ---------------- TUBE ----------------
            elif cmd.startswith("create tube"):
                print("Creating tube...")
                if len(model["operations"]) > 0:
                    print("Fusing objects...")
                try:
                    tokens = cmd.split()
                    outer = float(tokens[tokens.index("outer") + 1])
                    inner = float(tokens[tokens.index("inner") + 1])
                    h = float(tokens[tokens.index("height") + 1])
                    if outer <= inner or inner <= 0 or h <= 0:
                        raise ValueError("Invalid dimensions")
                    model["operations"].append({
                        "type": "create_tube", "outer": outer, "inner": inner, "height": h
                    })
                    if model["length"] is None:
                        model["length"], model["width"], model["height"] = outer*2, outer*2, h
                except Exception as e:
                    raise ValueError("Invalid tube command") from e

            # ---------------- MIRROR ----------------
            elif cmd.startswith("mirror along"):
                print("Applying mirror...")
                try:
                    tokens = cmd.split()
                    axis = tokens[tokens.index("along") + 1].lower()
                    if axis not in ['x', 'y', 'z']:
                        raise ValueError("Axis must be x, y, or z")
                    model["operations"].append({
                        "type": "mirror", "axis": axis
                    })
                except Exception as e:
                    raise ValueError("Invalid mirror command") from e

            # ---------------- SCALE ----------------
            elif cmd.startswith("scale"):
                print("Scaling model...")
                try:
                    tokens = cmd.split()
                    factor = float(tokens[1])
                    if factor <= 0:
                        raise ValueError("Scale factor must be positive")
                    model["operations"].append({
                        "type": "scale", "factor": factor
                    })
                except Exception as e:
                    raise ValueError("Invalid scale command") from e

            else:
                raise ValueError(f"Unsupported command: {cmd}")

    return model


# ===================== FREECAD SCRIPT =====================

def generate_script(model: dict, output_file: str) -> str:
    if not model["operations"]:
        raise ValueError("No operations defined")

    script = f"""import FreeCAD as App
import FreeCADGui as Gui
import Part

doc = App.newDocument("TextCAD")
result = None
"""

    L = model["length"]
    W = model["width"]
    H = model["height"]

    for i, op in enumerate(model["operations"]):
        typ = op["type"]

        # ---------------- BOX ----------------
        if typ == "create_box":
            script += f"""
box_{i} = doc.addObject("Part::Box", "Box_{i}")
box_{i}.Length = {op['length']}
box_{i}.Width = {op['width']}
box_{i}.Height = {op['height']}
doc.recompute()

if result is None:
    result = box_{i}
else:
    fusion_{i} = doc.addObject("Part::Fuse", "Fuse_{i}")
    fusion_{i}.Base = result
    fusion_{i}.Tool = box_{i}
    doc.recompute()
    result = fusion_{i}
"""

        # ---------------- PLATE ----------------
        elif typ == "create_plate":
            script += f"""
plate_{i} = doc.addObject("Part::Box", "Plate_{i}")
plate_{i}.Length = {op['length']}
plate_{i}.Width = {op['width']}
plate_{i}.Height = {op['thickness']}
doc.recompute()

if result is None:
    result = plate_{i}
else:
    fusion_{i} = doc.addObject("Part::Fuse", "Fuse_{i}")
    fusion_{i}.Base = result
    fusion_{i}.Tool = plate_{i}
    doc.recompute()
    result = fusion_{i}
"""

        # ---------------- CYLINDER ----------------
        elif typ == "create_cylinder":
            script += f"""
cyl_{i} = doc.addObject("Part::Cylinder", "Cyl_{i}")
cyl_{i}.Radius = {op['radius']}
cyl_{i}.Height = {op['height']}
"""
            if i > 0 and L is not None and W is not None:
                script += f"""cyl_{i}.Placement.Base = App.Vector({L}/2, {W}/2, 0)
"""
            script += f"""doc.recompute()

if result is None:
    result = cyl_{i}
else:
    fusion_{i} = doc.addObject("Part::Fuse", "Fuse_{i}")
    fusion_{i}.Base = result
    fusion_{i}.Tool = cyl_{i}
    doc.recompute()
    result = fusion_{i}
"""

        # ---------------- HOLE ----------------
        elif typ == "hole":
            r = op["radius"]
            count = op["count"]
            pattern = op["pattern"]
            
            if L is not None and W is not None:
                script += f"""
if {r}*2 <= min({L},{W}):
"""
                if pattern == "corner" and count == 4:
                    script += f"""
    offset = 10
    positions = [
        (offset, offset),
        ({L}-offset, offset),
        (offset, {W}-offset),
        ({L}-offset, {W}-offset)
    ]

    for j, pos in enumerate(positions):
        cut_cyl_{i}_j = doc.addObject("Part::Cylinder", f"CutCyl{i}_{{j}}")
        cut_cyl_{i}_j.Radius = {r}
        cut_cyl_{i}_j.Height = {H} + 10 if {H} else 50
        cut_cyl_{i}_j.Placement.Base = App.Vector(pos[0], pos[1], -5)
        doc.recompute()

        cut_{i}_j = doc.addObject("Part::Cut", f"Cut{i}_{{j}}")
        cut_{i}_j.Base = result
        cut_{i}_j.Tool = cut_cyl_{i}_j
        doc.recompute()
        result = cut_{i}_j
"""
                elif pattern == "linear":
                    script += f"""
    offset = {L} / ({count} + 1)
    positions = [(offset * (j + 1), {W}/2) for j in range({count})]
    
    for j, pos in enumerate(positions):
        cut_cyl_{i}_j = doc.addObject("Part::Cylinder", f"CutCyl{i}_{{j}}")
        cut_cyl_{i}_j.Radius = {r}
        cut_cyl_{i}_j.Height = {H} + 10 if {H} else 50
        cut_cyl_{i}_j.Placement.Base = App.Vector(pos[0], pos[1], -5)
        doc.recompute()

        cut_{i}_j = doc.addObject("Part::Cut", f"Cut{i}_{{j}}")
        cut_{i}_j.Base = result
        cut_{i}_j.Tool = cut_cyl_{i}_j
        doc.recompute()
        result = cut_{i}_j
"""
                elif pattern == "custom":
                    script += f"""
    cut_cyl_{i} = doc.addObject("Part::Cylinder", "CutCyl_{i}")
    cut_cyl_{i}.Radius = {r}
    cut_cyl_{i}.Height = {H} + 10 if {H} else 50
    cut_cyl_{i}.Placement.Base = App.Vector({L}/2 + {op['x']}, {W}/2 + {op['y']}, -5)
    doc.recompute()

    cut_{i} = doc.addObject("Part::Cut", "Cut_{i}")
    cut_{i}.Base = result
    cut_{i}.Tool = cut_cyl_{i}
    doc.recompute()
    result = cut_{i}
"""
                else:
                    script += f"""
    cut_cyl_{i} = doc.addObject("Part::Cylinder", "CutCyl_{i}")
    cut_cyl_{i}.Radius = {r}
    cut_cyl_{i}.Height = {H} + 10 if {H} else 50
    cut_cyl_{i}.Placement.Base = App.Vector({L}/2, {W}/2, -5)
    doc.recompute()

    cut_{i} = doc.addObject("Part::Cut", "Cut_{i}")
    cut_{i}.Base = result
    cut_{i}.Tool = cut_cyl_{i}
    doc.recompute()
    result = cut_{i}
"""
            else:
                script += f"""
cut_cyl_{i} = doc.addObject("Part::Cylinder", "CutCyl_{i}")
cut_cyl_{i}.Radius = {r}
cut_cyl_{i}.Height = {H} + 10 if {H} else 50
cut_cyl_{i}.Placement.Base = App.Vector(0, 0, -5)
doc.recompute()

cut_{i} = doc.addObject("Part::Cut", "Cut_{i}")
cut_{i}.Base = result
cut_{i}.Tool = cut_cyl_{i}
doc.recompute()
result = cut_{i}
"""

        # ---------------- FILLET ----------------
        elif typ == "fillet":
            r = op["radius"]
            script += f"""
try:
    shape = result.Shape
    fillet_shape = shape.makeFillet({r}, shape.Edges)
    fillet_obj = doc.addObject("Part::Feature", "Fillet_{i}")
    fillet_obj.Shape = fillet_shape
    result = fillet_obj
    doc.recompute()
except Exception as e:
    print(f"Fillet failed: {{e}}")
"""

        # ---------------- CHAMFER ----------------
        elif typ == "chamfer":
            r = op["radius"]
            script += f"""
try:
    shape = result.Shape
    chamfer_shape = shape.makeChamfer({r}, shape.Edges)
    chamfer_obj = doc.addObject("Part::Feature", "Chamfer_{i}")
    chamfer_obj.Shape = chamfer_shape
    result = chamfer_obj
    doc.recompute()
except Exception as e:
    print(f"Chamfer failed: {{e}}")
"""

        # ---------------- SLOT ----------------
        elif typ == "slot":
            slen = op["length"]
            swid = op["width"]
            script += f"""
# Slot components
sbox_{i} = doc.addObject("Part::Box", "SlotBox_{i}")
sbox_{i}.Length = {slen} - {swid}
sbox_{i}.Width = {swid}
sbox_{i}.Height = {H} + 10 if {H} else 50
if {L} is not None and {W} is not None:
    cx, cy = {L}/2, {W}/2
else:
    cx, cy = 0, 0

sbox_{i}.Placement.Base = App.Vector(cx - ({slen}-{swid})/2, cy - {swid}/2, -5)

scyl1_{i} = doc.addObject("Part::Cylinder", "SlotCyl1_{i}")
scyl1_{i}.Radius = {swid}/2
scyl1_{i}.Height = {H} + 10 if {H} else 50
scyl1_{i}.Placement.Base = App.Vector(cx - ({slen}-{swid})/2, cy, -5)

scyl2_{i} = doc.addObject("Part::Cylinder", "SlotCyl2_{i}")
scyl2_{i}.Radius = {swid}/2
scyl2_{i}.Height = {H} + 10 if {H} else 50
scyl2_{i}.Placement.Base = App.Vector(cx + ({slen}-{swid})/2, cy, -5)

doc.recompute()

sfuse1_{i} = doc.addObject("Part::Fuse", "SlotFuse1_{i}")
sfuse1_{i}.Base = sbox_{i}
sfuse1_{i}.Tool = scyl1_{i}
doc.recompute()

sfuse2_{i} = doc.addObject("Part::Fuse", "SlotFuse2_{i}")
sfuse2_{i}.Base = sfuse1_{i}
sfuse2_{i}.Tool = scyl2_{i}
doc.recompute()

cut_{i} = doc.addObject("Part::Cut", "SlotCut_{i}")
cut_{i}.Base = result
cut_{i}.Tool = sfuse2_{i}
doc.recompute()
result = cut_{i}
"""

        # ---------------- BOSS ----------------
        elif typ == "boss":
            r = op["radius"]
            h = op["height"]
            script += f"""
boss_{i} = doc.addObject("Part::Cylinder", "Boss_{i}")
boss_{i}.Radius = {r}
boss_{i}.Height = {h}
if {L} is not None and {W} is not None:
    boss_{i}.Placement.Base = App.Vector({L}/2, {W}/2, {H} if {H} else 0)
else:
    boss_{i}.Placement.Base = App.Vector(0, 0, {H} if {H} else 0)
doc.recompute()

bfuse_{i} = doc.addObject("Part::Fuse", "BossFuse_{i}")
bfuse_{i}.Base = result
bfuse_{i}.Tool = boss_{i}
doc.recompute()
result = bfuse_{i}
"""

        # ---------------- SPHERE ----------------
        elif typ == "create_sphere":
            script += f"""
sphere_{i} = doc.addObject("Part::Sphere", "Sphere_{i}")
sphere_{i}.Radius = {op['radius']}
"""
            if i > 0 and L is not None and W is not None:
                script += f"""sphere_{i}.Placement.Base = App.Vector({L}/2, {W}/2, {H} if {H} else 0)
"""
            script += f"""doc.recompute()

if result is None:
    result = sphere_{i}
else:
    fusion_{i} = doc.addObject("Part::Fuse", "Fuse_{i}")
    fusion_{i}.Base = result
    fusion_{i}.Tool = sphere_{i}
    doc.recompute()
    result = fusion_{i}
"""

        # ---------------- CONE ----------------
        elif typ == "create_cone":
            script += f"""
cone_{i} = doc.addObject("Part::Cone", "Cone_{i}")
cone_{i}.Radius1 = {op['radius1']}
cone_{i}.Radius2 = {op['radius2']}
cone_{i}.Height = {op['height']}
"""
            if i > 0 and L is not None and W is not None:
                script += f"""cone_{i}.Placement.Base = App.Vector({L}/2, {W}/2, {H} if {H} else 0)
"""
            script += f"""doc.recompute()

if result is None:
    result = cone_{i}
else:
    fusion_{i} = doc.addObject("Part::Fuse", "Fuse_{i}")
    fusion_{i}.Base = result
    fusion_{i}.Tool = cone_{i}
    doc.recompute()
    result = fusion_{i}
"""

        # ---------------- TUBE ----------------
        elif typ == "create_tube":
            script += f"""
tube_outer_{i} = doc.addObject("Part::Cylinder", "TubeOuter_{i}")
tube_outer_{i}.Radius = {op['outer']}
tube_outer_{i}.Height = {op['height']}

tube_inner_{i} = doc.addObject("Part::Cylinder", "TubeInner_{i}")
tube_inner_{i}.Radius = {op['inner']}
tube_inner_{i}.Height = {op['height']}

doc.recompute()

tube_{i} = doc.addObject("Part::Cut", "Tube_{i}")
tube_{i}.Base = tube_outer_{i}
tube_{i}.Tool = tube_inner_{i}
doc.recompute()
"""
            if i > 0 and L is not None and W is not None:
                script += f"""tube_{i}.Placement.Base = App.Vector({L}/2, {W}/2, {H} if {H} else 0)
doc.recompute()
"""
            script += f"""
if result is None:
    result = tube_{i}
else:
    fusion_{i} = doc.addObject("Part::Fuse", "Fuse_{i}")
    fusion_{i}.Base = result
    fusion_{i}.Tool = tube_{i}
    doc.recompute()
    result = fusion_{i}
"""

        # ---------------- MIRROR ----------------
        elif typ == "mirror":
            axis = op["axis"]
            if axis == 'x':
                norm = "App.Vector(1,0,0)"
            elif axis == 'y':
                norm = "App.Vector(0,1,0)"
            else:
                norm = "App.Vector(0,0,1)"
            
            script += f"""
mirror_{i} = doc.addObject("Part::Mirroring", "Mirror_{i}")
mirror_{i}.Source = result
mirror_{i}.Normal = {norm}
doc.recompute()
result = mirror_{i}
"""

        # ---------------- SCALE ----------------
        elif typ == "scale":
            factor = op["factor"]
            script += f"""
try:
    shape = result.Shape
    scaled_shape = shape.scale({factor})
    scaled_obj = doc.addObject("Part::Feature", "Scaled_{i}")
    scaled_obj.Shape = scaled_shape
    result = scaled_obj
    doc.recompute()
except Exception as e:
    print(f"Scale failed: {{e}}")
"""

    script += f"""
doc.recompute()
try:
    if Gui.ActiveDocument and Gui.ActiveDocument.ActiveView:
        Gui.ActiveDocument.ActiveView.viewIsometric()
        Gui.ActiveDocument.ActiveView.fitAll()
except Exception as e:
    print(f"View scaling failed: {{e}}")

App.ActiveDocument.saveAs("{output_file}")
"""
    return script
