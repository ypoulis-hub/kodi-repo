# YPoulis Kodi Repository

**One-click installer for the YPoulis Kodi add-ons. Install this repository once and Kodi will automatically pick up updates.**

[![License](https://img.shields.io/github/license/ypoulis-hub/kodi-repo)](LICENSE)
[![Kodi](https://img.shields.io/badge/Kodi-21%20Omega-blue)](https://kodi.tv/)
[![Pages](https://img.shields.io/badge/site-ypoulis--hub.github.io%2Fkodi--repo-green)](https://ypoulis-hub.github.io/kodi-repo/)

This repository serves [YouTube Music for Kodi](https://github.com/ypoulis-hub/kodi-youtube-music) and [MotoGP VideoPass for Kodi](https://github.com/ypoulis-hub/kodi-motogp-videopass) as a proper Kodi repository so you don't have to download and re-install the ZIPs each time there is an update.

[![Donate with PayPal](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://www.paypal.com/donate/?business=ypoulis%40gmail.com&currency_code=EUR)

---

## Install (one-time)

1. Download **`repository.ypoulis-1.0.0.zip`** from the [Releases page](https://github.com/ypoulis-hub/kodi-repo/releases/latest) (or directly from [the hosted folder](https://ypoulis-hub.github.io/kodi-repo/zips/repository.ypoulis/repository.ypoulis-1.0.0.zip)).
2. In Kodi, open **Settings → Add-ons → Install from zip file**.
3. Select the downloaded ZIP. Kodi will install **YPoulis Kodi Repository**.
4. Open **Install from repository → YPoulis Kodi Repository** and pick the add-on you want.
5. Enjoy automatic updates.

> First-timers may need to enable **Settings → System → Add-ons → Unknown sources** so Kodi will install ZIPs that are not from the official Kodi repo.

## What is hosted here

| Add-on | Latest |
|---|---|
| **`repository.ypoulis`** — this repository | 1.0.0 |
| **`plugin.audio.ytmusic`** — [YouTube Music for Kodi](https://github.com/ypoulis-hub/kodi-youtube-music) | 1.0.8 |
| **`plugin.video.motogp`** — [MotoGP VideoPass for Kodi](https://github.com/ypoulis-hub/kodi-motogp-videopass) | 0.2.0 |

The repository index (`addons.xml`) and add-on ZIPs are served via GitHub Pages from the [`docs/`](docs/) folder.

## How updates work

When you publish a new release of an add-on:

1. Drop its new ZIP into `docs/zips/<addon_id>/<addon_id>-<version>.zip`.
2. Run `python scripts/build_index.py` (regenerates `docs/addons.xml` and `docs/addons.xml.md5`).
3. Commit and push.

Kodi clients will pick the new version up on the next "check for updates" cycle (every few hours by default).

## Layout

```
kodi-repo/
├── repository.ypoulis/          # source of the repository add-on itself
│   ├── addon.xml
│   └── icon.png
├── docs/                        # served by GitHub Pages
│   ├── index.html               # landing page
│   ├── addons.xml               # repository index
│   ├── addons.xml.md5
│   └── zips/
│       ├── repository.ypoulis/
│       ├── plugin.audio.ytmusic/
│       └── plugin.video.motogp/
└── scripts/
    └── build_index.py
```

## License

[MIT](LICENSE) for the repository tooling. Each hosted add-on ships with its own MIT licence.
