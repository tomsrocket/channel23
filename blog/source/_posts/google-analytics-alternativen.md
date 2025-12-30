---
title: "Self Hosted Google Analytics Alternativen"
date: 2025-12-23
author: tom
categories:
- ["various"]
tags:
---

Ich brauche einen neuen "Besucherzähler" für meine Webseite. Google Analytics kommt nicht in Frage, denn ich möchte das datensparsam per Self-Hosting lösen. Es gibt unzählige Tools, die man dafür nutzen kann. Mein bisheriger Favorit "Fathom" ist kommerziell geworden und wird außerdem anscheinend nicht mehr weiterentwickelt. In diesem Blogpost habe ich Alternativen aufgelistet.

<!-- more -->

## Fathom
* War früher mal cool
* Ist jetzt kommerziell

## Umami
* Homepage: https://umami.is/
* Github: https://github.com/umami-software/umami
* Stats: 34.3k stars, 130 watching, 6.1k forks
* Lizenz: MIT
* Tech-Stack: Typescript, Postgres, (Redis optional)

## Goatcounter
* Homepage: https://www.goatcounter.com/
* Github: https://github.com/arp242/goatcounter
* Stats:  5.3k stars, 29 watching, 249 forks
* Lizenz: ~EUPL 1.2
* Tech-Stack: Go, Sqlite (optional Postgres)
* Nachteil: Sieht etwas altmodisch aus, und unterstützt mehrere Domain nicht, bzw. nur rudimentär: https://www.goatcounter.com/help/domains

## Rybbit
* Github: https://github.com/rybbit-io/rybbit
* Stats:  10.5k stars, 26 watching, 501 forks
* Tech-Stack: Typescript Frontend, Backend, Postgres, Clickhouse
* Lizenz: AGPL-3.0

## Plausible
* Homepage: https://plausible.io
* Github: https://github.com/plausible/analytics
* Stats: 24k stars, 136 watching, 1.3k forks, 118 Contributors
* Lizenz: AGPL-3.0
* Tech-Stack: Elixir, Postgres, Clickhouse
* Plausible Analytics Cloud vs. Plausible Community Edition

## Vince
* Homepage: https://www.vinceanalytics.com/
* Github: https://github.com/vinceanalytics/vince
* Stats: 2k stars, 7 watching, 71 forks
* Lizenz: AGPL-3.0

## Counter
* Homepage: https://counter.dev/
* Github: https://github.com/ihucos/counter.dev
* Stats: 982 stars, 10 watching, 46 forks
* Lizenz: AGPL-3.0
* Tech-Stack: Go + Redis
* Nachteil: Keine Dockerfile, seit 2 Jahren kein Update, extra Repo für Self Hosted Version

Blog Artikel mit etwas mehr Text zu dem Thema: https://aaronjbecker.com/posts/umami-vs-plausible-vs-matomo-self-hosted-analytics/
