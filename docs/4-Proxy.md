[← Transport](3-Transport.md) | Proxy[(中文)](4-Proxy-zh.md) | [Timeout →](5-Timeout.md)

---

## HTTP(S) Proxy

> **Default**
>
> - No proxy

### Configure HTTP(S) Proxy

```python
import byteplussdkcore, byteplussdkecs
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your AK"
configuration.sk = "Your SK"

configuration.http_proxy = "http://your_proxy:8080"
configuration.https_proxy = "http://your_proxy:8080"

byteplussdkcore.Configuration.set_default(configuration)

api_instance = byteplussdkecs.ECSApi()
```

### Notes

Supported environment variables for proxy configuration:

- `http_proxy` / `HTTP_PROXY`
- `https_proxy` / `HTTPS_PROXY`
- `no_proxy` / `NO_PROXY`

Priority: code > environment variables.

---

[← Transport](3-Transport.md) | Proxy[(中文)](4-Proxy-zh.md) | [Timeout →](5-Timeout.md)
