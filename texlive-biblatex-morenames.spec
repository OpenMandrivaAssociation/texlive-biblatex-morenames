Name:		texlive-biblatex-morenames
Version:	43049
Release:	2
Summary:	New names for standard BibLaTeX entry type
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-morenames
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-morenames.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-morenames.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package adds new fields of "name" type to the standard
entry types of BibLaTeX. For example: maineditor, for a
@collection, means the editor of @mvcollection, and not the
editor of the @collection. bookineditor, for a @bookinbook,
means the editor of the entry, and not, as the standard editor
field, the editor of the volume in which the entry is
contained.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/biblatex-morenames
%doc %{_texmfdistdir}/doc/latex/biblatex-morenames

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
