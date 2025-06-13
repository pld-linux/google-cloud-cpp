Summary:	Google Cloud Platform C++ Client Libraries
Summary(pl.UTF-8):	Biblioteki klienckie C++ platformy Google Cloud
Name:		google-cloud-cpp
Version:	2.29.0
Release:	1
License:	Apache v2.0
Group:		Libraries
#Source0Download: https://github.com/googleapis/google-cloud-cpp/releases
Source0:	https://github.com/googleapis/google-cloud-cpp/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	4a5ed436e6cf5924b2bdd0afa27999ab
# see external/googleapis/CMakeLists.txt and cmake/GoogleapisConfig.cmake
Source1:	https://github.com/googleapis/googleapis/archive/6a474b31c53cc1797710206824a17b364a835d2d.tar.gz
# Source1-md5:	dfa7d767e92a8bf795e7fa96589faff8
Patch0:		%{name}-pc.patch
URL:		https://github.com/googleapis/google-cloud-cpp
BuildRequires:	abseil-cpp-devel >= 20210324.2
BuildRequires:	c-ares-devel
BuildRequires:	cmake >= 3.13
BuildRequires:	crc32c-devel >= 1.1.2
BuildRequires:	curl-devel >= 7.47.0
BuildRequires:	grpc-devel >= 1.35
BuildRequires:	libstdc++-devel >= 6:7.5
BuildRequires:	nlohmann-json-devel >= 3.4.0
BuildRequires:	openssl-devel >= 1.0.2
# >= 21.1 ? (docs say so); 3.14 was not sufficient, builds with 3.17
BuildRequires:	protobuf-devel >= 3.17
BuildRequires:	re2-devel
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	zlib-devel
Requires:	crc32c >= 1.1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains idiomatic C++ client libraries for Google Cloud
Platform (<https://cloud.google.com/>) services.

%description -l pl.UTF-8
Ten pakiet zawiera biblioteki klienckie C++ do usług Google Cloud
Platform (<https://cloud.google.com/>).

%package devel
Summary:	Header files for Google Cloud C++ libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek Google Cloud C++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	abseil-cpp-devel >= 20210324.2
Requires:	c-ares-devel
Requires:	curl-devel >= 7.47.0
Requires:	grpc-devel >= 1.35
Requires:	libstdc++-devel >= 6:7.5
Requires:	openssl-devel >= 1.0.2
Requires:	protobuf-devel >= 3.17
Requires:	zlib-devel

%description devel
Header files for Google Cloud C++ libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek Google Cloud C++.

%prep
%setup -q
%patch -P0 -p1

install -d build/external/googleapis/src
ln -sf %{SOURCE1} build/external/googleapis/src

%build
%cmake -B build \
	-DCMAKE_CXX_STANDARD=17 \
	-DGOOGLE_CLOUD_CPP_ENABLE_WERROR=OFF

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ARCHITECTURE.md CHANGELOG.md README.md SECURITY.md
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_annotations_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_annotations_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_auth_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_auth_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_backend_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_backend_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_billing_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_billing_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_client_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_client_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_config_change_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_config_change_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_consumer_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_consumer_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_context_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_context_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_control_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_control_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_distribution_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_distribution_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_documentation_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_documentation_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_endpoint_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_endpoint_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_error_reason_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_error_reason_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_field_behavior_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_field_behavior_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_field_info_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_field_info_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_httpbody_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_httpbody_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_http_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_http_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_label_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_label_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_launch_stage_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_launch_stage_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_logging_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_logging_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_log_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_log_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_metric_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_metric_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_monitored_resource_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_monitored_resource_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_monitoring_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_monitoring_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_policy_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_policy_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_quota_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_quota_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_resource_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_resource_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_routing_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_routing_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_service_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_service_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_source_info_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_source_info_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_system_parameter_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_system_parameter_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_usage_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_usage_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_visibility_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_api_visibility_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_bigquery.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_bigquery.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_bigquery_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_bigquery_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_bigtable.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_bigtable.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_bigtable_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_bigtable_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_cloud_common_common_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_cloud_common_common_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_cloud_extended_operations_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_cloud_extended_operations_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_cloud_orgpolicy_v1_orgpolicy_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_cloud_orgpolicy_v1_orgpolicy_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_common.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_common.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_grpc_utils.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_grpc_utils.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_iam.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_iam.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_iam_credentials_v1_common_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_iam_credentials_v1_common_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_iam_credentials_v1_iamcredentials_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_iam_credentials_v1_iamcredentials_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_iam_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_iam_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_iam_v1_iam_policy_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_iam_v1_iam_policy_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_iam_v1_options_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_iam_v1_options_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_iam_v1_policy_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_iam_v1_policy_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_iam_v2_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_iam_v2_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_logging.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_logging.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_logging_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_logging_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_logging_type_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_logging_type_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_longrunning_operations_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_longrunning_operations_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_pubsub.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_pubsub.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_pubsub_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_pubsub_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_rest_internal.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_rest_internal.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_rest_protobuf_internal.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_rest_protobuf_internal.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_rpc_code_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_rpc_code_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_rpc_context_attribute_context_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_rpc_context_attribute_context_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_rpc_error_details_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_rpc_error_details_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_rpc_status_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_rpc_status_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_spanner.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_spanner.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_spanner_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_spanner_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_storage.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_storage.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_calendar_period_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_type_calendar_period_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_color_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_type_color_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_date_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_type_date_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_datetime_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_type_datetime_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_dayofweek_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_type_dayofweek_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_decimal_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_type_decimal_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_expr_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_type_expr_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_fraction_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_type_fraction_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_interval_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_type_interval_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_latlng_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_type_latlng_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_localized_text_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_type_localized_text_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_money_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_type_money_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_month_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_type_month_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_phone_number_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_type_phone_number_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_postal_address_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_type_postal_address_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_quaternion_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_type_quaternion_protos.so.2
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_timeofday_protos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoogle_cloud_cpp_type_timeofday_protos.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_annotations_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_auth_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_backend_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_billing_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_client_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_config_change_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_consumer_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_context_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_control_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_distribution_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_documentation_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_endpoint_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_error_reason_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_field_behavior_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_field_info_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_httpbody_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_http_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_label_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_launch_stage_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_logging_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_log_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_metric_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_monitored_resource_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_monitoring_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_policy_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_quota_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_resource_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_routing_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_service_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_source_info_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_system_parameter_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_usage_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_api_visibility_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_bigquery.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_bigquery_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_bigtable.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_bigtable_mocks.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_bigtable_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_cloud_common_common_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_cloud_extended_operations_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_cloud_orgpolicy_v1_orgpolicy_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_common.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_grpc_utils.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_iam.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_iam_credentials_v1_common_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_iam_credentials_v1_iamcredentials_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_iam_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_iam_v1_iam_policy_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_iam_v1_options_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_iam_v1_policy_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_iam_v2_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_logging.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_logging_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_logging_type_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_longrunning_operations_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_pubsub.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_pubsub_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_rest_internal.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_rest_protobuf_internal.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_rpc_code_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_rpc_context_attribute_context_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_rpc_error_details_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_rpc_status_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_spanner.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_spanner_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_storage.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_calendar_period_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_color_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_date_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_datetime_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_dayofweek_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_decimal_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_expr_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_fraction_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_interval_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_latlng_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_localized_text_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_money_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_month_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_phone_number_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_postal_address_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_quaternion_protos.so
%attr(755,root,root) %{_libdir}/libgoogle_cloud_cpp_type_timeofday_protos.so
%dir %{_includedir}/google
%{_includedir}/google/api
%{_includedir}/google/bigtable
%{_includedir}/google/cloud
%{_includedir}/google/iam
%{_includedir}/google/logging
%{_includedir}/google/longrunning
%{_includedir}/google/pubsub
%{_includedir}/google/rpc
%{_includedir}/google/spanner
%{_includedir}/google/type
%{_pkgconfigdir}/google_cloud_cpp_api_annotations_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_auth_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_backend_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_billing_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_client_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_config_change_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_consumer_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_context_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_control_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_distribution_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_documentation_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_endpoint_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_error_reason_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_field_behavior_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_field_info_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_http_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_httpbody_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_label_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_launch_stage_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_log_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_logging_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_metric_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_monitored_resource_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_monitoring_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_policy_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_quota_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_resource_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_routing_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_service_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_source_info_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_system_parameter_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_usage_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_api_visibility_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_bigquery.pc
%{_pkgconfigdir}/google_cloud_cpp_bigquery_mocks.pc
%{_pkgconfigdir}/google_cloud_cpp_bigquery_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_bigtable.pc
%{_pkgconfigdir}/google_cloud_cpp_bigtable_mocks.pc
%{_pkgconfigdir}/google_cloud_cpp_bigtable_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_cloud_bigquery_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_cloud_extended_operations_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_cloud_common_common_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_cloud_orgpolicy_v1_orgpolicy_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_common.pc
%{_pkgconfigdir}/google_cloud_cpp_grpc_utils.pc
%{_pkgconfigdir}/google_cloud_cpp_iam.pc
%{_pkgconfigdir}/google_cloud_cpp_iam_credentials_v1_common_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_iam_credentials_v1_iamcredentials_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_iam_mocks.pc
%{_pkgconfigdir}/google_cloud_cpp_iam_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_iam_v1_iam_policy_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_iam_v1_options_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_iam_v1_policy_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_iam_v2_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_logging.pc
%{_pkgconfigdir}/google_cloud_cpp_logging_mocks.pc
%{_pkgconfigdir}/google_cloud_cpp_logging_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_logging_type_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_logging_type_type_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_longrunning_operations_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_mocks.pc
%{_pkgconfigdir}/google_cloud_cpp_pubsub.pc
%{_pkgconfigdir}/google_cloud_cpp_pubsub_mocks.pc
%{_pkgconfigdir}/google_cloud_cpp_pubsub_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_rest_internal.pc
%{_pkgconfigdir}/google_cloud_cpp_rest_protobuf_internal.pc
%{_pkgconfigdir}/google_cloud_cpp_rpc_code_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_rpc_context_attribute_context_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_rpc_error_details_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_rpc_status_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_spanner.pc
%{_pkgconfigdir}/google_cloud_cpp_spanner_mocks.pc
%{_pkgconfigdir}/google_cloud_cpp_spanner_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_storage.pc
%{_pkgconfigdir}/google_cloud_cpp_type_calendar_period_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_type_color_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_type_date_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_type_datetime_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_type_dayofweek_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_type_decimal_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_type_expr_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_type_fraction_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_type_interval_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_type_latlng_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_type_localized_text_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_type_money_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_type_month_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_type_phone_number_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_type_postal_address_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_type_quaternion_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_type_timeofday_protos.pc
%{_pkgconfigdir}/googleapis.pc
%{_libdir}/cmake/google_cloud_cpp_bigquery
%{_libdir}/cmake/google_cloud_cpp_bigquery_mocks
%{_libdir}/cmake/google_cloud_cpp_bigtable
%{_libdir}/cmake/google_cloud_cpp_bigtable_mocks
%{_libdir}/cmake/google_cloud_cpp_common
%{_libdir}/cmake/google_cloud_cpp_googleapis
%{_libdir}/cmake/google_cloud_cpp_grpc_utils
%{_libdir}/cmake/google_cloud_cpp_iam
%{_libdir}/cmake/google_cloud_cpp_iam_mocks
%{_libdir}/cmake/google_cloud_cpp_iam_v2
%{_libdir}/cmake/google_cloud_cpp_logging
%{_libdir}/cmake/google_cloud_cpp_logging_mocks
%{_libdir}/cmake/google_cloud_cpp_logging_type
%{_libdir}/cmake/google_cloud_cpp_mocks
%{_libdir}/cmake/google_cloud_cpp_pubsub
%{_libdir}/cmake/google_cloud_cpp_pubsub_mocks
%{_libdir}/cmake/google_cloud_cpp_rest_internal
%{_libdir}/cmake/google_cloud_cpp_rest_protobuf_internal
%{_libdir}/cmake/google_cloud_cpp_spanner
%{_libdir}/cmake/google_cloud_cpp_spanner_mocks
%{_libdir}/cmake/google_cloud_cpp_storage
