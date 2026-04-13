"""
Setup script for ChartM3 package.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_path = Path(__file__).parent / "README.md"
long_description = ""
if readme_path.exists():
    long_description = readme_path.read_text(encoding="utf-8")

# Read requirements
requirements_path = Path(__file__).parent / "requirements.txt"
requirements = []
if requirements_path.exists():
    with open(requirements_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                requirements.append(line)

setup(
    name="chartm3",
    version="1.0.0",
    author="Duo Xu, Hao Cheng, Xin Lin, Zhen Xie, Hao Henry Wang",
    author_email="xuduo@example.com",
    description="ChartM3: A Multi-Stage Code-Driven Pipeline for Constructing Multi-Dimensional and Multi-Step Visual Reasoning Data in Chart Comprehension",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Duo-Xu/ChartM3",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=23.0.0",
            "isort>=5.12.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "chartm3-topics=scripts.step1_generate_topics:main",
            "chartm3-data=scripts.step2_generate_data:main",
            "chartm3-vis=scripts.step3_generate_visualization:main",
            "chartm3-qa=scripts.step4_generate_qa:main",
            "chartm3-eval=scripts.step5_evaluate_quality:main",
            "chartm3-export=scripts.step6_export_dataset:main",
        ],
    },
    include_package_data=True,
    package_data={
        "chartm3": ["prompts/*.py"],
    },
)
