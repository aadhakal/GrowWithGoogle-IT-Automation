# System Login Monitor

## Purpose
Tracks user login/logout events across multiple machines to monitor active sessions.

## What it does
- Records login and logout events with timestamps
- Sorts events chronologically 
- Maintains active user sessions per machine
- Handles user session state changes (login adds user, logout removes user)

## Components
- `Event.py`: Represents a single login/logout event
- `SessionTracker.py`: Processes events and tracks active sessions
- `Report.py`: Generates the report

## Usage
Create events and pass to SessionTracker to get current active sessions by machine.