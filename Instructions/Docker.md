# 🐳 How to Install Docker on Windows
The instructions are inspired by: https://youtu.be/bw-bMhlhcpg?si=q8gUtxmWBVMBNhHm 

## Install Docker Desktop

- Visit `https://docs.docker.com/`
- Press `Get Docker` to navigate to this page `https://docs.docker.com/get-started/get-docker/`
- Press `Docker Desktop for Windows`
- Press the first option `Docker Desktop for Windows -x86_64`
- As you wait for it to download go to the next step...


## Set the System Requirements

### Install Windows System for Linux (WSL)
- Open `cmd` and type `wsl` and click enter
- If you see a response, then it is installed
- If not, type `wsl --install` and click enter

### Check Version of OS
- Press the "windows key + r" and type `wiver` and press enter
- You are fine, if the Version is:
    * for Windows 11: 22H2 or higher
    * for Windows 10: 22H2 (build 19045) or higher


### Turn WSL 2 feature on Windows
- Go to the search bar of your pc and type `Turn Windows features on or off`
- Ensure that `Windows Subsystem for Linux` is checked and click OK (if asked click Don't restart)

### Check visualization on your system
- Press "ctrl + shift + esc"
- Go to the "Performance" tab and click "CPU"
- Check whether the "Visualization" is Enabled
- If it not, go to the search bar of your pc and type `Turn Windows features on or off` and try checking "Virtual Machine Platform"


## Continue with Installation
- Go to the .exe file you downloaded and double click it
- If you want, check "Add shortcut to desktop" and click OK
- When the message "Installation succeeded", press the button

## Set up
- Open "Docker Desktop"
- Press `Accept`
- Press `Skip` to the next 2 questions and wait...


# How to Set up Dockerhub

## Create Dockerhub account
- Visit `https://hub.docker.com/`
- Press `Sign up` if you do not have an account already
- Suggest signing up with Github or Google (You can then sign in to Docker Desktop using that Docker Hub account)

## Create a repository
- Press `Create a repository`
- Give it a name (e.g, devops) and make it public!!! (IMPORTANT so we can find it and assess you!)
