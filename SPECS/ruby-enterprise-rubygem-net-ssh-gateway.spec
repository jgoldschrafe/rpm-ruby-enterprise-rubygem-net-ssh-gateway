%define _prefix /opt/ruby-enterprise
%define _gem %{_prefix}/bin/gem
%define _ruby %{_prefix}/bin/ruby

# Generated from net-ssh-gateway-1.0.1.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(%{_ruby} -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(%{_ruby} -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname net-ssh-gateway
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: A simple library to assist in establishing tunneled Net::SSH connections
Name: ruby-enterprise-rubygem-%{gemname}
Version: 1.0.1
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://net-ssh.rubyforge.org/gateway
Source0: http://gemcutter.orggems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby-enterprise-rubygems
Requires: ruby-enterprise-rubygem(net-ssh) >= 1.99.1
Requires: ruby-enterprise-rubygem(echoe) >= 0
BuildRequires: ruby-enterprise-rubygems
BuildArch: noarch
Provides: ruby-enterprise-rubygem(%{gemname}) = %{version}

%description
A simple library to assist in establishing tunneled Net::SSH connections


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
%{_gem} install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/CHANGELOG.rdoc
%doc %{geminstdir}/lib/net/ssh/gateway.rb
%doc %{geminstdir}/README.rdoc
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Mon Oct  3 2011 Jeff Goldschrafe <jeff@holyhandgrenade.org> - 1.0.1-1.hhg
- Rebuild for Ruby Enterprise Edition

* Tue Apr 12 2011 Sergio Rubio <rubiojr@frameos.org> - 1.0.1-1
- Initial package
