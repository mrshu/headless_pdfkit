from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(name='headless_pdfkit',
      version='0.1.2',
      description='A headless version of pdfkit which makes use of xvfb-run',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='http://github.com/mrshu/headless_pdfkit',
      author='Marek Suppa (mr.Shu)',
      author_email='mr@shu.io',
      license='MIT',
      packages=['headless_pdfkit'],
      zip_safe=False)
