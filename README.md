# Durham Spintronics Group
A collection of instrument control and analysis tools for the Spintronics group at Durham University.

## Installation
Currently, this package is only installable using ```pip```. You can still install this pacakge within the anaconda environment, however, you must use ```pip install``` an not ```conda install```.
```
pip install durhamspintronics
```
Once installed, there are several differnt sub-modules.

### Instruments
```durhamspintronics.instruments``` contains a variety of ```class``` objects, each of which provides a user friendly wrapper for various instruments. The instruments are sorted by manufacturer.

### Experiments
```durhamspintronic.experiments``` contins the ```class```objects for the various experiements, such as the sotmoke. These classes combine the aforementioned instrument classes to create one object to control your experiment.

### Data Loaders
```durhamspintronics.dataloader``` contains ```class``` objects for loading the result files from various experiments.

### Anaylsis
```durhamspintronics.analysis``` contains anaylsis methods, sorted by measurement type.

### General
```durhamspintronics.general``` contains an unsorted, yet useful, set of functions.
