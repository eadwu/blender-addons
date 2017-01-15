bl_info = {
    "name": "View Menu: Key: 'E'",
    "description": "View Modes",
    "blender": (2, 78, 0),
    "category": "3d View"
}

import bpy
from bpy.types import (Menu, Operator)

class VIEW3D_PIE_view_more_of(Menu):
    bl_label = "More"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        pie.operator("VIEW3D_OT_view_persportho", text = "Persp/Ortho", icon = 'RESTRICT_VIEW_OFF')
        pie.operator("VIEW3D_OT_view_all")
        pie.operator("VIEW3D_OT_view_selected")
        pie.operator("VIEW3D_OT_camera_to_view")
        pie.operator("SCREEN_OT_region_quadview")


class VIEW3D_PIE_view_of(Menu):
    bl_label = "View"
    bl_idname = "pie.view_of"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        pie.operator_enum("VIEW3D_OT_viewnumpad", "type")
        pie.operator("wm.call_menu_pie", text = "More", icon = 'PLUS').name = "VIEW3D_PIE_view_more_of"

classes = [VIEW3D_PIE_view_more_of, VIEW3D_PIE_view_of]
addon_keymaps = []

def register():
    addon_keymaps.clear()
    for cls in classes:
        bpy.utils.register_class(cls)
    wm = bpy.context.window_manager

    if wm.keyconfigs.addon:
        km = wm.keyconfigs.addon.keymaps.new(name = 'Object Non-modal')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'E', 'PRESS')
        kmi.properties.name = "pie.view_of"
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
