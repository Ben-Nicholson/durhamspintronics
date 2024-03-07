# Durham Spintronics Group
A collection of instrument control and analysis tools for the Spintronics group at Durham University.

## Installation
Currently, this package is only installable using ```pip```. You can still install this pacakge within the anaconda environment, however, you must use ```pip install```, not ```conda install```.
```
pip install durhamspintronics
```
Once installed, there are several differnt sub-modules.

### Instruments
```durhamspintronics.instruments``` contains a variety of class objects, each of which provides a user friendly wrapper for various instruments. The instruments are sorted by manufacturer. Currently included devices:
* ```ni.NI_pci6713``` National Instruments analogue output device.
* ```ni.NI_PCI6034E``` National Instruments analogue input device.
* ```newport.ESP300``` Newport motion controller, model ESP300.

### Experiments
```durhamspintronic.experiments``` contins the class objects for the various experiements, such as the sotmoke. These classes combine the aforementioned instrument classes to create one object to control your experiment.
* ```sotmoke``` Various experiment classes for running hysteresis loops which are field driven, current driven, or a combination of both.
### Data Loaders
```durhamspintronics.dataloader``` contains class objects for loading the result files from various experiments.

### Anaylsis
```durhamspintronics.analysis``` contains anaylsis methods, sorted by measurement type.

### General
```durhamspintronics.general``` contains an unsorted, yet useful, set of functions.
* ```get_symbols()``` prints a list of common symbolts along which the respective chr() values.
* ```format_uncertainty(value, error)``` Returns a nicely formatted string in the form of "value ± error".
* ```GenerateSampleDiagram``` A tool for quickly generating sample diagrams for presentations and reports.
