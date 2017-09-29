import os
from latex.build import PdfLatexBuilder
from django.http import HttpResponse
from io import BytesIO

from datetime import datetime

#latex document template
DOCUMENT = """
\\documentclass{{article}}
\\begin{{document}}
The current time is {}.
\\end{{document}}
"""

# view for downloading a simple PDF
def download_pdf(request):

    data = DOCUMENT.format(datetime.now())

    # Looks for a latex installation in the normal location
    builder = PdfLatexBuilder(pdflatex=os.path.join(os.path.sep, 'usr', 'local', 'texlive', '2017', 'bin', 'x86_64-linux', 'pdflatex'))
    if not builder.is_available():
        raise RuntimeError('No available builder could be instantiated. '
                'Please make sure LaTeX is installed.')
    pdf = builder.build_pdf(data)

    s = BytesIO(bytes(pdf))
    y = s.getvalue()

    response = HttpResponse(y, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="current_time.pdf"'

    return response
