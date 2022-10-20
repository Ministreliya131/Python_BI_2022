# Virtual environment research

## Description
This work was inspired by Mikhail's article on exploring the possibilities of virtual environments. I offer adapted for the Ubuntu 20.04.5 LTS (64-bit) operating system instructions for installing a virtual environment to reproduce the results presented in the article.

The detailed description of the script is presented in the publication: Awesome virtual environment research. Serious Mikhail. 2022. J V Env. [doi:10.1111/1000-7](doi:10.1111/1000-7)

## Instruction
To run the script `pain.py`, follow the steps below:

### Step 0. Install conda
If you don't have conda installed, you can get it with the following commands. The last version of Anaconda for Python 3 is available [here](https://www.anaconda.com/products/distribution). 
And here you can find the great installation guide: [click meow =^.^=](https://www.digitalocean.com/community/tutorials/how-to-install-the-anaconda-python-distribution-on-ubuntu-20-04-ru)

### Step 1. Create your environment
pain.py requires Python3 version `3.10.x`
Scpecify python version while creating your environment
```
conda create -n envv python=3.10
```
Then, do not forget to activate your virtual environment!
```
conda activate envv
```

### Step 2. Get the script and it's requirements
Clone this branch with command in directory you want
```
git clone https://github.com/Ministreliya131/Python_BI_2022.git -b Modules_environments_painfull_pain_hw
```
Change your directory to `Python_BI_2022`
```
cd Python_BI_2022
```


If you still don't have git installed, you can always get it with:
```
sudo apt install git-core
```

### Step 3. Install requirements
You can install all requirements for `pain.py` by running
```
pip3 install -r requirements.txt
```
Excellent! You can run the script!
```
python3.10 pain.py
```





