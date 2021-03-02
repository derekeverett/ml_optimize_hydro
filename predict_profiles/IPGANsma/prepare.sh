
#download the training events to disk
mkdir training_profiles
cd training_profiles
wget http://quark.phy.bnl.gov/~bschenke/ipglasma-events.tar.gz
tar -xvf ipglasma-events.tar.gz
cd ..

#make a directory to store trained GANs
mkdir generators
mkdir generated_profiles
mkdir plots
