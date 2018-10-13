---
title: Idea for an Overlay Journal Platform
tags: open science, open access, development
category: miscellaneous
permalink: 2018/10/idea-overlay-platform
layout: post
comments: true
---

Something that has been in the back of my mind for a while, an overlay journal platform. Started thinking about this more recently again and had some good discussion on [Scholar.Social](https://scholar.social/@drb/100882764015004813).

**TL;DR** Articles published (almost) anywhere, reviews conducted on Hypothes.is, status and meta-data stored on the platform

## Platform
The basic idea is that there is a platform similar to Reddit. Perhaps built using the open source [Postmill](https://postmill.xyz/).
1. Authors submit articles as link submissions on the platform.
1. On submission, the author also provides a text abstract and links to any connected data or code.
1. Links can be to just about anywhere that is web accessible. Could use a preprint server or even just their personal blog.
1. The comment section facilitates the peer-review process, but does not actually host the reviews.
1. Instead the reviews are conducted through [Hypothes.is](https://web.hypothes.is/).
1. This keeps the reviews accessible should the platform go down and also ties them directly to the article, wherever it lives.
1. If something like Postmill is used, the sub-community feature could allow disciplinary focus such as a sub-community for `mathematics` or something that allows for independent management.
1. The author edits their document after the reviews are complete and notifies when this is done.


## A bot
It would be helpful to have a bot or two to deal with a few maintenance things. Similar to how JOSS has [Whedon](https://github.com/openjournals/whedon).
1. An editor can be assigned and the editor can assign reviewers using the bot.
1. When a new article is posted, the bot checks the URL. If the article host is not archival (ie. on Arxiv or a preprint server or a repository), then the bot submits it to Internet Archive to get a stable version and comments with this link.
1. The bot creates a unique hashtag for use in Hypothes.is annotation and then embeds a Hypothes.is stream for that tag.
1. Reviewers can provide their Hypothes.is username, then when they conduct their review, a separate Hypostes.is stream is created for the "official" reviews.
1. After the article has been edited by the author. They notify the bot of the new version and this is archived as necessary.
1. Reviewers can indicate their review status to the bot (ie. accept, revise, etc.).
1. Once both reviewers accept, the bot can record the "final" version and grab a DOI.
