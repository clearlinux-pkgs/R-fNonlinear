#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fNonlinear
Version  : 3042.79
Release  : 1
URL      : https://cran.r-project.org/src/contrib/fNonlinear_3042.79.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fNonlinear_3042.79.tar.gz
Summary  : Rmetrics - Nonlinear and Chaotic Time Series Modelling
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-fNonlinear-lib
Requires: R-fBasics
Requires: R-timeDate
Requires: R-timeSeries
BuildRequires : R-fBasics
BuildRequires : R-timeDate
BuildRequires : R-timeSeries
BuildRequires : clr-R-helpers

%description
univariate time series including independence and neglected
	nonlinearities. Further provides functions to investigate the chaotic
	behavior of time series processes and to simulate different types of chaotic
	time series maps.

%package lib
Summary: lib components for the R-fNonlinear package.
Group: Libraries

%description lib
lib components for the R-fNonlinear package.


%prep
%setup -q -c -n fNonlinear

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530472278

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530472278
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fNonlinear
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fNonlinear
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fNonlinear
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library fNonlinear|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fNonlinear/COPYRIGHT.html
/usr/lib64/R/library/fNonlinear/DESCRIPTION
/usr/lib64/R/library/fNonlinear/INDEX
/usr/lib64/R/library/fNonlinear/Meta/Rd.rds
/usr/lib64/R/library/fNonlinear/Meta/features.rds
/usr/lib64/R/library/fNonlinear/Meta/hsearch.rds
/usr/lib64/R/library/fNonlinear/Meta/links.rds
/usr/lib64/R/library/fNonlinear/Meta/nsInfo.rds
/usr/lib64/R/library/fNonlinear/Meta/package.rds
/usr/lib64/R/library/fNonlinear/NAMESPACE
/usr/lib64/R/library/fNonlinear/R/fNonlinear
/usr/lib64/R/library/fNonlinear/R/fNonlinear.rdb
/usr/lib64/R/library/fNonlinear/R/fNonlinear.rdx
/usr/lib64/R/library/fNonlinear/help/AnIndex
/usr/lib64/R/library/fNonlinear/help/aliases.rds
/usr/lib64/R/library/fNonlinear/help/fNonlinear.rdb
/usr/lib64/R/library/fNonlinear/help/fNonlinear.rdx
/usr/lib64/R/library/fNonlinear/help/paths.rds
/usr/lib64/R/library/fNonlinear/html/00Index.html
/usr/lib64/R/library/fNonlinear/html/R.css
/usr/lib64/R/library/fNonlinear/libs/symbols.rds
/usr/lib64/R/library/fNonlinear/unitTests/Makefile
/usr/lib64/R/library/fNonlinear/unitTests/runTests.R
/usr/lib64/R/library/fNonlinear/unitTests/runit.Gallery.R
/usr/lib64/R/library/fNonlinear/unitTests/runit.NonLinModelling.R
/usr/lib64/R/library/fNonlinear/unitTests/runit.NonLinPlots.R
/usr/lib64/R/library/fNonlinear/unitTests/runit.NonLinTests.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/fNonlinear/libs/fNonlinear.so
/usr/lib64/R/library/fNonlinear/libs/fNonlinear.so.avx2
/usr/lib64/R/library/fNonlinear/libs/fNonlinear.so.avx512
