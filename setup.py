from setuptools import setup
def readme():
    with open('README.md') as f:
        README = f.read()
    return README  
setup(
  name = 'Data_Split',         
  packages = ['Data_Split_by_Bhawika'],
  version = '1.0.0',      
  license='MIT',        
  description = 'A python package to split Directory into Training, Testing and Validation Directory',
  long_description=readme(),
  long_description_content_type="text/markdown",
  author = 'BHAWIKA ARORA',                   
  author_email = 'bhawikavk2@gmail.com',  
  url = 'https://github.com/Bhawika16/Data_Split',   # Provide either the link to your github or to your website
  include_package_data=True,    
  classifiers=[
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
  entry_points={
        "console_scripts": [
            "train_test_split=Data_Split_by_Bhawika.split_train_validation:main",
        ]
    },
)