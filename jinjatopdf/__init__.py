from os import remove
from time import sleep
from jinja2 import filters
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
    costom_filters,
    service='wkhtmltopdf',
    serviсe_opts='',
):

    if costom_filters:
        for filter in costom_filters:
            filters.FILTERS[filter] = costom_filters[filter]

    template_obj = make_template_from_jinja(template)
    html = save_html_from_template(template_obj, context, pdf)
    make_pdf_with_wkhtmltopdf(html, pdf, serviсe_opts)

    if service == 'wkhtmltopdf':
        make_pdf_with_wkhtmltopdf(html, pdf, serviсe_opts)
    elif service == 'athenapdf':
        make_pdf_with_athenapdf(html, pdf, serviсe_opts)

    sleep(3)
    remove(html)
