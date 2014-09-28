mtts
====

Mulit Tab Triggers for Sublime 3 snippets

I know its a bit ridiculous but since sublime snippets does not support multiple keywords as tab triggers i made this as workaround.

This plugin provides window command that generates snippets for every keyword specified in 
```
<multiTabTrigger></multiTabTrigger>
```
snippet tag.

Usage:
* install plugin by cloning this repo inside your sublime package dir
* for each snippet that you want to make subject to multi tabs trigger add 
```
<multiTabTrigger>some trigger 1, some trigger 2</multiTabTrigger>
```
tag to your snippet
* type 
```
window.run_command("mtts")
```

Also, you need to set up a sublime project in order to use this plugin.
Settings:

* `mtts_output` : path to directory for generated snippets. Relative to project file.
* `mtts_source` : plugin starts recursive search for all snippets from provided path. Relative to project file.

If still confused, please check my [Haxime plugin](https://github.com/mikomize/haxime), project file.
