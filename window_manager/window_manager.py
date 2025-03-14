import pygetwindow as gw

class WindowManager:
    def __init__(self, window_name: str, no_input: bool = False):
        self.window = self._get_window(window_name, no_input)

    def _get_window(self, window_name: str, no_input: bool = False):
        """Find windows matching the given name."""
        windows = gw.getAllWindows()
        matched_windows = [w for w in windows if window_name.lower() in w.title.lower()]
        
        if not matched_windows:
            print(f"No windows found with the name '{window_name}'.")
            return None
        
        print("Found windows:")
        for i, window in enumerate(matched_windows, 1):
            print(f"{i}: {window.title}")
        
        if len(matched_windows) == 1 or no_input:
            return matched_windows[0]
        
        while True:
            try:
                choice = int(input(f"Select a window by number (1-{len(matched_windows)}): "))
                if 1 <= choice <= len(matched_windows):
                    print(f"Hint: Use the window name '{matched_windows[choice - 1].title}' next time for faster selection.")
                    return matched_windows[choice - 1]
                print(f"Invalid selection. Please enter a number between 1 and {len(matched_windows)}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    def minimize(self):
        """Minimize the window."""
        if self.window and not self.window.isMinimized:
            self.window.minimize()
    
    def maximize(self):
        """Maximize the window."""
        if self.window and not self.window.isMaximized:
            self.window.maximize()
    
    def restore(self):
        """Restore the window."""
        if self.window and (self.window.isMinimized or self.window.isMaximized):
            self.window.restore()
            self.window.activate()
    
    def close(self):
        """Close the window."""
        if self.window:
            self.window.close()

    def bring_to_front(self):
        """Bring the window to the front."""
        if not self.window.isMinimized:
            self.window.minimize()
        self.window.restore()
        # Bring the window to the front
        self.window.activate()
