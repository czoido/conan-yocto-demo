from conans import ConanFile, CMake


class LedBlinkConan(ConanFile):
    name = "led_blink"
    version = "0.1"
    license = "MIT"
    description = "Application to control leds with RPi"
    settings = "os", "compiler", "build_type", "arch"
    requires = "wiringpi/2.50"  # comma-separated list of requirements
    generators = "cmake", "gcc", "txt"
    default_options = {"wiringpi:shared": False, "wiringpi:skipHWDetectionRPIModel3": True}
    exports_sources = "CMakeLists.txt", "*cpp", "LICENSE"
    keep_imports = True

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")  # From bin to bin
        self.copy("*.dylib*", dst="bin", src="lib")  # From lib to bin
        self.copy("*.so")

    def package(self):
        self.copy("*", src="bin", dst="bin")
        self.copy("*", src="lib", dst="bin", symlinks=True)

    def deploy(self):
        self.copy("*", src="bin", dst="bin")
        self.copy_deps("*", src="lib", dst="bin")
