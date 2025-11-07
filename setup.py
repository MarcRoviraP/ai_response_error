from setuptools import setup, find_packages

setup(
    name="ai_response_error",
    version="0.1.0",
    description="Explica errores usando Gemini AI",
    packages=find_packages(),
    install_requires=["requests"],
    python_requires=">=3.7",
)