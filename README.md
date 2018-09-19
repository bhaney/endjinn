# endjinn
ML-powered multi-agent simulation toolkit

## Components

* Main simulation runner
* Prototypes for Agents, Actions, and Environments
* Built-in ES solver for policy networks
* (Coming soon) Javascript action service
* (Coming soon) Reporter connectors
* (Coming soon) Real time viz server

## Quick start guide

1. Copy the endjinnfile_proto.json file and rename it endjinnfile.json
2. Do `python setup.py install`
3. Edit parameters in endjinnfile.json to your liking
4. Do `python runsim.py`

Note that if you don't use agents and environments which are already present in global_registry.json and have
corresponding files, you will need to place your own subclasses in local_registry_objects and ensure that their entries
in local_registry.json are complete.

`local_registry_objects/` is ignored by Git, so you may need to create the directory.

## Running Tests

`nosetests --nologcapture`

Drop nologcapture if you prefer to use nose's standard capturing. However,
note that in its standard mode it is likely to spit out a bunch of
Tensorflow log messages before proceeding to the tests.

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
