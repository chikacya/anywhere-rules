# Anywhere Rules

适用于 [Anywhere](https://github.com/NodePassProject/Anywhere) 的规则库，基于公开规则源转换为可导入的 `.arrs` 和 `.amrs` 文件。

[English](README.md)

## 关于 Anywhere

[Anywhere](https://github.com/NodePassProject/Anywhere) 是一款完全基于 Swift 开发的原生零依赖代理客户端。无 Electron，无 WebView，非 sing-box 壳程序。从底层实现纯协议封装，支持 vless、trojan、hysteria、shadowsocks、http 等多种主流协议，同时兼顾稳定与性能。

## 内容

- `rules/common/`：常用路由规则集。
- `rules/all/`：blackmatrix7 全量转换路由规则集，超过 100,000 条的规则会自动切片。
- `mitm/`：实验性 MITM 规则集及相关 Reject 规则集。

## 使用

### 路由规则

点击导入链接会先打开一个 HTTPS 跳转页，再通过 `anywhere://add-rule-set` deep link 唤起 Anywhere。

```text
https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FAI.arrs
```

部分规则集带有 `routing` header，导入后 Anywhere 会自动分配初始策略。其他规则集仍保持 Default，需要在 App 内选择 `DIRECT`、`REJECT` 或代理策略。

GitHub README 不会保留可点击的自定义 `anywhere://` 链接，所以下方表格使用 `https://chikacya.github.io/anywhere-rules/import.html` 作为可点击入口。

### MITM 规则

MITM 规则为实验性内容，仅供学习交流。

将 `.amrs` 文件导入 Anywhere 的 MITM 规则集。部分 MITM 规则还需要搭配 Reject 规则，例如将 `mitm/DomainReject.arrs` 作为路由规则集导入，并分配给 `REJECT`。

请只在你有权检查的流量上启用 MITM。

## 常用规则

推荐策略只是起点，请按自己的代理配置调整。

| 规则 | 数量 | 建议策略 | 用途 | 导入 |
| --- | ---: | --- | --- | --- |
| `Reject` | 6204 | `REJECT` | 广告、恶意站点和跟踪拦截基础集合。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FReject.arrs) |
| `Ads_AWAvenue` | 899 | `REJECT` | 秋风广告规则 AWAvenue。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FAds_AWAvenue.arrs) |
| `PCDN` | 37 | `REJECT` | PCDN 与 P2P CDN 域名拦截。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FPCDN.arrs) |
| `AI` | 49 | 代理 | 常见 AI 服务。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FAI.arrs) |
| `Proxy` | 1559 | 代理 | 常用代理域名集合。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FProxy.arrs) |
| `ProxyGFW` | 7597 | 代理 | GFW 代理集合。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FProxyGFW.arrs) |
| `GFW` | 4253 | 代理 | GFW 域名列表。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FGFW.arrs) |
| `Direct` | 36 | `DIRECT` | 常用直连补充。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FDirect.arrs) |
| `AppleCN` | 9 | `DIRECT` | 苹果中国和苹果 CDN 直连。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FAppleCN.arrs) |
| `AppleProxy` | 39 | 代理 | 通常需要代理的苹果服务。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FAppleProxy.arrs) |
| `Apple` | 44 | 按需 | 苹果基础服务。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FApple.arrs) |
| `AppleServices` | 17 | 按需 | 苹果系统服务。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FAppleServices.arrs) |
| `AppleMusic` | 9 | 按需 | Apple Music。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FAppleMusic.arrs) |
| `Google` | 25 | 代理 | Google 服务。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FGoogle.arrs) |
| `YouTube` | 14 | 代理 | YouTube。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FYouTube.arrs) |
| `Microsoft` | 79 | 按需 | Microsoft 服务。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FMicrosoft.arrs) |
| `GitHub` | 6 | 按需 | GitHub。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FGitHub.arrs) |
| `OneDrive` | 15 | 按需 | OneDrive。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FOneDrive.arrs) |
| `Telegram` | 45 | 代理 | Telegram 域名与 IP。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FTelegram.arrs) |
| `Telegram_NoIP` | 30 | 代理 | Telegram 域名，不含 IP。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FTelegram_NoIP.arrs) |
| `Twitter` | 12 | 代理 | X / Twitter。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FTwitter.arrs) |
| `Instagram` | 4 | 代理 | Instagram。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FInstagram.arrs) |
| `Facebook` | 21 | 代理 | Facebook。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FFacebook.arrs) |
| `Netflix` | 40 | 代理 | Netflix。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FNetflix.arrs) |
| `Disney` | 172 | 代理 | Disney+。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FDisney.arrs) |
| `Spotify` | 29 | 代理 | Spotify。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FSpotify.arrs) |
| `TikTok` | 81 | 代理 | TikTok。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FTikTok.arrs) |
| `Bilibili` | 20 | `DIRECT` | Bilibili。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FBilibili.arrs) |
| `Emby` | 51 | 按需 | 从 blackmatrix7 转换的 Emby 规则。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FEmby.arrs) |
| `WeChat` | 339 | `DIRECT` | WeChat。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FWeChat.arrs) |
| `ChinaDomain` | 857 | `DIRECT` | 中国大陆常见域名直连。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FChinaDomain.arrs) |
| `CN_Additional` | 43245 | `DIRECT` | 中国大陆域名补充。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FCN_Additional.arrs) |
| `Geosite_CN` | 4733 | `DIRECT` | 从 geosite.dat 的 `GEOLOCATION-CN` 提取的中国大陆域名。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FGeosite_CN.arrs) |
| `CN_Accelerated` | 63338 | `DIRECT` | 基于 dnsmasq-china-list 并经 DNS 验证的中国大陆域名补充。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FCN_Accelerated.arrs) |
| `ChinaIP` | 5711 | `DIRECT` | 中国大陆 IP CIDR。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FChinaIP.arrs) |
| `GeoIP_CN` | 5946 | `DIRECT` | 从 Country.mmdb 提取的中国大陆 IP CIDR。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FGeoIP_CN.arrs) |
| `Lan` | 8 | `DIRECT` | 局域网和私有地址。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FLan.arrs) |
| `Game` | 597 | 按需 | 游戏平台集合。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FGame.arrs) |
| `Steam` | 54 | 按需 | Steam。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FSteam.arrs) |
| `PayPal` | 247 | 按需 | PayPal。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FPayPal.arrs) |
| `Cloudflare` | 65 | 按需 | Cloudflare。 | [导入](https://chikacya.github.io/anywhere-rules/import.html?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchikacya%2Fanywhere-rules%2Fmain%2Frules%2Fcommon%2FCloudflare.arrs) |

## CN_Accelerated

`CN_Accelerated` 基于 dnsmasq-china-list 的 `accelerated-domains.china.conf` 生成，并再次通过中国 DNS 与 Country.mmdb 验证解析结果是否落在中国大陆 IP。生成时会排除 Anywhere 内置 CN 规则、`Geosite_CN` 和 geosite.dat 的 `GEOLOCATION-!CN`，用于在不重复主要 CN 规则集的前提下，补充 Anywhere no-resolve 路由下 GeoIP CN 无法接住的域名，尤其适合需要访问非高频中国域名的用户。

## 更新

GitHub Actions 每天定时运行常规规则生成任务。由于目前无法取得最新版 Anywhere 内置规则数据库，`CN_Accelerated` 已暂停定期更新；现有规则仍可使用。

## 说明

Anywhere 路由规则集当前支持域名后缀、域名关键词、IPv4 CIDR 和 IPv6 CIDR。上游中无法等价表达的规则类型会在转换时跳过。

Anywhere 单个自定义规则集最多 100,000 条规则。本仓库会自动将超限规则集拆成编号分片。

## 致谢

感谢以下公开规则与脚本项目/作者的长期维护：

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
- 等
