Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "cmd.exe /c run.bat", 0, False
Set WshShell = Nothing

Set objShell = WScript.CreateObject("WScript.Shell")
objShell.SendKeys "% " 'Alt+Space to activate the system menu
WScript.Sleep 100 'Pause for a moment
objShell.SendKeys "n" 'Press "n" to minimize the window

