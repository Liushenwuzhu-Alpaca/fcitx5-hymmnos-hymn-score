# fcitx5-hymmnos-hymn-score

[中文](README.md)

A [fcitx5](https://fcitx-im.org) skin themed on the **Hymmnos language** from
Ar tonelico. Sister project:
[fcitx5-hymmnos-datastream](https://github.com/Liushenwuzhu-Alpaca/fcitx5-hymmnos-datastream).

**Hymn Score** Hymmnos glyph notes flow along a five-line staff, the **Power vowel `A`** badge sits at the upper left, the
highlighted candidate is a sixth note with a **Love vowel `E`** head

## Themes

| Theme | Preview |
|---|---|
| **Obsidian** (default dark) | ![obsidian](images/obsidian.png) |
| **Ivory** (default light) | ![ivory](images/ivory.png) |
| Nocturne | ![nocturne](images/nocturne.png) |
| Twilight | ![twilight](images/twilight.png) |
| Frost | ![frost](images/frost.png) |
| Verdant | ![verdant](images/verdant.png) |

## Installation

```bash
git clone https://github.com/Liushenwuzhu-Alpaca/fcitx5-hymmnos-hymn-score.git
cd fcitx5-hymmnos-hymn-score
./install.sh   # copies dist/* to ~/.local/share/fcitx5/themes and restarts fcitx5
```

Then pick `Hymmnos Hymn Score Obsidian` (dark) or `Hymmnos Hymn Score Ivory`
(light) in fcitx5 Configtool -> Addon -> Classic User Interface. Noto Sans CJK and
Noto Sans Mono CJK fonts are recommended.

## Regenerating

`dist/` is produced by a generator script (glyph outlines come from the bundled
Hymmnos font):

```bash
python3 scripts/generate_assets.py
```

## Disclaimer

Fan work, unaffiliated with GUST / Bandai Namco. Hymmnos and Ar tonelico belong to
their respective owners. The bundled font is only used to bake SVG outlines and is
not required at runtime.

## License

[MIT](LICENSE)
