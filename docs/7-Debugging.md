[← Error Handling](6-ErrorHandling.md) | [Environment Variables →](EnvironmentVariables.md)

---

# Debugging

## Enable Debug Mode

```python
import byteplussdkcore
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your AK"
configuration.sk = "Your SK"
configuration.debug = True
byteplussdkcore.Configuration.set_default(configuration)
```

## Set Debug Level

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

[← Error Handling](6-ErrorHandling.md) | [Environment Variables →](EnvironmentVariables.md)
