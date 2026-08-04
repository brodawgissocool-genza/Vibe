# banner.py
# VibeOS Core Module -- Handles system-level startup visuals

def boot_system_banner(console, tk_module):
    """
    Renders the official VibeOS ASCII cat mascot and log data 
    directly onto the designated system console text widget.
    """
    cat_banner = r"""
       /\_/\
      ( o.o )    ___________________________________________
       > ^ <    |                                           |
      /     \   |        VibeOS -- Custom Scripting         |

     |       |  |     .rdr /.redirect Engine v00.01         |
    (___)_(___) |___________________________________________|

[SYS_LOG] Initializing interpreter pipeline...
[SYS_LOG] Mounting /os/TerminalShells/SyS/binary/Info.redirect
[SYS_LOG] Mascot initialized: PURRfect system state detected.
    """
    
    # Safely targets the passed console instance using the imported tk module structure
    console.insert(tk_module.END, cat_banner)
