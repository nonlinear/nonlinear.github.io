## Requirements
- [Sublime Text](http://www.sublimetext.com) (2 or 3)
- [nonlinear/snippets](https://github.com/nonlinear/snippets/#snippets)

## Markdown snippets

|Shortcut|Description|
|---|---|
|`h1`|Heading 1|
|`h2`|Heading 2|
|`h3`|Heading 3|
|`h4`|Heading 4|
|`h5`|Heading 5|
|`h6`|Heading 6|
|`b`|Bold|
|`i`|Italic|
|`bq`|Blockquote|
|`strike`|Strikeout|
|`hr`|Horizontal Rule, Divider|
|`code`|Inline Code|
|`pre`|Code Block with language based highlighting.|
|`a`|Anchor|
|`img`|Image|
|`ol`|Ordered List|
|`ul`|Unordered List|
|`table`|Table|

A consolidated guide is available [here](http://praveenpuglia.github.io/github_markdown_snippets).

### Using with Emmet

If you have Emmet installed, tab triggers may not function as expected due to [this](https://github.com/sergeche/emmet-sublime#tab-key-handler).

To get around the problem, go to
```
Preferences > Package Settings > Emmet > User Settings
```
and add the following in your settings file.

```
{
    "disable_tab_abbreviations_for_scopes": "source.md"
}
```

This should let markdown snippets take precedence over emmet's tab to expand abbreviations feature and provide correct snippets.

Note that any tab trigger not set by this plugin will be converted to HTML tags which is convenient for people
who want to use HTML tags inside Markdown files.

##  Examples

**Bold Text**

*Italic Text*

> Put a nice, beautiful
> quote here...

~~Strike Through~~

---

```
code    // Inline Code
pre     // Code Block with language based highlighting.
```
`Inline Code Snippet`

```javascript
var message = "Code Block";
alert( message );
```

```
a      // Anchor
img    // Image
```
[Link Title](Link)

![Puppies are cute](https://c1.staticflickr.com/5/4112/5170590074_714d36db83_b.jpg)

```
ol       // Ordered List
ul       // Unordered List
table    // Table
```

1. First Item
2. Second Item
3. Third Item


- I
- Love
- Markdown

| Column 1 | Column 2 |
| ------------- | ------------- |
| Cell 1-1 | Cell 1-2 |
| Cell 2-1 | Cell 2-2 |