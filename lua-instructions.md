---
layout: page
title: Using Lua in OpenTX 2.0 
header: Using Lua in OpenTX 2.0
group:
---
{% include JB/setup %}

## What is Lua?
Lua is a general purpose scripting language. Support for Lua-scripting is a new feature in OpenTX 2.0. Lua-scripts are stored in text files and are loaded and unloaded whenever they are needed by the radio. The scripts are not part of the firmware. They are firmware customization options.

### Persistent scripts
Persistent scripts are loaded by the radio and run until they are no longer needed. Several scripts may be active at the same time. There is a limitation (due to RAM usage) on the number of persistent scripts. 7 is the maximum (shared by all categories). If a script uses too much memory or processor time it will be forcefully terminated.

There are three kinds of OpenTX persistent Lua scripts. Model scripts, Function scripts and Telemetry scripts. They all use the same script language, but are used in slightly different roles. 

- **Model scripts**
  A model script runs on a continuous basis once loaded into a model. As long as the model is selected, the script is running. You should never use a model script for calculating any sort of input that is vital to your model. Remember that scripts may be terminated at any time. 

- **Function scripts (new in 2.0.3)**
  Scripts that can be called from the Special Functions screen. Much like the available firmware functions.  

- **Telemetry scripts (planned for 2.0.4)**
  Used for building customized telemetry screens. Theoretically it is possible to have up to 7 custom telemetry screens, all written in Lua. It is possible to use different scripts on a per model basis.

### One time scripts

These scripts start when called upon by a specific radio function or when the user selects them from a contextual menu. They do their task and are then terminated and unloaded.
Please note that all persistent scripts are halted during the execution of one time scripts. They are automatically restarted once the one time script is finished. This is done to provide enough system resources to execute the one time script.

- **The model wizard script**
  This scripts adds a wizard function to the radio that provides guidance in setting up models. Once installed it is called automatically when a model is created.

- **Template scripts (planned for 2.0.5)**
  Functionality not yet described.


### Folder structure
The script folders have been reorganized in OpenTX 2.0.3. The folder structure looks like this:

* /SCRIPTS/WIZARD/ - For the Wizard script
* /SCRIPTS/MIXES/ - For model scripts
* /SCRIPTS/FUNCTIONS/ - For function scripts
* /SCRIPTS/<<modelname>>/telemXX.lua - For telemetry scripts
* /SCRIPTS/TEMPLATES/ - For template scripts 

More folders may be added over time. 

### Make your own scripts
The scripts are text files. Anyone can edit them and change how they work. If you would like to try this there is a section in the OpenTX development wiki that will be helpefull:

[Wiki Link](https://github.com/opentx/opentx/wiki/Lua-scripting-in-OpenTX)

The easiest way to develop scripts is to first test them in the OpenTX Taranis simulator. When things seem to work as far as the simulator goes, you transfer the scripts to the radio and test them there.
