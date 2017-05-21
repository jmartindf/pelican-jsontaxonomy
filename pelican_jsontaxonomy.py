#!/usr/bin/env python
# encoding: utf-8

"""
JSON based Metadata Generator for Pelican.
"""

from __future__ import unicode_literals

import six
from jinja2 import Markup
from pelican import signals
from pelican.writers import Writer
from pelican.generators import Generator
import json
import os.path

def metadata_loop(generator,writer):
	file_name = "meta.json"
	output_root = generator.settings['OUTPUT_PATH']
	input_root = generator.settings['PATH']

	cat_index = []
	tag_index = []
	title_index = {}

	for tag in generator.tags:
		tag_index.append(tag.name)
	for category, articles in generator.categories:
		cat_index.append(category.name)

	for article in generator.articles:
		# Post Title [Year/Month]
		title = article.title
		date = article.date.strftime("%Y/%m")
		title_index["%s [%s]" % (title,date)] = os.path.relpath(article.source_path,input_root)

	sorted_cats = sorted(cat_index)
	sorted_tags = sorted(tag_index)
	with open(os.path.join(output_root,file_name),"w") as fp:
		json.dump( {
			"tags":sorted_tags,
			"cats":sorted_cats,
			"posts":title_index}
		,fp)


def register():
	"""Registers the module function `metadata_loop`."""
	signals.article_writer_finalized.connect(metadata_loop)
