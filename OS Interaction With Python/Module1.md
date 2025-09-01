# Module 1: Using Python to Interact with the Operating System

## Course Environment
- **Platform**: Linux
- **Lab Environment**: Qwiklabs by Google (simulates real-world IT problems)
- **Python Version**: 3.x required

## Operating System Fundamentals

### What is an Operating System?
The software that manages everything that goes on in the computer:
- Reads, writes, and deletes files from the hard drive
- Handles how processes start, interact with each other, and finish
- Manages memory allocation to different processes
- Handles network packet transmission and reception
- Manages hardware component access for programs

### OS Architecture

**Kernel**
- Main core of the OS
- Talks directly to hardware
- Manages system resources
- Users don't interact with kernel directly

**User Space**
- Everything outside the kernel
- System programs and user interfaces
- Where we write our automation scripts

### Common Operating Systems
- **macOS**: Apple's operating system
- **Windows**: Microsoft's operating system
- **Linux**: Open source, preferred by developers for customization flexibility

## Python Package Management

### Finding Modules
- Visit **Python Package Index** (PyPI) to find available modules
- Use `pip` to install, manage, and remove external Python modules

### Installation
```bash
pip install module_name
```

## Programming Language Types

### Compiled Languages
- Source code → Compiler → Machine code → Execution
- **Pros**: Fast execution
- **Cons**: Slow compilation time
- **Examples**: C++, Go, Rust

### Interpreted Languages
- Source code → Interpreter → Execution
- **Pros**: Faster development cycle, cross-platform compatibility
- **Cons**: Slower execution
- **Examples**: Python, Ruby, JavaScript, Bash, PowerShell

### Intermediate Languages
- Source code → Compiler → Intermediate code → Platform-specific runtime
- **Examples**: Java (JVM), C# (CLR)
- Portable across platforms with appropriate runtime

## Linux Commands

### Basic File Operations
```bash
cat filename.extension    # Create/view file content
python3 filename.py      # Run Python script
```

### Making Scripts Executable
1. Add shebang line to script:
   ```python
   #!/usr/bin/env python3
   ```
2. Make file executable:
   ```bash
   chmod +x filename.py
   ```
3. Run script:
   ```bash
   ./filename.py
   ```

## Common Python Modules for System Administration

### System Monitoring Modules
- **shutil**: Disk usage operations
- **psutil**: CPU and system usage monitoring

### Health Check Script Example
```python
#!/usr/bin/env python3
import shutil
import psutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR!")
else:
    print("Everything seems to be in order")
```

## Automation Decision Formula

To determine if automating a process saves time:

```
Time_to_automate < (time_to_perform × amount_of_times_done)
```

## Virtual Environments

### Problem Scenario
As an IT automation engineer working with:
- Multiple Python libraries
- Different versions of libraries
- Team collaboration
- Version conflicts and errors

### Solution
Virtual environments help by:
- Isolating project dependencies
- Managing different library versions per project
- Preventing conflicts between team members' environments
- Ensuring consistent execution across different systems

## Benefits and Pitfalls of Automation

### Benefits
- Reduces manual labor
- Increases consistency
- Minimizes human error
- Scales operations efficiently

### Pitfalls
- Initial time investment
- Maintenance overhead
- Potential for over-automation
- Debugging complexity

## Common Linux Commands Reference

```bash
ls                    # List directory contents
pwd                   # Print working directory
cd directory_name     # Change directory
mkdir directory_name  # Create directory
rm filename          # Remove file
cp source dest       # Copy file
mv source dest       # Move/rename file
chmod permissions    # Change file permissions
nano filename        # Edit file in terminal
```