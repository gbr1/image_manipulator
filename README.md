# image_manipulator
A simple ros2 package to manipulate image topics


## Nodes

### 1. flipper

This node flip an image.
- topics:
    - /image/raw, subscription
    - /image/flipped, published
- parameters:
    - flip_horizontal, _bool_
    - flip_vertical, _bool_

Example:<br>
`ros2 run image_manipulator flipper --ros-args -p flip_horizontal:=True` <br>


## How to install

Clone this repo:
```bash
cd dev_ws/src
git clone https://github.com/gbr1/image_manipulator
```
Build:
```bash
cd ..
colcon build --symlink-install
source install/setup.bash
```


---
> ***Copyright © 2022 G. Bruno under MIT License***