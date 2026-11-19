# CLAUDE.md: CV and Cover Letter Workspace

## Purpose

This repo exists for one job: keep my CV current and tailor it, plus a cover letter, to specific job postings. Work here means one of:

1. Updating the master CV from new facts (projects, skills, experience).
2. Tailoring a CV version to a job posting.
3. Writing a cover letter for a job posting.
4. Auditing a CV or letter for accuracy, ATS fit, and clarity.

Nothing else belongs here. If a request is off-topic, say so and stop.

## Who I am (context for tone and targeting)

- <Your name, background and how you are learning or working now>
- <Core languages and tools today>
- <Target roles>
- <Location and work-authorization context; check each posting for language and on-site requirements and flag mismatches>

## Sources of truth (priority order)

1. `data/master_cv.md`: my canonical facts. Everything in a CV or letter must trace back here.
2. GitHub: https://github.com/<your_id>. Use it to verify projects, tech stack, dates, and which projects were solo vs team work.
3. LinkedIn: https://www.linkedin.com/in/<your_id>/. Use it for job titles, dates, and wording consistency. It may be blocked or login-gated. If it can't be read, say so and ask me to paste the relevant sections. Do not guess its content.
4. Job posting text saved in `jobs/<company>-<role>/posting.md`.

If sources conflict, do not pick one silently. List the conflict and ask me.

## Hard rules: honesty

- Never invent or inflate: employers, titles, dates, degrees, certifications, metrics, tools, or team sizes.
- Do not claim a skill I have only touched once as a core skill. Match the level the repo evidence supports (e.g. "used in a project" vs "proficient").
- Mark team projects as team projects. Mark school or course projects as such; don't present them as paid work.
- Metrics (users, speedups, uptime) only if they are in my data or I confirm them. Otherwise ask, or write the bullet without a number.
- If a job requires something I lack, say so in a gap report. Don't paper over it in the CV. In the cover letter, frame it honestly as "learning" or "adjacent experience" only when true.
- AI-assisted work: if a project was built with AI coding agents, don't describe it as hand-written. Wording should be accurate if asked in an interview.

## Repo layout (create if missing)

```
CLAUDE.md
data/
  master_cv.md          # canonical facts, all projects, all skills
  projects/<name>.md    # per-project detail: problem, stack, my role, outcome, link
  github_snapshot.md    # last verified GitHub summary + date
  linkedin_snapshot.md  # pasted/verified LinkedIn text + date
templates/
  cv_base.md            # CV structure
  cover_letter.md       # letter structure
jobs/<company>-<role>/
  posting.md            # raw posting text + URL + date saved
  analysis.md           # keywords, requirements, gap report
  cv.md                 # tailored CV
  cover_letter.md       # tailored letter (plain text, ready to paste)
  notes.md              # contacts, application status
output/<company>-<role>/  # final CV exports (PDF/DOCX) + cover letter (.txt)
```

Never edit `data/master_cv.md` as part of tailoring. Tailoring only writes inside `jobs/<company>-<role>/`. Changes to the master happen only in an explicit "update master" task.

## Workflows

### A. Update master CV
1. Read GitHub and LinkedIn (or snapshots), diff against `master_cv.md`.
2. Propose additions and changes as a list. Wait for my approval on anything not directly verifiable.
3. Apply approved changes. Update the snapshot dates.

### B. Tailor to a job posting
1. Save the posting to `jobs/<slug>/posting.md`.
2. Write `analysis.md`: must-have vs nice-to-have requirements, keywords to mirror, seniority signals, red flags, and a gap report (requirement → my evidence, or "no evidence").
3. Build `cv.md` from the master: reorder projects and skills by relevance, rewrite bullets with the posting's vocabulary where it is truthful, cut what doesn't help.
4. Run the audit (below).

### C. Cover letter
1. Requires `analysis.md` first.
2. Structure: one specific hook about the company or role, two short paragraphs of matched evidence from real projects, one honest line on growth areas if relevant, a brief close. Target 100 to 250 words.
3. Voice: direct, concrete, no filler. No "I am writing to express my interest" and no "passionate", "dynamic", "rockstar". Name actual projects and what I built.
4. Don't repeat the CV line by line. The letter adds the "why this role, why me".
5. Format: plain text for pasting into an application text box or an email body. No letterhead, address block or date; start at the greeting and end at the sign-off. No Markdown, bullets, bold or special characters that break in web forms (use straight quotes and plain hyphens). Paragraphs separated by one blank line. Never exported to PDF or ODT.

### D. Audit (run before declaring anything done)
- Every claim traced to the master, GitHub, or LinkedIn. List any untraceable claim.
- Dates, project names, and links are consistent across CV, letter, and LinkedIn.
- Keywords from the posting present where truthful.
- ATS-safe: single column, standard headings (Summary, Skills, Projects, Experience, Education), no tables for core content, no icons or images, plain-text-friendly.
- Length: CV at most 1 page unless I say otherwise. Letter 250 to 350 words, plain text.
- Spelling and consistent tense. Past tense for completed work.

## CV style

- Lead with projects, since experience is project-driven. Each project: name, one-line purpose, stack, 2 to 3 bullets on what I built and the result, link.
- Bullets: action verb + what + how/tech + outcome. No bullet longer than two lines.
- Skills section grouped (Languages, Tools/Infra, Practices), ordered by relevance to the posting.
- Education: state your school or programme accurately (type of programme, what was completed). Don't imply a degree you don't hold.
- Relevant to DevOps/sysadmin postings: surface Linux administration, VM setup and hardening, SSH/firewall, scripting and automation, monitoring, and any home lab work. Verify each against the repos before use.
- Relevant to AI/agentic postings: surface agentic workflow practice only where there is a real project to point to.
- Relevant to data analyst/engineer postings: surface SQL, Python, a relevant degree, data-checking work and log analysis. Use university statistics tools only once they are approved in the master.

## Skills and agents (build these as needed)

Suggested split. Each should be a small, single-purpose unit:

- `cv-sync`: pull GitHub/LinkedIn facts, diff against master, propose updates.
- `job-analyzer`: turn a posting into `analysis.md` with the gap report.
- `cv-tailor`: produce `jobs/<slug>/cv.md` from master + analysis.
- `cover-letter-writer`: produce the letter from analysis + master.
- `cv-auditor`: independent review agent. It must not have written the draft it reviews. It checks truthfulness and ATS fit and returns a pass/fail list.

Rule: the writer agents and the auditor must be separate so the work isn't grading itself.

## Output formats

- Working files: Markdown.
- CV file names always follow `<Name>_CV_<language>`, with language as `ENG` or `CZ` (e.g. `<Name>_CV_ENG.pdf`). The company never goes in the file name, since recruiters see it.
- Base CVs live in `base_cv/`: `<Name>_CV_<language>.odt` (for editing) and `.pdf` (for sending).
- Tailored CV: export to PDF (and DOCX if the posting asks) into `output/<company>-<role>/` as `<Name>_CV_<language>.pdf`. The folder keeps applications apart.
- Cover letter: plain text only, saved as `output/<company>-<role>/<Name>_CoverLetter_<language>.txt` for copy-pasting into a website text box or email. No PDF or ODT.
- Keep the file name pattern stable so applications are easy to find.

## Working preferences

- When I ask for code or scripts, give an outline or pseudocode first. Write exact code only when I ask for it.
- Ask before spending effort on anything ambiguous, such as which role variant to target or which projects to feature.
- Be blunt about weak points in my CV or a poor-fit posting. Honest feedback is more useful than encouragement.
- Don't send or submit anything on my behalf. Drafts only.
- Keep personal data minimal: no ID numbers, no home address in files unless I add it for a specific application.
- Keep git commits small, with messages like `tailor: <company> <role>` or `master: add <project>`.
