from setuptools import setup, find_packages
version = '0.0.1'

setup(name='open_hotelling',
      version=version,
      description=("Django application for workstation hotelling and reservations"),
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python'],
      keywords='hotelling',
      author='Shaun Duncan',
      author_email='shaun.duncan@gmail.com',
      url='http://www.github.com/shaunduncan/open-hotelling',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      )
