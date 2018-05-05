from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='Learning-Automata',
      version='0.1',
      description='A simple Reinforced Learning library implemented in Python 3.6',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License, version 2 ',
        'Programming Language :: Python :: 3.6',
        'Topic :: Artificial Intelligence :: Reinforced Learning',
      ],
      keywords='Reinforced Learning Automata',
      url='https://github.com/brandonesford/Learning-Automata',
      author='Brandon Esford',
      author_email='brandonesford@gmail.com',
      license='GPL-2.0',
      packages=['Learning-Automata'],
      install_requires=[
          'numpy',
          'scipy'
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['Learning-Automata=learning.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)