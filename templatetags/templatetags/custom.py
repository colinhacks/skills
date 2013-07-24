from django import template
import datetime

register = template.Library()

#Example custom filter
def cut(value, arg):     
    #"Removes all values of arg from the given string"     
    return value.replace(arg, '')

#Example custom tag
def do_current_time(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, format_string = token.split_contents()
    except ValueError:
        msg = '%r tag requires a single argument' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)
    return CurrentTimeNode(format_string[1:-1])

class CurrentTimeNode(template.Node):
    def __init__(self, format_string):
        self.format_string = str(format_string)

    def render(self, context):
        now = datetime.datetime.now()
        context['current_time'] = now.strftime(self.format_string)
        # current time can be referenced like {{current_time}}
        return now.strftime(self.format_string)

#example of tag with contents
#changes all text between {% upper %} and {% endupper%} to uppercase
def do_upper(parser, token):
    nodelist = parser.parse(('endupper',))
    parser.delete_first_token()
    return UpperNode(nodelist)

class UpperNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context)
        return output.upper()

# Simple_tag shortcut
def current_time(format_string):
    try:
        return datetime.datetime.now().strftime(str(format_string))
    except UnicodeEncodeError:
        return ''

# Inclusion tags (with decorator syntax)
# Can only be used in a ocntext w/ variables 'home_link' and 'home_title'
@register.inclusion_tag('link.html', takes_context=True)
def jump_link(context):
    return {
        'link': context['home_link'],
        'title': context['home_title'],
    }

def books_for_author(author):
    books = Book.objects.filter(authors__id=author.id)
    return {'books': books}

# link.html
'''
Jump directly to <a href="{{ link }}">{{ title }}</a>.
'''

# book_snippet.html
'''
<ul>
{% for book in books %}
    <li>{{ book.title }}</li>
{% endfor %}
</ul>
'''


register.filter('cut', cut)
register.tag('current_time', do_current_time)
register.tag('upper',do_upper)
register.simple_tag(current_time)
register.inclusion_tag('book_snippet.html')(books_for_author)
