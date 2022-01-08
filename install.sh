#!system/bin/sh
pkg install root-repo -y
pkg install unstable-repo -y
pkg install x11-repo -y
pkg up
pkg install git python -y
term
git clone https://github.com/RayhanAhmedAbir/Raje
cd Raje


clear
python raje.py
