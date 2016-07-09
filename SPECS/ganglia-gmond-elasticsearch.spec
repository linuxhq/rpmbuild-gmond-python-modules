%global date 20160120
%global commit 7cb2422532c3ba1e83344ec5f9cf328d69badb3c
%global short_commit %(c=%{commit}; echo ${c:0:7})

%define         __module elasticsearch

Name:           ganglia-gmond-%{__module}
Version:        %{date}git%{short_commit}
Release:        1%{?dist}
Summary:        Gmond Python DSO metric module: %{__module}
Group:          Development/Languages
License:        GPL
URL:            https://github.com/ganglia/gmond_python_modules
Source0:        https://github.com/ganglia/gmond_python_modules/archive/%{commit}/gmond_python_modules-%{commit}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       ganglia-gmond-python, python-jsonpath-rw

%description
Gmond Python DSO metric module: %{__module}

%prep
%setup -q -n gmond_python_modules-%{commit}
%build
%install
%{__install} -m 0755 -d %{buildroot}%{_sysconfdir}/ganglia/conf.d \
                        %{buildroot}%{_libdir}/ganglia/python_modules

%{__install} -m 0644 %{__module}/conf.d/%{__module}.pyconf \
                     %{buildroot}%{_sysconfdir}/ganglia/conf.d

%{__install} -m 0644 %{__module}/python_modules/%{__module}.py \
                     %{buildroot}%{_libdir}/ganglia/python_modules

%{__sed} -i -e 's/1.2/1.5/' %{buildroot}%{_sysconfdir}/ganglia/conf.d/%{__module}.pyconf

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc %{__module}/README.mkdn
%{_sysconfdir}/ganglia/conf.d/%{__module}.pyconf
%{_libdir}/ganglia/python_modules/%{__module}.py
%{_libdir}/ganglia/python_modules/%{__module}.pyc
%{_libdir}/ganglia/python_modules/%{__module}.pyo

%changelog
* Thu Jan 21 2016 Taylor Kimball <taylor@linuxhq.org> - 20160121git7cb2422-1
- Initial spec.
