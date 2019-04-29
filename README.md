# phosphorene-abinitio-qe
Ab initio calculation of electronic band structure of phosphorene using Quantum ESPRESSO


## How to run
1. Clone the repository. 
```
git clone https://github.com/smfarzaneh/phosphorene-abinitio-qe.git
```
2. Change directory and run. 
```
cd phosphorene-abinitio-qe/
bash run
```

## Customize calculations 
To carry out calculations in the presence of spin-orbit coupling or external electric field, there are a few varialbes in the `run` file that need to be changed. 

### Spin-Orbit Coupling 
To include spin-orbit coupling in the calculation change `soc='.FALSE.'` to `soc='.TRUE.'`.

### Electric Field 
To turn on an external electric field change `efield=.FALSE.` to `efield='.TRUE.'`. The amplitude of the electric field is denoted by the variable `efield_amp`.


