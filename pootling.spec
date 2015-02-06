%define name pootling
%define version 0.2
%define release 7

Summary: GUI editor for offline translation editing
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://downloads.sourceforge.net/translate/%{name}-%{version}.tar.gz
# (blino) fix importing __version__
Patch0: pootling-0.2-version.patch
License: GPL
Group: Editors
Url: http://translate.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: python-devel
Requires: python-translate python-qt4

%description
Pootling is an user-friendly offline translation editor that make the
translation process with a bundle of files more easier for you!

Pootling is also one aspect of the Translate project at Sourceforge,
along with the Translate Toolkit (a technical/conversion base for
Pootling and other translation processes (Pootle)) and this
TranslateWiki. Together, these three parts of the Translate Project
offer you easier translation, better tools and user-friendly.

%prep
%setup -q
%patch0 -p1 -b .version
# fix prefix path for images
perl -pi -e 's,/usr/local,%{_prefix},' %{name}/modules/MainEditor.py 

%build
python %{name}setup.py build

%install
rm -rf %{buildroot}
python %{name}setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}-editor.py
%{python_sitelib}/%{name}-%{version}-*.egg-info
%{python_sitelib}/%{name}


%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.2-6mdv2010.0
+ Revision: 441898
- rebuild

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 0.2-5mdv2009.1
+ Revision: 325806
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.2-4mdv2009.0
+ Revision: 259186
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.2-3mdv2009.0
+ Revision: 247129
- rebuild

* Thu Jan 17 2008 Olivier Blin <oblin@mandriva.com> 0.2-1mdv2008.1
+ Revision: 154352
- require python-translate
- buildrequire python-devel
- fix prefix path for images
- fix importing __version__
- initial pootling package
- create pootling

