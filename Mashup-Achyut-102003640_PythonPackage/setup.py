from distutils.core import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name = 'Mashup-Achyut-102003640',
  packages = ['Mashup-Achyut-102003640'],
  version = '0.0.2',      
  license='MIT',        
  description = 'This package will allow user to create mashup of audios which are extracted from youtube videos requested singer',
  long_description=long_description,
  long_description_content_type='text/markdown',   
  author = 'Achyut Tiwari',                   
  author_email = 'achyuttiwari22@gmail.com',      
  url = 'https://github.com/Achyut22/Mashup-Achyut-102003640',
  keywords = ['MASHUP', 'YOUTUBE', 'PROJECT', 'UCS654','MUSIC','MP3'],   
  install_requires=[           
          'pytube',
          'pydub',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)