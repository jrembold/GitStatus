# GitStatus

I wrote these little scripts as a way of setting up notification indicators on my polybar to ensure I don't forget to push class content at the end of a day. The scripts `git_status` and `status_all` should be linked to your bin folder or otherwise added to your system PATH. Full path names to the desired git folders should be placed in `git_folders.txt`. Rofi is also needed for the click display.

In the polybar config I can then add the module as
```
[module/gitstatus]
type = custom/script
exec = ~/Git/GitStatus/poly_git
label = %output%  Git
interval = 15
click-left = ~/Git/GitStatus/status_click
```

The interval could of course be made longer as desired. If you want to change the bullet symbol in front or any of the colors, those need to be edited directly in the scripts at the moment. Your terminal of choice also needs to be changed at the end of `status_click` unless you are also using alacritty.

Honestly, I probably should have just written these all as various functions in a single Python script, but I was enjoying practicing / learning some bash scripting.
