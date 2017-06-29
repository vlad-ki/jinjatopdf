from zope.dottedname.resolve import resolve
from importlib.machinery import SourceFileLoader

import os

import jinja2
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


def parce_filters(filters):
    if filters is None:
        return None

    for filter in filters.keys():
        if os.path.isabs(filters[filter]):
            module = SourceFileLoader('module', filters[filter]).load_module()
            filters[filter] = getattr(module, filter)
        else:
            filters[filter] = resolve('.'.join((filters[filter], filter)))

    return filters


def make_template_from_jinja(template):
    template = parse_filepath(template)
    with open(template) as template_file:
        return jinja2.Template(template_file.read())


def save_html_from_template(file_obj, template_obj, context, pdf):
    html_str = template_obj.render(context)
    file_obj.write(html_str)
    file_obj.flush()
    return file_obj.name
