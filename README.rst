Demo using a Conan package cross-compiling to a Yocto image
===========================================================

Prerequisites:

- Raspberry Pi with Yocto image: https://gist.github.com/czoido/c46b264d7e44ae57974a6b029491229c
- Valid Yocto SDK for Raspberry Pi: http://downloads.yoctoproject.org/releases/yocto/yocto-2.6.2/toolchain/x86_64/poky-glibc-x86_64-core-image-minimal-aarch64-toolchain-ext-2.6.2.sh

In Linux:

.. code-block:: bash

    git clone --branch demo https://github.com/czoido/conan-wiringpi.git
    cd conan-wiringpi/
    conan create . #creates package for default linux profile, not arm
    conan upload wiringpi/2.50 --all --confirm -r local
    cd ..
    git clone https://github.com/czoido/conan-yocto-demo.git
    cd conan-yocto-demo/
    conan create . --build missing
    conan install led_blink/0.1@
    ./bin/yocto_led # will run the linux (not arm) version


Let's cross-compile the RPi version:

.. code-block:: bash

    source ~/poky_sdk/environment-setup-aarch64-poky-linux 
    cd conan-yocto-demo/
    cp profiles/armv8 ~/.conan/profiles/armv8 
    conan create . --profile armv8 --build missing
    conan install led_blink/0.1@ --profile armv8
    ssh root@raspberry_pi_ip 'killall yocto_led'
    scp bin/yocto_led root@raspberry_pi_ip:~
    ssh root@raspberry_pi_ip '~/yocto_led'

