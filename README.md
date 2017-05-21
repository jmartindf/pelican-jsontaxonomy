# pelican-jsontaxonomy #

Generate a JSON file with all of your blog's tags, categories, and posts. The format will be:

    {
        'tags': ["Tag 1", "Tag 2"],
        'categories': ["Category 1", "Category 2"],
        'posts': {
            "Post Title 1 [2017/05]": "posts/post-title1.md",
            "Post Title 2 [2017/04]": "posts/post-title2.md",
        }
    }

The file will be named `meta.json` and placed in the root of the output folder.

I've used the output for an [Editorial](http://omz-software.com/editorial/) workflow that can prompt for tags &amp; categories based on what I've already used on my blog.
