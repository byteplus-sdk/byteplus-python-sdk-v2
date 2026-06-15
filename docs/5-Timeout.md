[← Proxy](4-Proxy.md) | Timeout[(中文)](5-Timeout-zh.md) | [Retry →](6-Retry.md)

---

## Timeouts

> **Default**
>
> - `connect_timeout`: 30s
> - `read_timeout`: 30s

```python
import byteplussdkcore
from byteplussdkcore.interceptor import RuntimeOption

configuration = byteplussdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.connect_timeout = 10
configuration.read_timeout = 10
byteplussdkcore.Configuration.set_default(configuration)

runtime_options = RuntimeOption(
    connect_timeout=10,
    read_timeout=20,
    client_side_validation=True,
)
```

---

[← Proxy](4-Proxy.md) | Timeout[(中文)](5-Timeout-zh.md) | [Retry →](6-Retry.md)
