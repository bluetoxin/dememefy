# dememefy

**dememefy** is a lightweight utility for creating demotivators from your own images or feed of popular social networks

* [Installation](#installation)
* [Supported Media](#supported-media)
* [Usage](#usage)
* [FAQ](#faq)

## Installation
```
pip install dememefy
```

## Supported Media

- Reddit 

## Usage

In "plain" mode you got to specify only image and text. 

```
$ cat pic1.jpg | dememefy --text "Is It Alive?" --open
```

In "social network" mode the utility parses specified social network and makes memes from feed more fun. So, first you need to generate correct credentials then set them in the config toml-file (you may see "config.toml.example") and pass filename and service to the utility.

```
$ dememefy -s reddit -c config.toml --open
```

**Flags:**

`--open/-o`

Force open generated demotivator(s). Disabled by default because it won't work for example inside Docker.

`--save-to/-st`

Path to save the generated demotivator(s).

## FAQ 

**How to get credentials?**

<p align="center">
<img src="https://miro.medium.com/max/1400/1*GQ8IREDENnkCRQT3VS55mQ.png">
</p><br>

For Reddit you need to create an "another app".

<p align="center">
<img src="https://miro.medium.com/max/1400/1*ssLYczSLGzfm6SPM7mWzBg.png">
</p><br>

Select "script".

<p align="center">
<img src="https://miro.medium.com/max/1400/1*khszOCCaCtqZ6jM19uhpiQ.png">
</p><br>

Copy credentials to config.toml file

<hr>

<p> This software is under BSD License, so you can do what you want. I mean, copy, modify, make money on it, literally everything. Contributions are also welcome.</p>
