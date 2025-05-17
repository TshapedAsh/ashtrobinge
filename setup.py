from setuptools import setup, find_packages

setup(
    name='ashtrobinge',
    version='0.1.0',
    description='A meme-powered, ultra-fast astro data wrangling toolkit',
    author='Ash',
    author_email='your@email.com',  # <-- update this if you want
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        # 'astroquery',
        # 'matplotlib',
        # Add more as you develop
    ],
    keywords=['astronomy', 'data science', 'meme', 'astro', 'wrangling'],
    url='https://github.com/tshapedash/ashtrobinge',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Astronomy',
    ],
    python_requires='>=3.8',
)
