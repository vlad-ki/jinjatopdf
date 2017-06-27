from sys import path as sys_path
from zope.dottedname.resolve import resolve
from os.path import(
    isabs,
    basename,
    dirname
)

from jinja2 import Template
from yaml import load


def parse_filepath(filepath):
    if ':' in filepath:
        module = filepath[:filepath.find(':')]
        filepath_to_module = resolve(module).__file__
        path = filepath[(filepath.find(':') + 1):]
        filepath = ''.join((filepath_to_module, path))

    return filepath


def make_data_from_yaml(yaml):
    with open(yaml) as stream:
        return load(stream)


def parce_filters(costom_filters):
    if costom_filters is None:
        return None

    for filter in costom_filters.keys():
        if isabs(costom_filters[filter]):
            sys_path.append(dirname(costom_filters[filter]))
            resolve(basename(costom_filters[filter]))
            costom_filters[filter] = resolve('.'.join((basename(costom_filters[filter]), filter)))
            sys_path.pop()
        else:
            costom_filters[filter] = resolve('.'.join((costom_filters[filter], filter)))

    return costom_filters


def make_template_from_jinja(template):
    template = parse_filepath(template)
    with open(template) as template_file:
        return Template(template_file.read())


def save_html_from_template(template_obj, context, pdf):
    html = pdf[:pdf.rfind('.')] + '.html'
    html_obj = template_obj.render(context)

    with open(html, 'w') as html_file:
        html_file.write(html_obj)
    return html
