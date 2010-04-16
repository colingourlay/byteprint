from django.template import add_to_builtins

add_to_builtins('bp.contrib.filebrowser.templatetags.fb_csrf')
add_to_builtins('bp.contrib.filebrowser.templatetags.fb_pagination')
add_to_builtins('bp.contrib.filebrowser.templatetags.fb_tags')
add_to_builtins('bp.contrib.filebrowser.templatetags.fb_versions')