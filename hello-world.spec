# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           hello-world
Version:        0
Release:        0
Summary:        Hello World application 
License:        GPL-2.0+
Group:          Development/Tools/Building
Url:            https://github.com/ChrisBr/hello-fosdem
Source:         %{name}-%{version}.tar.bz2
Requires:  	ruby
Requires:  	tar
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Hello world application for OBS workshop

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_prefix}/bin
install -m 755 hello-world %{buildroot}%{_prefix}/bin


%files
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/hello-world

%changelog
