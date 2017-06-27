from os import remove
from time import sleep
from .html import (
    make_template_from_jinja,
    save_html_from_template,
)
from .pdf import (
    make_pdf_with_wkhtmltopdf,
    make_pdf_with_athenapdf
)

def make_jinja_to_pdf(template_filepath, pdf_filepath, data, service='wkhtmltopdf', serviсe_opts=''):
    template = make_template_from_jinja(template_filepath)
    html_filepath = save_html_from_template(template, data, pdf_filepath)
    make_pdf_with_wkhtmltopdf(html_filepath, pdf_filepath, serviсe_opts)

    if service == 'wkhtmltopdf':
        make_pdf_with_wkhtmltopdf(html_filepath, pdf_filepath, serviсe_opts)
    elif service == 'athenapdf':
        make_pdf_with_athenapdf(html_filepath, pdf_filepath, serviсe_opts)

    sleep(3)
    remove(html_filepath)
