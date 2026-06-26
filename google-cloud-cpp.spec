Summary:	Google Cloud Platform C++ Client Libraries
Summary(pl.UTF-8):	Biblioteki klienckie C++ platformy Google Cloud
Name:		google-cloud-cpp
Version:	3.6.0
Release:	1
License:	Apache v2.0
Group:		Libraries
#Source0Download: https://github.com/googleapis/google-cloud-cpp/releases
Source0:	https://github.com/googleapis/google-cloud-cpp/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9f46c596c81c0b452c584b654cf65bda
# see external/googleapis/CMakeLists.txt and cmake/GoogleapisConfig.cmake
Source1:	https://github.com/googleapis/googleapis/archive/ef19b7b7a73f19f33ab86c5b3603e9590025acd7.tar.gz
# Source1-md5:	cadacc4f1bbff4452dd43235b24d2982
URL:		https://github.com/googleapis/google-cloud-cpp
BuildRequires:	abseil-cpp-devel >= 20250814.1
BuildRequires:	c-ares-devel
BuildRequires:	cmake >= 3.22
BuildRequires:	crc32c-devel >= 1.1.2
BuildRequires:	curl-devel >= 7.74.0
BuildRequires:	google-benchmark-devel
BuildRequires:	grpc-devel >= 1.76
BuildRequires:	libstdc++-devel >= 6:7.5
BuildRequires:	nlohmann-json-devel >= 3.4.0
BuildRequires:	openssl-devel >= 3.0.17
BuildRequires:	opentelemetry-cpp-devel >= 1.23.0
# >= 6.33? (docs say so); builds fine with 5.29.6
BuildRequires:	protobuf-devel >= 4.25
BuildRequires:	re2-devel
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	zlib-devel
Requires:	crc32c >= 1.1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# _ZN4absl12lts_2025081413cord_internal17cordz_next_sampleE
# _ZN6google8protobuf8internal15ThreadSafeArena13thread_cache_E
%define		skip_post_check_so libgoogle_cloud_cpp_.*_protos.so.* libgoogle_cloud_cpp_bigtable.so.* libgoogle_cloud_cpp_iam.so.* libgoogle_cloud_cpp_logging.so.* libgoogle_cloud_cpp_pubsub.so.* libgoogle_cloud_cpp_spanner.so.* libgoogle_cloud_cpp_opentelemetry.so.*

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
Requires:	abseil-cpp-devel >= 20250814.1
Requires:	c-ares-devel
Requires:	crc32c-devel >= 1.1.2
Requires:	curl-devel >= 7.74.0
Requires:	grpc-devel >= 1.76
Requires:	libstdc++-devel >= 6:7.5
Requires:	nlohmann-json-devel >= 3.4.0
Requires:	openssl-devel >= 3.0.17
Requires:	opentelemetry-cpp-devel >= 1.23.0
Requires:	protobuf-devel >= 4.25
Requires:	zlib-devel

%description devel
Header files for Google Cloud C++ libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek Google Cloud C++.

%prep
%setup -q

install -d build/external/googleapis/src
ln -sf %{SOURCE1} build/external/googleapis/src

%build
# C++ version must be at least that which opentelemetry-cpp uses (-DWITH_STL=...)
%cmake -B build \
	-DCMAKE_CXX_STANDARD=20 \
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
%{_libdir}/libgoogle_cloud_cpp_api_annotations_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_annotations_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_auth_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_auth_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_backend_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_backend_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_billing_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_billing_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_client_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_client_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_config_change_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_config_change_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_consumer_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_consumer_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_context_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_context_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_control_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_control_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_distribution_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_distribution_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_documentation_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_documentation_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_endpoint_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_endpoint_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_error_reason_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_error_reason_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_field_behavior_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_field_behavior_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_field_info_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_field_info_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_httpbody_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_httpbody_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_http_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_http_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_label_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_label_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_launch_stage_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_launch_stage_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_logging_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_logging_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_log_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_log_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_metric_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_metric_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_monitored_resource_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_monitored_resource_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_monitoring_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_monitoring_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_policy_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_policy_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_quota_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_quota_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_resource_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_resource_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_routing_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_routing_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_service_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_service_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_source_info_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_source_info_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_system_parameter_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_system_parameter_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_usage_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_usage_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_api_visibility_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_api_visibility_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_bigquery.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_bigquery.so.3
%{_libdir}/libgoogle_cloud_cpp_bigquery_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_bigquery_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_bigtable.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_bigtable.so.3
%{_libdir}/libgoogle_cloud_cpp_bigtable_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_bigtable_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_cloud_common_common_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_cloud_common_common_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_cloud_extended_operations_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_cloud_extended_operations_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_cloud_location_locations_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_cloud_location_locations_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_cloud_orgpolicy_v1_orgpolicy_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_cloud_orgpolicy_v1_orgpolicy_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_common.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_common.so.3
%{_libdir}/libgoogle_cloud_cpp_grpc_utils.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_grpc_utils.so.3
%{_libdir}/libgoogle_cloud_cpp_iam.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_iam.so.3
%{_libdir}/libgoogle_cloud_cpp_iam_credentials_v1_common_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_iam_credentials_v1_common_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_iam_credentials_v1_iamcredentials_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_iam_credentials_v1_iamcredentials_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_iam_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_iam_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_iam_v1_iam_policy_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_iam_v1_iam_policy_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_iam_v1_options_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_iam_v1_options_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_iam_v1_policy_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_iam_v1_policy_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_iam_v1_resource_policy_member_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_iam_v1_resource_policy_member_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_iam_v2_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_iam_v2_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_iam_v3_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_iam_v3_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_logging.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_logging.so.3
%{_libdir}/libgoogle_cloud_cpp_logging_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_logging_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_logging_type_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_logging_type_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_longrunning_operations_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_longrunning_operations_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_monitoring.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_monitoring.so.3
%{_libdir}/libgoogle_cloud_cpp_monitoring_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_monitoring_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_opentelemetry.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_opentelemetry.so.3
%{_libdir}/libgoogle_cloud_cpp_pubsub.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_pubsub.so.3
%{_libdir}/libgoogle_cloud_cpp_pubsub_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_pubsub_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_rest_internal.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_rest_internal.so.3
%{_libdir}/libgoogle_cloud_cpp_rest_protobuf_internal.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_rest_protobuf_internal.so.3
%{_libdir}/libgoogle_cloud_cpp_rpc_code_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_rpc_code_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_rpc_context_attribute_context_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_rpc_context_attribute_context_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_rpc_error_details_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_rpc_error_details_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_rpc_status_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_rpc_status_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_spanner.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_spanner.so.3
%{_libdir}/libgoogle_cloud_cpp_spanner_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_spanner_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_storage.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_storage.so.3
%{_libdir}/libgoogle_cloud_cpp_trace.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_trace.so.3
%{_libdir}/libgoogle_cloud_cpp_trace_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_trace_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_type_calendar_period_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_type_calendar_period_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_type_color_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_type_color_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_type_date_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_type_date_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_type_datetime_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_type_datetime_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_type_dayofweek_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_type_dayofweek_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_type_decimal_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_type_decimal_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_type_expr_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_type_expr_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_type_fraction_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_type_fraction_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_type_interval_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_type_interval_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_type_latlng_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_type_latlng_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_type_localized_text_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_type_localized_text_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_type_money_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_type_money_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_type_month_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_type_month_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_type_phone_number_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_type_phone_number_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_type_postal_address_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_type_postal_address_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_type_quaternion_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_type_quaternion_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_type_timeofday_protos.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_type_timeofday_protos.so.3
%{_libdir}/libgoogle_cloud_cpp_universe_domain.so.*.*.*
%ghost %{_libdir}/libgoogle_cloud_cpp_universe_domain.so.3

%files devel
%defattr(644,root,root,755)
%{_libdir}/libgoogle_cloud_cpp_api_annotations_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_auth_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_backend_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_billing_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_client_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_config_change_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_consumer_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_context_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_control_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_distribution_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_documentation_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_endpoint_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_error_reason_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_field_behavior_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_field_info_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_httpbody_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_http_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_label_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_launch_stage_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_logging_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_log_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_metric_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_monitored_resource_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_monitoring_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_policy_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_quota_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_resource_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_routing_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_service_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_source_info_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_system_parameter_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_usage_protos.so
%{_libdir}/libgoogle_cloud_cpp_api_visibility_protos.so
%{_libdir}/libgoogle_cloud_cpp_bigquery.so
%{_libdir}/libgoogle_cloud_cpp_bigquery_protos.so
%{_libdir}/libgoogle_cloud_cpp_bigtable.so
%{_libdir}/libgoogle_cloud_cpp_bigtable_mocks.so
%{_libdir}/libgoogle_cloud_cpp_bigtable_protos.so
%{_libdir}/libgoogle_cloud_cpp_cloud_common_common_protos.so
%{_libdir}/libgoogle_cloud_cpp_cloud_extended_operations_protos.so
%{_libdir}/libgoogle_cloud_cpp_cloud_location_locations_protos.so
%{_libdir}/libgoogle_cloud_cpp_cloud_orgpolicy_v1_orgpolicy_protos.so
%{_libdir}/libgoogle_cloud_cpp_common.so
%{_libdir}/libgoogle_cloud_cpp_grpc_utils.so
%{_libdir}/libgoogle_cloud_cpp_iam.so
%{_libdir}/libgoogle_cloud_cpp_iam_credentials_v1_common_protos.so
%{_libdir}/libgoogle_cloud_cpp_iam_credentials_v1_iamcredentials_protos.so
%{_libdir}/libgoogle_cloud_cpp_iam_protos.so
%{_libdir}/libgoogle_cloud_cpp_iam_v1_iam_policy_protos.so
%{_libdir}/libgoogle_cloud_cpp_iam_v1_options_protos.so
%{_libdir}/libgoogle_cloud_cpp_iam_v1_policy_protos.so
%{_libdir}/libgoogle_cloud_cpp_iam_v1_resource_policy_member_protos.so
%{_libdir}/libgoogle_cloud_cpp_iam_v2_protos.so
%{_libdir}/libgoogle_cloud_cpp_iam_v3_protos.so
%{_libdir}/libgoogle_cloud_cpp_logging.so
%{_libdir}/libgoogle_cloud_cpp_logging_protos.so
%{_libdir}/libgoogle_cloud_cpp_logging_type_protos.so
%{_libdir}/libgoogle_cloud_cpp_longrunning_operations_protos.so
%{_libdir}/libgoogle_cloud_cpp_monitoring.so
%{_libdir}/libgoogle_cloud_cpp_monitoring_protos.so
%{_libdir}/libgoogle_cloud_cpp_opentelemetry.so
%{_libdir}/libgoogle_cloud_cpp_pubsub.so
%{_libdir}/libgoogle_cloud_cpp_pubsub_protos.so
%{_libdir}/libgoogle_cloud_cpp_rest_internal.so
%{_libdir}/libgoogle_cloud_cpp_rest_protobuf_internal.so
%{_libdir}/libgoogle_cloud_cpp_rpc_code_protos.so
%{_libdir}/libgoogle_cloud_cpp_rpc_context_attribute_context_protos.so
%{_libdir}/libgoogle_cloud_cpp_rpc_error_details_protos.so
%{_libdir}/libgoogle_cloud_cpp_rpc_status_protos.so
%{_libdir}/libgoogle_cloud_cpp_spanner.so
%{_libdir}/libgoogle_cloud_cpp_spanner_protos.so
%{_libdir}/libgoogle_cloud_cpp_storage.so
%{_libdir}/libgoogle_cloud_cpp_trace.so
%{_libdir}/libgoogle_cloud_cpp_trace_protos.so
%{_libdir}/libgoogle_cloud_cpp_type_calendar_period_protos.so
%{_libdir}/libgoogle_cloud_cpp_type_color_protos.so
%{_libdir}/libgoogle_cloud_cpp_type_date_protos.so
%{_libdir}/libgoogle_cloud_cpp_type_datetime_protos.so
%{_libdir}/libgoogle_cloud_cpp_type_dayofweek_protos.so
%{_libdir}/libgoogle_cloud_cpp_type_decimal_protos.so
%{_libdir}/libgoogle_cloud_cpp_type_expr_protos.so
%{_libdir}/libgoogle_cloud_cpp_type_fraction_protos.so
%{_libdir}/libgoogle_cloud_cpp_type_interval_protos.so
%{_libdir}/libgoogle_cloud_cpp_type_latlng_protos.so
%{_libdir}/libgoogle_cloud_cpp_type_localized_text_protos.so
%{_libdir}/libgoogle_cloud_cpp_type_money_protos.so
%{_libdir}/libgoogle_cloud_cpp_type_month_protos.so
%{_libdir}/libgoogle_cloud_cpp_type_phone_number_protos.so
%{_libdir}/libgoogle_cloud_cpp_type_postal_address_protos.so
%{_libdir}/libgoogle_cloud_cpp_type_quaternion_protos.so
%{_libdir}/libgoogle_cloud_cpp_type_timeofday_protos.so
%{_libdir}/libgoogle_cloud_cpp_universe_domain.so
%dir %{_includedir}/google
%{_includedir}/google/api
%{_includedir}/google/bigtable
%{_includedir}/google/cloud
%{_includedir}/google/devtools
%{_includedir}/google/iam
%{_includedir}/google/logging
%{_includedir}/google/longrunning
%{_includedir}/google/monitoring
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
%{_pkgconfigdir}/google_cloud_cpp_cloud_extended_operations_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_cloud_common_common_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_cloud_location_locations_protos.pc
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
%{_pkgconfigdir}/google_cloud_cpp_iam_v1_resource_policy_member_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_iam_v2_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_iam_v3_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_logging.pc
%{_pkgconfigdir}/google_cloud_cpp_logging_mocks.pc
%{_pkgconfigdir}/google_cloud_cpp_logging_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_logging_type_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_longrunning_operations_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_mocks.pc
%{_pkgconfigdir}/google_cloud_cpp_monitoring.pc
%{_pkgconfigdir}/google_cloud_cpp_monitoring_mocks.pc
%{_pkgconfigdir}/google_cloud_cpp_monitoring_protos.pc
%{_pkgconfigdir}/google_cloud_cpp_opentelemetry.pc
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
%{_pkgconfigdir}/google_cloud_cpp_trace.pc
%{_pkgconfigdir}/google_cloud_cpp_trace_mocks.pc
%{_pkgconfigdir}/google_cloud_cpp_trace_protos.pc
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
%{_pkgconfigdir}/google_cloud_cpp_universe_domain.pc
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
%{_libdir}/cmake/google_cloud_cpp_iam_v3
%{_libdir}/cmake/google_cloud_cpp_logging
%{_libdir}/cmake/google_cloud_cpp_logging_mocks
%{_libdir}/cmake/google_cloud_cpp_logging_type
%{_libdir}/cmake/google_cloud_cpp_mocks
%{_libdir}/cmake/google_cloud_cpp_monitoring
%{_libdir}/cmake/google_cloud_cpp_monitoring_mocks
%{_libdir}/cmake/google_cloud_cpp_opentelemetry
%{_libdir}/cmake/google_cloud_cpp_pubsub
%{_libdir}/cmake/google_cloud_cpp_pubsub_mocks
%{_libdir}/cmake/google_cloud_cpp_rest_internal
%{_libdir}/cmake/google_cloud_cpp_rest_protobuf_internal
%{_libdir}/cmake/google_cloud_cpp_spanner
%{_libdir}/cmake/google_cloud_cpp_spanner_mocks
%{_libdir}/cmake/google_cloud_cpp_storage
%{_libdir}/cmake/google_cloud_cpp_trace
%{_libdir}/cmake/google_cloud_cpp_trace_mocks
%{_libdir}/cmake/google_cloud_cpp_universe_domain
