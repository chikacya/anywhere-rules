"""Independent AI rule sources inspired by VPSDance/ai-proxy-rules.

The provider selection and several core rules are adapted from its MIT-licensed
configuration; see sources/VPSDance-LICENSE. Generated lists are not consumed.
"""

V2 = "https://raw.githubusercontent.com/v2fly/domain-list-community/master/data/"
BM = "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/"

AI_RULE_SETS = [
    {
        "name": "ChatGPT", "description": "OpenAI / ChatGPT / Codex",
        "sources": [BM + "OpenAI/OpenAI.list", "v2fly:" + V2 + "openai"],
        "extra_rules": [
            "DOMAIN-SUFFIX,ai.com", "DOMAIN-SUFFIX,chatgpt.livekit.cloud",
            "DOMAIN-SUFFIX,sora.com", "DOMAIN-KEYWORD,chatgpt-async-webps-prod",
            "IP-CIDR,199.47.142.0/23", "IP-CIDR6,2604:f20::/32",
            "PROCESS-NAME,ChatGPT", "PROCESS-NAME,Codex",
        ],
        "excluded_values": ["20473"],
    },
    {
        "name": "Claude", "description": "Anthropic / Claude / Claude Code",
        "sources": [
            "html-yaml:https://ip.net.coffee/claude/site.html",
            "https://raw.githubusercontent.com/xiaolai/anthropic-claude-surge-rules-set/main/anthropic.list",
            "v2fly:" + V2 + "anthropic",
        ],
        "extra_rules": [
            "DOMAIN-SUFFIX,anthropic.com.cn", "DOMAIN-SUFFIX,claude.app",
            "DOMAIN-SUFFIX,claude.new", "DOMAIN-SUFFIX,claude.site",
            "DOMAIN-SUFFIX,claudemcpclient.com", "DOMAIN-SUFFIX,claudemcpcontent.com",
            "DOMAIN-SUFFIX,claudepages.dev", "DOMAIN-SUFFIX,claudestudio.com",
            "DOMAIN-SUFFIX,modelcontextprotocol.com", "DOMAIN-SUFFIX,modelcontextprotocol.net",
            "DOMAIN-SUFFIX,modelcontextprotocol.org", "DOMAIN-SUFFIX,modelcontextprotocol.io",
            "IP-CIDR,160.79.104.0/21", "IP-CIDR6,2607:6bc0::/32",
            "PROCESS-NAME,Claude",
        ],
        # Shared Google storage is not Claude-specific.
        "excluded_values": ["storage.googleapis.com", "time.apple.com", "datadog", "sift", "sentry", "sentry.io", "statsigapi.net", "intercom.io", "intercomcdn.com"],
    },
    {
        "name": "Gemini", "description": "Google AI / Gemini / AI Studio / NotebookLM",
        "sources": [BM + "Gemini/Gemini.list", "v2fly:" + V2 + "google-deepmind"],
        "extra_rules": ["PROCESS-NAME,Antigravity"],
        "excluded_values": ["apis.google.com", "colab", "developerprofiles", "generativelanguage"],
    },
    {"name": "Grok", "description": "xAI / Grok", "sources": ["v2fly:" + V2 + "xai"]},
    {
        "name": "Muse", "description": "Meta Muse / Meta AI",
        "sources": ["v2fly-no-includes:" + V2 + "meta"],
        "extra_rules": [
            "DOMAIN,ai.meta.com", "DOMAIN,ai.developer.meta.com", "DOMAIN,aidemos.meta.com",
            "DOMAIN,llama.developer.meta.com", "DOMAIN,developer.meta.com",
            "DOMAIN-SUFFIX,llamameta.net",
        ],
        "excluded_values": ["meta.com"],
    },
    {"name": "Perplexity", "description": "Perplexity AI", "sources": ["v2fly:" + V2 + "perplexity"]},
    {
        "name": "Copilot", "description": "GitHub / Microsoft Copilot",
        "sources": [BM + "Copilot/Copilot.list", "v2fly:" + V2 + "github-copilot"],
        "extra_rules": ["DOMAIN-SUFFIX,copilot.microsoft.com", "DOMAIN-SUFFIX,githubcopilot.com"],
        "excluded_values": [
            "chat.openai.com.cdn.cloudflare.net", "openai-api.arkoselabs.com",
            "openaicomproductionae4b.blob.core.windows.net", "production-openaicom-storage.azureedge.net",
            "r.bing.com", "services.bingapis.com", "www.bing.com", "chatgpt.com",
            "chatgpt.livekit.cloud", "host.livekit.cloud", "oaistatic.com", "oaiusercontent.com",
            "openai.com", "openaiapi-site.azureedge.net", "openaicom.imgix.net", "turn.livekit.cloud",
            "openaicom-api", "24.199.123.28/32", "64.23.132.171/32",
        ],
    },
    {
        "name": "Cursor", "description": "Cursor AI editor",
        "sources": ["v2fly:" + V2 + "cursor"],
        "extra_rules": ["PROCESS-NAME,Cursor"],
    },
]
