# Changelog

All notable changes to **Akana Qt** are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/); versioning follows
[SemVer](https://semver.org/). Aligned with web Akana tags where practical.

## [0.5.0] - 2026-07-16

### Added
- **DESIGN.md**, **AGENTS.md**, **TOKENS.md**, **CHANGELOG.md** (design-system docs parity with web).
- Theme persistence via `QSettings` (`load_saved_theme` / `set_theme` persist).
- Semantic `ink_hover` / `ink_active` for primary button affordance without hue.
- `FS["4xl"]`, `CONTROL_H` (44), field label object name `akFieldLabel`.
- Overview **cards** row (icon mark + title + body + action) matching web `.ak-card`.
- Editorial content column capped at `MAX_W` (1080).
- Placeholder text palette applied on theme refresh.
- `setup_venv.py` entry for explicit environment bootstrap.

### Changed
- Version **0.3.x → 0.5.0** (web Akana v0.5 component/pattern parity).
- Page titles: weight 700 / size 3xl (web h1).
- Lead text: size lg, max ~60ch.
- Button / input / select / card QSS closer to web `components.css`.
- Modal body spacing and monochrome shadow balance for light/dark.
- Gallery meta/version strings use package `__version__`.

### Fixed
- Primary buttons no longer lacked hover/press feedback in QSS.
- Input/select heights locked to web 44px control height.

## [0.3.1] - 2026-07-15

### Fixed
- Frameless gallery UI polish and Windows window chrome / snap.

## [0.3.0] - 2026-07-15

### Added
- Initial Akana Qt design system: tokens, theme, QSS, IBM Plex TTF.
- Components: button, card, input, badge, nav, modal, toggle, table,
  checkbox, radio, select, textarea, tabs, alert, accordion, breadcrumb,
  pagination, empty-state, titlebar, showcase.
- Demo gallery pages: Overview · Buttons · Forms · Feedback · Data · Patterns.
