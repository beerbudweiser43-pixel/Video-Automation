#!/usr/bin/env python
"""
Simple wrapper to run the Gospel music creator app

Usage:
    python run_gospel_app.py
"""

import subprocess
import sys

try:
    # Try using streamlit module directly
    from streamlit.cli import main
    
    # Set up arguments for streamlit
    sys.argv = ["streamlit", "run", "gospel_music_creator_app.py"]
    
    # Run streamlit
    main()
    
except Exception as e:
    print(f"Error running Streamlit: {e}")
    print("Attempting alternative method...")
    
    # Try subprocess as fallback
    try:
        result = subprocess.run(
            [sys.executable, "-m", "streamlit", "run", "gospel_music_creator_app.py"],
            cwd=".",
            check=False
        )
        sys.exit(result.returncode)
    except Exception as e2:
        print(f"Alternative method also failed: {e2}")
        sys.exit(1)
