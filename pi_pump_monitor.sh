#!/bin/bash
# pi_pump monitor
# Remember to make me executable: sudo chmod a+x pi_pump_monitor.sh

clear
echo "Starting pi_pump monitor"

pi_pump_is_running=false

while true
do
  ps aux | grep '[p]ump.py' >/dev/null && pi_pump_is_running=true
  if [ "$pi_pump_is_running" = true ]
  then
    #echo "pi_pump is running"
    pi_pump_is_running=true
  else
    echo "pi_pump is not running - starting it up"
    pi_pump_is_running=false
    nohup sudo python pump.py &>/dev/null &
  fi
  sleep 5
  pi_pump_is_running=false
done
