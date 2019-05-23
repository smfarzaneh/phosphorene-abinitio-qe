# phosphorene-abinitio-qe
Ab initio calculation of electronic band structure of phosphorene using Quantum ESPRESSO with Python post processing


## How to run
#### 1. Clone the repository and change directory. 
```
git clone https://github.com/smfarzaneh/phosphorene-abinitio-qe.git
cd phosphorene-abinitio-qe/
```
#### 2. Edit `qe-path` file and set the path to your Quantum ESPRESSO directory.
```
#!/bin/sh

QE_PATH=$HOME/code/espresso6.0  # replace with your QE path 
```
#### 3. Run relevant *shell* files.

* Calculates band structure in the absence of spin orbit coupling. The output is written in `out/non-relativistic`.
```
. run-non-relativistic 
```

* Calculates band structure in the presence of spin orbit coupling. The output is written in `out/relativistic`.
```
. run-relativistic
```

* Calculates the expectation value of spin over the elliptic constant energy contours in the presence of spin orbit coupling and external electric field. The output is written in `out/contour`. To change the amplitude of the electric field you can modify `efield_amp` variable in `run-contour` file.
```
. run-contour 
```

