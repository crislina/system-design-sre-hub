# System Design & SRE Knowledge Hub

A Chinese-first, mobile-friendly, searchable static knowledge base for Senior / Staff SRE interviews.

## Deploy to GitHub Pages

1. Create an empty GitHub repository, e.g. `system-design-sre-hub`.
2. Upload **the contents of this folder** to the repository root on the `main` branch (including `.github`).
3. In repository **Settings → Pages → Build and deployment**, choose **GitHub Actions**.
4. In **Actions**, run `Publish Knowledge Hub` if it has not started automatically.
5. The website will appear at `https://<username>.github.io/<repository>/` (after deployment).

## Daily automation (22:00 SGT)

`.github/workflows/nightly.yml` runs at 14:00 UTC daily. It validates knowledge entries, optionally merges `content/inbox.json` into `topics.json`, updates the last-updated timestamp and commits changes. The commit triggers the Pages deployment workflow. Scheduled GitHub jobs can be delayed.

**Important:** GitHub Actions cannot read private ChatGPT conversations by itself. This version does **not** automatically ingest chat messages, summarize conversations with AI, or upload new discussions without an input feed. To update from a conversation, prepare a reviewed `content/inbox.json` containing a JSON array of entries in the same schema as `content/topics.json`, commit it, then run `Nightly Knowledge Refresh` (or wait for the scheduled run). The workflow merges entries by `id`, replacing a matching topic. Avoid including confidential employer incident details or credentials.

For fully automated ingestion, add a separately authorized data source/export or integration that sends curated notes to the repository, then optionally add a summarization job with a securely stored API key and human review. Do not assume a ChatGPT account gives GitHub Actions access to conversation history.

## Local preview

```bash
python -m http.server 8000
```

Open `http://localhost:8000`. No Node.js or build dependencies required.

## Content model

Each topic: `id`, `category`, `title`, `level`, `summary`, `sections` (array of `heading` and `body`).

## Editorial roadmap

- Add topic-level diagrams and references.
- Add quiz / interview scenario cards and progress tracking.
- Add review status, source discussion dates and revision history.
- Establish an authorized daily discussion-to-inbox pipeline.
