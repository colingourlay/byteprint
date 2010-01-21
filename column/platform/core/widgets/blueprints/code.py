from django import forms
from platform.core.widgets import Blueprint

class CodeExample(Blueprint):
    
    name = 'code-example'
    display_name = 'Code Example'
    fields = {
        'code': forms.CharField(
            widget = forms.Textarea(
                attrs = {
                    'id':'code_editor'
                }
            ),
            label = "Code",
            help_text = "Enter the source code you want to appear within the \
                widget",
            initial = "print \"Hello World\""
        ),
        'language': forms.ChoiceField(
            label = "Language",
            help_text = "Enter the language your code is written in. This will \
                be added to the <code> tag's class attribute, which can be \
                used with various javascript code highlighting plugins.",
            initial = "python",
            choices = (
                ('basic', 'Basic'),
                ('c', 'C'),
                ('cpp', 'C++'),
                ('coldfusion', 'Coldfusion'),
                ('css', 'CSS'),
                ('html', 'HTML'),
                ('js', 'Javascript'),
                ('perl', 'Perl'),
                ('php', 'PHP'),
                ('python', 'Python'),
                ('ruby', 'Ruby'),
                ('sql', 'SQL'),
                ('vb', 'Visual Basic'),
                ('xml', 'XML'),
            )
        )
    }

    def render(self, widget_data):
        output = "<pre><code class=\"" + widget_data['language'] + \
            "\">" + widget_data['code'] + "</code></pre>"
        return output