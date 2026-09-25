Output list.gif
Set Shell "zsh"
Set FontSize 18
Set Width 1560
Set Height 900
Set Theme {"background":"#0E1621","foreground":"#D8DEE9","cursor":"#FFE052","cursor_text":"#0E1621","selection_background":"#387EB8","selection_foreground":"#F2F7FC","palette":["#22303C","#E06C5E","#6FBF73","#FFE052","#6FB3E0","#C88AD2","#62C1D8","#D8DEE9","#3E525F","#EC8B7D","#8FD48A","#FFD43B","#82BCE6","#D8A8E0","#7FD0E4","#EDF2F7"]}
Set Padding 42
Set CursorBlink false
Hide
Type "source .venv/bin/activate"
Enter
Sleep 2s
Type "lcpy list --tag blind-75 --difficulty Easy > /dev/null 2>&1"
Enter
Sleep 8s
Type "clear"
Enter
Sleep 1s
Show
Type "lcpy list --tag blind-75 --difficulty Easy"
Enter
Sleep 4s
