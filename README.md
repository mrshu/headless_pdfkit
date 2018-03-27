Headless PDFKit
===============

The PDFKit package makes use of `wkhtmltopdf`, which in turn needs an X Server
to run. In Debian land, this generally requires `xvfb-run` wrapper.

The `headless_pdfkit` package tries to make the [hotfix](https://github.com/JazzCore/python-pdfkit/issues/56#issuecomment-305593936)
proposed by [jakewins](https://github.com/jakewins) a bit easier to work with.

Installation
------------

    pip install headless-pdfkit

Examples
--------

Save a simple PDF from string.

    ret = headless_pdfkit.generate_pdf('<html></html>')
    with open('output.pdf', 'wb') as w:
        w.write(ret)


