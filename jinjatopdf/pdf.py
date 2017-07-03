import subprocess
import os


def make_pdf_with_wkhtmltopdf(html, pdf, serviсe_opts=[]):
    child = 'wkhtmltopdf'
    command = [child, html, pdf]

    if serviсe_opts:
        for option in serviсe_opts:
            command.insert(1, option)

    pipe = subprocess.Popen(command,
                            stdout=subprocess.PIPE,
                            stdin=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    returnconde = pipe.wait()

    return pipe.stderr.read().decode('utf-8'), returnconde


def make_pdf_with_athenapdf(html, pdf, serviсe_opts=[]):
    filename = os.path.basename(html)
    command = ('docker run --rm -v $(pwd):/converted/ arachnysdocker/athenapdf '
               'athenapdf {0} /converted/{1} {2}'.format(' '.join(serviсe_opts), filename, pdf))

    pipe = subprocess.Popen(command,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=True)
    returnconde = pipe.wait()

    return pipe.stderr.read().decode('utf-8'), returnconde
