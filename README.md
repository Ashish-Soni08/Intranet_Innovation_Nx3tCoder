# Intranet Innovation: Empowering staff for enhanced citizen services 

The [Project](https://n3xtcoder.org/intranet-innovation-empowering-staff-for-enhanced-citizen-services) is organised by the City of Moers and [N3XTCODER](https://n3xtcoder.org/).

## Description

As the administration of the City of Moers seeks to meet the evolving needs of its approximately 104,000 residents, the municipal intranet emerges as a pivotal platform for information dissemination and management. Improving the intranet is essential for enhancing the productivity and satisfaction of municipal employees, which in turn will lead to faster, more efficient, and effective services for the citizens of Moers. The challenge is to transform the municipal intranet into a more user-friendly, interactive, and intelligent platform that excels in understanding and generating answers, thereby improving the administration's knowledge base and search capabilities.

**GOAL:** Improve municipal intranet search experience
**Objective:** Optimise the intranet search capabilities, leading to faster and more precise information retrieval for increased productivity and enhanced value of the intranet as a central communication medium to optmize the performance and satisfaction of administrative staff.
**Metric:** Projected acceptance rate of search results.

### Impacted People

1. **780** Municipal Workers
2. **106241** citizens in the city of Moers
3. More than *800* sections published in the city intranet

## Environment Setup

```bash
# python version -> 3.10.13
python -V 

# create a environment named -> google-ai
python -m venv intranet-ai

# activate the environment
source intranet-ai/bin/activate

# create a Jupyter Notebook kernel
pip install jupyter
pip install ipykernel

# add your virtual environment as a kernel
python -m ipykernel install --user --name=intranet-ai --display-name="Py3.10-intranet-ai"

# verify kernel installation
jupyter kernelspec list

```

### Download Data

```bash

pip install gdown

# download the zip file from the google drive
gdown <Link to the zip file in the google drive >

# unzip Data
unzip v2-20240508T101819Z-001.zip
```
