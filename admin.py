from flask import redirect, url_for, request
from flask_security import current_user
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView


class AdminMixin:
	def is_accessible(self):
		#return current_user.has_role('admin')
		try:
			return current_user.nickname == 'BotVasy'
		except:
			return False

	def inaccessible_callback(self, name, **kwargs):
		return redirect( url_for('security.login', next=request.url) )

class BaseModelView(ModelView):
	def on_model_change(self, form, model, is_created):
		model.generate_slug()
		return super(BaseModelView, self).on_model_change(form, model, is_created)


class HomeAdminView(AdminMixin, AdminIndexView):
	pass

class UserAdminView(AdminMixin, ModelView):
	form_columns = ['email','nickname','password','about_me']

	def on_model_change(self, form, model, is_created):
		model.active = True

		return super(UserAdminView, self).on_model_change(form, model, is_created) 
	
		