from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='pro_video_ferramentas',
    version=1.0,
    description='Este pacote irá fornecer ferramentas de processamento de vídeo',
    long_description=Path('README.md').read_text(),
    author='Anderson',
    author_email='anderson@email.com',
    keywords=['camera', 'video', 'processamento'],
    packages=find_packages()
)