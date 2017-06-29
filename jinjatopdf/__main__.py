import sys
from argparse import ArgumentParser

from .html import (
    make_data_from_yaml,
    parce_filters,
)
from .__init__ import jinja_to_pdf


def main():
    opts = parse_options()
    data = make_data_from_yaml(opts.yaml)
    context = data['context']
    filters = parce_filters(data.get('filters', None))

    try:
        jinja_to_pdf(
            opts.template, opts.pdf, context,
            filters, opts.service, opts.service_opts
        )
    except ValueError:
        sys.stderr.write('\nError! No such service "{}"\n'.format(opts.service))
        sys.exit(1)


def parse_options():
    parser = ArgumentParser()

    parser.add_argument(
        'template', type=str,
        help='Path to template file. Can be "package.subpackage:/path_inside_module')
    parser.add_argument(
        'pdf', type=str, help='The path, where do you want to save result file')
    parser.add_argument(
        'yaml', type=str, help='The path to .yaml file with context')
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
