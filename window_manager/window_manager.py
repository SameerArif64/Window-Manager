import pygetwindow as gw

class WindowManager(gw.Window):
    def __init__(self, window_name: str, no_input: bool = False):
        window = self._get_window(window_name, no_input)
        if window:
            super().__init__(window._hWnd)
        else:
            self._hWnd = None

    def _get_window(self, window_name: str, no_input: bool = False):
        """Find windows matching the given name."""
        windows = gw.getAllWindows()
        matched_windows = [w for w in windows if window_name.lower() in w.title.lower()]
        
        if not matched_windows:
            raise Exception(f"No windows found with the name '{window_name}'.")
        
        if len(matched_windows) == 1 or no_input:
            return next((window for window in matched_windows if window.title.lower() == window_name.lower()), matched_windows[0])
        
        print("Found windows:")
        for i, window in enumerate(matched_windows, 1):
            print(f"{i}: {window.title}")
        
        while True:
            try:
                choice = int(input(f"Select a window by number (1-{len(matched_windows)}): "))
                if 1 <= choice <= len(matched_windows):
                    print(f"Hint: Use the window name '{matched_windows[choice - 1].title}' next time for faster selection.")
                    return matched_windows[choice - 1]
                print(f"Invalid selection. Please enter a number between 1 and {len(matched_windows)}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    def minimize2(self):
        """Minimize the window."""
        if self._hWnd and not self.isMinimized:
            self.minimize()
    
    def maximize2(self):
        """Maximize the window."""
        if self._hWnd and not self.isMaximized:
            self.maximize()
    
    def restore2(self):
        """Restore the window."""
        if self._hWnd and (self.isMinimized or self.isMaximized):
            self.restore()
            self.activate()
    
    def close(self):
        """Close the window."""
        if self._hWnd:
            self.close()
    
    def bring_to_front(self):
        """Bring the window to the front."""
        if self._hWnd: 
            if not self.isMinimized:
                self.minimize()
            self.restore()
            self.activate()
