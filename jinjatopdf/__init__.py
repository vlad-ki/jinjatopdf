import tempfile
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
    """
    The function for convert jinja template to pdf.
    Args:
    template - the path to the jinja teplate file
    pdf - the path, where you want to save result pdf file
    context - dict with context for jinja template
    filters - mapping function name to function object for jinfa template filters

    """
    if filters:
        for filter in filters:
            jinja2.filters.FILTERS[filter] = filters[filter]

    template_obj = make_template_from_jinja(template)

    with tempfile.NamedTemporaryFile(mode='w', suffix='.html',) as file_obj:
        html = save_html_from_template(file_obj, template_obj, context, pdf)
        make_pdf_with_wkhtmltopdf(html, pdf, serviсe_opts)

        if service == 'wkhtmltopdf':
            make_pdf_with_wkhtmltopdf(html, pdf, serviсe_opts)
        elif service == 'athenapdf':
            make_pdf_with_athenapdf(html, pdf, serviсe_opts)
