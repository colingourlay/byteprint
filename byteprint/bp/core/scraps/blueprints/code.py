from django import forms

from bp.core.scraps import Blueprint

class SourceListing(Blueprint):
    
    name = 'code-source-listing'
    family = 'Code'
    display_name = 'Source Listing'
    description = 'This scrap allows you to write preformatted <code> \
        elements in a syntax-highlighted text editor.'
    fields = {
        'code': forms.CharField(
            widget = forms.Textarea(
                attrs = {
                    'id':'code_editor',
                    'class':'monospaced'
                }
            ),
            label = "Code",
            help_text = "Enter the source code you want to appear within the \
                scrap",
            initial = "print \"Hello World\""
        ),
        'language': forms.ChoiceField(
            label = "Language",
            help_text = "Enter the language your code is written in. This will \
                be added to the &lt;code&gt; tag's class attribute, which can be \
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

    def render(self, scrap_data):
        output = "<pre><code class=\"" + scrap_data['language'] + \
            "\">" + scrap_data['code'] + "</code></pre>"
        return output