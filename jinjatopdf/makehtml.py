from sys import path as sys_path
from zope.dottedname.resolve import resolve
from os.path import(
    isabs,
    basename,
    dirname
)

from jinja2 import Template, filters
from yaml import load


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


def add_filters(yaml_filepath):
    data = make_data_from_yaml(yaml_filepath)
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
