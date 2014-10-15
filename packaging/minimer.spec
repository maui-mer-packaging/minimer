# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       minimer

# >> macros
# << macros

Summary:    Simple QML-only example to test basic graphics functionality of a device
Version:    0.1.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        https://github.com/mer-packages/minimer
Source0:    %{name}-%{version}.tar.xz
Source100:  minimer.yaml
Requires:   systemd
Requires:   qt5-qtdeclarative
Requires:   qt5-qtdeclarative-qmlscene
Requires:   qt5-qtdeclarative-tool-qml
Requires(preun): systemd
Requires(post): systemd
Requires(postun): systemd

%description
Simple QML-only example to test basic graphics functionality of a device.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre

# Copy files
mkdir -p %{buildroot}%{_datadir}/minimer
cp *.qml *.jpg %{buildroot}%{_datadir}/minimer

# Create script
mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/minimer <<EOF
#!/bin/sh

pushd %{_datadir}/minimer >/dev/null
exec qmlscene $* main.qml
popd >/dev/null
EOF

chmod 755 %{buildroot}%{_bindir}/minimer

# Create systemd unit
mkdir -p %{buildroot}/lib/systemd/system
cat > %{buildroot}/lib/systemd/system/minimer.service <<EOF
[Unit]
Description=minimer

[Service]
ExecStart=%{_bindir}/minimer
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
EOF

# << install pre

# >> install post
# << install post

%preun
if [ "$1" -eq 0 ]; then
systemctl stop minimer.service
fi

%post
systemctl daemon-reload
systemctl reload-or-try-restart minimer.service

%postun
systemctl daemon-reload

%files
%defattr(-,root,root,-)
%{_bindir}/minimer
%{_datadir}/minimer/*
/lib/systemd/system/minimer.service
# >> files
# << files
