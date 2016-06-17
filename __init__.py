#
# Happy Brithday Andrew Addon
#

bl_info = {
	"name": "Happy Birthday Andrew Addon",
	"author": "Patrick W. Crawford <support@theduckcow.com>",
	"version": (1, 0, 0),
	"blender": (2, 77, 0),
	"location": "Property panel > World (below PLStudio/Skies)",
	"description": "A happy birthday addon",
	"warning": "",
	"wiki_url": "",
	"category": "Animation"
}


import os
import bpy

class birthdaypress(bpy.types.Operator):
	"""It's ur birthday? it's ur birthday. Happy birthday"""
	bl_idname = "animation.birthdaypress"
	bl_label = "Press in case of Birthday"
	bl_options = {'REGISTER', 'UNDO'}

	def invoke(self, context, event):
		return context.window_manager.invoke_props_dialog(self,)

	def draw(self, context):
		layout = self.layout
		layout.label("Happy Birthday!!")
		

	def runthing(self, context):
		direc = os.path.join(os.path.dirname(__file__),"confetti.blend","Group")
		bpy.ops.wm.append(directory=direc, filename="confetti-source")
		bpy.ops.screen.animation_play()


	def execute(self, context):
		self.runthing(context)
		# bring up a menu here then.
		self.report({'INFO'}, "Have a happy birthday, Andrew!")
		bpy.ops.animation.birthdaypressed()

		return {'FINISHED'}

		
class birthdaypressed(bpy.types.Operator):
	"""It's ur birthday? it's ur birthday. Happy birthday"""
	bl_idname = "animation.birthdaypressed"
	bl_label = "Have a happy Blenderguru Birthday"

	def invoke(self, context, event):
		return context.window_manager.invoke_props_dialog(self)

	def draw(self, context):
		layout = self.layout
		layout.label("Happy Birthday, Andrew!!")


	def execute(self, context):
		# bring up a menu here then.
		self.report({'INFO'}, "Enjoy the confetti")

		return {'FINISHED'}


class birthdayPanel(bpy.types.Panel):
	"""Happy birthday Andrew Panel"""
	bl_label = "Birthday Panel"
	bl_idname = "guru_birthdaypanel"
	bl_space_type = 'PROPERTIES'
	bl_region_type = 'WINDOW'
	bl_context = "world"

	def draw(self, context):
		layout = self.layout
		pcoll = preview_collections["main"]

		row = layout.row()
		row.scale_y = 3
		my_icon = pcoll["my_icon"]
		row.operator("animation.birthdaypress", icon_value=my_icon.icon_id)

		# my_icon.icon_id can be used in any UI function that accepts
		# icon_value # try also setting text=""
		# to get an icon only operator button


# We can store multiple preview collections here,
# however in this example we only store "main"
preview_collections = {}


def register():

	# Note that preview collections returned by bpy.utils.previews
	# are regular py objects - you can use them to store custom data.
	import bpy.utils.previews
	pcoll = bpy.utils.previews.new()

	# path to the folder where the icon is
	# the path is calculated relative to this py file inside the addon folder
	my_icons_dir = os.path.join(os.path.dirname(__file__), "icons")

	# load a preview thumbnail of a file and store in the previews collection
	pcoll.load("my_icon", os.path.join(my_icons_dir, "donut.png"), 'IMAGE')

	preview_collections["main"] = pcoll

	# bpy.utils.register_class(PreviewsExamplePanel)
	bpy.utils.register_module(__name__)


def unregister():

	for pcoll in preview_collections.values():
		bpy.utils.previews.remove(pcoll)
	preview_collections.clear()

	# bpy.utils.unregister_class(PreviewsExamplePanel)
	bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
	register()
