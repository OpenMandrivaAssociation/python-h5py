%define module	h5py
%define name	python-%{module}
%define version 1.3.1
%define release %mkrel 1

Summary:	A Python interface to the HDF5 library
Name: 		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{module}-%{version}.tar.gz
Patch0:		h5py-setup.patch
License:	BSD
Group:		Development/Python
Url:		http://h5py.alfven.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	python >= 2.5, python-numpy >= 1.0.3
BuildRequires:	python-devel >= 2.5, python-numpy-devel >= 1.0.3, hdf5 >= 1.8.0
BuildRequires:	hdf5-devel >= 1.8.0
BuildRequires:	python-setuptools, python-sphinx

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
accesed using the tradional POSIX /path/to/resource syntax.

In addition to providing interoperability with existing HDF5 datasets
and platforms, h5py is a convienient way to store and retrieve
arbitrary NumPy data and metadata.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1 

%build
%__python setup.py configure --api=18
PYTHONDONTWRITEBYTECODE= %__python setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
pushd docs
export PYTHONPATH=`dir -d ../build/lib.linux*`
make html
rm -rf build/html/.buildinfo build/html/.doctrees 
popd
chmod 644 %{buildroot}%{py_platsitedir}/h5py*egg-info/*
chmod 644 LICENSE.txt README.txt

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc LICENSE.txt README.txt docs/build/html/

