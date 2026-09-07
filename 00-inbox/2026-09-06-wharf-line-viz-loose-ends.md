---
type: idea-seed
status: unexplored
created: 2026-09-06
tags: [idea, visualization, steady-flux, future]
---

# Wharf-line visualization: loose ends after the first ship

Idea seed captured 2026-09-06 after `apps/steadyflux-wharf-line/` shipped (artifact published, badge in, 23-s MP4 clip delivered to Jesse for his contact at Steady Flux). The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** three things were left on the table. (1) The surveyed GPS route is an L-shape ending ~3,300 ft from the launch point, which contradicts the report's "launched and received at the same site"; the page plots the survey as given and says so, but the right answer is to ask Steady Flux which is wrong. (2) The opening overview scene is the weakest of the ten — dots on black with a faint thread; a stronger opener would change the first impression. (3) Recording is now a repeatable path (`apps/steadyflux-wharf-line/record.py`: Playwright drives installed Chrome, bundled ffmpeg encodes) but only from installed Chrome — Playwright's own Chromium cannot launch from the desktop app's virtualized AppData.

**To explore:** whether the CEO showing wants a portrait-phone cut of the clip; whether the odometer→route mapping should anchor to the short-joint clusters at the bends instead of scaling uniformly; whether this build becomes a template for other Steady Flux reports (the data block is verbatim text, so a second report is a data swap plus a new scene list).
