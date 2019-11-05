Demo using a Conan package cross-compiling to a Yocto image
===========================================================

Prerequisites:

- Raspberry Pi with Yocto image: https://gist.github.com/czoido/c46b264d7e44ae57974a6b029491229c
- Valid Yocto SDK for Raspberry Pi: http://downloads.yoctoproject.org/releases/yocto/yocto-2.6.2/toolchain/x86_64/poky-glibc-x86_64-core-image-minimal-aarch64-toolchain-ext-2.6.2.sh

In Linux:

.. code-block:: bash

    git clone https://github.com/czoido/conan-wiringpi.git
    cd conan-wiringpi/
    git checkout demo
    conan create . #creates package for default linux profile, not arm
    conan upload wiringpi/2.50 --all --confirm -r local
    cd ..
    git clone https://github.com/czoido/conan-yocto-demo.git
    cd conan-yocto-demo/
    conan create .

    

