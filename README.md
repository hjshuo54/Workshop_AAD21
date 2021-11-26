# Robotic 360° Light Painting Workshop

at Department of Architecture, National Cheng Kung University (NCKU), Taiwan


## Workshop Team

* ChiaChing Yen
* Jia Shao Hsu
* Wai Ting Hsiao


## Workshop Description

This workshop will introduce parametric tools and produce 360° light drawings using SJSU's [UR5 robot](https://www.universal-robots.com/e-series/) and an [Insta360](https://www.insta360.com/) camera. The workshop will focus on two areas:

* Generative Design

    Using a combination of Rhino, Grasshopper and custom python tools, you will learn how to develop a parametric workflow to explore an infinite number of variations of a light design. We will provide you with a visualisation tool to anticipate how your 360° light drawing will look like.

* Robotic Light Drawing

    We will bring custom-made light tools for different light *strokes* to create the 360° light paintings. You will test different light tools, learn how to automate tasks and plan for safe robot motions. 


## Light Tools

We will bring different light tools with different attachments that allow you to control your light *stroke*. This can range from a single point to a line to diffused light. We will provide tools that allow you to easily adjust the light intensity and colour.

## Outcome
* 360° image to view in a browser
* picture for exhibition
* video of creation

## Schedule

### Part I: Introduction to Python / COMPAS
Saturday, 27th, Nov, 2021
09:00 - 17:00 AM GMT+8


### Part 2: Introduction to Robotics / ROS
Sunday, 27th, Nov, 2021
09:00 - 17:00 AM GMT+8


# Files

We will share the main tools and files via this repository.


# Platforms

## Software

### Rhino

We will be using Rhino as the primary platform. 
If you don't have it already, you can download a 90-day free evaluation version of Rhino 7 here:

* [Windows 90-day Evaluation](https://www.rhino3d.com/download/rhino-for-windows/evaluation)

* [MacOS 90-day Evaluation](https://www.rhino3d.com/download/rhino-for-mac/evaluation)

### Grasshopper

[Grasshopper](https://www.rhino3d.com/features/#grasshopper) is a plugin for Rhino, and as of version 7, is installed by default in both the Mac and Windows versions. To open Grasshopper within Rhino, simply type "Grasshopper" in the command line or click the Grasshopper icon in the Standard toolbar (second from far right, green circle with insect).


### Anaconda 3

We use Anaconda to make sure Python and all required libraries are installed correctly on all platforms. Please use the following download to install it:

* [Anaconda Individual Edition](https://www.anaconda.com/products/individual)

### Visual Studio Code

Most of the examples will be used from Rhino/Grasshopper, but the option to use them as stand alone scripts might create more opportunities. For that reason, we recommend installing the free code editor Visual Studio Code along with its Python extension:

* [VS Code](https://code.visualstudio.com/)
* [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)



## Installation

We use `conda` to make sure we create a clean, isolated coding environment:

### Get the workshop files

    (base) conda activate AAD21
    (AAD21) git clone https://github.com/

### Add COMPAS to Rhino

    (AAD21) python -m compas_rhino.install -v 7.0
