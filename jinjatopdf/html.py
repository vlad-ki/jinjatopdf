from zope.dottedname.resolve import resolve
from importlib.machinery import SourceFileLoader

import os

from yaml import load


def parse_filepath(filepath):
    if ':' in filepath:
        module, path = filepath.split(':', 1)
        filepath_to_module = resolve(module).__file__
        filepath = ''.join((filepath_to_module, path))

    return filepath


def make_data_from_yaml(yaml):
    with open(yaml) as stream:
        return load(stream)


def parse_filters(filters):
    if filters is None:
        return None

    for name, func in filters.items():
        if os.path.isabs(func):
            module = SourceFileLoader('module', func).load_module()
            func = getattr(module, name)
        else:
            func = resolve('.'.join((func, name)))

    return filters


def save_html_from_template(file_obj, template_obj, context, pdf):
    html_str = template_obj.render(context)
    file_obj.write(html_str)
    file_obj.flush()
    return file_obj.name
