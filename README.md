# MetaDECK

![MetaDECK Logo](src/gui/img/Metadeck_LOGO.png)

A fork of [Steam Metadata Editor](https://github.com/tralph3/Steam-Metadata-Editor) by tralph3, redesigned and compiled specifically for **SteamOS on Steam Deck**.

MetaDECK lets you rename your Steam games and add custom launch menu options — just like SteamEdit used to do on Windows.

---

## Features

- Rename any Steam game in your library
- Add or edit launch menu options
- Silent background patching on boot via autostart
- Splash screen on launch
- Fully standalone — no Distrobox, no Flatpak, no dependencies needed
- Native SteamOS dark green theme

---

## Installation

1. Download `metadeck.sh` from the [Releases](../../releases) page
2. Move it to a permanent location:
   ```bash
   mkdir -p ~/Applications
   mv ~/Downloads/metadeck.sh ~/Applications/metadeck.sh
   chmod +x ~/Applications/metadeck.sh
   ```
3. Run it:
   ```bash
   bash ~/Applications/metadeck.sh
   ```

---

## Autostart (Silent Patching on Boot)

To automatically patch your metadata every time you boot into Desktop Mode:

1. Open **System Settings > Autostart**
2. Click **Add New > Login Script**
3. Set the command to:
   ```
   bash /home/deck/Applications/metadeck.sh --splash-only
   ```
4. Click OK

This will show the MetaDECK splash screen for 2 seconds on every login, silently patch your metadata, then close automatically.

---

## Usage

- **Open GUI:** `bash metadeck.sh`
- **Silent patch only (autostart):** `bash metadeck.sh --splash-only`

---

## How it Works

MetaDECK edits Steam's `appinfo.vdf` file located at:
```
~/.local/share/Steam/appcache/appinfo.vdf
```

Your modifications are saved to:
```
~/.local/share/Steam-Metadata-Editor/config/modifications.json
```

---

## Limitations

- Cannot create launch options for games with no Linux depot on Steam
- Cannot add/edit launch options for Non-Steam games
- Cannot rename the first launch option of a game
- Some pre-existing launch options cannot be removed or renamed

---

## Credits

- Original app by [tralph3](https://github.com/tralph3/Steam-Metadata-Editor)
- MetaDECK fork — theme, splash screen, autostart patching, and SteamOS compilation

---

## License

GPL — same as the original project.
