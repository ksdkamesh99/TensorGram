import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tensorgram",
    version="0.0.1",
    author="Sai Durga Kamesh Kota",
    author_email="ksdkamesh99@gmail.com",
    description="A realtime remote service to get the keras callbacks to the telegram including the details of metrics ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ksdkamesh99/TensorGram",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=["tensorgram"],
    package_dir={'':'src'},
    
)
