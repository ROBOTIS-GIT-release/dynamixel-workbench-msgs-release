Name:           ros-kinetic-dynamixel-workbench-msgs
Version:        0.1.7
Release:        0%{?dist}
Summary:        ROS dynamixel_workbench_msgs package

Group:          Development/Libraries
License:        Apache License 2.0
URL:            http://wiki.ros.org/dynamixel_workbench
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-std-msgs

%description
dynamixel_workbench_msgs package This package includes ROS messages and services
for dynamixel-workbench packages

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Feb 19 2018 Pyo <pyo@robotis.com> - 0.1.7-0
- Autogenerated by Bloom

* Thu Oct 19 2017 Pyo <pyo@robotis.com> - 0.1.6-0
- Autogenerated by Bloom

* Thu Aug 10 2017 Pyo <pyo@robotis.com> - 0.1.5-2
- Autogenerated by Bloom

* Wed Aug 09 2017 Pyo <pyo@robotis.com> - 0.1.5-1
- Autogenerated by Bloom

* Wed Aug 09 2017 Pyo <pyo@robotis.com> - 0.1.5-0
- Autogenerated by Bloom

