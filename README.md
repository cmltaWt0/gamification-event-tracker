RG Gamification Tracking
=========================

Parse the edX tracking log, convert the events to Gamma format, and publish them to an RG Gamification storage known Gamma.


# Configuration

Add the following configuration to the lms settings:

```python
RG_GAMIFICATION = {
    "ENABLED": True,
    "RG_GAMIFICATION_ENDPOINT": "https://localhost:9000/",
    "KEY": "key",
    "SECRET": "secret",
    "IRNORED_TYPES": []
}
```
