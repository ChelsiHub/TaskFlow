from notification.notifier import Notifier
from config.config_loader import load_config

config = load_config()
notifier = Notifier(config)

# Send alerts for failures immediately
notifier.send_failure_alerts()

# Send daily summary (can also be scheduled)
notifier.send_daily_summary()
