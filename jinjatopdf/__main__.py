from argparse import ArgumentParser

from .html import (
    make_data_from_yaml,
    add_filters,
)
from .__init__ import make_jinja_to_pdf


def main():
    opts = parse_options()
    data = make_data_from_yaml(opts.yaml_filepath)
    if data['filters']:
        add_filters(data)

    make_jinja_to_pdf(
        opts.template_filepath, opts.pdf_filepath, data, opts.service, opts.service_opts)


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
        '-s', '--service', type=str, default='wkhtmltopdf',
        help='''Name of converter service to use. It may be "wkhtmltopdf" or "athenapdf".\
Default it is "wkhtmltopdf"''')
    parser.add_argument(
        '-o', '--service-opts', dest='service_opts', type=str, default='',
        help='Main options of service')

    opts = parser.parse_args()

    return opts

if __name__ == '__main__':
    main()