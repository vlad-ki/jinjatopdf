import sys
from argparse import ArgumentParser

from . import jinja_to_pdf, BadServiceError
from .html import make_data_from_yaml, parse_filters


def main():
    opts = parse_options()
    data = make_data_from_yaml(opts.yaml)
    context = data.get('context', {})
    filters = parse_filters(data.get('filters', {}))
    functions = parse_filters(data.get('functions', {}))

    try:
        err, returncode = jinja_to_pdf(template=opts.template,
                                       pdf=opts.pdf,
                                       context=context,
                                       filters=filters,
                                       functions=functions,
                                       service=opts.service,
                                       serviсe_opts=opts.service_opts)

    except BadServiceError:
        sys.stderr.write('\nError! No such service "{}"\n'.format(opts.service))
        sys.exit(1)

    if returncode != 0:
        sys.stderr.write(
            'The child application "{}" return error:\n{}'.format(opts.service, err))
        sys.exit(1)


def parse_options():
    parser = ArgumentParser()

    parser.add_argument(
        'template', type=str,
        help=("Path to template file."
              " Can be 'package.subpackage:/path_inside_module'"),
    )
    parser.add_argument(
        'pdf', type=str,
        help="The path, where do you want to save result file",
    )
    parser.add_argument(
        'yaml', type=str,
        help="The path to yaml file with context",
    )
    parser.add_argument(
        '-s', '--service', type=str, default='wkhtmltopdf',
        help=("Name of converter service to use."
              " It may be 'wkhtmltopdf' or 'athenapdf'. Default it is 'wkhtmltopdf'"),
    )

    parser.add_argument(
        '-o', '--service-opts', dest='service_opts', type=str, default='',
        help='Main options of service',
    )

    opts = parser.parse_args()

    return opts

if __name__ == '__main__':
    main()
