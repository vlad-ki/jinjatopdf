import os
import time
import jinja2
from .html import (
    make_template_from_jinja,
    save_html_from_template,
)
from .pdf import (
    make_pdf_with_wkhtmltopdf,
    make_pdf_with_athenapdf
)


def jinja_to_pdf(
    template,
    pdf,
    context,
    filters,
    service='wkhtmltopdf',
    serviсe_opts='',
):

    if filters:
        for filter in filters:
            jinja2.filters.FILTERS[filter] = filters[filter]

    template_obj = make_template_from_jinja(template)
    html = save_html_from_template(template_obj, context, pdf)
    make_pdf_with_wkhtmltopdf(html, pdf, serviсe_opts)

    if service == 'wkhtmltopdf':
        make_pdf_with_wkhtmltopdf(html, pdf, serviсe_opts)
    elif service == 'athenapdf':
        make_pdf_with_athenapdf(html, pdf, serviсe_opts)

    time.sleep(3)
    os.remove(html)
