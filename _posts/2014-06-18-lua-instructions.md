---
layout: post
title: "Using Lua Scripts in OpenTX 2.0"
description: ""
category: ""
tags: [Lua]
---
{% include JB/setup %}

## What is Lua?
Support for Lua-scripting is a new feature in OpenTX 2.0. Lua-scripts are stored in text files and are loaded and unloaded whenever they are needed by the radio. The scripts are not part of the firmware. They are rather customization options.
One limitation (due to RAM usage) is on the scripts count. 7 is the maximum (shared by all categories). 

### Lua script types
There are five kinds of of OpenTX lua scripts. One time scripts, Model scripts, Function scripts, Telemetry scripts and Template scripts. They all use the same script language, but are used in slightly different roles. 

- One time scripts

  The wizard is currently the only one time script. These scripts start when called upon by a specific radio function. They do their task and are then terminate and unloaded. 

- Model scripts

  A model script runs on a continuous basis once loaded into a model. As long as the model is selected, the script is running. If a model script uses too much memory or processor time it will be forcefully terminated. You obviously do not want to use a model script for calculating any sort of input vital to your model, since any scripting error can lead to unexpected terminations. 

- Function scripts (new in 2.0.3)

  Scripts that can be called from the Special Functions screen. Much like the available firmware functions.

- Telemetry scripts (planned for 2.0.4)

  Used for building customized telemetry screens. Theorically it will be possible to have up to 7 custom telemetry screens, all written in Lua. It is possible to use different scripts on a per model basis.

- Template scripts (planned for 2.0.5)

  These scripts will be available in a contextual menu, just like the Wizard.


### Folder structure
The script folders have been reorganized in OpenTX 2.0.3. The folder structure looks like this:

* /SCRIPTS/WIZARD/ - For the Wizard one time script
* /SCRIPTS/MIXES - For model scripts
* /SCRIPTS/FUNCTIONS/ - For function scripts
* /SCRIPTS/<<modelname>>/telemXX.lua - For telemetry screen scripts
* /SCRIPTS/TEMPLATES/ - For template scripts 
