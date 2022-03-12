Name:           linux-sgx-driver
Version:        2.6
Release:        1
Summary:        Intel Software Guard Extension (sgx)
License:        BSD
Group:          System/Base
URL:            https://01.org/intel-softwareguard-extensions
Source:         https://github.com/intel/linux-sgx-driver/archive/sgx_driver_%{version}.tar.gz
BuildRequires:  automake

%description
Intel Software Guard Extensions (Intel SGX) is an Intel technology for application developers seeking to protect select code and 
data from disclosure or modification.

%prep
%setup -q -n linux-sgx-driver-sgx_driver_%{version}

%build
make

%install
%make_install

%files
%license License.txt
%doc README.md
