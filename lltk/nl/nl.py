#!/usr/bin/python
# -*- coding: UTF-8 -*-

__all__ = ['scrapers', 'scrape', 'pos', 'articles', 'plural', 'ipa', 'conjugate', 'gender', 'miniaturize']

import scrapers
from lltk.scraping import scrape
from lltk.decorators import language

ISO639_1 = 'nl'
scrape = language(ISO639_1)(scrape)

def pos(word):
	''' Returns a list of possible POS-tags (part-of-speech) for a given word. '''
	return scrape('pos', word)

def articles(word):
	''' Returns the articles (singular and plural) for a given noun. '''
	return scrape('articles', word)

def plural(word):
	''' Returns the plural version for a given noun. '''
	return scrape('plural', word)

def ipa(word):
	''' Returns the International Phonetic Alphabet (IPA) writing for a given word. '''
	return scrape('ipa', word)

def conjugate(word, tense = 'present'):
	''' Returns the conjugation of a given verb. '''
	return scrape('conjugate', word, tense)

def gender(word):
	''' Returns the gender for a given word. '''
	return scrape('gender', word)

def miniaturize(word):
	''' Returns the miniaturized version for a given word. '''
	return scrape('miniaturize', word)
