from setuptools import setup, find_packages

setup(
    name='django-kana',
    version='0.1',
    description='Django helper for handling Japanese text',
    long_description=open('README.md', 'r').read(),
    keywords='django hiragana katakana romaji japanese',
    author='Olof Sjöbergh',
    author_email='olofsj at gmail com',
    url='https://github.com/olofsj/django-kana',
    license='GPL',
    package_dir={'kana': 'kana'},
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
)

