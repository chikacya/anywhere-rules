# Anywhere Rules

Routing rule sets, MITM rules, and modules for [Anywhere](https://github.com/NodePassProject/Anywhere), maintained and converted from public sources.

[简体中文](README.zh-CN.md)

## About Anywhere

[Anywhere](https://github.com/NodePassProject/Anywhere) is a native proxy client built entirely with Swift. It has no Electron, no WebView, and is not a sing-box wrapper. It implements protocols directly from the lower layers, supports vless, trojan, hysteria, shadowsocks, http, and other mainstream protocols, and focuses on stability and performance.

## Contents

- [`rules/common/`](rules/common/) — curated routing rule sets for common services and uses (`.arrs`).
- [`rules/all/`](rules/all/) — routing rule sets converted from blackmatrix7 (`.arrs`); large sets are split into numbered parts.
- [`mitm/`](mitm/) — standalone MITM rule sets (`.amrs`) and associated routing rule sets (`.arrs`).
- [`modules/`](modules/) — modules (`.amod`) that combine MITM rules with their associated routing rules.
- [`hub/`](hub/) — metadata catalogs used by Anywhere Hub.
- [`scripts/`](scripts/) — rule conversion and catalog generation scripts.

## Usage

Visit [Anywhere Hub](https://anywhere-hub.chikacya.indevs.in/) to browse and import routing rule sets and MITM modules into Anywhere. The [Anywhere Hub repository](https://github.com/chikacya/anywhere-hub) contains more information about the service.

After importing routing rules, choose the policy that matches your configuration. Some sets specify an initial routing policy; others need one assigned in Anywhere.

MITM modules can include both MITM and associated routing rules. If you previously imported the same rules separately, disable the old copies to avoid duplicate matches. MITM rules are experimental and are provided for learning and research only. Only enable MITM for traffic you are allowed to inspect.

## Notes

Anywhere supports domain suffix, domain keyword, IPv4 and IPv6 CIDR, and process-name routing rules. Process-name rules match only on macOS. Rule types that cannot be represented in Anywhere are skipped during conversion; exact domain rules are converted to suffix rules and also match subdomains. See the [Anywhere routing documentation](https://github.com/NodePassProject/Anywhere/blob/main/Documentations/Routing.md) for matching behavior.

A custom routing rule set can contain at most 100,000 rules. Generated sets that exceed this limit are split into numbered parts.

## Thanks

Thanks to the upstream projects and authors who maintain public rules and scripts:

- blackmatrix7/ios_rule_script
- ACL4SSR/ACL4SSR
- SukkaW/Surge
- ConnersHua/RuleGo
- NobyDa/Script
- Loyalsoldier/v2ray-rules-dat
- Loyalsoldier/surge-rules
- Loyalsoldier/geoip
- TG-Twilight/AWAvenue-Ads-Rule
- limbopro/Adblock4limbo
- dler-io/Rules
- geekdada/surge-list
- fmz200/wool_scripts
- VirgilClyne/iRingo
- app2smile/rules
- and more
