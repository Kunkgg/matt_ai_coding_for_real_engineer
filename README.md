## 哔哩哔哩音频转文字

1. 导出浏览器的 cookies.txt 文件，放在项目根目录下。需要安装 [Get cookies.txt LOCALLY](https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc?hl=en-US&utm_source=ext_sidebar)
2. 下载音频, 将下载的音频文件放在 `audio` 文件夹下

```
yt-dlp --cookies ../www.bilibili.com_cookies.txt -f ba -o "%(playlist_index)03d-%(title)s.%(ext)s" "https://www.bilibili.com/video/BV1Y6Ju6vEeN"
```
3. 运行 `python convert.py`，将音频文件转换为字幕文件（.srt）
4. 运行 `python merge_subs.py`，将字幕文件合并为一个字幕文件（merged_subs.md）