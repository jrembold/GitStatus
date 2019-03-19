# GitStatus

---

I wrote this little script as a way of setting up notification indicators on my i3bar to ensure I don't forget to push class content at the end of a day. The script takes two non-optional arguments:

flag | Description
--- | ---
-f | The folder to check the git status of
-fn | The short name for the folder that will be output

In i3blocks I then call the script as:
```
[Mechanics]
command=<location of getstatus.py> -f <mechanics class folder> -fn Mech
interval=10
markup=pango
```

The interval could of course be made longer as desired. If you want to change the bullet symbol in front or any of the colors, those need to be edited directly in the script (lines 30-37).
