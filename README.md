# fcitx5-hymmnos-hymn-score

[English](README.en.md)

以《魔塔大陆》(Ar tonelico) **Hymmnos 语**为主题的 fcitx5 输入法皮肤,姊妹篇:
[fcitx5-hymmnos-datastream](https://github.com/Liushenwuzhu-Alpaca/fcitx5-hymmnos-datastream)。

**诗谱 (Hymn Score)** -- 五线谱上流淌着 Hymmnos 字形音符,左上角是**力音 `A`** 徽章,候选高亮是六分音符配**爱音 `E`** 符头

## 主题

| 主题 | 预览 |
|---|---|
| **Obsidian** (默认深色) | ![obsidian](images/obsidian.png) |
| **Ivory** (默认浅色) | ![ivory](images/ivory.png) |
| Nocturne | ![nocturne](images/nocturne.png) |
| Twilight | ![twilight](images/twilight.png) |
| Frost | ![frost](images/frost.png) |
| Verdant | ![verdant](images/verdant.png) |

## 安装

```bash
git clone https://github.com/Liushenwuzhu-Alpaca/fcitx5-hymmnos-hymn-score.git
cd fcitx5-hymmnos-hymn-score
./install.sh   # 复制 dist/* 到 ~/.local/share/fcitx5/themes 并重启 fcitx5
```

然后在 fcitx5 配置 → 附加组件 → 经典用户界面中选择
`Hymmnos Hymn Score Obsidian`(深色)或 `Hymmnos Hymn Score Ivory`(浅色),
亦可搭配 datastream 系列混搭。

建议安装 Noto Sans CJK 与 Noto Sans Mono CJK 字体以获得最佳效果。

## 重新生成

`dist/` 由生成脚本产出(字形取自自带的 Hymmnos 字体):

```bash
python3 scripts/generate_assets.py   # 需要 python3,字体文件与字形轮廓已在仓库内
```

## 声明

粉丝作品,与 GUST / 万代南梦宫无关。Hymmnos 语与《魔塔大陆》相关权利归原作者所有。
字体文件来自公开的 Hymmnos 字库,仅用于生成 SVG 轮廓,运行时不再需要。

## 许可

[MIT](LICENSE)
