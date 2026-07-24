# coding=utf-8
"""Shared helpers for STS credential providers.

Mirrors the Go ``defaultSTSHostFor`` (byteplus/credentials/sts_credentials.go)
and Java ``StsFormRequest.defaultSTSHostFor`` so the three Python STS
providers resolve to the same region-aware host.
"""

DEFAULT_STS_REGION = 'ap-southeast-1'
DEFAULT_STS_ENDPOINT = 'sts.' + DEFAULT_STS_REGION + '.byteplusapi.com'

_CN_NON_MAINLAND_REGION_SET = {'cn-hongkong'}


def default_sts_host_for(region):
    """Returns the STS host for ``region``.

    Mainland ``cn-*`` regions resolve to ``byteplusapi.com.cn``; every other
    region (including ``cn-hongkong``) resolves to ``byteplusapi.com``. An
    empty or None region falls back to ``DEFAULT_STS_REGION``.
    """
    normalized = (region or '').strip().lower()
    if not normalized:
        normalized = DEFAULT_STS_REGION
    suffix = 'byteplusapi.com'
    if normalized.startswith('cn-') and normalized not in _CN_NON_MAINLAND_REGION_SET:
        suffix = 'byteplusapi.com.cn'
    return 'sts.' + normalized + '.' + suffix
