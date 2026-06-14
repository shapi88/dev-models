# Unix Process Management (model patterns)

```bash
# Background a long-running task safely
nohup ./my-script.sh > /var/log/my-script.log 2>&1 &

# Find and kill by name (careful!)
pkill -f "my-process-name"

# Nice resource view
htop   # or btop / glances
```

See also `models/` for full small script projects that include proper signal handling, logging, and pidfile patterns.