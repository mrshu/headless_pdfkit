Headless PDFKit
===============

The PDFKit package makes use of ``wkhtmltopdf``, which in turn needs an X Server
to run. In Debian land, this generally requires ``xvfb-run`` wrapper.

The ``headless_pdfkit`` package tries to make the `hotfix`_ proposed by
`jakewins`_ a bit easier to work with.

Installation
------------

You can install ``headless_pdfkit`` by running::

    pip install headless-pdfkit

Examples
--------

Save a simple PDF from string.::

    from headless_pdfkit import generate_pdf

    ret = generate_pdf('<html></html>')
    with open('output.pdf', 'wb') as w:
        w.write(ret)

Save a simple PDF from string while passing the `--auto-servernum`_
parameter to ``xvfb-run``.::

    options = {
        'auto_servernum': ''
    }

    ret = generate_pdf('<html></html>', options=options)
    with open('output.pdf', 'wb') as w:
        w.write(ret)


.. _hotfix: https://github.com/JazzCore/python-pdfkit/issues/56#issuecomment-305593936
.. _jakewins: https://github.com/jakewins
.. _--auto-servernum: https://manpages.debian.org/testing/xvfb/xvfb-run.1.en.html#OPTIONS
