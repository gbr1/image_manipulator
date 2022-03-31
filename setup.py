from setuptools import setup
from os import path

package_name = 'image_manipulator'

here = path.abspath(path.dirname(__file__))
with open(path.join(here,'requirements.txt'),encoding='utf-8') as f:
    requirements = f.read().splitlines()

setup(
    name=package_name,
    version='1.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['requirements.txt'])
    ],
    install_requires=requirements,
    zip_safe=True,
    maintainer='gbr1',
    maintainer_email='giovannididio.bruno@gmail.com',
    description='Simple image manipulation package',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'flipper = image_manipulator.flipper_node:main',
        ],
    },
)
