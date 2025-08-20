# FOV & GSD Calculator

This project computes the **Field of View (FOV)** and **Ground Sampling Distance (GSD)** for a space-borne sensor based on its sensor width, focal length, and altitude.

## Formulas

The calculations use the following equations:

- $\text{FOV} = 2 \times \arctan\left(\frac{\text{sensor width}}{2 \times \text{focal length}}\right)$
- $\text{FOV}_\text{deg} = \text{FOV}_\text{rad} \times \frac{180}{\pi}$
- $\text{GSD} = \text{altitude} \times \tan\left(\frac{\text{FOV}_\text{rad}}{2}\right)$

## Installation

Clone the repository and install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Command Line Interface

Run the CLI script with sensor width (mm), focal length (mm), and altitude (m):

```bash
python fov_gsd_cli.py <sensor_width_mm> <focal_length_mm> <altitude_m>
```

Example:

```bash
python fov_gsd_cli.py 36 50 500000
```

### Jupyter Notebook

Launch Jupyter and open `field_of_view_Calcs.ipynb` for an interactive version of the calculations.

## Example

The CLI example above outputs something like:

```
FOV: 39.60 degrees
GSD: 180000.00 m
```

Optionally, you can generate plots or screenshots from the notebook to visualize FOV and GSD relationships.
