from setuptools import setup, find_packages

setup(	name='wolfgang', version='0.1',
		description='CI/CD Example',
		url='https://github.com/yoon-gu/ci-cd/',
		author='Yoon-gu Hwang',
		author_email='yz0624@gmail.com',
		license='MIT',
		packages=find_packages(),
		install_requires=[
			'numpy',
		],
		include_package_data=True,
		zip_safe=False)