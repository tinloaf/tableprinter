from setuptools import setup

setup(name='tableprinter',
      version='0.2',
      description='Yet another python table printer. This one outputs your tables to HTML, LaTeX, Unicode and ASCII. It can deal with hierarchical rows / columns, output in color, ...',
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
      project_urls={
          "Bug Tracker": "https://github.com/tinloaf/tableprinter/issues",
          "Documentation": "https://tinloaf.github.io/tableprinter/",
      },
      keywords='pretty-printing printing table tabular',
      packages=['tableprinter'],
      include_package_data=True,
      zip_safe=False)