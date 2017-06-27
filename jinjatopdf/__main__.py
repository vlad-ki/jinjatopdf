from os import remove
from time import sleep
from argparse import ArgumentParser

from .makehtml import (
    make_data_from_yaml,
    add_filters,
    make_template_from_jinja,
    save_html_from_template,
)
from .makepdf import (
    make_pdf_with_wkhtmltopdf,
    make_pdf_with_athenapdf
)


def main():
    opts = parse_options()
    if make_data_from_yaml(opts.yaml_filepath)['filters']:
        add_filters(opts.yaml_filepath)

    data = make_data_from_yaml(opts.yaml_filepath)
    template = make_template_from_jinja(opts.template_filepath)
    html_filepath = save_html_from_template(template, data, opts.pdf_filepath)

    if opts.serviсe == 'wkhtmltopdf':
        make_pdf_with_wkhtmltopdf(html_filepath, opts.pdf_filepath, opts.serviсe_opts)
    elif opts.serviсe == 'athenapdf':
        make_pdf_with_athenapdf(html_filepath, opts.pdf_filepath, opts.serviсe_opts)

    sleep(3)
    remove(html_filepath)


def parse_options():
    parser = ArgumentParser()

    parser.add_argument(
        'template_filepath', type=str,
        help='Path to template file. Can be "package.subpackage:/path_inside_module')
    parser.add_argument(
        'pdf_filepath', type=str, help='The path, where do you want to save result file')
    parser.add_argument(
        'yaml_filepath', type=str, help='The path to .yaml file with context')
    parser.add_argument(
        '-s', '--serviсe', type=str, default='wkhtmltopdf',
        help='''Name of converter serviсe to use. It may be "wkhtmltopdf" or "athenapdf".\
Default it is "wkhtmltopdf"''')
    parser.add_argument(
        '-o', '--serviсe-opts', dest='serviсe_opts', type=str, default='',
        help='Main options of serviсe')

    opts = parser.parse_args()

    return opts

if __name__ == '__main__':
    main()
