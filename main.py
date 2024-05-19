import datetime
import os
from tempfile import NamedTemporaryFile

import pdfkit
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('main.html')

main_params = {
    'brand': 'Toyota',
    'model': 'Corolla',
    'factory_year': 2020,
    'model_year': 2021,
    'plate': 'ABC-1234',
    'color': 'Prata',
    'value': 50000.0,
}

footer_params = {
    'now': datetime.datetime.now().strftime('%d/%m/%Y às %H:%M:%S'),
}

rendered_main_html = template.render(**main_params)

# normal
# template_footer = env.get_template('footer.html')
# with open('temp_footer.html', 'w') as html_file:
#     html = template_footer.render(**footer_params)
#     html_file.write(html)

# temp file
template_footer = env.get_template('footer.html')
rendered_footer = template_footer.render(**footer_params)
with NamedTemporaryFile(delete=False, suffix='.html', mode='w') as temp:
    temp.write(rendered_footer)
    temp_footer = temp.name

options = {
    'footer-html': temp_footer,
    'encoding': 'UTF-8',
    'no-outline': None,
}

pdfkit.from_string(
    input=rendered_main_html,
    output_path='output.pdf',
    options=options,
    verbose=True,
)

# os.remove('temp_footer.html')
os.remove(temp_footer)
