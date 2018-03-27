from setuptools import setup

setup(name='headless_pdfkit',
      version='0.1.4',
      description='A headless version of pdfkit which makes use of xvfb-run',
      long_description=open('README.rst').read(),
      url='http://github.com/mrshu/headless_pdfkit',
      author='Marek Suppa (mr.Shu)',
      author_email='mr@shu.io',
      license='MIT',
      packages=['headless_pdfkit'],
      zip_safe=False)
