# rpmbuild-gmond-python-modules

Create a gmond python module RPM for RHEL/CentOS.

## Requirements

To download package sources and install build dependencies

    yum -y install rpmdevtools yum-utils

## Build process

Available modules

  * bind_xml
  * elasticsearch
  * nginx_status

Select a module to build (example: bind_xml)

    GMOND_MODULE_BUILD=bind_xml

To build the package follow the steps outlined below

    git clone https://github.com/linuxhq/rpmbuild-gmond-python-modules.git rpmbuild
    mkdir rpmbuild/SOURCES
    spectool -g -R rpmbuild/SPECS/ganglia-gmond-${GMOND_MODULE_BUILD}.spec
    yum-builddep rpmbuild/SPECS/ganglia-gmond-${GMOND_MODULE_BUILD}.spec
    rpmbuild -ba rpmbuild/SPECS/ganglia-gmond-${GMOND_MODULE_BUILD}.spec

## License

BSD

## Author Information

This package was created by [Taylor Kimball](http://www.linuxhq.org).
