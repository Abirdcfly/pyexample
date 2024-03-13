from setuptools import setup

setup(
    name='abirdcfly-pyexample',
    version='0.1.1',    
    description='A example Python package',
    url='https://github.com/Abirdcfly/pyexample',
    author='Stephen Hudson',
    author_email='shudson@anl.gov',    
    license='BSD 2-clause',
    packages=['abirdcfly-pyexample'],
    install_requires=['mpi4py>=2.0',
                      'numpy',
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)    
