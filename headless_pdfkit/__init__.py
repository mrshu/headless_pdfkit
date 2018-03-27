import pdfkit


class HeadlessPdfKit(pdfkit.PDFKit):
    def command(self, path=None):
        cmdlist = ['xvfb-run', '--']
        # if `auto_servernum` is in options, add the `-a` parameter which
        # should ensure that each xvfb has its own DISPLAY ID
        if 'auto_servernum' in self.options:
            cmdlist = ['xvfb-run', '-a', '--']
        return cmdlist + super().command(path)


def generate_pdf(rendered, options=None, fix_method=True):
    """Generate a PDF from a given HTML string.

    :param rendered: A string that contains HTML.
    :param options: A set of options to pass to wkhtmltopdf
    :param fix_method: Fix a long standing issue with wkhtmltopdf that does not
    like resolving methods (from things like `<a href="//test.com">Test</a>`)
    """
    if fix_method:
        rendered = rendered.replace('src="//', 'src="http://')
        rendered = rendered.replace("src='//", "src='http://")
        rendered = rendered.replace('href="//', 'href="http://')
        rendered = rendered.replace("href='//", "href='http://")
    pdf = HeadlessPdfKit(rendered, 'string',
                         options=options).to_pdf(False)
    return pdf
