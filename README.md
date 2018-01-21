### Dot files for unix ricing

#### Tested using Arch Linux

## Requirements

- WM: [i3](https://github.com/i3/i3)
- DM: lightDM with [mini-greeter](https://github.com/prikhi/lightdm-mini-greeter)
- bar: [polybar](https://github.com/jaagr/polybar)
- lock: [i3lock-fancy](https://github.com/meskarune/i3lock-fancy)
- dotfile manager: [yadm](https://github.com/TheLocehiliosan/yadm)
- lock: [i3lock-fancy](https://github.com/meskarune/i3lock-fancy)

## Getting Started
- Install requirements
- cd into your home
- yadm clone https://github.com/NanoPish/nanodots.git
- change greeter-session=XXX to greeter-session=lightdm-mini-greeter in /etc/lightdm/lightdm.conf
- change user=prikhi to user=yourusername in /etc/lightdm/lightdm-mini-greeter.conf
