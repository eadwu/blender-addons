import bpy
import importlib
from bpy.props import (BoolProperty, PointerProperty)
from bpy.types import (PropertyGroup, AddonPreferences)

bl_info = {
    'name': 'Pie Menu Essentials',
    'author': 'Gensoki',
    'version': (0, 0, 1),
    'blender': (2, 7, 8),
    'description': 'Common actions I use in pie menus',
    'location': 'Addons Preferences',
    'warning': '',
    'wiki_url': '',
    'category': 'Pie Menu'
}

sub_modules = (
    "object_modes",
    "manipulator",
    "mesh_select",
    "brushes",
    "shade",
    "pivot",
    "edit",
    "view"
)

sub_mods = [importlib.import_module(__package__ + ".assets." + submod) for submod in sub_modules]
sub_mods.sort(key = lambda mod: (mod.bl_info['category'], mod.bl_info['name']))

def register_submodule(mod):
    mod.register()
    mod.__addon_enabled__ = True

def unregister_submodule(mod):
    if mod.__addon_enabled__:
        mod.unregister()
        mod.__addon_enabled__ = False

def register():
    for mod in sub_mods:
        if not hasattr(mod, '__addon_enabled__'):
            mod.__addon_enabled__ = False
        register_submodule(mod)

def unregister():
    for mod in sub_mods:
        if mod.__addon_enabled__:
            unregister_submodule(mod)

if __name__ == "__main__":
    register()
