import os
import tempfile
import jinja2

from .html import save_html_from_template, parse_filepath
from .pdf import make_pdf_with_wkhtmltopdf, make_pdf_with_athenapdf


class BadServiceError(ValueError):
    pass


def jinja_to_pdf(template: str,
                 pdf: str,
                 context: dict,
                 filters: dict,
                 service: str='wkhtmltopdf',
                 serviсe_opts: str=''):
    """ The function for convert jinja template to pdf.
    Args:
    template - the path to the jinja teplate file
    pdf - the path, where you want to save result pdf file
    context - dict with context for jinja template
    filters - mapping function name to function object for jinfa template filters

    """
    template = parse_filepath(template)
    environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(template)),
        autoescape=jinja2.select_autoescape(['html', 'jinja2', 'xml', 'jinja'])
    )

    if filters:
        for filter in filters:
            environment.filters[filter] = filters[filter]

    template_obj = environment.get_template(os.path.basename(template))

    with tempfile.NamedTemporaryFile(mode='w', suffix='.html',) as file_obj:
        html = save_html_from_template(file_obj, template_obj, context, pdf)

        if service == 'wkhtmltopdf':
            make_pdf_with_wkhtmltopdf(html, pdf, serviсe_opts)
        elif service == 'athenapdf':
            make_pdf_with_athenapdf(html, pdf, serviсe_opts)
        else:
            raise BadServiceError("No such service '{}'".format(service))
