%define module h5py

Name: 		python-h5py
Summary:	A Python interface to the HDF5 library
Version:	3.16.0
Release:	1
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://github.com/h5py/h5py
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildRequires:	make
BuildRequires:	hdf5-devel
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(numpy)
BuildRequires:	python%{pyver}dist(packaging)
BuildRequires:	python%{pyver}dist(pkgconfig)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
# For docs
BuildRequires:	python%{pyver}dist(sphinx)
BuildRequires:	python%{pyver}dist(sphinx-rtd-theme)


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

%build -p
export LDFLAGS="%{ldflags} -lpython%{pyver}"

%build -a
# docs
make -C docs html SPHINXOPTS=
rm -rf docs/_build/html/.buildinfo

%files
%doc licenses/*.txt README.rst
%doc docs/_build/html
%{py_platsitedir}/%{module}
%{py_platsitedir}/%{module}-%{version}.dist-info
