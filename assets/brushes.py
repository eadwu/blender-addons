bl_info = {
    "name": "Brushes Menu: Key: 'R'",
    "description": "Sculpt Brushes",
    "blender": (2, 78, 0),
    "category": "Sculpt"
}

import bpy
from bpy.types import (Menu, Operator)

class VIEW3D_PIE_brushes_of(Menu):
    bl_label = "View"
    bl_idname = "pie.brushes_of"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        pie.operator_enum("PAINT_OT_brush_select", "sculpt_tool")

classes = [VIEW3D_PIE_brushes_of]
addon_keymaps = []

def register():
    addon_keymaps.clear()
    for cls in classes:
        bpy.utils.register_class(cls)
    wm = bpy.context.window_manager

    if wm.keyconfigs.addon:
        km = wm.keyconfigs.addon.keymaps.new(name = 'Sculpt')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'R', 'PRESS')
        kmi.properties.name = "pie.brushes_of"
        addon_keymaps.append((km, kmi))

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    wm = bpy.context.window_manager

    kc = wm.keyconfigs.addon
    if kc:
        for km, kmi in addon_keymaps:
            km.keymap_items.remove(kmi)
    addon_keymaps.clear()

if __name__ == "__main__":
    register()
