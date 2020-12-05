#!/bin/bash
# pump monitor
# Remember to make me executable: sudo chmod a+x pump_monitor.sh

clear
echo "Starting pump monitor"

pump_is_running=false

while true
do
  ps aux | grep '[p]ump.py' >/dev/null && pump_is_running=true
  if [ "$pump_is_running" = true ]
  then
    #echo "pump is running"
    pump_is_running=true
  else
    echo "pump is not running - starting it up"
    pump_is_running=false
    nohup sudo python pump.py &>/dev/null &
  fi
  sleep 5
  pump_is_running=false
done
