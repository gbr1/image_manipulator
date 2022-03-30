from setuptools import setup

package_name = 'image_manipulator'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
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
