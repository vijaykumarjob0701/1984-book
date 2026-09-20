# Nineteen Eighty-Four — page-by-page English study guide

A learner-friendly companion to George Orwell's novel *Nineteen Eighty-Four* (also called *1984*). Each file in `pages/` covers **one page of a specific PDF edition** and offers:

- a short original summary
- difficult vocabulary
- short phrases with plain-English paraphrases

This repository is a **study aid only**. It is not a substitute for the novel.

## How to use the guide

1. Read the matching page from **your own legal copy** of the book (print, ebook, library, or other licensed edition).
2. Open the matching file in `pages/` (for example `pages/page-005.md` for PDF page 5).
3. Read the summary first if you want orientation, then study the vocabulary and phrases.
4. Track what is finished in [`PROGRESS.md`](PROGRESS.md).
5. Use [`vocab/glossary.md`](vocab/glossary.md) as a running word list.
6. Use [`chapters/index.md`](chapters/index.md) to jump from Part/Chapter to PDF page ranges.

Page numbers in this guide are **not** universal. They follow one 284-page PDF used while writing (front matter included). Other editions paginate differently. If your copy's page 5 is not the opening of Part One, Chapter 1, use the chapter index rather than raw page numbers.

Suggested study loop for each page:

1. Read the page in your book.
2. Check any words or phrases you could not parse.
3. Write one or two sentences of your own about what happened.
4. Compare with the summary here — if they disagree, re-read the page, not this file.

## What is in the repo

```
README.md              how to use the guide, copyright note
PROGRESS.md            which PDF pages are done vs remaining
pages/page-NNN.md      one study file per PDF page
chapters/index.md      Part/Chapter → PDF page ranges
vocab/glossary.md      cumulative hard words
templates/             shared page template for later work
```

Each completed novel page file has four sections: PDF page and Part/Chapter, summary (3–8 sentences), difficult vocabulary, and difficult phrases.

Front-matter pages (title, biography, license notices) are still given a short file so the numbering stays aligned with the PDF.

## Progress

See [`PROGRESS.md`](PROGRESS.md) for the live checklist. The first shipping goal is **all pages through the end of Part One, Chapter 1** (PDF pages 1–20 in this edition). This guide now covers **the whole of Part One** (PDF pages 1–96). Part Two begins at PDF page 97.

## Copyright and licence

*Nineteen Eighty-Four* remains **copyrighted in the United States** (and in other territories). GitHub is a US service. This repository therefore:

- does **not** include the novel PDF
- does **not** dump the book or long verbatim passages
- includes only original summaries, short quoted phrases or single words needed for vocabulary teaching, plus definitions and explanations

Learners should read from **their own legal copy**. Do not add the full text, chapter transcripts, or long quotations in pull requests.

The study-guide text in this repository (summaries, tables, and notes written for this project) is released under the [MIT License](LICENSE) so others can improve the teaching material. That licence does **not** grant any rights in Orwell's novel.

A Project Gutenberg of Australia notice appears in the source PDF's front matter. Public-domain status in Australia does **not** make the novel free to reproduce on GitHub.

## Contributing later pages

1. Read the target PDF page from a legal copy (do not paste the page into the repo).
2. Copy [`templates/page-template.md`](templates/page-template.md).
3. Write an accurate, page-only summary in your own words.
4. Add learner-level vocabulary and short phrases.
5. Update `PROGRESS.md`, `chapters/index.md` if a chapter boundary changes, and `vocab/glossary.md`.
6. Run `python3 templates/check-pages.py` to confirm required sections exist and quoted phrases stay short.
