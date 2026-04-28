import subprocess

class Apps:

    def __init__(self):
        self.apps = {

            # SYSTEM APPS
            "camera": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -Command \"Start-Process microsoft.windows.camera:\"",
            "notepad": "notepad.exe",
            "calculator": "calc.exe",
            "paint": "mspaint.exe",
            "command prompt": "cmd.exe",
            "powershell": "powershell.exe",
            "task manager": "taskmgr.exe",
            "control panel": "control.exe",
            "file explorer": "explorer.exe",

            # BROWSERS
            "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
            "edge": "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
            "firefox": "C:\\Program Files\\Mozilla Firefox\\firefox.exe",

            # DEVELOPMENT
            "vscode": "C:\\Users\\tiwar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
            "pycharm": "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.1\\bin\\pycharm64.exe",

            # MEDIA
            "vlc": "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe",
            "spotify": "spotify.exe",

            # WINDOWS TOOLS
            "settings": "start ms-settings:",
            "snipping tool": "snippingtool.exe",
            "wordpad": "write.exe",

            # OFFICE (if installed)
            "word": "winword.exe",
            "excel": "excel.exe",
            "powerpoint": "powerpnt.exe"
        }

    def open_app(self, command, speak):

        for app in self.apps:

            if app in command:

                speak(f"Opening {app}")

                process = subprocess.Popen(
                    self.apps[app],
                    shell=True
                )

                return process

        return None