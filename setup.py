from setuptools import setup

setup(name='tableprinter',
      version='0.1',
      description='Yet another python table printer. This one outputs your tables to HTML, LaTeX and ASCII. It can deal with hierarchical rows / columns, output in color, ...',
      url='https://github.com/tinloaf/tableprinter',
      author='Lukas Barth',
      author_email='pypi@mbox.tinloaf.de',
      license='MIT',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='pretty-printing printing table tabular',
      packages=['tableprinter'],
      include_package_data=True,
      zip_safe=False)