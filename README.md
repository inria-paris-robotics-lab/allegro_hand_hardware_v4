# allegro_hand_hardware
Hardware interface to attach an Allegro Hand v4 to a UR5 arm.

![Hand mounted on ur5](images/Allegro_support_1.jpeg) | ![Hand on stand](images/Allegro_support_2.jpeg)
:-------------------------:|:-------------------------:
![Base plate on interface](images/Allegro_support_3.jpeg) | ![Interface bottom](images/Allegro_support_4.jpeg)

## Available files
* [Freecad](https://www.freecad.org) source file : [CAD/Allegro_support.FCStd](CAD/Allegro_support.FCStd)
* Exported **.step** : [CAD/Allegro_support_v1_1.step](CAD/Allegro_support_v1_1.step)
* Exported stl : [CAD/Allegro_support_v1_1.stl](CAD/Allegro_support_v1_1.stl)

* Technical drawing : [CAD/Allegro_support_v1_1.pdf](CAD/Allegro_support_v1_1.pdf)

## About the part
* Machined in **aluminium** with a **CNC**.
* Weight: **200g**
* **Sand blasted** for a mat surface finish (to prevent unwanted reflection with our Motion Capture system)
* Price (2024): <200€ from local machinist (Including sand blasting, VAT, shipping, ...). Machinist found from [usineur.fr](https://usineur.fr).
* Computed inertial parameters (see [compute_inertia.py](compute_inertia.py))
```python
cog_pos = [0, -2.4e-04, 1.5e-02] # m
inertia = [[ 1.0e-04 -1.2e-13  3.5e-13],
           [-1.2e-13  1.0e-04 -4.0e-07],
           [ 3.5e-13 -4.0e-07  1.2e-04]]
```

## Assembly
Requires:
* 4x M6 * 10mm screws
* 6x M3 * 8mm screws