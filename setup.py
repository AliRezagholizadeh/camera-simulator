from setuptools import setup

setup(
    name='camera-simulator',
    version='0.0.2',
    description='A example Python package',
    url='https://github.com/AliRezagholizadeh/camera-simulator.git',
    author='Ali Rezagholizadeh',
    author_email='ali.rezagholizadeh.1@ens.etsmtl.ca',
    license='-',
    packages=['camera-simulator'],
    install_requires=[
                      'numpy',
                      ],

    classifiers=[
        'Development Status :: First phase',
        'Intended Audience :: A test',
        'License :: OSI Approved :: -',
        'Operating System :: POSIX :: macOS Monterey 12.0.1',
        'Programming Language :: Python :: 3.8.10',
    ],
)