from setuptools import setup, find_packages

setup(
    name='pyqt-svg-label',
    version='0.2.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt SVG icon only label',
    url='https://github.com/yjg30737/pyqt-svg-label.git',
    install_requires=[
        'PyQt5>=5.8',
        'python-get-absolute-resource-path @ git+https://git@github.com/yjg30737/python-get-absolute-resource-path.git@main'
    ]
)