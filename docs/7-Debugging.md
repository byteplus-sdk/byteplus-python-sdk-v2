[← Error Handling](6-ErrorHandling.md) | Debugging[(中文)](7-Debugging-zh.md) | [Overview →](0-Overview.md)

---

## Debugging

To help with troubleshooting and debugging when handling requests, the SDK supports logging with multiple levels. Configure your logging settings based on your needs to get detailed request/response information and improve observability.

### Enable Debug Mode

> **Default**
>
> - `debug` - `False`

```python
import byteplussdkcore
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your AK"
configuration.sk = "Your SK"
configuration.debug = True
byteplussdkcore.Configuration.set_default(configuration)
```

### Set Debug Level

By default, when debug is enabled the SDK emits all debug logs. To filter the output, configure `configuration.log_level` as follows:

```python
import byteplussdkcore
from byteplussdkcore.observability.debugger import LogLevel

configuration = byteplussdkcore.Configuration()
configuration.ak = "Your AK"
configuration.sk = "Your SK"
configuration.debug = True
configuration.log_level = LogLevel.LOG_DEBUG_WITH_CONFIG.mask | LogLevel.LOG_DEBUG_WITH_REQUEST.mask | LogLevel.LOG_DEBUG_WITH_RESPONSE.mask
byteplussdkcore.Configuration.set_default(configuration)
```

# Log Output

```python
import byteplussdkcore
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your AK"
configuration.sk = "Your SK"
configuration.logger_file = "app.log"
configuration.logger_format = "%(asctime)s %(levelname)s %(message)s"
byteplussdkcore.Configuration.set_default(configuration)
```

---

[← Error Handling](6-ErrorHandling.md) | Debugging[(中文)](7-Debugging-zh.md) | [Overview →](0-Overview.md)
