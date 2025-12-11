# Authentication Fix - Bearer Token Support

## Issue Resolved

The Python TMI API client had a critical bug that prevented Bearer token authentication from working. The `Configuration.auth_settings()` method was returning an empty dictionary, causing all authenticated API requests to fail with `401 Unauthorized` errors.

## Problem Description

**Original Issue**: As documented in `/Users/efitz/Projects/tmi-tf/WORKAROUND-auth-settings.md`

The generated client's `Configuration.auth_settings()` method looked like this:

```python
def auth_settings(self):
    """Gets Auth Settings dict for api client.
    :return: The Auth Settings information dict.
    """
    return {}  # Empty - should return bearerAuth configuration
```

This meant that even when users configured their API key:
```python
config.api_key["bearerAuth"] = token
config.api_key_prefix["bearerAuth"] = "Bearer"
```

The API client had no way to know how to construct the Authorization header, resulting in failed authentication.

## The Fix

The `auth_settings()` method has been updated to properly return Bearer token configuration:

```python
def auth_settings(self):
    """Gets Auth Settings dict for api client.

    :return: The Auth Settings information dict.
    """
    auth = {}
    if 'bearerAuth' in self.api_key:
        auth['bearerAuth'] = {
            'type': 'api_key',
            'in': 'header',
            'key': 'Authorization',
            'value': self.get_api_key_with_prefix('bearerAuth')
        }
    return auth
```

## Impact

- **Severity**: CRITICAL - Prevented all authenticated API access
- **Affected Users**: Anyone using the Python client with Bearer token authentication
- **Status**: ✅ FIXED in this regeneration

## Migration from Workaround

If you were using the monkey-patch workaround described in the issue document, you can now **remove that workaround code**. The fix is built into the client.

### Before (with workaround):
```python
from tmi_client import Configuration, ApiClient

def auth_settings_override(self):
    return {
        'bearerAuth': {
            'type': 'api_key',
            'in': 'header',
            'key': 'Authorization',
            'value': self.get_api_key_with_prefix('bearerAuth')
        }
    }

# Configure client
config = Configuration()
config.host = 'https://api.example.com'
config.api_key['bearerAuth'] = 'your_jwt_token'
config.api_key_prefix['bearerAuth'] = 'Bearer'

# WORKAROUND: Monkey-patch the auth_settings method
config.auth_settings = auth_settings_override.__get__(config, Configuration)

api_client = ApiClient(config)
```

### After (with fix):
```python
from tmi_client import Configuration, ApiClient

# Configure client
config = Configuration()
config.host = 'https://api.example.com'
config.api_key['bearerAuth'] = 'your_jwt_token'
config.api_key_prefix['bearerAuth'] = 'Bearer'

# That's it! No workaround needed - authentication works automatically
api_client = ApiClient(config)
```

## Testing

The fix has been verified with comprehensive tests in `test_auth_settings_fix.py`:

✅ All 3 authentication tests passing:
1. auth_settings() returns empty dict when no API key is configured
2. auth_settings() returns correct Bearer token configuration
3. auth_settings() works with and without Bearer prefix

Run the tests:
```bash
cd python-client-generated
uv run python3 test_auth_settings_fix.py
```

## Technical Details

### Location
- File: `tmi_client/configuration.py`
- Method: `Configuration.auth_settings()`
- Lines: 229-242

### How It Works

1. When you set `config.api_key["bearerAuth"] = token`, the token is stored in the configuration
2. When you set `config.api_key_prefix["bearerAuth"] = "Bearer"`, the prefix is stored
3. When the API client makes a request, it calls `auth_settings()` to get authentication configuration
4. The method checks if `bearerAuth` is configured and returns the proper structure
5. The API client uses this information to add the `Authorization: Bearer <token>` header

### What Gets Sent

When configured properly, the API client will send:
```
Authorization: Bearer your_jwt_token
```

## Regeneration Script

The fix is automatically applied by the regeneration script at:
- `scripts/regenerate_client.sh` (lines 182-224)

When you regenerate the client in the future, this patch will be automatically applied.

## References

- Original issue: `/Users/efitz/Projects/tmi-tf/WORKAROUND-auth-settings.md`
- Test script: `test_auth_settings_fix.py`
- Regeneration script: `scripts/regenerate_client.sh`
- Main regeneration report: `/Users/efitz/Projects/tmi-clients/REGENERATION_REPORT.md`

## Questions?

If you have any questions about this fix or encounter any authentication issues:

1. Check that you're setting both the API key and prefix:
   ```python
   config.api_key['bearerAuth'] = 'your_token'
   config.api_key_prefix['bearerAuth'] = 'Bearer'
   ```

2. Run the authentication tests to verify the fix is working:
   ```bash
   uv run python3 test_auth_settings_fix.py
   ```

3. Check the debug output by enabling debug mode:
   ```python
   config.debug = True
   ```

---

**Fixed in**: Python Client v1.0.0 regeneration (2025-12-11)
**Status**: ✅ Production Ready
