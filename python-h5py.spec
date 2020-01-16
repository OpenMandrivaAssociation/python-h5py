%define module	h5py

Summary:	A Python interface to the HDF5 library
Name: 		python-%{module}
Version:	2.10.0
Release:	1
Source0:	%{module}-%{version}.tar.gz
Source1:	docs.tar.gz
Patch0:		docs-py3-fix.patch
License:	BSD
Group:		Development/Python
Url:		http://h5py.alfven.org/
Requires:	python >= 2.6
Requires:   	python-numpy >= 1.0.3
BuildRequires:	python-devel >= 2.6
BuildRequires:	python-numpy-devel >= 1.0.3
BuildRequires:	hdf5 >= 1.8.3
BuildRequires:	hdf5-devel >= 1.8.3
BuildRequires:	python-cython >= 0.13
BuildRequires:	python-setuptools
BuildRequires:	python-sphinx
BuildRequires:	python-numpy
BuildRequires:	pkgconfig(lapack)

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

%prep
%setup -q -n %{module}-%{version}
tar zxf %SOURCE1
%autopatch -p1

%build
PYTHONDONTWRITEBYTECODE= %__python setup.py build

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
pushd docs
export PYTHONPATH=`dir -d ../build/lib.linux*`
make html
rm -rf build/html/.buildinfo build/html/.doctrees 
popd
#chmod 644 %{buildroot}%{py_platsitedir}/h5py*egg-info*



%files  -f FILE_LIST
%doc examples/ docs/build/html/
