%define module	h5py

Summary:	A Python interface to the HDF5 library
Name: 		python-%{module}
Version:	3.7.0
Release:	1
Source0:	https://github.com/h5py/h5py/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://www.h5py.org/

BuildRequires:	hdf5-devel
BuildRequires:	pkgconfig(python3)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pkgconfig)
BuildRequires:  python3dist(pytools)
BuildRequires:	python3dist(pip)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(wheel)
BuildRequires:  python3dist(sphinx)

%description
HDF5 for Python (h5py) is a general-purpose Python interface to the
Hierarchical Data Format library, version 5.  HDF5 is a versatile,
mature scientific software library designed for the fast, flexible
storage of enormous amounts of data.

From a Python programmer's perspective, HDF5 provides a robust way to
store data, organized by name in a tree-like fashion.  You can create
datasets (arrays on disk) hundreds of gigabytes in size, and perform
random-access I/O on desired sections.  Datasets are organized in a
filesystem-like hierarchy using containers called "groups", and 
accessed using the traditional POSIX /path/to/resource syntax.

In addition to providing interoperability with existing HDF5 datasets
and platforms, h5py is a convenient way to store and retrieve
arbitrary NumPy data and metadata.

%files
%doc licenses/*.txt README.rst
%doc docs/_build/html
%{py_platsitedir}/%{module}/
%{py_platsitedir}/%{module}-%{version}.dist-info/

#---------------------------------------------------------------------------

%prep
%autosetup -n %{module}-%{version}

%build
%py_build

# docs
make -C docs html SPHINXOPTS=
rm -rf docs/_build/html/.buildinfo

%install
%py_install
