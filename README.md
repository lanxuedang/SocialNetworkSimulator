# SocialNetworkSimulator
Currently, social media has been playing an important role in the process of information diffusion. Exploring the pattern of message propagation on social network help us better prepare for natural disasters or human crises. So, we developed models, algorithms, and tools to generate simulated networks, analyze simulated networks, and simulate information diffusion on social network over time. This software provides the following functions: (1) Simulated social network generators. This network generator is designed to generate networks with different configuration, such as Random network, Full network, Circle Network, Prefattached network, SmallWord network, and so on. (2) Network analysis. Network analysis was designed to explore the characteristics of a network. Now this module can be used to analysis characters of network and nodes of network.  (3) Community detection. In this tool, we integrated two algorithms for community detection, including CNM (Clauset-Newman-Moore community detection) and GN (Girvan-Newman community detection).  (4) Simulating information diffusion on simulated network. In this module, we implemented two information diffusion models, independent cascade model (IC model) and linear threshold model (LT model).  (5) Case study. This module provides functions to conduct case study.  (6) Data preprocessing. Because there are some functions may need you load your data that organized as a special format. This module help user prepare data for further use.

Environment Requirements

1.1Installation
Before the code is being used some installation is required so errors can be avoided. All the packages locate in the folder named softwares_and_packages.
1) Python 2.7 64 version is required.
  a. Double click python-2.7.13.amd64.msi to install python 2.7 64 version.
  b. Follow steps below to set the path variables in the environment variables.
     (1) Right-click This PC, and then click Properties.
     (2) Click Advance system setting.
     (3) Click Environment variables.     
     (4) Go to the above location and change the Path variable.
     (5) If you install python at C:\Python27, add the following paths to Path variable. Otherwise you need to change the path according your actual path.
      i. C:\Python27\
      ii. C:\Python27\Lib\
      iii. C:\Python27\Scripts\
    This gives the user the access to use all the scripts available in python from command prompt. It will let the user fire the pip command from the command prompt.
2) Double click PyQt4-4.11.4-gpl-Py2.7-Qt4.8.7-x64.exe to install PyQt package.
3) Double click vcredist_x64.exe to install it.
4) Install module numpy, matplotlib, Snap, and xlrd.

      a. Open command prompt and change path to the location where packages are. Here you are supposed to extract the tool file to C:\SocialNetworkSimulator. Use the command: 
      cd C:\SocialNetworkSimulator\softwares_and_packages to change the path.
 
      b. Execute the following commands using command prompt.
         Pip install numpy-1.13.1-cp27-none-win_amd64.whl
         Pip install matplotlib-2.0.2-cp27-cp27m-win_amd64.whl
         Pip install snap-4.0.0-4.0-Win-x64-py2.7.zip

1.2 Start

To start this software, please use the command for command prompt, for example, Python C:\SocialNetworkSimulator\ SocialNetworkSimulator.py
