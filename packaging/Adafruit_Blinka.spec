%global srcname Adafruit-Blinka

Name:           python-%{srcname}
Version:        6.2.2
Release:        0%{?dist}
Summary:        CircuitPython hardware API and libraries

License:        MIT
URL:            https://github.com/adafruit/Adafruit_Blinka
Source0:        %pypi_source

BuildARch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm_git_archive

%description
unused


%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       libgpiod_pulsein

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Python 3 library for GPIO access on a Raspberry Pi.
This repository contains a selection of packages mirroring
the CircuitPython API on hosts running micropython.
Working code exists to emulate the CircuitPython packages;

- board - breakout-specific pin identities
- microcontroller - chip-specific pin identities
- analogio - analog input/output pins, using pin identities from board+microcontroller packages
- digitalio - digital input/output pins, using pin identities from board+microcontroller packages
- bitbangio - software-driven interfaces for I2C, SPI
- busio - hardware-driven interfaces for I2C, SPI, UART
- pulseio - contains classes that provide access to basic pulse IO (PWM)

%prep
%autosetup -n %{srcname}-%{version}

%build
CFLAGS="${RPM_OPT_FLAGS} -fcommon"
%py3_build

%install
%py3_install

# This is binary blob, we do not want that. Instead, depend on a package
rm -f %{buildroot}%{python3_sitelib}/adafruit_blinka/microcontroller/bcm283x/pulseio/libgpiod_pulsein

%files -n python3-%{srcname}
%doc CODE_OF_CONDUCT.md README.rst
%license LICENSE
%{python3_sitelib}/adafruit_*
%{python3_sitelib}/Adafruit_*.egg-info
%{python3_sitelib}/microcontroller
%pycached %{python3_sitelib}/analogio.py
%pycached %{python3_sitelib}/bitbangio.py
%pycached %{python3_sitelib}/board.py
%pycached %{python3_sitelib}/busio.py
%pycached %{python3_sitelib}/digitalio.py
%pycached %{python3_sitelib}/micropython.py
%pycached %{python3_sitelib}/neopixel_write.py
%pycached %{python3_sitelib}/pulseio.py
%pycached %{python3_sitelib}/pwmio.py

%changelog
