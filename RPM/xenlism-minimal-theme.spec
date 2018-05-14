%global srcname minimalism
%global project xenlism

Name:           %{project}-%{srcname}-theme
Version:        2018.05
Release:        1%{?dist}
Summary:        xenlism-minimalism simplicity theme for gnome desktop.

License:        GPLv3+
URL:            https://%{project}.github.io/%{srcname}
Source0:        https://github.com/%{project}/%{srcname}/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz


BuildArch:      noarch
BuildRequires:  coreutils


%description
xenlism is Computer Graphic And Programming project to make something better.
xenlism is about minimalism and realism.
xenlism minimalism is Gnome / GTK theme for Gnome 3.x desktop environment.
xenlism minimalism inspired by Elementary OS.

%prep
%setup -qn%{srcname}-%{version}
# W: hidden-file-or-dir, E: zero-length
find themes -name '.*' -print -delete
# W: spurious-executable-perm
#chmod -x Screenshot/*.png


%build
# nothing

%install
# copied from upstream install script
install -dm755 %{buildroot}%{_datadir}
cp -pr themes %{buildroot}%{_datadir}
find  %{buildroot}%{_datadir}/themes -type d -exec chmod 755 '{}' \;
find  %{buildroot}%{_datadir}/themes -type f -exec chmod 644 '{}' \;



%post
/bin/touch --no-create %{_datadir}/themes/Xenlism-Minimalism* &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/themes/Xenlism-Minimalism* &>/dev/null
fi


%files
%license LICENSE
%doc README.md
%{_datadir}/themes/Xenlism-Minimalism/



%changelog
* Wed May 4 2018 Nattapong Pullkhow <ixenatt@gmail.com> - 2018.05
- Next build


