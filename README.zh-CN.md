# Anywhere Rules

适用于 [Anywhere](https://github.com/NodePassProject/Anywhere) 的路由规则、MITM 规则和模块，基于公开来源维护与转换。

[English](README.md)

## 关于 Anywhere

[Anywhere](https://github.com/NodePassProject/Anywhere) 是一款完全基于 Swift 开发的原生零依赖代理客户端。无 Electron，无 WebView，非 sing-box 壳程序。从底层实现纯协议封装，支持 vless、trojan、hysteria、shadowsocks、http 等多种主流协议，同时兼顾稳定与性能。

## 内容

- [`rules/common/`](rules/common/)：面向常用服务和场景的路由规则集（`.arrs`）。
- [`rules/all/`](rules/all/)：从 blackmatrix7 转换的路由规则集（`.arrs`）；大型规则集会拆成编号分片。
- [`mitm/`](mitm/)：独立的 MITM 规则集（`.amrs`）及配套路由规则集（`.arrs`）。
- [`modules/`](modules/)：整合 MITM 规则及配套路由规则的模块（`.amod`）。
- [`hub/`](hub/)：供 Anywhere Hub 使用的目录元数据。
- [`scripts/`](scripts/)：规则转换与目录生成脚本。

## 使用

前往 [Anywhere Hub](https://anywhere-hub.chikacya.indevs.in/) 浏览路由规则和 MITM 模块，并导入 Anywhere。服务相关信息可查看 [Anywhere Hub 仓库](https://github.com/chikacya/anywhere-hub)。

导入路由规则后，请根据自己的配置选择策略。部分规则集会指定初始路由策略，其他规则集需要在 Anywhere 中分配策略。

MITM 模块可以同时包含 MITM 规则及配套路由规则。如果此前已单独导入相同规则，请停用旧副本，避免重复匹配。MITM 规则为实验性内容，仅供学习交流；请只在有权检查的流量上启用。

## 说明

Anywhere 路由规则支持域名后缀、域名关键词、IPv4/IPv6 CIDR 和进程名；进程名规则仅在 macOS 匹配。无法用 Anywhere 等价表达的上游规则类型会在转换时跳过；精确域名会转换为后缀规则，也会匹配子域名。匹配方式详见 [Anywhere 路由文档](https://github.com/NodePassProject/Anywhere/blob/main/Documentations/Routing.md)。

单个自定义路由规则集最多包含 100,000 条规则；超过限制的生成规则集会拆成编号分片。

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
