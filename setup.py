from setuptools import setup, find_packages

setup(
    name="make_question_google_gemini_api",
    version="0.1",
    packages=find_packages(),
    author="Danilo",
    author_email="contact@danilocgsilva.me",
    install_requires=[
        "make_question_interface @ git+https://git@github.com/danilocgsilva/make_question_interface.git@1.2.0#egg=make_question_interface"
    ],
    description="Implements a question-making function using Google Gemini API.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

