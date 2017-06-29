import subprocess
import sys


def make_pdf_with_wkhtmltopdf(html, pdf, serviсe_opts=''):
    child = 'wkhtmltopdf'
    command = [child, html, pdf]

    if serviсe_opts:
        command.insert(1, serviсe_opts)

    pipe = subprocess.Popen(command, stdin=subprocess.PIPE)
    returnconde = pipe.wait()

    pipe.stdin.close()
    if returnconde != 0:
        sys.exit(returnconde)


def make_pdf_with_athenapdf(html, pdf, serviсe_opts=''):
    command = ('docker run --rm -v $(pwd):/converted/arachnysdocker/athenapdf'
               ' athenapdf {0} {1} {2}'.format(serviсe_opts, html, pdf))

    pipe = subprocess.Popen(command, stdin=subprocess.PIPE, shell=True)
    returnconde = pipe.wait()

    pipe.stdin.close()
    if returnconde != 0:
        sys.exit(returnconde)
