# Build configuration file
# https://www.sphinx-doc.org/en/master/usage/configuration.html
from datetime import date

project = u'Digital garden starter'
# author = u'example'
copyright = ('%s, %s' % (date.today().year, u'example'))
# project_copyright = u'example'
version = u'1.0'
release = u'1.0.0'
extensions = [
    'myst_parser',
    'sphinx_inline_tabs'
]
exclude_patterns = []
templates_path = ['_templates']
html_theme = 'furo'
html_title = ("% s v% s" % (project, version))
html_short_title = project
# html_logo = 'https://via.placeholder.com/50.webp'
html_favicon = 'https://via.placeholder.com/32.ico'
html_static_path = ['_static']
# html_copy_source = False
# html_show_sourcelink = False
# html_show_copyright = False
# html_show_sphinx = False
suppress_warnings = ["myst.header"]
