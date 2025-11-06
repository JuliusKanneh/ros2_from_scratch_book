from setuptools import find_packages, setup

package_name = 'my_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='drwise',
    maintainer_email='jkanneh@andrew.cmu.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "my_custom_node = my_py_pkg.my_custom_node:main",
            "number_publisher = my_py_pkg.number_publisher:main",
            "number_subscriber_node = my_py_pkg.number_subscriber:main",
            "hardware_status_publisher_node = my_py_pkg.hardware_status_publisher:main",
        ],
    },
)
