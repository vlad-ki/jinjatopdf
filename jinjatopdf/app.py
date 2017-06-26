from sys import path as sys_path
from os.path import isabs, basename, dirname
from os import remove
import subprocess
from zope.dottedname.resolve import resolve
from optparse import OptionParser
from jinja2 import Template, filters
from yaml import load
from time import sleep


def main():
    opts = parse_options()
    if make_data_from_yaml(opts.yaml_filepath)['filters']:
        add_filters(opts)

    data = make_data_from_yaml(opts.yaml_filepath)
    template = make_template_from_jinja(opts.template_filepath)
    html_filepath = save_html_from_template(template, data, opts.pdf_filepath)

    if opts.serviсe == 'wkhtmltopdf':
        make_pdf_with_wkhtmltopdf(opts, html_filepath)
    elif opts.serviсe == 'athenapdf':
        make_pdf_with_athenapdf(opts, html_filepath)

    sleep(3)
    remove(html_filepath)


def parse_options():
    parser = OptionParser(usage='\njinjatopdf [options] template_filepath\
 pdf_filepath yaml_filepath\n\n\
    template_filepath - Path to template file. Can be "package.subpackage:/path_inside_module"\n\
    pdf_filepath - The path, where do you want to save result file" \n\
    yaml_filepath - The path to .yaml file with context')
    parser.disable_interspersed_args()

    parser.add_option(
        '-s', '--serviсe', dest='serviсe', type='str',
        help=('''Name of converter serviсe to use. It may be "wkhtmltopdf" or "athenapdf".\
Default it is "wkhtmltopdf"'''))
    parser.add_option(
        '-o', '--serviсe-opts', dest='serviсe_opts', type='str',
        help=('Main options of serviсe'))
    parser.set_defaults(
        serviсe='wkhtmltopdf',
        serviсe_opts='',
    )
    opts, args = parser.parse_args()
    setattr(opts, 'template_filepath', args[0])
    setattr(opts, 'pdf_filepath', args[1])
    setattr(opts, 'yaml_filepath', args[2])

    return opts


def parse_filepath(filepath):
    if ':' in filepath:
        module = filepath[:filepath.find(':')]
        filepath_to_module = resolve(module).__file__
        path = filepath[(filepath.find(':') + 1):]
        filepath = ''.join((filepath_to_module, path))

    return filepath


def make_data_from_yaml(yaml_filepath):
    with open(yaml_filepath) as stream:
        return load(stream)


def add_filters(opts):
    data = make_data_from_yaml(opts.yaml_filepath)
    for filter in data['filters'].keys():
        if isabs(data['filters'][filter]):
            sys_path.append(dirname(data['filters'][filter]))
            resolve(basename(data['filters'][filter]))
            filters.FILTERS[filter] = resolve('.'.join((basename(data['filters'][filter]), filter)))
            sys_path.pop()
        else:
            filters.FILTERS[filter] = resolve('.'.join((data['filters'][filter], filter)))


def make_template_from_jinja(template_filepath):
    template_filepath = parse_filepath(template_filepath)
    with open(template_filepath) as template_file:
        return Template(template_file.read())


def save_html_from_template(template, data, pdf_filepath):
    html_filepath = pdf_filepath[:pdf_filepath.rfind('.')] + '.html'
    html_document = template.render(data['context'])

    with open(html_filepath, 'w') as html_file:
        html_file.write(html_document)
    return html_filepath


def make_pdf_with_wkhtmltopdf(opts, html_filepath):
    child = 'wkhtmltopdf'
    command = [child, html_filepath, opts.pdf_filepath]

    if opts.serviсe_opts:
        command.insert(1, opts.serviсe_opts)

    pipe = subprocess.Popen(command, stdin=subprocess.PIPE)
    pipe.stdin.close()


def make_pdf_with_athenapdf(opts, html_filepath):
    command = 'docker run --rm -v $(pwd):/converted/\
     arachnysdocker/athenapdf athenapdf {0} {1} {2}'.format(
        opts.serviсe_opts, html_filepath, opts.pdf_filepath)

    pipe = subprocess.Popen(command, stdin=subprocess.PIPE, shell=True)
    pipe.stdin.close()
