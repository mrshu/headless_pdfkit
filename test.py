import headless_pdfkit


options = {
    'quiet': ''
}

with open('tests/fixtures/example.html') as f:
    s = f.read()
    ret = headless_pdfkit.generate_pdf(s, options=options)
    with open('output.pdf', 'wb') as w:
        w.write(ret)
