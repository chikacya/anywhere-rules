#!/usr/bin/env python3
"""Build a compact Anywhere common rules catalog."""

from __future__ import annotations

import argparse
import ipaddress
import json
import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

from convert_blackmatrix7 import convert_line, fetch_bytes, split_rule_line


MAX_RULES_PER_SET = 100000
PRESERVED_COMMON_RULE_GLOBS = ("CN_Accelerated*.arrs",)


COMMON_RULE_SETS: list[dict[str, object]] = [
    {
        "name": "Reject",
        "description": "广告、恶意站点和跟踪拦截基础集合",
        "routing": 2,
        "sources": [
            "https://raw.githubusercontent.com/ConnersHua/RuleGo/master/Surge/Ruleset/Extra/Reject/Advertising.list",
            "https://raw.githubusercontent.com/ConnersHua/RuleGo/master/Surge/Ruleset/Extra/Reject/Malicious.list",
            "https://raw.githubusercontent.com/ConnersHua/RuleGo/master/Surge/Ruleset/Extra/Reject/Tracking.list",
            "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanEasyListChina.list",
            "https://raw.githubusercontent.com/Repcz/Tool/X/Surge/Custom/Reject.list",
        ],
    },
    {
        "name": "Ads_AWAvenue",
        "description": "秋风广告规则 AWAvenue",
        "routing": 2,
        "sources": [
            "https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/Filters/AWAvenue-Ads-Rule-Surge.list",
        ],
    },
    {
        "name": "AI",
        "description": "常见 AI 服务",
        "sources": [
            "https://ruleset.skk.moe/List/non_ip/ai.conf",
            "https://raw.githubusercontent.com/Repcz/Tool/X/Surge/Custom/xAI.list",
            "https://raw.githubusercontent.com/Repcz/Tool/X/Surge/Custom/AI.list",
            "local:common/sources/AI.synara-usage.list",
        ],
    },
    {
        "name": "Proxy",
        "description": "常用代理域名集合",
        "sources": [
            "https://ruleset.skk.moe/List/non_ip/global.conf",
            "https://raw.githubusercontent.com/Repcz/Tool/X/Surge/Custom/Proxy.list",
        ],
    },
    {
        "name": "ProxyGFW",
        "description": "GFW 代理集合",
        "sources": [
            "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ProxyGFWlist.list",
            "https://ruleset.skk.moe/List/non_ip/global.conf",
        ],
    },
    {
        "name": "GFW",
        "description": "GFW 域名列表",
        "sources": [
            "https://raw.githubusercontent.com/Loyalsoldier/v2ray-rules-dat/release/gfw.txt",
        ],
    },
    {
        "name": "Direct",
        "description": "常用直连补充",
        "routing": 1,
        "sources": [
            "https://raw.githubusercontent.com/Repcz/Tool/X/Surge/Custom/Direct.list",
        ],
    },
    {
        "name": "AppleCN",
        "description": "苹果中国和苹果 CDN 直连",
        "routing": 1,
        "sources": [
            "https://ruleset.skk.moe/List/non_ip/apple_cn.conf",
            "https://ruleset.skk.moe/List/non_ip/apple_cdn.conf",
        ],
    },
    {
        "name": "AppleProxy",
        "description": "需要代理的苹果服务",
        "sources": [
            "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/AppleProxy/AppleProxy.list",
        ],
    },
    {
        "name": "Apple",
        "description": "苹果基础服务",
        "sources": [
            "https://raw.githubusercontent.com/NobyDa/Script/master/Surge/Apple.list",
        ],
    },
    {
        "name": "AppleServices",
        "description": "苹果系统服务",
        "sources": [
            "https://ruleset.skk.moe/List/non_ip/apple_services.conf",
        ],
    },
    {
        "name": "AppleMusic",
        "description": "Apple Music",
        "sources": [
            "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/AppleMusic/AppleMusic.list",
        ],
    },
    {
        "name": "Google",
        "description": "Google 服务",
        "sources": [
            "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/Google.list",
        ],
    },
    {
        "name": "YouTube",
        "description": "YouTube",
        "sources": [
            "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/YouTube.list",
        ],
    },
    {
        "name": "Microsoft",
        "description": "Microsoft 服务",
        "sources": [
            "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/Microsoft.list",
        ],
    },
    {
        "name": "GitHub",
        "description": "GitHub",
        "sources": [
            "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/Github.list",
        ],
    },
    {
        "name": "OneDrive",
        "description": "OneDrive",
        "sources": [
            "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/OneDrive.list",
        ],
    },
    {
        "name": "Telegram",
        "description": "Telegram 域名与 IP",
        "sources": [
            "https://raw.githubusercontent.com/Repcz/Tool/X/Surge/Custom/Telegram.list",
        ],
    },
    {
        "name": "Telegram_NoIP",
        "description": "Telegram 域名，不含 IP",
        "sources": [
            "https://raw.githubusercontent.com/Repcz/Tool/X/Surge/Custom/Telegram_NoIP.list",
        ],
    },
    {
        "name": "Twitter",
        "description": "X / Twitter",
        "sources": [
            "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/Twitter.list",
        ],
    },
    {
        "name": "Instagram",
        "description": "Instagram",
        "sources": [
            "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/Instagram.list",
        ],
    },
    {
        "name": "Facebook",
        "description": "Facebook",
        "sources": [
            "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/Facebook.list",
        ],
    },
    {
        "name": "Netflix",
        "description": "Netflix",
        "sources": [
            "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/Netflix.list",
        ],
    },
    {
        "name": "Disney",
        "description": "Disney+",
        "sources": [
            "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Disney/Disney.list",
        ],
    },
    {
        "name": "Spotify",
        "description": "Spotify",
        "sources": [
            "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Spotify/Spotify.list",
        ],
    },
    {
        "name": "TikTok",
        "description": "TikTok",
        "sources": [
            "https://raw.githubusercontent.com/Repcz/Tool/X/Surge/Rules/TikTok.list",
        ],
    },
    {
        "name": "Bilibili",
        "description": "Bilibili",
        "routing": 1,
        "sources": [
            "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/Bilibili.list",
        ],
    },
    {
        "name": "WeChat",
        "description": "WeChat",
        "routing": 1,
        "sources": [
            "https://raw.githubusercontent.com/NobyDa/Script/master/Surge/WeChat.list",
        ],
    },
    {
        "name": "ChinaDomain",
        "description": "中国大陆常见域名直连",
        "routing": 1,
        "sources": [
            "https://ruleset.skk.moe/List/non_ip/domestic.conf",
        ],
    },
    {
        "name": "CN_Additional",
        "description": "中国大陆域名补充",
        "routing": 1,
        "sources": [
            "https://static-file-global.353355.xyz/rules/cn-additional-list.txt",
        ],
    },
    {
        "name": "ChinaIP",
        "description": "中国大陆 IP CIDR",
        "routing": 1,
        "sources": [
            "https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/ruleset/cncidr.txt",
        ],
    },
    {
        "name": "Lan",
        "description": "局域网和私有地址",
        "routing": 1,
        "sources": [
            "https://raw.githubusercontent.com/Repcz/Tool/X/Surge/Custom/Lan.list",
        ],
    },
    {
        "name": "Game",
        "description": "游戏平台集合",
        "sources": [
            "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Game/Game.list",
        ],
    },
    {
        "name": "Steam",
        "description": "Steam",
        "sources": [
            "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Steam/Steam.list",
        ],
    },
    {
        "name": "PayPal",
        "description": "PayPal",
        "sources": [
            "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/PayPal/PayPal.list",
        ],
    },
    {
        "name": "Cloudflare",
        "description": "Cloudflare",
        "sources": [
            "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Cloudflare/Cloudflare.list",
        ],
    },
]


@dataclass
class BuiltCommonRuleSet:
    name: str
    description: str
    output_path: str
    rule_count: int
    skipped_count: int
    unsupported_types: dict[str, int] = field(default_factory=dict)
    sources: list[str] = field(default_factory=list)


def preserve_external_common_rules(output_dir: Path) -> dict[str, bytes]:
    preserved: dict[str, bytes] = {}
    if not output_dir.exists():
        return preserved
    for pattern in PRESERVED_COMMON_RULE_GLOBS:
        for path in output_dir.glob(pattern):
            if path.is_file():
                preserved[path.name] = path.read_bytes()
    return preserved


def parse_existing_rule_set(output_dir: Path, path: Path) -> BuiltCommonRuleSet:
    headers: dict[str, str] = {}
    sources: list[str] = []
    rule_count = 0
    in_sources = False

    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if line.startswith("# SOURCES:"):
            in_sources = True
            continue
        if in_sources and line.startswith("# - "):
            sources.append(line[4:].strip())
            continue
        if line.startswith("# ") and ":" in line:
            key, value = line[2:].split(":", 1)
            headers[key.strip().upper()] = value.strip()
            in_sources = False
            continue
        if line and not line.startswith("#") and not line.startswith("name") and not line.startswith("routing"):
            rule_count += 1

    name = headers.get("NAME", path.stem)
    description = headers.get("DESCRIPTION", "")
    try:
        rule_count = int(headers.get("RULES", rule_count))
    except ValueError:
        pass
    try:
        skipped_count = int(headers.get("SKIPPED", "0"))
    except ValueError:
        skipped_count = 0

    return BuiltCommonRuleSet(
        name=name,
        description=description,
        output_path=path.relative_to(output_dir.parent).as_posix(),
        rule_count=rule_count,
        skipped_count=skipped_count,
        unsupported_types={},
        sources=sources,
    )


ALIASES = {
    "HOST": "DOMAIN",
    "HOST-SUFFIX": "DOMAIN-SUFFIX",
    "HOST-KEYWORD": "DOMAIN-KEYWORD",
    "HOST-WILDCARD": "DOMAIN-WILDCARD",
    "IP6-CIDR": "IP-CIDR6",
}

SOURCE_MARKER_DOMAINS = {
    "this_rule_set_is_made_by_sukkaw",
    "this_ruleset_is_made_by_sukkaw",
    "this_ruleset_is_made_by_sukkaw.ruleset.skk.moe",
    "th1s_rule5et_1s_m4d3_by_5ukk4w_ruleset.skk.moe",
    "this_rule_set_is_made_by_sukkaw.skk.moe",
    "7h1s_rul35et_i5_mad3_by_5ukk4w-ruleset.skk.moe",
}


def clean_line(raw: str) -> str | None:
    line = raw.strip()
    if not line or line.startswith("#") or line.startswith(";"):
        return None
    if line in {"payload:", "rules:", "rule-providers:"}:
        return None
    if line.startswith("- "):
        line = line[2:].strip()
    if line.startswith("'") and line.endswith("'"):
        line = line[1:-1].strip()
    if line.startswith('"') and line.endswith('"'):
        line = line[1:-1].strip()
    line = re.sub(r"\s+#.*$", "", line)
    line = re.sub(r"\s+//.*$", "", line)
    return line.strip() or None


def infer_bare_rule(line: str) -> str | None:
    bare = line.strip().strip("'\"")
    if not bare:
        return None
    if bare.startswith("."):
        return f"DOMAIN-SUFFIX,{bare[1:]}"
    if bare.startswith("+."):
        return f"DOMAIN-SUFFIX,{bare[2:]}"
    try:
        network = ipaddress.ip_network(bare, strict=False)
    except ValueError:
        network = None
    if network is not None:
        return f"IP-CIDR6,{bare}" if network.version == 6 else f"IP-CIDR,{bare}"
    if "," not in bare and "." in bare and " " not in bare:
        return f"DOMAIN,{bare}"
    return bare


def normalize_rule_syntax(line: str) -> str | None:
    line = infer_bare_rule(line)
    if line is None:
        return None
    fields = split_rule_line(line)
    if not fields:
        return None
    rule_type = ALIASES.get(fields[0].upper(), fields[0].upper())
    if len(fields) == 1:
        return infer_bare_rule(fields[0])
    value = fields[1]
    return f"{rule_type},{value}"


def convert_lines(lines: Iterable[str]) -> tuple[list[tuple[int, str]], dict[str, int]]:
    seen: set[tuple[int, str]] = set()
    rules: list[tuple[int, str]] = []
    unsupported: dict[str, int] = {}
    for raw in lines:
        cleaned = clean_line(raw)
        if cleaned is None:
            continue
        normalized = normalize_rule_syntax(cleaned)
        if normalized is None:
            continue
        converted, skipped_type = convert_line(normalized)
        if converted is not None and converted[1] in SOURCE_MARKER_DOMAINS:
            continue
        if converted is not None and converted not in seen:
            seen.add(converted)
            rules.append(converted)
        elif skipped_type:
            unsupported[skipped_type] = unsupported.get(skipped_type, 0) + 1
    return rules, unsupported


def fetch_source_lines(source: str) -> list[str]:
    if source.startswith("local:"):
        relative = source.removeprefix("local:")
        path = Path(__file__).resolve().parent.parent / "rules" / relative
        return path.read_text(encoding="utf-8-sig").splitlines()
    return fetch_bytes(source, token=None).decode("utf-8-sig", errors="replace").splitlines()


def write_rule_set_file(
    output: Path,
    name: str,
    description: str,
    rules: list[tuple[int, str]],
    sources: list[str],
    unsupported: dict[str, int] | None = None,
    total_rules: int | None = None,
    routing: int | None = None,
) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    body = [
        f"# NAME: {name}",
        "# GENERATED-FOR: Anywhere Routing Rule Set",
        f"# DESCRIPTION: {description}",
        f"# RULES: {len(rules)}",
        f"# SKIPPED: {sum((unsupported or {}).values())}",
    ]
    if total_rules is not None and total_rules != len(rules):
        body.append(f"# SOURCE-RULES: {total_rules}")
    if unsupported:
        body.append(
            "# SKIPPED-TYPES: "
            + ", ".join(f"{key}={unsupported[key]}" for key in sorted(unsupported))
        )
    body.append("# SOURCES:")
    body.extend(f"# - {source}" for source in sources)
    body.extend(["", f"name = {name}"])
    if routing is not None:
        body.append(f"routing = {routing}")
    body.extend(f"{rule_type}, {value}" for rule_type, value in rules)
    output.write_text("\n".join(body) + "\n", encoding="utf-8")


def build_rule_set_outputs(
    name: str,
    description: str,
    rules: list[tuple[int, str]],
    unsupported: dict[str, int],
    sources: list[str],
    output_dir: Path,
    routing: int | None,
) -> list[BuiltCommonRuleSet]:
    if len(rules) <= MAX_RULES_PER_SET:
        output = output_dir / f"{name}.arrs"
        write_rule_set_file(output, name, description, rules, sources, unsupported, routing=routing)
        return [
            BuiltCommonRuleSet(
                name=name,
                description=description,
                output_path=output.relative_to(output_dir.parent).as_posix(),
                rule_count=len(rules),
                skipped_count=sum(unsupported.values()),
                unsupported_types=unsupported,
                sources=sources,
            )
        ]

    chunks = [
        rules[index:index + MAX_RULES_PER_SET]
        for index in range(0, len(rules), MAX_RULES_PER_SET)
    ]
    built: list[BuiltCommonRuleSet] = []
    for index, chunk in enumerate(chunks, start=1):
        part_name = f"{name}_{index:02d}"
        part_description = f"{description}（分片 {index}/{len(chunks)}）"
        output = output_dir / f"{part_name}.arrs"
        part_unsupported = unsupported if index == 1 else {}
        write_rule_set_file(
            output,
            part_name,
            part_description,
            chunk,
            sources,
            part_unsupported,
            total_rules=len(rules),
            routing=routing,
        )
        built.append(
            BuiltCommonRuleSet(
                name=part_name,
                description=part_description,
                output_path=output.relative_to(output_dir.parent).as_posix(),
                rule_count=len(chunk),
                skipped_count=sum(part_unsupported.values()),
                unsupported_types=part_unsupported,
                sources=sources,
            )
        )
    return built


def build_rule_set(config: dict[str, object], output_dir: Path) -> list[BuiltCommonRuleSet]:
    name = str(config["name"])
    description = str(config.get("description", ""))
    routing_value = config.get("routing")
    routing = int(routing_value) if routing_value is not None else None
    sources = [str(url) for url in config.get("sources", [])]
    all_lines: list[str] = []
    for source in sources:
        all_lines.extend(fetch_source_lines(source))
        all_lines.append("")

    rules, unsupported = convert_lines(all_lines)
    return build_rule_set_outputs(name, description, rules, unsupported, sources, output_dir, routing)


def write_catalog(output_dir: Path, built: list[BuiltCommonRuleSet]) -> None:
    lines = [
        "# Anywhere Common Rules",
        "",
        "常用规则集目录。",
        "",
        "| Name | Rules | Skipped | Description | File |",
        "| --- | ---: | ---: | --- | --- |",
    ]
    for item in built:
        description = item.description.replace("|", "\\|")
        lines.append(
            f"| {item.name} | {item.rule_count} | {item.skipped_count} | "
            f"{description} | [{item.output_path}](./{Path(item.output_path).name}) |"
        )
    (output_dir / "catalog.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dist", default="rules")
    args = parser.parse_args()

    dist = Path(args.dist)
    output_dir = dist / "common"
    preserved = preserve_external_common_rules(output_dir)
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    built: list[BuiltCommonRuleSet] = []
    for config in COMMON_RULE_SETS:
        built.extend(build_rule_set(config, output_dir))
    for name, data in preserved.items():
        restored = output_dir / name
        restored.write_bytes(data)
        built.append(parse_existing_rule_set(output_dir, restored))
    index = {
        "total_files": len(built),
        "total_rules": sum(item.rule_count for item in built),
        "total_skipped": sum(item.skipped_count for item in built),
        "files": [
            {
                "name": item.name,
                "description": item.description,
                "output_path": item.output_path,
                "rule_count": item.rule_count,
                "skipped_count": item.skipped_count,
                "unsupported_types": item.unsupported_types,
                "sources": item.sources,
            }
            for item in built
        ],
    }
    (output_dir / "index.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_catalog(output_dir, built)
    print(
        f"Built {index['total_files']} common files, "
        f"{index['total_rules']} rules, skipped {index['total_skipped']} entries."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
