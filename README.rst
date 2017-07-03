Welcome to "JINJATOPDF" application
===================================

Description
-----------
The application "jinjatopdf" converting jinja template to pdf document
with considering context, wich send to application in .yaml file.
It very easy to use. For the begining needs to satisfy some dependencies.

Dependencies
------------
"jinjatopdf" use functional of two application:

#.  `wkhtmltopdf <https://wkhtmltopdf.org/>`_
#.  `athenapdf <https://github.com/arachnys/athenapdf/blob/master/cli/docs/quick-start.md>`_

You must install and use one of them or both.

Usage
-----
How to send context with .yaml file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you do not know - what is it yaml file, you can `reed the docs <http://yaml.org/>`_

For send simple types - use *context* key.

**Example**:

.. code-block:: yaml

    context: 
        name: name
        list:
            - 1
            - 2
            - 3
            - 5
        map:
            value: mapvalue


If you need to send filters to jinja template - use *filters* key.

**Example**:

.. code-block:: yaml

    filters:
        filter_function_name: package.module


And the same with *functions*.

**Example**:

.. code-block:: yaml
    
    functions:
        function_name: package.module


If you want to send for child service a fixed arguments - you can do it very easily with yaml context.

    **Example**

    .. code-block:: yaml

        wkhtmltopdf:
            - -q
            - -g

        athenapdf:
            - --no-portrait



Quick start
~~~~~~~~~~~
.. code-block:: bash

    $pip install jinjatopdf
    $jinjatopdf <template_filepath> <pdf_filepath> <yaml_filepath>