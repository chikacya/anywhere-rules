"""Build live Hub catalogs from rule files and their latest Git commits."""

import hashlib
import json
import re
import subprocess
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
NOW = datetime.now(ZoneInfo("Asia/Shanghai")).date().isoformat()
NAME = re.compile(r"^\s*name\s*=\s*(.+?)\s*$", re.MULTILINE | re.IGNORECASE)
ICON = re.compile(r"^\s*icon-light\s*=\s*([A-Za-z0-9+/=]+)\s*$", re.MULTILINE | re.IGNORECASE)


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True)


def last_commit_dates():
    dates = {}
    date = None
    for line in git("log", "--format=@@%cI", "--name-only", "--no-renames", "--", "rules/common", "mitm").splitlines():
        if line.startswith("@@"):
            date = datetime.fromisoformat(line[2:]).astimezone(ZoneInfo("Asia/Shanghai")).date().isoformat()
        elif line and date:
            dates.setdefault(line, date)
    dirty = set(git("diff", "--name-only", "HEAD", "--", "rules/common", "mitm").splitlines())
    dirty.update(git("ls-files", "--others", "--exclude-standard", "--", "rules/common", "mitm").splitlines())
    return dates, dirty


def resource_entry(path, dates, dirty):
    contents = (ROOT / path).read_bytes()
    source = contents.decode("utf-8")
    title = NAME.search(source)
    icon = ICON.search(source)
    entry = {
        "title": title.group(1) if title else path.stem,
        "icon": icon.group(1) if icon else "",
        "updated": NOW if path.as_posix() in dirty else dates.get(path.as_posix(), ""),
    }
    if path.suffix == ".amrs":
        script_without_icons = re.sub(r"^[ \t]*icon-(?:light|dark)[ \t]*=[ \t]*[A-Za-z0-9+/=]+[ \t]*\r?\n?", "", source, flags=re.MULTILINE | re.IGNORECASE)
        entry["version"] = hashlib.sha256(script_without_icons.encode("utf-8")).hexdigest()
    return entry


def reject_for(path, rejects):
    base = path.stem
    candidates = [base + "Reject.arrs", re.sub(r"(?:BlockAD|PriceUnlock|Unlock)$", "", base, flags=re.IGNORECASE) + "Reject.arrs"]
    return next((rejects[name.casefold()].as_posix() for name in candidates if name.casefold() in rejects), "")


def main():
    dates, dirty = last_commit_dates()
    modules_path = ROOT / "modules/index.json"
    modules = json.loads(modules_path.read_text()).get("modules", {}) if modules_path.exists() else {}
    modules_by_primary = {m["primary"]: m for m in modules.values()}
    common = sorted((ROOT / "rules/common").glob("*.arrs"))
    mitm = sorted((ROOT / "mitm").glob("*.amrs"))
    rejects = {path.name.casefold(): path.relative_to(ROOT) for path in (ROOT / "mitm").glob("*.arrs")}
    output = ROOT / "hub"
    output.mkdir(exist_ok=True)
    for kind, paths in (("common", common), ("mitm", mitm)):
        resources = {}
        for source in paths:
            path = source.relative_to(ROOT)
            entry = resource_entry(path, dates, dirty)
            if kind == "mitm":
                entry["reject"] = reject_for(path, rejects)
                module = modules_by_primary.get(path.as_posix())
                if module:
                    entry.update(module=module["path"], moduleVersion=module["sha256"], description=module["description"])
            resources[path.as_posix()] = entry
        (output / f"{kind}.json").write_text(
            json.dumps({"resources": resources}, ensure_ascii=False, separators=(",", ":")) + "\n",
            encoding="utf-8",
        )
        print(f"Updated hub/{kind}.json: {len(resources)} resources")


if __name__ == "__main__":
    main()
