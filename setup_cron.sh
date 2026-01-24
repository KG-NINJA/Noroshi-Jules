#!/bin/bash

# Get the absolute path of the current directory
PROJECT_DIR=$(pwd)
SCRIPT_PATH="$PROJECT_DIR/src/main.py"
PYTHON_PATH=$(which python3)

echo "--------------------------------------------------------"
echo "KGNINJA AI Spreader - Scheduler Setup"
echo "--------------------------------------------------------"
echo ""
echo "To schedule the KGNINJA system to run every morning at 7:00 AM,"
echo "you should add a cron job."
echo ""
echo "1. Open your crontab configuration by running:"
echo "   crontab -e"
echo ""
echo "2. Add the following line to the bottom of the file:"
echo ""
echo "0 7 * * * cd $PROJECT_DIR && $PYTHON_PATH $SCRIPT_PATH >> $PROJECT_DIR/kgninja.log 2>&1"
echo ""
echo "--------------------------------------------------------"
echo "This will ensure the content generator runs daily and logs output to kgninja.log."
