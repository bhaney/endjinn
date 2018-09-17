# endjinn
ML-powered multi-agent simulation toolkit

## Components

    * Main simulation runner
    * Prototypes for Agents, Actions, and Environments
    * Built-in ES solver for policy networks
    * Javascript action service
    * (Coming soon) Reporter connectors
    * (Coming soon) Real time viz server

## Quick start guide

    1. Copy the endjinnfile_proto.json file and rename it endjinnfile.json
    2. Do `python setup.py install`
    3. Edit parameters in endjinnfile.json to your liking
    4. Do `python runsim.py`

## Dependencies

    * Numpy
    * Keras (TF backend)
    * Tensorflow

See [here](https://www.tensorflow.org/install/) for instructions on how to install Tensorflow on your target OS. Note that CUDA is required.

Note on TF/CUDA: While a GPU is not required for training due to use of
Evolution Strategies solver, TF backend must be present for Keras models
to compile correctly.

## Overview & Tips

    * Main objects are Environment, Agent, and Action.
    * Each object can be sub-classed and placed in `registry_objects`
    * To use local files, edit the `local_registry.json` file
    * `local_registry.json` objects will be looked for in `local_registry_objects`. Both the registry file and the directory are ignored
    by default, so you won't end up accidentally publishing your local work to the main repo.
    * To add a global object (Action, Agent, Environment), edit the registry, make sure all files are in `registry_objects`, and do a pull request

## Roadmap

    * Global registry will eventually get moved to Endjinn Package Manager (EPM)
    * Additional Object Packs for different simulation domains will be added over time
    * Work on additional policy types and solvers is ongoing, look for periodic updates
    * OpenMPI-based distributed processing

For suggestions please start an issue. Gitter forthcoming.

## Additional Info

The wiki will be frequently updated with more in-depth guides and info. Check back periodically.
