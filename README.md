# dememefy

**dememefy** is a lightweight utility for creating demotivators

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

This utility parses social networks and makes memes from their feeds more fun. So for using this util you need to generate tokens for parsing and pass them it to the utility. There are two ways to pass credentials: keys and toml file. The second one is more convenient tho. So, first you need to generate correct data then set the data in the config file and use a pipeline to pass it to the utility.

```
$ cat <config.toml> | dememefy -s reddit
```
## FAQ 

**How to get credentials?**

<h1 align="center">
<img src="https://miro.medium.com/max/1400/1*GQ8IREDENnkCRQT3VS55mQ.png">
</h1><br>

For Reddit you need to create an "another app".

<h1 align="center">
<img src="https://miro.medium.com/max/1400/1*ssLYczSLGzfm6SPM7mWzBg.png">
</h1><br>

Select "script".

<h1 align="center">
<img src="https://miro.medium.com/max/1400/1*khszOCCaCtqZ6jM19uhpiQ.png">
</h1><br>

Copy all data to config.toml file

<hr>

<h6> This software is under BSD License, so you can do what you want. I mean, copy, modify, make money on it, literally everything. Contributions are welcome :)</h6>