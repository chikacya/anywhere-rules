# Anywhere Rules

Rule sets for [Anywhere](https://github.com/NodePassProject/Anywhere), converted from public rule sources into importable `.arrs` and `.amrs` files.

[简体中文](README.zh-CN.md)

## About Anywhere

[Anywhere](https://github.com/NodePassProject/Anywhere) is a native proxy client built entirely with Swift. It has no Electron, no WebView, and is not a sing-box wrapper. It implements protocols directly from the lower layers, supports vless, trojan, hysteria, shadowsocks, http, and other mainstream protocols, and focuses on stability and performance.

## Contents

- `rules/common/` - curated routing rule sets for daily use.
- `rules/all/` - full converted routing rule sets from blackmatrix7. Large rule sets are split into 100,000-rule chunks for Anywhere imports.
- `mitm/` - experimental MITM rule sets and related reject rule sets.

## Usage

### Routing Rules

Click an import link to open a small HTTPS redirect page, which then launches Anywhere with an `anywhere://add-rule-set` deep link.

```text
https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FAI.arrs
```

Some rule sets include a `routing` header, so Anywhere can assign their initial target automatically on import. Other rule sets stay at Default until you choose `DIRECT`, `REJECT`, or a proxy policy.

GitHub README pages do not keep custom `anywhere://` links clickable, so the table below uses `https://chikacya.github.io/anywhere-rules/import.html` as the clickable entry point.

### MITM Rules

MITM rules are experimental and are provided for learning and research only.

Import `.amrs` files into Anywhere MITM rule sets. Some MITM rules also need a matching reject rule set, such as `mitm/DomainReject.arrs`, imported as a routing rule set and assigned to `REJECT`.

Only enable MITM for traffic you are allowed to inspect.

## Common Rules

Suggested targets are only a starting point. Pick the policy that matches your own proxy setup.

| Rule | Rules | Suggested | Purpose | Import |
| --- | ---: | --- | --- | --- |
| `Reject` | 6204 | `REJECT` | Basic ads, malicious sites, and tracking block list. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FReject.arrs) |
| `Ads_AWAvenue` | 899 | `REJECT` | AWAvenue ad-blocking rules. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FAds_AWAvenue.arrs) |
| `PCDN` | 37 | `REJECT` | Blocks PCDN and P2P CDN domains. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FPCDN.arrs) |
| `AI` | 49 | Proxy | Common AI services. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FAI.arrs) |
| `Proxy` | 1559 | Proxy | General proxy-domain collection. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FProxy.arrs) |
| `ProxyGFW` | 7597 | Proxy | Broad GFW proxy collection. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FProxyGFW.arrs) |
| `GFW` | 4253 | Proxy | GFW domain list. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FGFW.arrs) |
| `Direct` | 36 | `DIRECT` | Small direct-route supplement. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FDirect.arrs) |
| `AppleCN` | 9 | `DIRECT` | Apple China and Apple CDN direct-route rules. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FAppleCN.arrs) |
| `AppleProxy` | 39 | Proxy | Apple services that usually need a proxy. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FAppleProxy.arrs) |
| `Apple` | 44 | As needed | Basic Apple service rules. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FApple.arrs) |
| `AppleServices` | 17 | As needed | Apple system service rules. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FAppleServices.arrs) |
| `AppleMusic` | 9 | As needed | Apple Music rules. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FAppleMusic.arrs) |
| `Google` | 25 | Proxy | Google services. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FGoogle.arrs) |
| `YouTube` | 14 | Proxy | YouTube rules. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FYouTube.arrs) |
| `Microsoft` | 79 | As needed | Microsoft services. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FMicrosoft.arrs) |
| `GitHub` | 6 | As needed | GitHub rules. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FGitHub.arrs) |
| `OneDrive` | 15 | As needed | OneDrive rules. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FOneDrive.arrs) |
| `Telegram` | 45 | Proxy | Telegram domains and IP ranges. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FTelegram.arrs) |
| `Telegram_NoIP` | 30 | Proxy | Telegram domains only, without IP ranges. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FTelegram_NoIP.arrs) |
| `Twitter` | 12 | Proxy | X / Twitter rules. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FTwitter.arrs) |
| `Instagram` | 4 | Proxy | Instagram rules. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FInstagram.arrs) |
| `Facebook` | 21 | Proxy | Facebook rules. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FFacebook.arrs) |
| `Netflix` | 40 | Proxy | Netflix rules. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FNetflix.arrs) |
| `Disney` | 172 | Proxy | Disney+ rules. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FDisney.arrs) |
| `Spotify` | 29 | Proxy | Spotify rules. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FSpotify.arrs) |
| `TikTok` | 81 | Proxy | TikTok rules. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FTikTok.arrs) |
| `Bilibili` | 20 | `DIRECT` | Bilibili rules. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FBilibili.arrs) |
| `Emby` | 51 | As needed | Emby rules converted from blackmatrix7. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FEmby.arrs) |
| `WeChat` | 339 | `DIRECT` | WeChat rules. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FWeChat.arrs) |
| `ChinaDomain` | 857 | `DIRECT` | Common mainland China domains. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FChinaDomain.arrs) |
| `CN_Additional` | 43245 | `DIRECT` | Mainland China domain supplement. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FCN_Additional.arrs) |
| `Geosite_CN` | 4733 | `DIRECT` | Mainland China domains extracted from geosite.dat `GEOLOCATION-CN`. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FGeosite_CN.arrs) |
| `CN_Accelerated` | 63338 | `DIRECT` | DNS-verified mainland China domain supplement built from dnsmasq-china-list. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FCN_Accelerated.arrs) |
| `ChinaIP` | 5711 | `DIRECT` | Mainland China IP CIDR rules. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FChinaIP.arrs) |
| `GeoIP_CN` | 5946 | `DIRECT` | Mainland China IP CIDR rules extracted from Country.mmdb. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FGeoIP_CN.arrs) |
| `Lan` | 8 | `DIRECT` | LAN and private address rules. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FLan.arrs) |
| `Game` | 597 | As needed | Game platform rules. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FGame.arrs) |
| `Steam` | 54 | As needed | Steam rules. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FSteam.arrs) |
| `PayPal` | 247 | As needed | PayPal rules. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FPayPal.arrs) |
| `Cloudflare` | 65 | As needed | Cloudflare rules. | [Import](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FCloudflare.arrs) |

## CN_Accelerated

`CN_Accelerated` is built from dnsmasq-china-list `accelerated-domains.china.conf`, then rechecked with CN DNS and Country.mmdb. It excludes domains already covered by Anywhere's built-in CN rules, `Geosite_CN`, and geosite.dat `GEOLOCATION-!CN`, so it can supplement GeoIP CN for Anywhere's no-resolve routing without repeating the main CN sets. It is especially useful for less common China domains that may not appear in traffic-ranking based lists.

## Update

GitHub Actions runs the regular rule generation workflow daily. Scheduled updates for `CN_Accelerated` are paused because the latest Anywhere built-in rules database is currently unavailable; the existing rules remain available.

## Notes

Anywhere routing rule sets currently support domain suffix, domain keyword, IPv4 CIDR, and IPv6 CIDR. Unsupported upstream rule types are skipped during conversion.

Each custom Anywhere rule set can contain at most 100,000 rules. This repository automatically splits larger generated rule sets into numbered parts.

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

## Modules

`modules/*.amod` combine each plugin’s MITM rules and associated routing sets, including a module description. Standalone `.amrs` and `.arrs` remain available during the App Store transition. Disable the old standalone copies after importing a module to avoid duplicate host/routing matches.
