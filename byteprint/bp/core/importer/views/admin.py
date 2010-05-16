from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.simple import direct_to_template

from bp.core.importer.forms import ImportDataForm

IMPORT_DATA_TEMPLATE = 'importer/admin/import_data.html'

@login_required
def import_data(request, template=IMPORT_DATA_TEMPLATE):
    import_data_form = ImportDataForm()
    if request.method == 'POST':
        import_data_form = ImportDataForm(request.POST, request.FILES)
        if import_data_form.is_valid():
            import_source = import_data_form.cleaned_data['import_source']
            import_data_file = request.FILES['import_data_file']
            import_data = ""
            for line in import_data_file:
                import_data += line
            if import_source == 'wordpress':
                from bp.core.importer.processors import wordpress
                wordpress.run(request, import_data)
        
    return direct_to_template(
        request,
        template,
        {
            'menu_current': 'menu_tools',
            'h1': 'Import Data',
            'form': import_data_form,
        }
    )